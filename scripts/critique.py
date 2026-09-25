#!/usr/bin/env python3
"""critique.py — the d-pill machine gate.

Checks real HTML and CSS against the d-pill token scales and access floors.
The values it checks come from references/tokens.json (the verified export of
base.css) when that file is present; the built-in constants are the fallback.
The rule registry is references/rules.json; the engine verifies the registry
and the implementation agree before it runs, the same law check-tokens.py
enforces between base.css and the export.

Findings are written to stderr, one per line:
    file:line:col [dpill/rule-id] severity: message
Exit codes: 0 clean (warnings allowed unless --strict), 2 findings, 1 the
invocation itself is broken. Exit 2 with stderr is the Claude Code hook
contract: the agent receives the findings as the reason to react.

Usage:
    python3 scripts/critique.py [options] path [path ...]
    python3 scripts/critique.py --list-rules
    python3 scripts/critique.py --selftest
Options:
    --json        machine output on stdout (findings + summary)
    --quiet       errors only, warnings suppressed
    --strict      warnings fail too
    --allow ID    suppress a rule (repeatable); a suppression is a written
                  exception, not a habit
"""

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RULES_FILE = ROOT / "references" / "rules.json"
TOKENS_FILE = ROOT / "references" / "tokens.json"
FIXTURES = Path(__file__).resolve().parent / "fixtures"

VERSION = "1.5.0"

# Fallback scales (rem). Overridden by tokens.json when it is present.
FALLBACK = {
    "space": ["0.25rem", "0.5rem", "0.75rem", "1rem", "1.5rem", "2rem",
              "3rem", "4rem", "6rem", "8rem"],
    "ramp": ["0.75rem", "0.8125rem", "0.9375rem", "1rem", "1.125rem",
             "1.5rem", "2.25rem", "3.5rem"],
    "radius": ["4px", "6px", "10px", "999px"],
    "durations": ["120ms", "180ms", "240ms"],
    "z": [10, 20, 40, 50, 60],
}


def rem_to_px(text):
    try:
        return round(float(text.rstrip("rem")) * 16, 3)
    except ValueError:
        return None


def build_scales():
    """Space/radius/ramp/z/duration scales, from tokens.json when possible."""
    scales = {
        "space": set(), "ramp": set(), "radius": set(),
        "durations": set(), "z": set(FALLBACK["z"]),
    }
    try:
        data = json.loads(TOKENS_FILE.read_text())
    except (OSError, ValueError):
        data = None
    if data:
        for v in (data.get("space", {}).get("scale", {}) or {}).values():
            scales["space"].add(_norm_len(v))
        for v in (data.get("type", {}).get("ramp", {}) or {}).values():
            scales["ramp"].add(_norm_len(v))
        for v in (data.get("shape", {}) or {}).values():
            scales["radius"].add(_norm_len(v))
        for k, v in (data.get("motion", {}) or {}).items():
            if k.startswith("dur"):
                scales["durations"].add(_norm_len(v))
    if not scales["space"]:
        scales["space"] = {_norm_len(v) for v in FALLBACK["space"]}
    if not scales["ramp"]:
        scales["ramp"] = {_norm_len(v) for v in FALLBACK["ramp"]}
    # 16px is the iOS input floor: coarse-pointer inputs are authored at 1rem
    # (base.css) so Safari does not zoom the field on focus. An exception, kept.
    scales["ramp"].add("16px")
    if not scales["radius"]:
        scales["radius"] = {_norm_len(v) for v in FALLBACK["radius"]}
    if not scales["durations"]:
        scales["durations"] = {_norm_len(v) for v in FALLBACK["durations"]}
    return scales


def _norm_len(v):
    v = str(v).strip()
    if v.endswith("rem"):
        px = rem_to_px(v)
        if px is not None and float(px).is_integer():
            return f"{int(px)}px"
    return v


# ---------------------------------------------------------------------------
# Rule definitions. ids must match references/rules.json exactly.

SPACE_PROPS = re.compile(
    r"(?:^|[\s;{])(-?(?:margin|padding|gap|row-gap|column-gap)"
    r"(?:-(?:top|right|bottom|left|block|inline|start|end))?)\s*:\s*([^;{}]+)",
    re.I)
