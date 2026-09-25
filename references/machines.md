# Machines

This system is read by two audiences now: the person who ships the page, and the agent or pipeline that composes it. The machine audience has its own failure modes — hallucinated token names, invented spacing, screenshot "verification." This file is how d-pill stays machine-usable without becoming machine-shaped.

## Two files

- A design system for agents is two artifacts: a values file a program can read without judgment, and a rules file that says when each value applies. `references/tokens.json` is the values. This repo is the rules.
- Values answer "what is the step." Rules answer "when the step changes." A pipeline with only values ships correct-looking spacing in the wrong rhythm; a pipeline with only rules guesses the values.
- `base.css` is the authority. `tokens.json` is the export. When they disagree, one of them is wrong; run `scripts/check-tokens.py`, fix the loser, and do not hand-edit around it.

## The gate

The rules also have a machine half now: `scripts/critique.py` checks written HTML and CSS against the token scales and the access floors. It is the same law, executable.

- The rules are data: `references/rules.json` is the registry — id, severity, target, what the engine checks, the fix, the reference file behind the rule. The engine verifies the registry matches its implementation before every run and refuses to run an unverified rule set. Drift between engine and registry is the bug, same as drift between `base.css` and the export.
- The values it checks are the values in `tokens.json`. Change the export, and the gate changes with it. There is no second set of numbers anywhere.
- Findings are `file:line:col [dpill/rule] severity: message`, one per line, on stderr. Exit 0 clean, 2 findings, 1 the invocation itself is broken. `--json` for pipelines, `--quiet` errors-only, `--strict` warnings-count, `--list-rules` the registry.
- Suppression is a written exception: `--allow dpill/z-off-scale` once, with the reason in the commit that uses it. A suppression that lives in someone's memory is a rule that no longer exists.
- The honest scope: the machine checks scales (space, ramp, radius, duration, z), floors (alt, lang, names, hairlines), and tells (transition-all, literal colors). Direction, focal point, one material, one weather — that is the judgment half in `references/critique.md`. Zero machine findings is permission to be judged, not a pass.

## Writing rules agents can follow

Agents read everything they are given. They do not skim, and they do not infer politely. Write for that reader:

- Explicit beats convenient. Name the exact token (`--space-4`), the exact class (`.lede`), the exact script (`scripts/contrast.py`). "Use tighter spacing" is not a rule; it is a mood.
- One rule per line. A paragraph hiding three rules produces three failures with one signature.
- Tables for mappings: role to token, condition to treatment. Tables are the format machines parse without loss.
- Refusals are imperative lists. An agent cannot derive "don't" from praise of the opposite.
- Precise errors beat forgiving defaults: "fails; run `scripts/contrast.py text …`" — not "might look off."
- State the gate, not the vibe: "clears 4.5:1" is checkable; "feels readable" is not.
- The floor test for a rule: could an agent verify it on the rendered page with a computed style, a geometry measurement, or a grep? If not, rewrite it until it can.

## Token discipline

- Use the exact names. `--space-4`, not `space-4`, `spacing.4`, or a nearby 17px. A value outside the scale is a new token decision, written down the way `systems.md` says.
- Never invent a parallel set. `foundations.md` already refuses `--gray-7` and a hex beside a role; the same refusal covers JSON-shaped parallel sets (`{ gray: { 7: … } }`).
- Theme pairs travel together. If you emit `--ink` for light, you emit its dark counterpart from the same export, or you emit neither.
- A hue change is one value: `--hue`. The chroma and lightness structure stays. Agents re-derive, they do not re-tint.

## Feeding another tool

