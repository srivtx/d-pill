# Machines

This system is read by two audiences now: the person who ships the page, and the agent or pipeline that composes it. The machine audience has its own failure modes — hallucinated token names, invented spacing, screenshot "verification." This file is how d-pill stays machine-usable without becoming machine-shaped.

## Two files

- A design system for agents is two artifacts: a values file a program can read without judgment, and a rules file that says when each value applies. `references/tokens.json` is the values. This repo is the rules.
- Values answer "what is the step." Rules answer "when the step changes." A pipeline with only values ships correct-looking spacing in the wrong rhythm; a pipeline with only rules guesses the values.
- `base.css` is the authority. `tokens.json` is the export. When they disagree, one of them is wrong; run `scripts/check-tokens.py`, fix the loser, and do not hand-edit around it.

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

- Assert computed styles: `getComputedStyle(el).getPropertyValue('font-family')` matches the committed stack; the `--hue` var resolves to the direction's hue. A page can render and pass a screenshot while its stylesheet 404'd — invalid vars cascade silently to inherited values.
- Assert geometry: equal cards measure equal heights; the focus ring is drawn on every interactive element at both themes; nothing under a streaming block moves between two frames.
- Assert both themes: flip `data-theme` and re-run the same assertions. Dark is not a bonus.
- Assert the export: `python3 scripts/check-tokens.py` exits 0. If the machine export has drifted from `base.css`, the drift is the bug.
- Pair every visual check with a programmatic one before calling it verified. The lesson is general: rendered-looking output and correct output are different claims.

## An index for machines

- `llms.txt`-style indexes exist so a crawler or agent can find the rules without reading the repo: one line per file, path and what it decides. In this repo, that index is the routing table in `SKILL.md`. Keep it true: every file reachable, every row loadable on demand, no row pointing at a file that does not carry its weight.
- Progressive disclosure is the loading contract: the frontmatter description is the trigger, `SKILL.md` is the assignment, a reference file is the depth. Depth is pulled when the task touches it, not as homework. This file is only read when the consumer is a machine.
