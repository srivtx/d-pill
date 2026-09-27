#!/usr/bin/env python3
"""export-dtcg.py — the DTCG export of the token system.

Writes references/tokens.dtcg.json, the Design Tokens Community Group shape
($value + $type per token), from references/tokens.json — the verified
export of base.css. Tokens Studio, Style Dictionary, and the Figma plugins
that speak the standard can consume it directly, so a design-tool pipeline
and the gate read the same numbers.

The law: no silent omissions. Every leaf in tokens.json must map to a DTCG
token (the documented prose notes excepted) or this script exits 1 — a new
token that nobody mapped is drift, not a default.

Usage:
    python3 scripts/export-dtcg.py           write the export
    python3 scripts/export-dtcg.py --check   verify the file on disk is true
"""

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TOKENS = ROOT / "references" / "tokens.json"
DTCG = ROOT / "references" / "tokens.dtcg.json"

# Prose notes inside tokens.json, not tokens. Anything else unmapped fails.
PROSE = {"color.hue-linked", "space.scale-px"}

BORDER_RE = re.compile(r"^(\S+)\s+(solid|dashed|dotted|double)\s+(.+)$")
SHADOW_RE = re.compile(r"^((?:-?[\d.]+(?:px)?\s+){1,4})(.+)$")
EASE_RE = re.compile(r"^cubic-bezier\(([^)]*)\)$")


def parse_border(value):
    m = BORDER_RE.match(value.strip())
    if not m:
        return None
    return {"lineWidth": m.group(1), "style": m.group(2), "color": m.group(3).strip()}


def parse_shadow(value):
    m = SHADOW_RE.match(value.strip())
    if not m:
        return None
    nums = [n.strip() for n in m.group(1).split()]
    nums += ["0"] * (4 - len(nums))
    x, y, blur, spread = [n if n.endswith("px") else n + "px" for n in nums]
    return [{"offsetX": x, "offsetY": y, "blur": blur, "spread": spread,
             "color": m.group(2).strip()}]


def parse_easing(value):
    m = EASE_RE.match(value.strip())
    if not m:
        return None
    return [float(p.strip()) for p in m.group(1).split(",")]


def parse_font_stack(value):
    return [part.strip().strip('"') for part in value.split(",")]


def token(value, typ, description=None):
    out = {"$type": typ, "$value": value}
    if description:
        out["$description"] = description
    return out


