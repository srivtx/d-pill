<p align="center">
  <img src="assets/mark.svg" width="220" height="88" alt="d-pill, an iridescent capsule">
</p>

<h1 align="center">d-pill</h1>

<p align="center">
  A design skill for agents that build interfaces.
</p>

<p align="center">
  <a href="LICENSE"><img alt="MIT license" src="https://img.shields.io/badge/license-MIT-1a1814?style=flat-square"></a>
  <img alt="Skill format" src="https://img.shields.io/badge/format-SKILL.md-1a1814?style=flat-square">
  <img alt="Ten directions" src="https://img.shields.io/badge/directions-10-1a1814?style=flat-square">
  <img alt="Contrast floors checked" src="https://img.shields.io/badge/contrast-checked-c4552a?style=flat-square">
</p>

d-pill is how an agent should see, decide, and build a page. It is not a component kit and not a theme. The agent commits to one visual direction, sets type and color as roles, and passes a critique before calling the work done.

When a brand already exists, d-pill keeps the type and the color and fixes structure, hierarchy, states, and copy. When nothing has been chosen, it refuses the unset look: an interchangeable sans, a purple gradient, three equal cards, everything centered.

The mark is only the capsule. The spectrum is thin-film color on that object, the way a pill looks under a hard light. It is not a theme for the page. The page still gets one direction, one accent, and a lot of quiet.

## Install

Any agent that loads a `SKILL.md` from a folder:

```bash
git clone https://github.com/srivtx/d-pill.git ~/.grok/skills/d-pill
```

One repository only:

```bash
git clone https://github.com/srivtx/d-pill.git .grok/skills/d-pill
```

Then ask for the interface, or run `/d-pill`.

Claude and other skill runners use the same folder. The procedure is `SKILL.md`. The knowledge is `references/`.

## What the agent does

1. Names the job in one sentence. Who is here, what they do, what done feels like.
2. Commits to a named style if they gave one, otherwise to one of ten directions, and writes down what it is refusing.
3. Composes the page as a poster: uneven on purpose, one material, the headline set by hand.
4. Builds it from the tokens and classes in `references/base.css`, in whatever stack the repo already has.
5. Runs the critique at a wide window and at 390px. A fail gets fixed before the work is called done.

Text has to clear 4.5:1. Control edges and the focus ring have to clear 3:1. The default palette was checked with `scripts/contrast.py` before it shipped. A color outside the safe band gets checked again.

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
| `references/interaction.md` | Time, forms, failure, motion |
| `references/craft.md` | The visual tells and the fix for each |
| `references/surfaces.md` | App, marketing, dashboard, docs, auth |
| `references/writing.md` | Words on the interface |
| `references/critique.md` | The gate |
| `scripts/contrast.py` | Contrast for a custom OKLCH pair |
| `assets/mark.svg` | The mark |

## Use the stylesheet

`references/base.css` is the implementation: roles, type ramp, space scale, focus, and the classes (`.stack`, `.cluster`, `.split`, `.rows`, `.display`). Paste a direction's override after it. Do not invent a second set of names beside it.

Space is a fixed scale: 4, 8, 12, 16, 24, 32, 48, 64, 96, 128. Most of those steps go unused on a given screen. That unused space is the design.

## License

[MIT](LICENSE)
