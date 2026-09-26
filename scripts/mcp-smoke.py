#!/usr/bin/env python3
"""mcp-smoke.py — prove the MCP shell speaks, and its token tool knows its names.

Drives scripts/mcp-server.py over stdio with a real JSON-RPC session and
asserts the documented contract: the three tools, the documented dotted
token names, the refusal of a hallucinated one, and the critique summary.
Exit 0 pass, 1 fail.
"""
import json
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SERVER = HERE / "mcp-server.py"

REQUESTS = [
    {"jsonrpc": "2.0", "id": 0, "method": "initialize",
     "params": {"protocolVersion": "2024-11-05", "capabilities": {},
                "clientInfo": {"name": "smoke", "version": "0"}}},
    {"jsonrpc": "2.0", "method": "notifications/initialized"},
    {"jsonrpc": "2.0", "id": 1, "method": "tools/list"},
    {"jsonrpc": "2.0", "id": 2, "method": "tools/call",
     "params": {"name": "token", "arguments": {"name": "color.light.ink"}}},
    {"jsonrpc": "2.0", "id": 3, "method": "tools/call",
     "params": {"name": "token", "arguments": {"name": "motion.dur-1"}}},
    {"jsonrpc": "2.0", "id": 4, "method": "tools/call",
     "params": {"name": "token", "arguments": {"name": "type.ramp.text-lg"}}},
    {"jsonrpc": "2.0", "id": 5, "method": "tools/call",
     "params": {"name": "token", "arguments": {"name": "space-4"}}},
    {"jsonrpc": "2.0", "id": 6, "method": "tools/call",
     "params": {"name": "token", "arguments": {"name": "gray-7"}}},
    {"jsonrpc": "2.0", "id": 7, "method": "tools/call",
     "params": {"name": "critique",
                "arguments": {"paths": [str(HERE / "fixtures" / "bad.html")]}}},
]


def main():
    proc = subprocess.run(
        [sys.executable, str(SERVER)],
        input="\n".join(json.dumps(r) for r in REQUESTS) + "\n",
        capture_output=True, text=True, timeout=60)
    replies = {}
    for line in proc.stdout.splitlines():
        try:
            r = json.loads(line)
        except ValueError:
            continue
        if isinstance(r, dict) and r.get("id") is not None:
            replies[r["id"]] = r
    problems = []

    def result(i):
        return replies.get(i, {}).get("result")

    def payload(i):
        for c in (result(i) or {}).get("content", []):
            if c.get("type") == "text":
                try:
                    return json.loads(c.get("text", ""))
                except ValueError:
                    return {}
        return None

    if 0 not in replies:
        problems.append("no initialize reply")
    elif (result(0) or {}).get("protocolVersion") != "2024-11-05":
        problems.append("server did not honor the requested protocol version")

    tools = [t.get("name") for t in (result(1) or {}).get("tools", [])]
    if sorted(tools or []) != ["critique", "list_rules", "token"]:
        problems.append("tools/list returned {!r}".format(tools))

    for i in (2, 3, 4, 5):
        p = payload(i)
        if not isinstance(p, dict) or not p.get("value"):
            problems.append("token lookup id {} did not resolve".format(i))

    if (result(6) or {}).get("isError") is not True:
        problems.append("gray-7 was not refused (hallucination guard)")

    p7 = payload(7)
    if not isinstance(p7, dict) or not isinstance(p7.get("summary"), dict) \
            or p7["summary"].get("errors", 0) < 1:
        problems.append("critique on the bad fixture did not report errors")

    if problems:
        for p in problems:
            print("FAIL  " + p)
        print("raw stdout tail:", proc.stdout[-400:])
        return 1
    print("PASS  MCP speaks; three tools; dotted names resolve; gray-7 refused; critique reports.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