RADIUS_PROP = re.compile(
    r"(?:^|[\s;{])(border[\w-]*-radius)\s*:\s*([^;{}]+)", re.I)
BORDER_PROP = re.compile(
    r"(?:^|[\s;{])(border|border-(?:top|right|bottom|left|block|inline|"
    r"block-start|block-end|inline-start|inline-end)(?:-width)?)\s*:\s*([^;{}]+)",
    re.I)
FONT_SIZE_PROP = re.compile(r"(?:^|[\s;{])(font-size)\s*:\s*([^;{}]+)", re.I)
Z_PROP = re.compile(r"(?:^|[\s;{])(z-index)\s*:\s*([^;{}]+)", re.I)
TIME_SHORT = re.compile(
    r"(?:^|[\s;{])(transition|animation|transition-duration|"
    r"animation-duration)\s*:\s*([^;{}]+)", re.I)
TIMING_SHORT = re.compile(
    r"(?:^|[\s;{])(transition-timing-function|animation-timing-function)\s*:\s*([^;{}]+)",
    re.I)
LENGTH_RE = re.compile(r"(-?\d+(?:\.\d+)?)(px|rem)\b")
MS_RE = re.compile(r"\b(\d+(?:\.\d+)?)(ms|s)\b")
BEZIER_RE = re.compile(r"cubic-bezier\(([^)]*)\)")
COLOR_PROPS = re.compile(
    r"(?:^|[\s;{])(color|background|background-color|border-color|"
    r"border-top-color|border-bottom-color|fill|stroke|outline-color|"
    r"text-decoration-color|caret-color|box-shadow|text-shadow)\s*:\s*([^;{}]+)",
    re.I)
HEX_RE = re.compile(r"#[0-9a-fA-F]{3,8}\b")
FUNC_COLOR_RE = re.compile(r"\b(?:rgb|rgba|hsl|hsla|oklch|oklab|lab|lch)\(")

LENGTH_SPLIT_RE = re.compile(r"[,\s]+")
EASE_KEYWORDS = {"linear", "ease", "ease-in", "ease-out", "ease-in-out", "step-start", "step-end"}
ALLOWED_BEZIERS = {"0.16, 1, 0.3, 1", "0.7, 0, 0.84, 0"}

HOVER_RE = re.compile(r":hover\b")
FOCUS_RE = re.compile(r":focus(?:-visible)?\b")
REDUCED_RE = re.compile(r"prefers-reduced-motion")
COMMENT_RE = re.compile(r"/\*.*?\*/", re.S)

CSS_SUFFIXES = {".css", ".scss", ".vcss"}
HTML_SUFFIXES = {".html", ".htm", ".xhtml"}
SKIP_DIRS = {".git", "node_modules", ".next", "dist", "build", ".cache"}
SKIP_FILE = re.compile(r"\.min\.(css|js)$")


def walk(paths):
    for raw in paths:
        p = Path(raw)
        if p.is_dir():
            for child in sorted(p.rglob("*")):
                if any(part in SKIP_DIRS for part in child.parts):
                    continue
                if child.is_file() and child.suffix.lower() in (
                        CSS_SUFFIXES | HTML_SUFFIXES) and not SKIP_FILE.search(child.name):
                    if child.stat().st_size <= 1_000_000:
                        yield child
        elif p.is_file() and p.suffix.lower() in (CSS_SUFFIXES | HTML_SUFFIXES) \
                and not SKIP_FILE.search(p.name):
            yield p


class Finding(object):
    __slots__ = ("file", "line", "col", "rule", "severity", "message")

    def __init__(self, file, line, col, rule, severity, message):
        self.file, self.line, self.col = file, line, col
        self.rule, self.severity, self.message = rule, severity, message

    def human(self):
        return "{}:{}:{} [{}] {}: {}".format(
            self.file, self.line, self.col, self.rule, self.severity, self.message)

    def data(self):
        return {"file": self.file, "line": self.line, "col": self.col,
                "rule": self.rule, "severity": self.severity,
                "message": self.message}


def add(findings, path, lineno, col, rule, severity, message):
    findings.append(Finding(str(path), lineno, col, rule, severity, message))


