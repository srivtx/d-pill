<p align="center">
  <img src="assets/mark.svg" width="220" height="88" alt="d-pill, an iridescent capsule">
</p>

<h1 align="center">d-pill</h1>

<p align="center">
  A design skill for agents that build interfaces.<br>
  The rules, the values, and the check — in one repository.
</p>

<p align="center">
  <a href="LICENSE"><img alt="MIT license" src="https://img.shields.io/badge/license-MIT-1a1814?style=flat-square"></a>
  <img alt="Skill format" src="https://img.shields.io/badge/format-SKILL.md-1a1814?style=flat-square">
  <img alt="Ten directions" src="https://img.shields.io/badge/directions-10-1a1814?style=flat-square">
  <img alt="Machine-readable tokens" src="https://img.shields.io/badge/tokens-machine--readable-1a1814?style=flat-square">
  <a href="https://github.com/srivtx/d-pill/actions/workflows/ci.yml"><img alt="gate" src="https://img.shields.io/github/actions/workflow/status/srivtx/d-pill/ci.yml?label=gate&style=flat-square"></a>
</p>

d-pill is how an agent should see, decide, and build a page. It is not a component kit and not a theme. The agent commits to one visual direction, sets type and color as roles, and passes a critique before calling the work done.

When a brand already exists, d-pill keeps the type and the color and fixes structure, hierarchy, states, and copy. When nothing has been chosen, it refuses the unset look: an interchangeable sans, a purple gradient, three equal cards, everything centered.

## Install

Any agent that loads a `SKILL.md` from a folder:

```bash
git clone https://github.com/srivtx/d-pill.git ~/.grok/skills/d-pill
```

Any skills runner (Claude, Cursor, Codex, Copilot, and others):

```bash
npx skills add srivtx/d-pill
```

Claude Code, as a plugin marketplace:

```
/plugin marketplace add srivtx/d-pill
/plugin install d-pill@d-pill
```

Then ask for the interface, or run `/d-pill`. The procedure is `SKILL.md`. The knowledge is `references/`. The demo page is [`docs/index.html`](docs/index.html) — it passes its own gate, in CI, on every push.

## The gate

Most design systems are reading material. This one is executable. `scripts/critique.py` checks written HTML and CSS against d-pill's own token scales and access floors:

```
$ python3 scripts/critique.py src/

src/orders.css:41:8 [dpill/space-off-scale] error: 17px in padding is not on
  the space scale (4px 8px 12 16 24 32 48 64 96 128 px). Use the token, or
  write the exception down.
src/orders.css:42:3 [dpill/transition-all] error: transition: all animates
  layout. Name the properties that actually change.

2 files checked — 2 error(s), 0 warning(s); exit 2.
```

- **Rules as data.** The registry is `references/rules.json` — id, severity, what the engine checks, the fix, the reference behind each rule. The engine verifies the registry matches its implementation before every run, the same way `check-tokens.py` verifies the token export against `base.css`.
- **The values are the export.** The scales the gate checks come from `tokens.json`. Change the export, the gate changes with it. No second set of numbers anywhere.
- **The contract.** Findings on stderr as `file:line:col [rule] severity: message`. Exit 0 clean, 2 findings, 1 broken invocation. `--json` for pipelines, `--allow` for written exceptions, `--selftest` to prove every rule fires.
- **Zero dependencies.** Python's standard library and nothing else. Offline, auditable in one file.

The same engine, three shells: the CLI; `scripts/mcp-server.py`, a stdlib-only MCP server (`claude mcp add -s user dpill -- python3 …/scripts/mcp-server.py`) with `critique`, `list_rules`, and `token` tools; and this repository is itself a GitHub Action:

```yaml
- uses: srivtx/d-pill@v1
  with:
    paths: src/
```

For the wiring details — Claude Code `PostToolUse`/`Stop` hooks that feed findings back to the agent — read `references/machines.md`.

The number behind the gate: a 2026 audit of 375 production sites found average design-token coverage of 40.4% and 17,731 hardcoded values; only 7.5% of sites stayed above 90% coverage. Drift is not a vibe — it is counted, and nothing on the market closes it for agent-built pages. The critique has always had a judgment half; now it has a machine half, and the machine half travels with the skill.

## What the agent does

1. Names the job in one sentence. Who is here, what they do, what done feels like.
2. Commits to a named style if they gave one, otherwise to one of ten directions, and writes down what it is refusing.
3. Composes the page as a poster: uneven on purpose, one material, the headline set by hand.
4. Builds it from the tokens and classes in `references/base.css`, in whatever stack the repo already has.
5. Passes the gate: `scripts/critique.py` exits 0 on the written files, then the checklist in `references/critique.md` at a wide window and at 390px. A fail gets fixed before the work is called done.

Text has to clear 4.5:1. Control edges and the focus ring have to clear 3:1. The default palette was checked with `scripts/contrast.py` before it shipped. A color outside the safe band gets checked again.

## What it covers

Interfaces a person uses, and the new frontier: chat surfaces, copilots, agent consoles, streaming answers, tool-call and approval UI, and generative UI — the rules are in `references/ai-interfaces.md`, gated by `references/critique.md`.

