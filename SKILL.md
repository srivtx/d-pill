---
name: d-pill
description: >
  Design and build website and web-app interfaces that look decided: commit a
  visual direction, then type, color, layout, components, motion, and interface
  writing, then pass a critique gate before the UI is called done. Use for
  landing pages, marketing sites, app screens, dashboards, settings, auth,
  docs, pricing, design tokens, and visual redesigns. Use for AI-native
  surfaces: chat interfaces, copilots, agent consoles, streaming responses,
  tool-call and approval UI, citations, and generative UI. Use when the user
  runs /d-pill, asks for a design system, says "make it look good", "make this
  beautiful", "flawless UI", or asks you to design, restyle, or build a page,
  screen, site, or component.
when-to-use: >
  Any website or web-app interface: a page, screen, component, theme, or
  redesign. Chat, copilot, and agent surfaces. Machine-readable design tokens.
  /d-pill.
license: MIT
metadata:
  short-description: Interfaces that look decided
  version: "1.4"
---

# d-pill

You are designing an interface a person will use. Decide, then build. Paths below are relative to the directory that contains this file.

## Authority

1. The user's explicit instructions, and a brand the project already has (its type, color, and name).
2. The contrast, focus, and target-size floors. Direction never overrides these.
3. The direction you committed for this surface.
4. `references/base.css` for every token and class.
5. The way of seeing in `references/sense.md`.
6. The taste judgment in `references/taste.md`.
7. The taste rules in `references/craft.md` for anything still open.

If a brand exists, keep its type and color. Map them onto the roles in `references/foundations.md`. Apply structure, hierarchy, states, spacing, and the critique gate. Do not reskin a real brand into a different direction unless the user asks.

If nothing has been chosen, the unset look is not a design. Commit a direction. Do not reach for Inter, Roboto, a purple gradient, a centered hero, or three equal cards. The refusal list is in `references/craft.md`.

## What to read

Always read this file, `references/sense.md`, `references/taste.md`, and `references/direction.md` before drawing. If they name a style, a period, a movement, or a material, read `references/styles.md` before the direction tree. Read `references/critique.md` before you call the UI done.

Then only what the work touches:

| Work | Read |
|---|---|
| Any surface a person will see | `references/taste.md`, `references/craft.md`, `references/type.md`, `references/proportion.md`, `references/geometry.md`, `references/details.md` |
| A named style, period, movement, or material | `references/styles.md`, then `references/faces.md`, `references/grids.md`, and `references/harmony.md` |
| Color, theme, dark mode, a brand hex | `references/color.md`, then `references/foundations.md` |
| Tokens, CSS, a new page file | `references/foundations.md` and `references/base.css` |
| Page structure, navigation, breakpoints, which container | `references/layout.md`, `references/arrange.md`, and `references/behavior.md` |
| A control, menu, dialog, table, form, or state | `references/components.md` and `references/details.md` |
| Master-detail, filters, pagination, calendar, command palette, consent | `references/patterns.md` |
| Motion, focus, keyboard, loading, failure, empty | `references/interaction.md` |
| A chat surface, a copilot, an agent's actions, streaming text, citations, approvals, generative UI | `references/ai-interfaces.md` |
| Machine-readable tokens, feeding this system to another tool, verifying the export | `references/machines.md` and `references/tokens.json` |
| A named frontier move: barely-there, anti-grid, shader hero, expressive letters, dense dark tools, adaptive pages | `references/frontier.md` |
| Soft cards, a status strip, a personal site or portfolio with the craft look | `references/soft.md`, then `references/formats.md` |
| A landing page, a story, pricing, proof, photography | `references/narrative.md`, `references/art.md`, and `references/surfaces.md` |
| An app shell, dashboard, settings, auth, docs, or first run | `references/surfaces.md` |
| A shop, a product, a bag, checkout | `references/commerce.md` |
| A portfolio, event, help center, changelog, status, account, or inbox | `references/formats.md` |
| Another language, RTL, long labels, locale punctuation | `references/world.md` and `references/type.md` |
| A chart, a table of numbers, a diagram, a timeline | `references/dataviz.md` and `references/information.md` |
| A logo, a favicon, a wordmark, brand rules | `references/brand.md` |
| Drawing icons, pixel icons, glyph tiles, icon states | `references/icons.md` |
| A phone layout | `references/mobile.md` |
| Access, zoom, screen readers, motion sensitivity | `references/a11y.md`, then the floors in `references/critique.md` |
| Adding a token or a component to a system | `references/systems.md` |
| Labels, errors, empty copy, headlines | `references/writing.md` and `references/type.md` |
| The source behind a judgment, further reading | `references/reading.md` |
| A color outside the safe band | `scripts/contrast.py`, then the band in `references/foundations.md` |