def check_lengths(value, scales, kind, path, lineno, col, findings,
                  rule, prop, allow_zero=True):
    """Flag px/rem literals that are not on the scale."""
    if "var(" in value or "clamp(" in value or "calc(" in value:
        return
    for m in LENGTH_RE.finditer(value):
        num, unit = float(m.group(1)), m.group(2)
        px = num * 16 if unit == "rem" else num
        px = round(px, 3)
        if px == 0 and allow_zero:
            continue
        token = "{}px".format(int(px)) if float(px).is_integer() else "{}px".format(px)
        legal = scales[kind]
        if token not in legal and "{}px".format(int(round(px))) not in legal:
            legal_list = sorted(legal, key=lambda s: _sort_px(s))
            add(findings, path, lineno, col, rule, "error",
                "{} in {} is not on the {} scale ({}). Use the token, or write the exception down."
                .format(m.group(0), prop, kind, " ".join(legal_list)))


def _sort_px(s):
    try:
        return float(str(s).rstrip("px"))
    except ValueError:
        return 1e9


def check_css_line(line, lineno, path, scales, findings, state):
    for m in SPACE_PROPS.finditer(line):
        check_lengths(m.group(2), scales, "space", path, lineno,
                      m.start(2), findings, "dpill/space-off-scale", m.group(1))
    for m in RADIUS_PROP.finditer(line):
        value = m.group(2)
        if "50%" in value:
            add(findings, path, lineno, m.start(2), "dpill/radius-off-scale",
                "warn", "border-radius: 50% — circles are --radius-full in this system.")
        else:
            check_lengths(value, scales, "radius", path, lineno, m.start(2),
                          findings, "dpill/radius-off-scale", m.group(1))
    for m in BORDER_PROP.finditer(line):
        value = m.group(2)
        if value.strip() in ("none", "0", "0px"):
            continue
        if "var(" in value or "calc(" in value:
            continue
        for lm in LENGTH_RE.finditer(value):
            if float(lm.group(1)) > 1:
                add(findings, path, lineno, lm.start(), "dpill/border-not-hairline",
                    "error", "{} border in {}. Edges are 1px hairlines; weight comes from --line-strong."
                    .format(lm.group(0), m.group(1)))
    for m in FONT_SIZE_PROP.finditer(line):
        check_lengths(m.group(2), scales, "ramp", path, lineno, m.start(2),
                      findings, "dpill/font-off-ramp", m.group(1), allow_zero=False)
    for m in Z_PROP.finditer(line):
        value = m.group(2).strip()
        if value and value[0].isdigit():
            try:
                z = int(value)
            except ValueError:
                continue
            if z not in scales["z"]:
                add(findings, path, lineno, m.start(2), "dpill/z-off-scale", "error",
                    "z-index {} is not on the z scale ({}). Layers declare themselves."
                    .format(value, " ".join(str(v) for v in sorted(scales["z"]))))
    for m in TIME_SHORT.finditer(line):
        value = m.group(2)
        prop = m.group(1)
        if "var(" in value:
            pass
        else:
            for tm in MS_RE.finditer(value):
                ms = float(tm.group(1)) * (1000 if tm.group(2) == "s" else 1)
                if ms in (0.0, 0.01):
                    continue  # the reduced-motion disable, not a duration
                legal = scales["durations"]
                tok = "{}ms".format(int(ms)) if float(ms).is_integer() else "{}ms".format(ms)
                if tok not in legal:
                    add(findings, path, lineno, tm.start(), "dpill/duration-off-scale",
                        "error", "{} in {} is not on the duration scale ({}). --dur-1, --dur-2, --dur-3."
                        .format(tm.group(0), prop, " ".join(sorted(legal))))
        state["timed"] = True
        if prop in ("transition",) and re.search(r"(?:^|\s|,)all(?:\s|,|$)", value):
            add(findings, path, lineno, m.start(2), "dpill/transition-all", "error",
                "transition: all animates layout. Name the properties that actually change.")
    for m in TIMING_SHORT.finditer(line):
        _check_easing(m.group(2), path, lineno, m.start(2), findings)
    for m in TIME_SHORT.finditer(line):
        if m.group(1) == "transition" and "var(" not in m.group(2):
            _check_easing(m.group(2), path, lineno, m.start(2), findings)
    for m in COLOR_PROPS.finditer(line):
        value = m.group(2)
        if "var(" in value:
            continue
        hit = HEX_RE.search(value) or FUNC_COLOR_RE.search(value)
        if hit:
            add(findings, path, lineno, m.start(2), "dpill/hardcoded-color", "warn",
                "a literal color in {}. Roles come from base.css; a color outside the roles is a written exception."
                .format(m.group(1)))
    if HOVER_RE.search(line):
        state["hover"] = True
    if FOCUS_RE.search(line):
        state["focus"] = True
    if REDUCED_RE.search(line):
        state["reduced"] = True


