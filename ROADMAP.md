# Roadmap

Ambition parked where it cannot bloat the references. Each bet below waits
for a signal, and the signal is named. Anything not on this list and not in
the never list is probably a distraction — say so in an issue first.

## Shipped ahead of signal

Three bets left the table early, by owner decision, in 1.6.0 — the useful
release. The signals had not arrived; the owner's ask stood in for them,
and the record stays honest:

- **The DTCG export** (`references/tokens.dtcg.json`, written and verified
  by `scripts/export-dtcg.py`) — the Figma / Tokens Studio / Style
  Dictionary interop bet, pulled forward with its no-silent-omissions law
  intact.
- **Findings that teach** — every finding carries the registry's fix and
  reference; the registry refuses an entry that cannot teach. The `suggest`
  field the bet proposed turned out to already exist as `fix` + `reference`.
- **Release automation** — a `vX.Y.Z` tag hands the changelog section to the
  release workflow. The floating `v1` tag still moves by hand.

## Signal-gated bets

| Bet | Trigger | Shape |
|---|---|---|
| A chrome-devtools-mcp pairing recipe in `machines.md` | repeated "gate passes but the page looks wrong" reports | docs only: computed styles against `tokens.json`, mid-task |
| Translated READMEs | clustered non-English traffic, or ≥3 requests for one language | `README.<lang>.md`; the SKILL.md body stays English — the register is the judgment |
| Narrow direction proxies (a second accent hue with no written exception) | real reported misses, not vibes | one rule per miss; judgment stays human |
| Show HN and the agentskills.io showcase | an awesome-list merge, ≥100 skills.sh installs, a clean release | a launch, not a feature |
| skills.sh badge in the README | the listing exists (it needs real `npx skills add` installs first) | one badge line |

## Never

- **A component kit.** Not React, not Web Components, not a copy-paste
  components directory. That is shadcn's lane, and it forks taste every
  release; d-pill's own law is "do not invent a new checkbox."
- **A docs-framework site.** No Docusaurus, no build step. README, one demo
  page, and `llms.txt` are the right size for a design system.
- **An npm package for the engine.** The engine is Python's standard
  library; npx is a Node surface. Every real install surface is already
  covered — the skills CLI, the plugin marketplace, the Action, the clone.
  Revisit only on sustained non-Python demand.
- **CSS-framework positioning.** `base.css` serves the skill; the skill is
  not a CSS framework. That lane belongs to water.css, and it fades.
- **Editor extensions.** The audience is agents; impeccable already runs the
  17-harness playbook. A maintenance treadmill with zero differentiation.
- **A rule-count arms race.** 152 rules is not more honest than 16 verified
  ones. The selftest and the registry check are the credibility.
- **A machine taste score.** The machine half checks scales and floors;
  direction and focal point are the judgment half. A taste scorer
  manufactures false authority and destroys the product's philosophy.
- **Per-harness file forks** — `.cursor/rules`, `copilot-instructions`,
  AGENTS.md copies of the knowledge. One source of truth, three real
  surfaces (SKILL.md, `.claude-plugin`, `action.yml`). Fragmenting the
  system into per-agent files is the industry's problem, not the fix.

The test for any new file: it is verified in CI, or it is pull-not-push
prose an agent loads on demand, or it is an adoption surface with a named
owner. Otherwise it does not get added.
