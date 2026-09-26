#!/usr/bin/env python3
"""mcp-server.py — d-pill over the Model Context Protocol (stdio).

Zero dependencies: Python's standard library speaks JSON-RPC 2.0 over stdio
well enough for a tool server, which is the whole of MCP a checker needs.
No network, no subprocesses, no state — the same law as the rest of the repo.

Tools:
    critique    Run the machine gate on files or directories.
                args: {"paths": ["src/"], "allow": ["dpill/rule"], "strict": false}
    list_rules  The rule registry with severities and references.
    token       Read one value from references/tokens.json.
                args: {"name": "color.light.ink" | "space-4", "theme": "light"|"dark"}

Register with Claude Code:
    claude mcp add -s user dpill -- python3 /path/to/d-pill/scripts/mcp-server.py

Wire into any other MCP client the same way: command python3, args the path
to this file, transport stdio.
"""

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import critique  # noqa: E402

SERVER_INFO = {"name": "d-pill", "version": critique.VERSION}
PROTOCOL = "2025-06-18"
KNOWN_PROTOCOLS = ("2024-11-05", "2025-03-26", "2025-06-18")

TOOLS = [
    {
        "name": "critique",
        "description": "Run the d-pill machine gate on HTML/CSS paths. Returns "
                       "findings as file:line:col [rule] severity: message, plus a "
                       "summary. Exit semantics are folded into the payload: "
                       "errors>0 means fix before calling the UI done.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "paths": {"type": "array", "items": {"type": "string"},
                          "description": "Files or directories to check"},
                "allow": {"type": "array", "items": {"type": "string"},
                          "description": "Rule ids to suppress (a written exception)"},
                "strict": {"type": "boolean",
                           "description": "Warnings count as findings"},
            },
            "required": ["paths"],
        },
    },
    {
        "name": "list_rules",
        "description": "The d-pill rule registry: id, severity, target, summary, "
                       "fix, and the reference file behind each rule.",
        "inputSchema": {"type": "object", "properties": {}},
    },
    {
        "name": "token",
        "description": "Read one token value from the verified export "
                       "references/tokens.json. Exact dotted paths "
                       "('color.light.ink', 'motion.dur-1', 'type.ramp.text-lg'), "
                       "scale names ('space-4', 'text-lg', 'dur-1'), or a bare "
                       "role ('ink') with an optional theme.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "name": {"type": "string"},
                "theme": {"type": "string", "enum": ["light", "dark"]},
            },
            "required": ["name"],
        },
    },
]


def tool_critique(args):
    paths = args.get("paths") or []
    if not isinstance(paths, list) or not paths:
        return {"isError": True, "content": [_text(
            "critique needs a non-empty 'paths' array of files or directories.")]}
    allow = args.get("allow") or []
    strict = bool(args.get("strict"))
    broken = critique.unusable_paths(paths)
    if broken:
        return {"isError": True, "content": [_text(
            "not usable as HTML/CSS paths: " + "; ".join(broken))]}
    findings, stats, failed = critique.collect(paths, allow, strict)
    payload = {
        "summary": stats,
        "failed": failed,
        "findings": [f.data() for f in findings],
        "lines": [f.human() for f in findings],
        "note": "Fix every error before the work is called done; read every "
                "warning and either fix it or write the exception. The judgment "
                "half of the gate is references/critique.md — a clean machine "
                "pass is permission to be judged, not a pass.",
    }
    return {"content": [_text(json.dumps(payload, indent=2))]}


def tool_list_rules(_args):
    try:
        data = json.loads(critique.RULES_FILE.read_text())
    except (OSError, ValueError) as e:
        return {"isError": True, "content": [_text("rules.json unreadable: " + str(e))]}
    return {"content": [_text(json.dumps(data, indent=2))]}


def _dig(data, dotted):
    for step in dotted.split("."):
        if not isinstance(data, dict) or step not in data:
            return None
        data = data[step]
    return data


def tool_token(args):
    name = str(args.get("name", "")).strip()
    theme = args.get("theme")
    if theme not in ("light", "dark"):
        theme = None
    try:
        data = json.loads(critique.TOKENS_FILE.read_text())
    except (OSError, ValueError) as e:
        return {"isError": True, "content": [_text("tokens.json unreadable: " + str(e))]}
    # Resolution order: the exact dotted path as given, a theme-qualified
    # role, the light default, then the scale parents. Bare roles ('ink')
    # and dash names ('space-4', 'dur-1') resolve through the same list.
    leaf = name.split(".")[-1]
    candidates = [name]
    if theme:
        candidates.append("color." + theme + "." + leaf)
    candidates.append("color." + name)          # color.hue, color.chroma-neutral
    candidates.append("color.light." + leaf)    # bare role: ink, bg-subtle
    candidates.append("color.dark." + leaf)
    for prefix in ("space.scale", "type.ramp", "shape", "motion",
                   "z", "layout", "font"):
        candidates.append(prefix + "." + name)
    value = None
    resolved = None
    for c in candidates:
        v = _dig(data, c)
        if v is not None and not isinstance(v, dict):
            value, resolved = v, c
            break
    if value is None:
        return {"isError": True, "content": [_text(
            "no token named '{}' in the export. Exact names: 'space-4', "
            "'color.light.ink', 'motion.dur-1', 'type.ramp.text-lg', or a bare "
            "role ('ink') with an optional theme.".format(name))]}
    return {"content": [_text(json.dumps(
        {"name": name, "path": resolved, "value": value}, indent=2))]}


def _text(s):
    return {"type": "text", "text": s}


def dispatch(name, args):
    if name == "critique":
        return tool_critique(args)
    if name == "list_rules":
        return tool_list_rules(args)
    if name == "token":
        return tool_token(args)
    return {"isError": True, "content": [_text("unknown tool: " + name)]}


def respond(req):
    method = req.get("method", "")
    rid = req.get("id")
    if method == "initialize":
        requested = str((req.get("params") or {}).get("protocolVersion") or "")
        return _ok(rid, {
            "protocolVersion": requested if requested in KNOWN_PROTOCOLS else PROTOCOL,
            "capabilities": {"tools": {}},
            "serverInfo": SERVER_INFO,
        })
    if method == "ping":
        return _ok(rid, {})
    if method == "tools/list":
        return _ok(rid, {"tools": TOOLS})
    if method == "tools/call":
        params = req.get("params", {})
        result = dispatch(params.get("name", ""), params.get("arguments", {}) or {})
        return _ok(rid, result)
    if method.startswith("notifications/"):
        return None
    return {"jsonrpc": "2.0", "id": rid,
            "error": {"code": -32601, "message": "method not found: " + method}}


def _ok(rid, result):
    return {"jsonrpc": "2.0", "id": rid, "result": result}


def main():
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        try:
            req = json.loads(line)
        except ValueError:
            out = {"jsonrpc": "2.0", "id": None,
                   "error": {"code": -32700, "message": "parse error"}}
        else:
            try:
                out = respond(req)
            except Exception as e:  # the server never dies mid-conversation
                out = {"jsonrpc": "2.0", "id": req.get("id"),
                       "error": {"code": -32603, "message": "internal error: " + str(e)}}
        if out is not None:
            sys.stdout.write(json.dumps(out) + "\n")
            sys.stdout.flush()


if __name__ == "__main__":
    main()