def _check_easing(value, path, lineno, col, findings):
    if "var(" in value or "spring(" in value or "cubic-bezier" not in value:
        if "cubic-bezier" in value:
            pass
        else:
            for kw in EASE_KEYWORDS:
                if re.search(r"(?:^|[\s,]){}(?:\s|,|$)".format(re.escape(kw)), value):
                    add(findings, path, lineno, col, "dpill/easing-off-scale", "warn",
                        "'{}' is off the easing tokens. --ease-out / --ease-in, or write the exception."
                        .format(kw))
            return
    for bm in BEZIER_RE.finditer(value):
        pts = re.sub(r"\s+", "", bm.group(1))
        if pts not in ALLOWED_BEZIERS:
            add(findings, path, lineno, bm.start(), "dpill/easing-off-scale", "warn",
                "cubic-bezier({}) is not a system curve. --ease-out / --ease-in.".format(bm.group(1)))


IMG_RE = re.compile(r"<img\b[^>]*>", re.I)
ATTR_RE = re.compile(r"([\w-]+)\s*=\s*\"([^\"]*)\"|([\w-]+)\s*=\s*'([^']*)'", re.I)
HTML_TAG_RE = re.compile(r"<html\b[^>]*>", re.I)
BUTTON_RE = re.compile(r"<(button|summary)\b[^>]*>(.*?)</\1>", re.I | re.S)
A_RE = re.compile(r"<(a)\b[^>]*href=[^>]*>(.*?)</a>", re.I | re.S)
TAG_STRIP_RE = re.compile(r"<[^>]+>")
INLINE_STYLE_RE = re.compile(r"style\s*=\s*\"([^\"]*)\"", re.I)
WATCHED_INLINE = re.compile(
    r"(?:^|[;])(font-size|padding|margin|gap|border-radius|width|height)\s*:\s*[^;]*[0-9]", re.I)


def attrs_of(tag):
    out = {}
    for m in ATTR_RE.finditer(tag):
        name = (m.group(1) or m.group(3) or "").lower()
        out[name] = m.group(2) if m.group(1) is not None else m.group(4)
    return out


def check_html(source, path, findings, scales=None, css_state=None):
    for lineno, line in enumerate(source.splitlines(), 1):
        for m in IMG_RE.finditer(line):
            a = attrs_of(m.group(0))
            if "alt" not in a:
                add(findings, path, lineno, m.start(), "dpill/img-no-alt", "error",
                    "an <img> without alt. Meaningful gets words; decorative gets alt=\"\".")
            if "width" not in a or "height" not in a:
                add(findings, path, lineno, m.start(), "dpill/img-no-dimensions", "warn",
                    "an <img> without width and height reserves no space; the stream shifts under it.")
        for m in INLINE_STYLE_RE.finditer(line):
            if WATCHED_INLINE.search(m.group(1)):
                add(findings, path, lineno, m.start(), "dpill/inline-token-bypass", "warn",
                    "sizing inside a style attribute bypasses the tokens. Classes and vars, not literals.")
    for m in HTML_TAG_RE.finditer(source):
        tag = m.group(0)
        lineno = source.count("\n", 0, m.start()) + 1
        if "lang" not in attrs_of(tag):
            add(findings, path, lineno, m.start(), "dpill/lang-missing", "error",
                "<html> has no lang. Screen readers pick the wrong voice for every word on the page.")
    # <style> blocks are CSS. Scan them with the real line numbers.
    if scales is not None and css_state is not None:
        for sm in re.finditer(r"<style\b[^>]*>(.*?)</style>", source, re.I | re.S):
            block = sm.group(1)
            base_line = source.count("\n", 0, sm.start(1))
            for offset, line in enumerate(block.splitlines(), 1):
                check_css_line(line, base_line + offset, path, scales,
                               findings, css_state)
    for pattern in (BUTTON_RE, A_RE):
        for m in pattern.finditer(source):
            tag = m.group(0)
            a = attrs_of(tag)
            text = TAG_STRIP_RE.sub("", m.group(2) or "").strip()
            lineno = source.count("\n", 0, m.start()) + 1
            if not text and not (a.get("aria-label") or a.get("aria-labelledby")
                                 or a.get("title")):
                kind = "icon control" if "<svg" in (m.group(2) or "") else "control"
                add(findings, path, lineno, m.start(), "dpill/control-no-name", "error",
                    "a {} with no accessible name. Text, or aria-label with the verb."
                    .format(kind))