## Procedure

### 1. Name the job

One sentence: who is here, what they do on this surface, what done feels like. If the request and the repo already say that, do not ask. If they do not, ask once, then build. Do not ask which aesthetic they prefer when you can commit one.

### 2. Commit a direction

If they named a style, commit it from `references/styles.md` and start from the direction that style names. Otherwise pick one direction from `references/direction.md` with the decision tree there. The only legal mix is one borrowed slot, written as an exception. State the commitment before code, in the work and in the reply:

```
Job: A baker marks today's orders out.
Direction: Instrument, compact, hue 28. Borrowed: nothing.
Type: Instrument Sans. Sizes in play: meta, body, title.
Color: base tokens, --hue 28. Accent only on "New order".
Space: tight rows, one quiet gap under the title.
Refuse: hero, cards, a second accent, illustration.
```

### 3. Set tokens, then compose, then make controls

Copy `references/base.css`. Paste the direction's override after it. Compose with `references/sense.md`, then set the type with `references/type.md`, the color with `references/color.md`, and the edges with `references/geometry.md`. Build that composition from the primitives in `references/layout.md`, after `references/arrange.md` picks the container. Pictures follow `references/art.md`. Another language follows `references/world.md`. A conversation with a model or an agent's actions follow `references/ai-interfaces.md`, over the committed direction. A component exists only where a behavior exists. Ship the states in `references/components.md` and the pixel decisions in `references/details.md`. A page that has to be believed also follows `references/narrative.md`. A page a person operates also follows `references/behavior.md`. A shop follows `references/commerce.md`. A phone layout follows `references/mobile.md`. A mark follows `references/brand.md`. A frontier move asked for by name follows `references/frontier.md` before it is committed. Access is designed with `references/a11y.md`, not checked afterwards.

### 4. Write the words

Use `references/writing.md`. Buttons are verbs. Errors say what to do next. Do not claim a behavior the interface does not have.

### 5. Pass the gate

Run `references/critique.md` on the real markup at a wide viewport and a 390-wide viewport. Fix every fail. If a browser is available and the page runs, use it: tab through, fire the primary action, fire one error. A screenshot of the first paint is not the gate.

In the reply, name the direction and one sentence on what the critique changed. Do not paste the checklist.

## Laws

- One direction per surface. Stay inside the commitment.
- One focal point per view. Size, isolation, or contrast. Not all three at full volume.
- Hierarchy comes from type and space. Color is a role, and the accent is scarce.
- Use the scale in `base.css`. Most steps go unused on a given screen.
- Edges share an axis. Center a short statement or an empty state, not a paragraph, not a form, not a nav.
- Chrome earns its place. A border, a shadow, and a tint are three treatments. Most objects get one.
- A control with only a default state is unfinished. Focus-visible is always drawn.
- Motion shows where something came from or what changed. It does not perform.
- Density matches the job. The three densities are defined in `references/layout.md`.
- Recompose under 720px. Do not ship a squeezed desktop.
- The second typeface has to change the voice. If it does not, use one family.
- Invent composition. Do not invent a new checkbox, a new dialog, or a new focus ring. Platform elements are specified in `references/components.md`.
- Sample data is obviously sample and internally consistent. Do not invent customers, logos, or testimonials.

## For agents

This file is the whole assignment until the work narrows it. The routing table is the index: read a row, read only that row's files, load depth when the task touches it. Reading the whole repo is not diligence; it is noise.

- The description in the frontmatter is the trigger. If the task is an interface, you are in the right place.
- Escalate depth: `SKILL.md` now, the one row the task touches next, the recipe file only while composing. Reference files are pull, not homework.
- `references/base.css` is the authority for values. `references/tokens.json` is the machine export of it, verified by `scripts/check-tokens.py`. When they disagree, run the script and fix the loser.
- Verify like a machine: computed styles, geometry, both themes. A screenshot can pass while the stylesheet 404'd. The protocol is in `references/machines.md`.
- When you must go beyond the repo, write the exception the way `soft.md` writes exceptions: one paragraph, bounded, with a refuse list.

## Stack

Use the stack the repo already has. Translate the tokens and the HTML into it. If the repo has no front end yet, ship semantic HTML and `base.css`. Do not add Tailwind, a component kit, or an icon package to a project that does not already use one. Icons, when needed, are inline SVG at 20px, `currentColor`, one stroke weight.

## Redesigns

Read the existing UI first. Keep the information architecture and the meaning of the copy. Keep brand type and color if they exist. Rebuild hierarchy, spacing, composition, and states. Change the direction only when the user asks or when the current look is an unset default (indigo on white, Inter, generic card grid) with no brand behind it.
