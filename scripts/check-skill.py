#!/usr/bin/env python3
"""check-skill.py — the skill file is spec-legal and the versions agree.

Two failure modes, each of which has happened once: frontmatter that drifts
off the agentskills.io closed field set, and a version that disagrees
between SKILL.md, the plugin manifests, and the engine. Exit 0 pass, 1 fail.
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SPEC_KEYS = {"name", "description", "license", "compatibility", "metadata",
             "allowed-tools"}


def read_frontmatter():
    text = (ROOT / "SKILL.md").read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        return None, text
    fm = m.group(1)
    try:
        import yaml
        return yaml.safe_load(fm), text
    except ImportError:
        pass
    # Folded-scalar fallback, no dependencies: parse the keys the spec allows.
    data, desc, collecting = {}, [], False
    for ln in fm.splitlines():
        if re.match(r"^[A-Za-z_-]+:", ln):
            if collecting:
                data["description"] = " ".join(desc)
                collecting = False
            key, _, rest = ln.partition(":")
            if key == "description" and rest.strip() in (">", ">-", "|", "|-"):
                collecting = True
            elif rest.strip():
                data[key] = rest.strip().strip("'\"")
        elif collecting and ln.startswith("  "):
            desc.append(ln.strip())
    if collecting:
        data["description"] = " ".join(desc)
    return data, text


def main():
    problems = []
    data, text = read_frontmatter()
    if not isinstance(data, dict) or not data:
        print("FAIL  SKILL.md frontmatter is unreadable")
        return 1

    name = str(data.get("name", ""))
    if not re.fullmatch(r"[a-z0-9-]{1,64}", name):
        problems.append("name {!r} violates the spec (<=64 chars, [a-z0-9-])".format(name))
    if name != ROOT.name:
        problems.append("name {!r} must match the skill directory {!r}".format(name, ROOT.name))

    desc = str(data.get("description", ""))
    if not desc:
        problems.append("description is required (it is the trigger)")
    elif len(desc) > 1024:
        problems.append("description is {} chars; the spec max is 1024".format(len(desc)))

    extra = set(data) - SPEC_KEYS
    if extra:
        problems.append("off-spec frontmatter keys, dropped silently by strict clients: "
                        + ", ".join(sorted(extra)))

    meta = data.get("metadata")
    if meta is not None and (not isinstance(meta, dict)
                             or not all(isinstance(v, str) for v in meta.values())):
        problems.append("metadata must be a map of string -> string")

    versions = {}
    if isinstance(meta, dict) and "version" in meta:
        versions["SKILL.md"] = str(meta["version"])
    engine = re.search(r'^VERSION = "([^"]+)"',
                       (ROOT / "scripts/critique.py").read_text(encoding="utf-8"), re.M)
    if engine:
        versions["scripts/critique.py"] = engine.group(1)
    try:
        versions[".claude-plugin/plugin.json"] = str(
            json.loads((ROOT / ".claude-plugin/plugin.json").read_text(encoding="utf-8")).get("version", ""))
    except (OSError, ValueError):
        problems.append(".claude-plugin/plugin.json is unreadable")
    try:
        market = json.loads((ROOT / ".claude-plugin/marketplace.json").read_text(encoding="utf-8"))
        versions[".claude-plugin/marketplace.json"] = str(market["plugins"][0].get("version", ""))
    except (OSError, ValueError, KeyError, IndexError):
        problems.append(".claude-plugin/marketplace.json is unreadable or has no plugins[0]")
    if versions and len(set(versions.values())) > 1:
        problems.append("versions disagree: "
                        + ", ".join("{}={}".format(k, v) for k, v in versions.items()))

    body = text.split("---", 2)[-1]
    if len(body.splitlines()) >= 500:
        problems.append("SKILL.md body is {} lines; the spec recommends <500".format(len(body.splitlines())))

    if problems:
        for p in problems:
            print("FAIL  " + p)
        return 1
    agreed = next(iter(versions.values())) if versions else "(no version found)"
    print("PASS  SKILL.md is spec-legal; versions agree at {}".format(agreed))
    return 0


if __name__ == "__main__":
    sys.exit(main())