def build():
    """The DTCG document, or (None, problems) if a leaf will not map."""
    data = json.loads(TOKENS.read_text())
    problems = []
    mapped = set()
    out = {}

    color = data["color"]
    light, dark = {}, {}
    for role, value in color["light"].items():
        if role in ("border", "border-strong"):
            b = parse_border(value)
            if b is None:
                problems.append("unparsable border: color.light.{} = {!r}".format(role, value))
                continue
            light[role] = token(b, "strokeStyle")
        elif role == "shadow-overlay":
            s = parse_shadow(value)
            if s is None:
                problems.append("unparsable shadow: color.light.{}".format(role))
                continue
            light[role] = token(s, "shadow")
        else:
            light[role] = token(value, "color")
        mapped.add("color.light." + role)
    for role, value in color["dark"].items():
        if role in ("border", "border-strong"):
            b = parse_border(value)
            if b is None:
                problems.append("unparsable border: color.dark.{}".format(role))
                continue
            dark[role] = token(b, "strokeStyle")
        elif role == "shadow-overlay":
            s = parse_shadow(value)
            if s is None:
                problems.append("unparsable shadow: color.dark.{}".format(role))
                continue
            dark[role] = token(s, "shadow")
        else:
            dark[role] = token(value, "color")
        mapped.add("color.dark." + role)
    out["color"] = {
        "light": token_group(light, "The role palette in its light state. Pairs "
                                    "with dark; emit one or neither."),
        "dark": token_group(dark, "The role palette in its dark state. Pairs "
                                  "with light; emit one or neither."),
        "hue": token(float(color["hue"]), "number",
                     "The one re-tint value. Change hue alone; the lightness "
                     "and chroma structure stays."),
        "chroma-neutral": token(float(color["chroma-neutral"]), "number",
                                "The chroma of the neutral surfaces."),
    }
    mapped.update({"color.hue", "color.chroma-neutral"})

    fonts = {}
    for name, stack in data["font"].items():
        fonts[name] = token(parse_font_stack(stack), "fontFamily")
        mapped.add("font." + name)
    out["font"] = token_group(fonts)

    ramp = {}
    for name, size in data["type"]["ramp"].items():
        ramp[name] = token(size, "dimension")
        mapped.add("type.ramp." + name)
    typ = {"ramp": token_group(ramp, "The type ramp. 16px is the coarse-pointer "
                                    "input exception, not a text size.")}
    for name, value in data["type"].items():
        if name == "ramp":
            continue
        if name.startswith("leading"):
            typ[name] = token(float(value), "number",
                              "Line height as a unitless ratio.")
        else:
            typ[name] = token(value, "dimension")
        mapped.add("type." + name)
    out["type"] = token_group(typ)

    scale = {}
    for name, size in data["space"]["scale"].items():
        scale[name] = token(size, "dimension")
        mapped.add("space.scale." + name)
    out["space"] = token_group({"scale": token_group(
        scale, "The space scale. Most steps go unused on a given screen; the "
               "unused space is the design.")})

    shape = {}
    for name, size in data["shape"].items():
        shape[name] = token(size, "dimension")
        mapped.add("shape." + name)
    out["shape"] = token_group(shape, "Corner radii. radius-full is the circle.")

    motion = {}
    for name, value in data["motion"].items():
        if name.startswith("dur"):
            motion[name] = token(value, "duration")
        else:
            pts = parse_easing(value)
            if pts is None:
                problems.append("unparsable easing: motion.{} = {!r}".format(name, value))
                continue
            motion[name] = token(pts, "cubicBezier")
        mapped.add("motion." + name)
    out["motion"] = token_group(motion, "Durations for interactions; easings as "
                                        "system curves. Ambient loops are a "
                                        "written exception, not a token.")

    z = {}
    for name, value in data["z"].items():
        z[name] = token(int(value), "number",
                        "A layer declares itself; 9999 is an unmapped stack.")
        mapped.add("z." + name)
    out["z"] = token_group(z)

    layout = {}
    for name, value in data["layout"].items():
        layout[name] = token(value, "dimension")
        mapped.add("layout." + name)
    out["layout"] = token_group(layout)

    # The law: every leaf in tokens.json is mapped or the export refuses.
    for path, _value in leaves(data):
        if path in PROSE:
            continue
        if path not in mapped:
            problems.append("tokens.json leaf not exported: " + path)
    if problems:
        return None, problems
    return out, []


def token_group(tokens, description=None):
    out = dict(tokens)
    if description:
        out = {"$description": description}
        out.update(tokens)
    return out


def leaves(node, prefix=""):
    for key, value in node.items():
        if key.startswith("$"):
            continue
        path = prefix + key
        if isinstance(value, dict):
            for p, v in leaves(value, path + "."):
                yield p, v
        else:
            yield path, value


def count_tokens(node):
    """Count DTCG tokens: nodes carrying $value."""
    if isinstance(node, dict):
        if "$value" in node:
            return 1
        return sum(count_tokens(v) for v in node.values())
    return 0


def render(doc):
    top = {
        "$description": "d-pill design tokens — the DTCG export of "
                        "references/tokens.json, the verified export of "
                        "base.css. Generate: python3 scripts/export-dtcg.py. "
                        "Verify: python3 scripts/export-dtcg.py --check.",
        "$schema": "https://tr.designtokens.org/format/",
    }
    top.update(doc)
    return json.dumps(top, indent=2, ensure_ascii=False) + "\n"


def main(argv):
    if "--check" in argv[1:]:
        doc, problems = build()
        if doc is None:
            print("FAIL — the export cannot be built:")
            for p in problems:
                print("  - " + p)
            return 1
        try:
            on_disk = json.loads(DTCG.read_text())
        except (OSError, ValueError) as e:
            print("FAIL — tokens.dtcg.json is unreadable: {}".format(e))
            return 1
        fresh = json.loads(render(doc))
        if on_disk != fresh:
            print("FAIL — tokens.dtcg.json has drifted from tokens.json.")
            print("Regenerate: python3 scripts/export-dtcg.py")
            return 1
        count = count_tokens(fresh)
        print("PASS — tokens.dtcg.json is the DTCG shape of tokens.json "
              "({} tokens, types verified).".format(count))
        return 0
    doc, problems = build()
    if doc is None:
        print("FAIL — the export cannot be built:")
        for p in problems:
            print("  - " + p)
        return 1
    DTCG.write_text(render(doc), encoding="utf-8")
    count = count_tokens(json.loads(render(doc)))
    print("WROTE {} ({} tokens). Verify with: "
          "python3 scripts/export-dtcg.py --check".format(DTCG, count))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