- A pipeline consuming `tokens.json` should treat the `light` and `dark` groups as one palette in two states, the `hue-linked` note as a substitution instruction, and everything else as fixed.
- A code generator maps roles to component props, not to new names: `--danger` is the destructive fill, `--accent` is the one primary action, `--ok` and `--warn` are status text. The roles table in `foundations.md` is the contract.
- A template engine should consume `.stack`, `.section`, `.rows`, `.cluster`, `.quiet`, `.caps` as the structural vocabulary instead of re-deriving layout from raw spacing. The classes already encode the rhythm rules.
- When the target stack cannot hold OKLCH, convert once at build time, note the loss, and check the floors with `scripts/contrast.py` after conversion. Do not hand-tune per channel.

## Verification

A screenshot is evidence of pixels, not of correctness. Verify like a machine:

- Run the gate on the written files: `python3 scripts/critique.py src/`. Fix every finding before anything else claims to be verified.
- Assert computed styles: `getComputedStyle(el).getPropertyValue('font-family')` matches the committed stack; the `--hue` var resolves to the direction's hue. A page can render and pass a screenshot while its stylesheet 404'd — invalid vars cascade silently to inherited values.
- Assert geometry: equal cards measure equal heights; the focus ring is drawn on every interactive element at both themes; nothing under a streaming block moves between two frames.
- Assert both themes: flip `data-theme` and re-run the same assertions. Dark is not a bonus.
- Assert the export: `python3 scripts/check-tokens.py` exits 0. If the machine export has drifted from `base.css`, the drift is the bug.
- Pair every visual check with a programmatic one before calling it verified. The lesson is general: rendered-looking output and correct output are different claims.

## Wiring it in

One engine, three shells. The CLI is the engine; the others are thin skins over the same `collect()` call.

**Hooks (Claude Code).** A `PostToolUse` hook runs the gate on every write; exit code 2 routes stderr back into the agent as the reason to react:

```json
{
  "hooks": {
    "PostToolUse": [{
      "matcher": "Edit|Write",
      "hooks": [{
        "type": "command",
        "command": "python3 ~/.claude/skills/d-pill/scripts/critique.py \"$CLAUDE_FILE_PATHS\" || true"
      }]
    }]
  }
}
```

A `Stop` hook with the same command (no `|| true`) closes the loop: the task does not end while findings exist. Findings reach the agent as `file:line:col [rule] severity: message` — one rule per line, a message that names the fix.

**MCP.** `scripts/mcp-server.py` speaks JSON-RPC 2.0 over stdio on the standard library alone — no SDK, no network, auditable in one file. Three tools: `critique` (paths, allow, strict), `list_rules` (the registry), `token` (exact names from the export; `gray-7` is an error, not a guess). Register:

```
claude mcp add -s user dpill -- python3 /path/to/d-pill/scripts/mcp-server.py
```

Any MCP client takes the same command. The server never dies mid-conversation: internal errors return as JSON-RPC errors, and the conversation continues.

**CI.** This repository is itself an action, so the gate is one line in any workflow:

```yaml
- uses: srivtx/d-pill@v1
  with:
    paths: src/,docs/
```

The inputs are the CLI's: `paths`, `allow`, `strict`. A red check is a finding list, not a screenshot. This repo's own CI runs the whole contract on every push: the export is true, the registry agrees with the engine, every rule fires where it should, the demo and the law pass their own gate, and the demo's stylesheet has not drifted from the authority.

## An index for machines

- `llms.txt`-style indexes exist so a crawler or agent can find the rules without reading the repo: one line per file, path and what it decides. This repo ships one at the root, and the routing table in `SKILL.md` is the same idea for a reader already inside. Keep both true: every file reachable, every row loadable on demand, no row pointing at a file that does not carry its weight.
- The frontmatter is the standard's closed field set (name, description, license, compatibility, metadata, allowed-tools); anything else is dropped silently by tooling that follows the spec. Triggers live in `description` — it is the listing and the switch. `references/rules.json` and `scripts/critique.py` carry the gate; they travel with the repo, not with the harness.
- Progressive disclosure is the loading contract: the frontmatter description is the trigger, `SKILL.md` is the assignment, a reference file is the depth. Depth is pulled when the task touches it, not as homework. This file is only read when the consumer is a machine.
