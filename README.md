# d-pill

A design skill for agents that build interfaces.

d-pill is one skill. `SKILL.md` is the procedure. The files in `references/` are the system: ten visual directions, a token file with checked contrast, layout, components, interaction, craft, page types, interface writing, and a critique gate. An agent reads the procedure, commits to a direction, and opens only the references the screen needs.

When a brand already exists, the skill keeps it and fixes structure, hierarchy, spacing, states, and copy. When nothing has been chosen, it commits to a direction and refuses the unset look: an interchangeable sans, a purple gradient, three equal cards, everything centered.

Text, control edges, and focus rings have floors. A control is not done with only a default state.

## Install

Grok, Claude, and any agent that loads a `SKILL.md` from a skill folder:

```bash
git clone https://github.com/srivtx/d-pill.git ~/.grok/skills/d-pill
```

For one repository only:

```bash
git clone https://github.com/srivtx/d-pill.git .grok/skills/d-pill
```

Then ask for the interface, or run `/d-pill`.

## Files

| File | What it owns |
|---|---|
| `SKILL.md` | The procedure, the laws, what to read |
| `references/sense.md` | How to see a page: proportion, material, the headline, what to leave out |
| `references/type.md` | How type is set: pairing, leading, rag, figures, emphasis |
| `references/color.md` | How color is judged: value, temperature, dark themes, brand hex |
| `references/geometry.md` | Optical alignment, radius, bleed, crops, scanning |
| `references/details.md` | Hairlines, focus, press, truncation, skeletons, z-order |
| `references/behavior.md` | How people move: distance, choice, scent, trust, speed |
| `references/narrative.md` | How a site argues, and how its pictures behave |
| `references/direction.md` | The ten directions and their overrides |
| `references/foundations.md` | How to edit tokens without breaking them |
| `references/base.css` | The tokens and the classes |
| `references/layout.md` | Composition, density, breakpoints |
| `references/components.md` | Controls, overlays, anatomy |
| `references/interaction.md` | Time, forms, failure, focus, motion |
| `references/craft.md` | The visual tells and the fix for each |
| `references/surfaces.md` | Page types and two worked structures |
| `references/writing.md` | Words on the interface |
| `references/critique.md` | The gate before the UI is called done |
| `scripts/contrast.py` | A contrast check for a color outside the safe band |

## License

MIT
