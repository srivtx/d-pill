#!/usr/bin/env python3
"""check-tokens.py — verify references/tokens.json against references/base.css.

base.css is the authority. This script parses its :root and html[data-theme="dark"]
blocks, resolves var() references, and asserts the machine export matches. Exit 0
means the export is true; exit 1 prints every drift.

Usage: python3 scripts/check-tokens.py
"""

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BASE = ROOT / "references" / "base.css"
EXPORT = ROOT / "references" / "tokens.json"

VAR_RE = re.compile(r"var\(\s*(--[\w-]+)\s*\)")


def blocks(css: str):
    """Extract :root and html[data-theme=dark] declaration maps."""
    root, dark = {}, {}

    def grab(selector):
        m = re.search(selector + r"\s*\{([^}]*)\}", css)
        if not m:
            return {}
        out = {}
        for decl in m.group(1).split(";"):
            if ":" not in decl:
                continue
            name, value = decl.split(":", 1)
            name = name.strip()
            if name.startswith("--"):
                out[name] = re.sub(r"\s+", " ", value.strip())
        return out

    root = grab(r"(?<![\w-])\:root")
    dark = grab(r'html\[data-theme\s*=\s*"dark"\]')
    return root, dark


def resolve(value: str, scope: dict) -> str:
    """Resolve var() chains against the final scope map."""
    for _ in range(10):
        if "var(" not in value:
            return value
        value = VAR_RE.sub(
            lambda m: scope.get(m.group(1), m.group(0)), value)
        value = re.sub(r"\s+", " ", value).strip()
    return value


def norm(s: str) -> str:
    return re.sub(r"\s+", " ", s).strip()


def build_scopes(css: str):
    root, dark = blocks(css)
    light_scope = dict(root)
    dark_scope = dict(root)
    dark_scope.update(dark)
    light = {k: resolve(v, light_scope) for k, v in light_scope.items()}
    darkr = {k: resolve(v, dark_scope) for k, v in dark_scope.items()}
    return root, light, darkr


# JSON path -> (scope, css token). scope: "light", "dark", or "root"
COLOR_KEYS = [
    "bg", "bg-subtle", "surface", "ink", "ink-muted", "line", "line-strong",
    "accent", "accent-ink", "accent-soft", "focus", "danger", "danger-ink",
    "danger-soft", "ok", "warn", "border", "border-strong", "shadow-overlay",
]

CHECKS = []
for key in COLOR_KEYS:
    CHECKS.append((("color", "light", key), "light", f"--{key}"))
    CHECKS.append((("color", "dark", key), "dark", f"--{key}"))
for key in ["display", "text", "mono"]:
    CHECKS.append((("font", key), "root", f"--font-{key}"))
for key in ["text-xs", "text-sm", "text-md", "text-lg", "text-xl",
            "text-2xl", "text-3xl"]:
    CHECKS.append((("type", "ramp", key), "root", f"--{key}"))
for key in ["leading-display", "leading-ui", "leading-body",
            "tracking-display", "tracking-caps"]:
    CHECKS.append((("type", key), "root", f"--{key}"))
for i in range(1, 11):
    CHECKS.append((("space", "scale", f"space-{i}"), "root", f"--space-{i}"))
for key in ["radius-sm", "radius", "radius-lg", "radius-full"]:
    CHECKS.append((("shape", key), "root", f"--{key}"))
for key in ["dur-1", "dur-2", "dur-3", "ease-out", "ease-in"]:
    CHECKS.append((("motion", key), "root", f"--{key}"))
for key in ["sticky", "dropdown", "drawer", "dialog", "toast"]:
    CHECKS.append((("z", key), "root", f"--z-{key}"))
for key in ["measure", "page", "control-h", "header-h", "section-pad", "row-pad"]:
    CHECKS.append((("layout", key), "root", f"--{key}"))
# hue + chroma-neutral meta
CHECKS.append((("color", "hue"), "root", "--hue"))
CHECKS.append((("color", "chroma-neutral"), "root", "--chroma-neutral"))


def dig(data, path):
    for step in path:
        if not isinstance(data, dict) or step not in data:
            return None
        data = data[step]
    return data


def main():
    css = BASE.read_text()
    root, light, dark = build_scopes(css)
    # "root" checks resolve var() too (section-pad = var(--space-8) etc.)
    scopes = {"root": light, "light": light, "dark": dark}
    export = json.loads(EXPORT.read_text())

    fails = []
    for path, scope_name, token in CHECKS:
        exported = dig(export, path)
        if exported is None:
            fails.append(f"MISSING in tokens.json: {'.'.join(path)}")
            continue
        actual = scopes[scope_name].get(token)
        if actual is None:
            fails.append(f"MISSING in base.css: {token} (looking for "
                         f"{'.'.join(path)})")
            continue
        if norm(str(exported)) != norm(str(actual)):
            fails.append(
                f"DRIFT {'.'.join(path)}: tokens.json has "
                f"'{norm(str(exported))}', base.css has '{norm(actual)}'")

    if fails:
        print(f"FAIL — {len(fails)} mismatch(es):")
        for f in fails:
            print(f"  - {f}")
        print("Fix the loser. Do not hand-edit around the drift.")
        return 1
    print(f"PASS — tokens.json matches base.css "
          f"({len(CHECKS)} values across light, dark, and the shared scales).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