The 2025–26 moves are catalogued with entry gates in `references/frontier.md` — barely-there chrome, micro-interaction density, scrollytelling, page-transition identity, expressive letters, shader heroes, generative imagery, liquid glass, dense dark tools, adaptive pages. A trend that cannot write its own commitment paragraph is a vibe.

And the whole system is machine-readable: `references/tokens.json` is the verified export of `base.css`, `references/rules.json` is the verified rule registry, and `references/machines.md` is how pipelines, hooks, MCP clients, and coding agents consume the values and the rules without inventing parallel token names.

## Directions

The ten directions are the starting points. A named style (Swiss, Didone, a zine, a label, a terminal, a poster) is a harder commitment, in `references/styles.md`. The agent does not sand that request down into a generic app.

| Direction | For |
|---|---|
| Instrument | A tool someone uses every day |
| Spec | Rows of figures, logs, records |
| Editorial | A front page with a point of view |
| Atelier | A small set of work, hung rather than framed |
| Quiet luxury | Something expensive and still |
| Soft service | Health, school, care, a local business |
| Signal | A technical product, dark, precise |
| Civic | A public institution or a public dataset |
| Broadsheet | Long reading |
| Play | When delight is the product |

One direction per surface. The only mix allowed is a single borrowed slot, written down. A real brand beats the catalog.

## The system

Read `SKILL.md` first. It says which file to open. Do not load all of them for a button.

| File | Owns |
|---|---|
| `SKILL.md` | Procedure, laws, what to read |
| `references/sense.md` | Seeing: proportion, material, the headline, what to leave out |
| `references/taste.md` | The judgment: effort hidden, one weather, finish |
| `references/styles.md` | The styles: book, poster, object, screen, and the memes done properly |
| `references/faces.md` | How to judge a typeface and which class it is |
| `references/grids.md` | Manuscript, column, modular, and hierarchical grids |
| `references/harmony.md` | How hues relate: mono, analogous, complement, spectrum |
| `references/proportion.md` | Size relationships, rhythm, the first screen |
| `references/patterns.md` | Master-detail, filters, pagination, calendar, consent |
| `references/type.md` | Setting type: pairing, leading, rag, figures |
| `references/color.md` | Judging color: value, temperature, dark themes |
| `references/geometry.md` | Optical alignment, radius, bleed, crops |
| `references/details.md` | Hairlines, focus, press, skeletons |
| `references/behavior.md` | Distance, choice, scent, trust |
| `references/narrative.md` | How a page argues, and how pictures behave |
| `references/art.md` | Light, grade, crop, and when to have no picture |
| `references/arrange.md` | Which container: list, table, gallery, form, feed |
| `references/world.md` | Other languages, RTL, longer text, locale marks |
| `references/brand.md` | Marks, lockups, clear space, misuse |
| `references/icons.md` | Drawing a set that looks like one hand |
| `references/dataviz.md` | Charts and tables that tell the truth |
| `references/information.md` | Diagrams, steps, wayfinding |
| `references/commerce.md` | Product, bag, checkout |
| `references/mobile.md` | The phone as its own composition |
| `references/a11y.md` | Access as a design constraint |
| `references/formats.md` | Portfolio, event, help, changelog, status, account, inbox |
| `references/systems.md` | Adding tokens and components without forking |
| `references/direction.md` | The ten directions and their CSS |
| `references/foundations.md` | How to edit tokens |
| `references/base.css` | The tokens and the classes |
| `references/layout.md` | Primitives, density, breakpoints |
| `references/components.md` | Controls, overlays, anatomy |
| `references/interaction.md` | Time, forms, failure, motion, streaming, libraries, the craft exception |
| `references/soft.md` | The craft site: soft surfaces, status strip, pixel accents, its motion and override |
| `references/ai-interfaces.md` | Chat, copilots, agent actions, streaming stability, approvals, generative UI |
| `references/machines.md` | The machine contract: the gate, hooks, MCP, CI, verification |
| `references/tokens.json` | The machine-readable token export, verified against `base.css` |
| `references/rules.json` | The machine-readable rule registry, verified against the engine |
| `references/frontier.md` | The 2025–26 moves, each with a gate and a refuse list |
| `references/craft.md` | The visual tells and the fix for each |
| `references/surfaces.md` | App, marketing, dashboard, docs, auth |
| `references/writing.md` | Words on the interface |
| `references/critique.md` | The judgment half of the gate |
| `references/reading.md` | The sources behind the judgments |
| `scripts/critique.py` | The machine half of the gate: the checker |
| `scripts/mcp-server.py` | d-pill over MCP: critique, list_rules, token |
| `scripts/check-tokens.py` | Verifies `tokens.json` against `base.css` |
| `scripts/contrast.py` | Contrast for a custom OKLCH pair |
| `action.yml` | This repo as a GitHub Action: the gate in CI |
| `llms.txt` | The index for crawlers and agents |
| `assets/mark.svg` | The mark |

## Use the stylesheet

`references/base.css` is the implementation: roles, type ramp, space scale, focus, and the classes (`.stack`, `.cluster`, `.split`, `.rows`, `.display`). Paste a direction's override after it. Do not invent a second set of names beside it.

Space is a fixed scale: 4, 8, 12, 16, 24, 32, 48, 64, 96, 128. Most of those steps go unused on a given screen. That unused space is the design.

## License

[MIT](LICENSE)