LINK_RE = re.compile(r"<link\b[^>]*>", re.I)


def _linked_flags(path, text, flags):
    """Follow local <link rel=stylesheet> targets for project context only
    (does the page's own stylesheet carry reduced motion, focus, hover).
    The linked file is not rule-scanned: name it explicitly to check it."""
    for m in LINK_RE.finditer(text):
        a = attrs_of(m.group(0))
        href = a.get("href", "")
        rel = (a.get("rel") or "").lower()
        if "stylesheet" not in rel or not href or href.startswith(("http", "//", "data:")):
            continue
        target = (path.parent / href).resolve()
        if target.suffix.lower() not in CSS_SUFFIXES or not target.is_file():
            continue
        try:
            linked = target.read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue
        if REDUCED_RE.search(linked):
            flags["reduced"] = True
        if FOCUS_RE.search(linked):
            flags["focus"] = True
        if HOVER_RE.search(linked):
            flags["hover"] = True
        if TIME_SHORT.search(linked):
            flags["timed"] = True


def collect(paths, allow=(), strict=False):
    """The callable API. Returns (findings, stats) for humans, hooks, and MCP."""
    scales = build_scales()
    allow = set(allow or [])
    findings = []
    css_any = {"timed": False, "reduced": False}
    files = list(walk(paths))
    for path in files:
        try:
            text = COMMENT_RE.sub(" ", path.read_text(encoding="utf-8", errors="replace"))
        except OSError:
            continue
        if path.suffix.lower() in HTML_SUFFIXES:
            state = {"hover": False, "focus": False, "reduced": False, "timed": False}
            check_html(text, path, findings, scales, state)
            _linked_flags(path, text, state)
            css_any["timed"] = css_any["timed"] or state["timed"]
            css_any["reduced"] = css_any["reduced"] or state["reduced"]
            continue
        state = {"hover": False, "focus": False, "reduced": False, "timed": False}
        for lineno, line in enumerate(text.splitlines(), 1):
            check_css_line(line, lineno, path, scales, findings, state)
        css_any["timed"] = css_any["timed"] or state["timed"]
        css_any["reduced"] = css_any["reduced"] or state["reduced"]
        if state["hover"] and not state["focus"]:
            add(findings, path, 1, 1, "dpill/hover-no-focus", "warn",
                "this file styles :hover but never :focus or :focus-visible. "
                "If base.css draws the ring globally, declare that; otherwise the control is unreachable-looking.")
    if css_any["timed"] and not css_any["reduced"]:
        findings.append(Finding("(project)", 1, 1, "dpill/no-reduced-motion", "warn",
                                "transitions or animations are used but no scanned file "
                                "carries prefers-reduced-motion. base.css ships it; use it."))
    findings = [f for f in findings if f.rule not in allow]
    findings.sort(key=lambda f: (f.severity != "error", str(f.file), f.line))
    stats = {
        "files": len(files),
        "errors": sum(1 for f in findings if f.severity == "error"),
        "warnings": sum(1 for f in findings if f.severity == "warn"),
        "rules_fired": sorted({f.rule for f in findings}),
    }
    failed = stats["errors"] > 0 or (strict and stats["warnings"] > 0)
    return findings, stats, failed


# ---------------------------------------------------------------------------
# Registry sync + modes

RULE_IDS = [
    "dpill/space-off-scale", "dpill/radius-off-scale", "dpill/font-off-ramp",
    "dpill/z-off-scale", "dpill/duration-off-scale", "dpill/easing-off-scale",
    "dpill/transition-all", "dpill/border-not-hairline",
    "dpill/hardcoded-color", "dpill/hover-no-focus",
    "dpill/no-reduced-motion", "dpill/inline-token-bypass",
    "dpill/img-no-alt", "dpill/img-no-dimensions",
    "dpill/lang-missing", "dpill/control-no-name",
]


