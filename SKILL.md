---
name: d-pill
description: >
  Design and build website and web-app interfaces that look decided: commit a
  visual direction, then type, color, layout, components, motion, and interface
  writing, then pass a critique gate before the UI is called done. Use for
  landing pages, marketing sites, app screens, dashboards, settings, auth,
  docs, pricing, design tokens, and visual redesigns. Use when the user runs
  /d-pill, asks for a design system, says "make it look good", "make this
  beautiful", "flawless UI", or asks you to design, restyle, or build a page,
  screen, site, or component.
when-to-use: >
  Any website or web-app interface: a page, screen, component, theme, or
  redesign. /d-pill.
metadata:
  short-description: Interfaces that look decided
---

# d-pill

You are designing an interface a person will use. Decide, then build. Paths below are relative to the directory that contains this file.

## Authority

1. The user's explicit instructions, and a brand the project already has (its type, color, and name).
2. The contrast, focus, and target-size floors. Direction never overrides these.
3. The direction you committed for this surface.
4. `references/base.css` for every token and class.
5. The way of seeing in `references/sense.md`.
6. The taste rules in `references/craft.md` for anything still open.

If a brand exists, keep its type and color. Map them onto the roles in `references/foundations.md`. Apply structure, hierarchy, states, spacing, and the critique gate. Do not reskin a real brand into a different direction unless the user asks.

If nothing has been chosen, the unset look is not a design. Commit a direction. Do not reach for Inter, Roboto, a purple gradient, a centered hero, or three equal cards. The refusal list is in `references/craft.md`.

## What to read

Always read this file, `references/sense.md`, and `references/direction.md` before drawing. Read `references/critique.md` before you call the UI done.

Then only what the work touches:

| Work | Read |
|---|---|
| Any surface a person will see | `references/craft.md`, `references/type.md`, `references/geometry.md`, `references/details.md` |
| Color, theme, dark mode, a brand hex | `references/color.md`, then `references/foundations.md` |
| Tokens, CSS, a new page file | `references/foundations.md` and `references/base.css` |
| Page structure, navigation, breakpoints | `references/layout.md` and `references/behavior.md` |
| A control, menu, dialog, table, form, or state | `references/components.md` and `references/details.md` |
| Motion, focus, keyboard, loading, failure, empty | `references/interaction.md` |
| A landing page, a story, pricing, proof, photography | `references/narrative.md` and `references/surfaces.md` |
| An app shell, dashboard, settings, auth, docs, or first run | `references/surfaces.md` |
| A shop, a product, a bag, checkout | `references/commerce.md` |
| A portfolio, event, help center, changelog, or status page | `references/formats.md` |
| A chart, a table of numbers, a diagram, a timeline | `references/dataviz.md` and `references/information.md` |
| A logo, a favicon, a wordmark, brand rules | `references/brand.md` |
| Drawing icons | `references/icons.md` |
| A phone layout | `references/mobile.md` |
| Access, zoom, screen readers, motion sensitivity | `references/a11y.md`, then the floors in `references/critique.md` |
| Adding a token or a component to a system | `references/systems.md` |
| Labels, errors, empty copy, headlines | `references/writing.md` and `references/type.md` |
| A color outside the safe band | `scripts/contrast.py`, then the band in `references/foundations.md` |

## Procedure

### 1. Name the job

One sentence: who is here, what they do on this surface, what done feels like. If the request and the repo already say that, do not ask. If they do not, ask once, then build. Do not ask which aesthetic they prefer when you can commit one.

### 2. Commit a direction

Pick one direction from `references/direction.md` with the decision tree there. The only legal mix is one borrowed slot, written as an exception. State the commitment before code, in the work and in the reply:

```
Job: A baker marks today's orders out.
Direction: Instrument, compact, hue 28. Borrowed: nothing.
Type: Instrument Sans. Sizes in play: meta, body, title.
Color: base tokens, --hue 28. Accent only on "New order".
Space: tight rows, one quiet gap under the title.
Refuse: hero, cards, a second accent, illustration.
```

### 3. Set tokens, then compose, then make controls

Copy `references/base.css`. Paste the direction's override after it. Compose with `references/sense.md`, then set the type with `references/type.md`, the color with `references/color.md`, and the edges with `references/geometry.md`. Build that composition from the primitives in `references/layout.md`. A component exists only where a behavior exists. Ship the states in `references/components.md` and the pixel decisions in `references/details.md`. A page that has to be believed also follows `references/narrative.md`. A page a person operates also follows `references/behavior.md`. A shop follows `references/commerce.md`. A phone layout follows `references/mobile.md`. A mark follows `references/brand.md`. Access is designed with `references/a11y.md`, not checked afterwards.

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

## Stack

Use the stack the repo already has. Translate the tokens and the HTML into it. If the repo has no front end yet, ship semantic HTML and `base.css`. Do not add Tailwind, a component kit, or an icon package to a project that does not already use one. Icons, when needed, are inline SVG at 20px, `currentColor`, one stroke weight.

## Redesigns

Read the existing UI first. Keep the information architecture and the meaning of the copy. Keep brand type and color if they exist. Rebuild hierarchy, spacing, composition, and states. Change the direction only when the user asks or when the current look is an unset default (indigo on white, Inter, generic card grid) with no brand behind it.
