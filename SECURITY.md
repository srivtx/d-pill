# Security

d-pill is deterministic and offline by design.

- The scripts are Python's standard library and nothing else: no network
  calls, no subprocesses, no eval, no file writes. `scripts/critique.py`,
  `scripts/mcp-server.py`, `scripts/check-tokens.py`,
  `scripts/check-skill.py`, `scripts/mcp-smoke.py`, and
  `scripts/contrast.py` are each auditable in one sitting.
- The MCP server speaks JSON-RPC 2.0 over stdio only. It never opens a
  socket and never executes shell commands; internal errors return as
  protocol errors rather than crashing the session.
- The GitHub Action runs the engine on the paths you name. Inputs enter
  through the environment, never interpolated into the script — caller data
  stays data.
- Tokens and rules are data (`references/tokens.json`,
  `references/rules.json`), verified against their sources in CI on every
  push. The engine refuses to run an unverified rule set.

To report a vulnerability, use GitHub Security Advisories ("Report a
vulnerability") on this repository — not a public issue. Reports are
answered in kind: no network, no telemetry, no surprises.
