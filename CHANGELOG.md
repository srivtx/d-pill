# Changelog

d-pill versions its releases. Every version lands in the same commit as the
SKILL.md, plugin, and engine versions it ships — `scripts/check-skill.py`
enforces the agreement in CI.

## 1.5.1 — 2026-09-27

The robustness release. The engine is stricter and more honest, the repo
verifies more of itself, and the site has one deployment path.

- The gate refuses a broken invocation: a path that does not exist, or is not
  HTML/CSS, now exits 1 instead of silently checking nothing and passing.
- Durations and easings can no longer hide beside a `var()`: literal ms/s
  values next to token references are checked, animation shorthand easing is
  checked, and `linear` in an animation is treated as constant velocity, not
  a curve. The inline-token-bypass rule no longer fires on `var()` values —
  a token reference is not a bypass.
- The MCP `token` tool resolves its own documented names — `color.light.ink`,
  `motion.dur-1`, `type.ramp.text-lg`, bare roles with a theme, `color.hue` —
  and reports the resolved path. The server honors a client-requested
  protocol version. The critique tool refuses unusable paths.
- The Soft editorial recipe no longer fails its own gate: ambient loops run
  on named clocks (`--loop-*`) — the written exception — the equalizer bars
  are pills, and the micro-gaps are token-derived. The proof page moved to
  `docs/soft.html`, gated in CI, live on the site.
- One Pages deployment path: branch `main` / `docs`, served as written. The
  stock Jekyll workflow, which built the repo root and raced the branch
  deploy on every push, is gone.
- `action.yml` passes inputs through the environment, not string
  interpolation into the script.
- New guards in CI: `scripts/check-skill.py` (frontmatter spec + version
  agreement) and `scripts/mcp-smoke.py` (a real JSON-RPC session, including
  the hallucination refusal).
- The install path in the README and demo is the multi-agent
  `~/.agents/skills` (Claude Code: `~/.claude/skills`), and the gate example
  output is verbatim.
- Prose reconciled: type.md, direction.md, mobile.md, craft.md, details.md,
  and sense.md one-liners now agree with the tokens and with each other.

## 1.5.0 — the gate

The critique became executable and the system became machine-readable: rules
as data (`references/rules.json`), a zero-dependency engine with an
exit-code contract (`scripts/critique.py`), an MCP server
(`scripts/mcp-server.py`), this repository as a GitHub Action (`action.yml`),
a Claude Code plugin marketplace (`.claude-plugin/`), `llms.txt`, and a demo
page that passes its own gate in CI. AI-native interfaces and the 2025–26
frontier catalog, each move with an entry gate. Earlier history: `git log`.