def registry_sync():
    """Every rule implemented appears in rules.json; every entry is real."""
    try:
        data = json.loads(RULES_FILE.read_text())
    except (OSError, ValueError) as e:
        return False, ["rules.json unreadable: {}".format(e)]
    declared = [r.get("id") for r in data.get("rules", [])]
    problems = []
    for rid in RULE_IDS:
        if rid not in declared:
            problems.append("implemented but not in rules.json: " + rid)
    for rid in declared:
        if rid not in RULE_IDS:
            problems.append("in rules.json but not implemented: " + rid)
    return (not problems), problems


def list_rules():
    ok, problems = registry_sync()
    try:
        data = json.loads(RULES_FILE.read_text())
        rows = data.get("rules", [])
    except (OSError, ValueError):
        rows = []
    print("d-pill machine gate — {} rules (v{})".format(len(rows), VERSION))
    for r in rows:
        print("  {:<34} {:<6} {}".format(r["id"], r["severity"], r["summary"]))
    if problems:
        print("REGISTRY DRIFT:")
        for p in problems:
            print("  - " + p)
        print("Fix the loser. Do not hand-edit around the drift.")
        return 1
    print("Registry and engine agree.")
    return 0


def selftest():
    bad_css = FIXTURES / "bad.css"
    bad_html = FIXTURES / "bad.html"
    expected = {
        "dpill/space-off-scale", "dpill/radius-off-scale", "dpill/font-off-ramp",
        "dpill/z-off-scale", "dpill/duration-off-scale", "dpill/easing-off-scale",
        "dpill/transition-all", "dpill/border-not-hairline",
        "dpill/hardcoded-color", "dpill/hover-no-focus",
        "dpill/img-no-alt", "dpill/img-no-dimensions", "dpill/lang-missing",
        "dpill/control-no-name", "dpill/inline-token-bypass",
    }
    findings, stats, failed = collect([str(bad_css), str(bad_html)])
    fired = set(stats["rules_fired"])
    missing = expected - fired
    if missing:
        print("SELFTEST FAIL — these rules did not fire on the fixtures:")
        for r in sorted(missing):
            print("  - " + r)
        return 1
    print("SELFTEST PASS — {} findings across {} rules; every rule fires where it should."
          .format(len(findings), len(fired)))
    return 0


def main(argv):
    args = argv[1:]
    flags = {"json": False, "quiet": False, "strict": False}
    allow, paths = [], []
    i = 0
    while i < len(args):
        a = args[i]
        if a == "--json":
            flags["json"] = True
        elif a == "--quiet":
            flags["quiet"] = True
        elif a == "--strict":
            flags["strict"] = True
        elif a == "--list-rules":
            return list_rules()
        elif a == "--selftest":
            return selftest()
        elif a in ("--allow",):
            i += 1
            if i >= len(args):
                print("--allow needs a rule id", file=sys.stderr)
                return 1
            allow.append(args[i])
        elif a in ("--version",):
            print("d-pill critique " + VERSION)
            return 0
        elif a in ("-h", "--help"):
            print(__doc__)
            return 0
        elif a.startswith("-"):
            print("unknown flag: " + a, file=sys.stderr)
            return 1
        else:
            paths.append(a)
        i += 1
    if not paths:
        print(__doc__)
        return 1
    ok, problems = registry_sync()
    if not ok:
        print("REGISTRY DRIFT — refusing to run an unverified rule set:", file=sys.stderr)
        for p in problems:
            print("  - " + p, file=sys.stderr)
        return 1
    findings, stats, failed = collect(paths, allow, flags["strict"])
    shown = [f for f in findings if f.severity == "error" or not flags["quiet"]]
    if flags["json"]:
        print(json.dumps({"tool": "d-pill critique", "version": VERSION,
                          "summary": stats,
                          "findings": [f.data() for f in shown]}, indent=2))
    else:
        for f in shown:
            print(f.human(), file=sys.stderr)
        print("{} files checked — {} error(s), {} warning(s){}.".format(
            stats["files"], stats["errors"], stats["warnings"],
            "; exit 2" if failed else ""))
    return 2 if failed else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
