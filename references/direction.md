# Direction

Commit one direction before any layout. State the six slots: type, color, shape, density, motion, material. Then name what you are refusing.

Density words (compact, regular, generous) are defined in `layout.md`. Token edits follow `foundations.md`. Overrides below assume `base.css` is already loaded.

## Tree

- Here to do a job, repeatedly, on objects → **Instrument**
- Here to work rows of figures, logs, or records → **Spec**
- Here to read a long document → **Broadsheet**
- Here to look at a small set of work → **Atelier**
- Here for a front page with a point of view → **Editorial**
- Buying or booking something quiet and expensive → **Quiet luxury**
- A human service: health, school, care, a local business → **Soft service**
- A technical product whose personality is the system → **Signal**
- A public institution or a public dataset → **Civic**
- Delight is the product → **Play**

A brand that already has type and color skips the tree. Map that brand onto the slots and keep going.

If they name a style, a decade, a material, or a kind of object, do not stop at this tree. Commit the style in `styles.md`.

## The only legal mix

Borrow one slot from a second direction and write it in the commitment. "Spec, with Soft's hue 25." Do not borrow three. Contrast floors still hold.

## Instrument

A tool. The person has done this before and will do it again.

- Type: Instrument Sans for everything. Mono only for code and IDs.
- Color: neutrals take the product hue. Accent on the primary action and the selected row. Hue 215 if you cannot name a material.
- Shape: radius 6. Borders. Shadow only on overlays.
- Density: compact.
- Motion: color at `--dur-1`. Panels at `--dur-2`. The page does not animate in.
- Material: flat tinted paper.
- Refuse: serif display, illustrations, card grids, a second accent, a welcome banner.

```html
<link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500&family=Instrument+Sans:ital,wght@0,400..700;1,400..700&display=swap" rel="stylesheet">
```

```css
:root {
  --hue: 215;
  --font-display: "Instrument Sans", "Avenir Next", "Segoe UI", sans-serif;
  --font-text: "Instrument Sans", "Avenir Next", "Segoe UI", sans-serif;
  --font-mono: "IBM Plex Mono", ui-monospace, monospace;
  --radius-sm: 4px;
  --radius: 6px;
  --radius-lg: 8px;
  --tracking-display: -0.03em;
  --text-md: 0.875rem;
  --control-h: 2rem;
  --header-h: 3rem;
  --section-pad: var(--space-6);
  --row-pad: var(--space-2);
}
```

Primary actions are `button.primary`. For a marketing page in this voice, set `--text-md` back to `0.9375rem` and use one `.display`.

## Spec

The job is to read a value, compare it, and act.

- Type: IBM Plex Sans. IBM Plex Mono for every figure, ID, and timestamp.
- Color: hue 220, chroma of neutrals 0.006. Accent is rare: the row you are in, and one action.
- Shape: radius 2. Rules between rows. No zebra unless the rows are very dense and the rule is not enough.
- Density: compact. Tighter than Instrument: row padding `--space-2`.
- Motion: almost none. A value that changes may flash `--accent-soft` once at `--dur-2`.
- Material: a spec sheet. Lines, labels, units.
- Refuse: cards, illustrations, display serifs, rounded pills, decorated empty states.

```html
<link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500&family=IBM+Plex+Sans:ital,wght@0,400;0,500;0,600;1,400&display=swap" rel="stylesheet">
```

```css
:root {
  --hue: 220;
  --chroma-neutral: 0.006;
  --font-display: "IBM Plex Sans", "Avenir Next", "Segoe UI", sans-serif;
  --font-text: "IBM Plex Sans", "Avenir Next", "Segoe UI", sans-serif;
  --font-mono: "IBM Plex Mono", ui-monospace, monospace;
  --radius-sm: 2px;
  --radius: 2px;
  --radius-lg: 4px;
  --tracking-display: -0.02em;
  --text-md: 0.875rem;
  --control-h: 2rem;
  --header-h: 3rem;
  --section-pad: var(--space-6);
  --row-pad: var(--space-2);
}
```

## Editorial

A front page with a point of view. One argument, then the evidence.

- Type: Newsreader for display and quotes. Instrument Sans for UI and body.
- Color: warm paper, hue 40, neutral chroma 0.012. The accent is ink. A single rust mark (`oklch(0.48 0.12 35)`) may appear once on the page.
- Shape: radius 0. Rules and hairlines. No shadows on the page.
- Density: generous in the opening, regular in the rest.
- Motion: none on the page. Overlays only, at `--dur-2`.
- Material: paper, ink, a rule.
- Refuse: card grids, gradient text, a product screenshot in a fake browser, three equal features above the argument.

```html
<link href="https://fonts.googleapis.com/css2?family=Instrument+Sans:ital,wght@0,400..700;1,400..700&family=Newsreader:ital,opsz,wght@0,6..72,400..700;1,6..72,400..700&display=swap" rel="stylesheet">
```

```css
:root {
  --hue: 40;
  --chroma-neutral: 0.012;
  --accent: oklch(0.28 0.02 40);
  --accent-ink: oklch(0.97 0.01 40);
  --font-display: "Newsreader", "Iowan Old Style", Georgia, serif;
  --font-text: "Instrument Sans", "Avenir Next", "Segoe UI", sans-serif;
  --radius-sm: 0;
  --radius: 0;
  --radius-lg: 0;
  --tracking-display: -0.02em;
  --text-md: 1.0625rem;
  --control-h: 2.5rem;
  --section-pad: var(--space-9);
  --row-pad: var(--space-4);
}
html[data-theme="dark"] {
  --accent: oklch(0.9 0.02 40);
  --accent-ink: oklch(0.18 0.02 40);
}
```

The primary action is `button.ink`. The claim is `h1.display`.

## Atelier

The work is the design. You are hanging it, not framing it in chrome.

- Type: Fraunces for the piece's name. Instrument Sans in `.caps` for the only labels.
- Color: hue 50, neutral chroma 0.01. Accent is ink. No bright color.
- Shape: radius 0. No shadow. A caption under the work, not a card around it.
- Density: generous. The first viewport is often one image and one name.
- Motion: none, unless the work itself moves.
- Material: a wall. Lots of `--bg`.
- Refuse: hero copy stacked on the image, icon rows, testimonials, a tinted badge, rounded thumbnails.

```html
<link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,400..700;1,9..144,400..700&family=Instrument+Sans:ital,wght@0,400..700;1,400..700&display=swap" rel="stylesheet">
```

```css
:root {
  --hue: 50;
  --chroma-neutral: 0.01;
  --accent: oklch(0.25 0.015 50);
  --accent-ink: oklch(0.97 0.005 50);
  --font-display: "Fraunces", "Iowan Old Style", Georgia, serif;
  --font-text: "Instrument Sans", "Avenir Next", "Segoe UI", sans-serif;
  --radius-sm: 0;
  --radius: 0;
  --radius-lg: 0;
  --tracking-display: -0.01em;
  --control-h: 2.5rem;
  --text-md: 1.0625rem;
  --section-pad: var(--space-9);
  --row-pad: var(--space-4);
}
html[data-theme="dark"] {
  --accent: oklch(0.92 0.01 50);
  --accent-ink: oklch(0.16 0.01 50);
}
```

## Quiet luxury

Stillness, a warm ground, a name set well. Hospitality, objects, tailoring, a practice.

- Type: Cormorant Garamond for names and the claim. Source Sans 3 for everything a person uses.
- Color: hue 70, neutral chroma 0.014. Accent is a deep bronze used as text or a 1px rule, not as a bright fill.
- Shape: radius 2. Thin rules. No shadow on the page.
- Density: generous. Measure of a paragraph 62ch.
- Motion: opacity only, `--dur-1`. Do not reveal sections on scroll.
- Material: warm paper, a metal rule, a photograph with real darkness in it.
- Refuse: bright accent buttons, rounded consumer UI, exclamation, urgency banners, stock handshakes.

```html
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,500;0,600;1,500&family=Source+Sans+3:ital,wght@0,400..700;1,400..700&display=swap" rel="stylesheet">
```

```css
:root {
  --hue: 70;
  --chroma-neutral: 0.014;
  --accent: oklch(0.40 0.05 70);
  --accent-ink: oklch(0.97 0.01 70);
  --font-display: "Cormorant Garamond", "Iowan Old Style", Georgia, serif;
  --font-text: "Source Sans 3", "Avenir Next", "Segoe UI", sans-serif;
  --radius-sm: 2px;
  --radius: 2px;
  --radius-lg: 2px;
  --tracking-display: -0.01em;
  --text-md: 1.0625rem;
  --control-h: 2.5rem;
  --section-pad: var(--space-9);
  --row-pad: var(--space-4);
}
html[data-theme="dark"] {
  --accent: oklch(0.78 0.05 70);
  --accent-ink: oklch(0.18 0.02 70);
}
```

Display size for the claim: `clamp(3rem, 8vw, 6rem)`. Primary action is `button.ink`.

## Soft service

A person is being helped. The interface should feel calm and specific, not childish.

- Type: Atkinson Hyperlegible for everything. It is a humanist sans with a job, not a rounded toy face.
- Color: hue 25 (clay) by default. Hue 155 if the material is actually green. Accent on the one action.
- Shape: radius 12 on controls, 10 on images. No shadow except overlays.
- Density: regular. More air than a tool, less than a gallery.
- Motion: `--dur-2` on panels. A 4px rise is enough. Nothing bounces.
- Material: warm paper, one accent, photographs of the real place if you have them.
- Refuse: pastel rainbows, bubbly illustrations you invented, all-caps shouting, three cute feature cards.

```html
<link href="https://fonts.googleapis.com/css2?family=Atkinson+Hyperlegible:ital,wght@0,400;0,700;1,400;1,700&display=swap" rel="stylesheet">
```

```css
:root {
  --hue: 25;
  --font-display: "Atkinson Hyperlegible", "Avenir Next", "Segoe UI", sans-serif;
  --font-text: "Atkinson Hyperlegible", "Avenir Next", "Segoe UI", sans-serif;
  --radius-sm: 8px;
  --radius: 12px;
  --radius-lg: 16px;
  --tracking-display: -0.02em;
  --text-md: 1rem;
  --control-h: 2.5rem;
}
```

Atkinson ships 400 and 700 only. `base.css` asks buttons for 600, which resolves to 700 on this face, and asks labels for 500, which resolves to 400. Leave those weights. Do not add a 500 weight to the font URL.

## Signal

Dark-first. A technical product. The personality is precision.

- Type: IBM Plex Sans, IBM Plex Mono for anything a machine said.
- Color: the page is the dark theme. Hue 145 (phosphor) or 75 (amber). Pick one. Accent is text and a 1px line, used rarely. The primary button uses the light accent with dark `--accent-ink`.
- Shape: radius 4.
- Density: compact.
- Motion: state changes at `--dur-1`. No scroll theater.
- Material: a dark field, one phosphor, hairline rules.
- Refuse: purple glow, grid-dot wallpaper, gradient text, a tilted browser mock, glassmorphism, green-on-black as a costume when the product is not a terminal.

```html
<link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500&family=IBM+Plex+Sans:ital,wght@0,400;0,500;0,600;1,400&display=swap" rel="stylesheet">
```

```html
<html lang="en" data-theme="dark">
```

```css
:root {
  --hue: 145;
  --font-display: "IBM Plex Sans", "Avenir Next", "Segoe UI", sans-serif;
  --font-text: "IBM Plex Sans", "Avenir Next", "Segoe UI", sans-serif;
  --font-mono: "IBM Plex Mono", ui-monospace, monospace;
  --radius-sm: 2px;
  --radius: 4px;
  --radius-lg: 6px;
  --tracking-display: -0.03em;
  --text-md: 0.875rem;
  --control-h: 2rem;
  --header-h: 3rem;
  --section-pad: var(--space-6);
  --row-pad: var(--space-2);
}
```

Amber alternative: `--hue: 75`. Do not add a text-shadow glow. The color is the effect.

## Civic

A public thing. A resident, a reader, a researcher. Clarity is the personality.

- Type: Public Sans. Source Serif 4 only if there is a long essay, and then only for that essay.
- Color: hue 230, or 145 when the material is land or water. Accent is functional. Neutrals stay quiet.
- Shape: radius 4.
- Density: regular.
- Motion: `--dur-1` on state, nothing else.
- Material: a document that happens to be on a screen. High contrast. Obvious labels.
- Refuse: whimsy, jargon in labels, low-contrast muted text, illustrations of diverse people you generated, a hero that delays the task.

```html
<link href="https://fonts.googleapis.com/css2?family=Public+Sans:ital,wght@0,400..700;1,400..700&display=swap" rel="stylesheet">
```

Add Source Serif 4 only when the page has an essay column:

```html
<link href="https://fonts.googleapis.com/css2?family=Source+Serif+4:ital,opsz,wght@0,8..60,400..700;1,8..60,400..700&display=swap" rel="stylesheet">
```

```css
:root {
  --hue: 230;
  --font-display: "Public Sans", "Avenir Next", "Segoe UI", sans-serif;
  --font-text: "Public Sans", "Avenir Next", "Segoe UI", sans-serif;
  --radius-sm: 2px;
  --radius: 4px;
  --radius-lg: 6px;
  --tracking-display: -0.02em;
  --text-md: 1rem;
  --control-h: 2.5rem;
}
```

Essay column, when there is one:

```css
.article {
  font-family: "Source Serif 4", Georgia, serif;
  font-size: 1.125rem;
  line-height: 1.65;
  max-width: 62ch;
}
```

## Broadsheet

The person came to read. Get out of the way.

- Type: Literata for display and body. Mono for code. UI chrome is the same serif; do not add a third family.
- Color: newsprint. Hue 85, neutral chroma 0.008. Links are underlined ink. Accent is optional and appears once.
- Shape: radius 0. A rule between stories. No cards.
- Density: the article is generous; the masthead is regular.
- Motion: none.
- Material: a column of text, marginalia if you have a real note, a caption under a figure.
- Refuse: a hero image behind the headline, a newsletter modal on load, share-button jewelry, pull quotes in quotation-mark graphics.

```html
<link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500&family=Literata:ital,opsz,wght@0,7..72,400..700;1,7..72,400..700&display=swap" rel="stylesheet">
```

```css
:root {
  --hue: 85;
  --chroma-neutral: 0.008;
  --font-display: "Literata", Georgia, serif;
  --font-text: "Literata", Georgia, serif;
  --font-mono: "IBM Plex Mono", ui-monospace, monospace;
  --radius-sm: 0;
  --radius: 0;
  --radius-lg: 0;
  --tracking-display: -0.015em;
  --measure: 62ch;
}
.article { font-size: 1.125rem; line-height: 1.65; max-width: 62ch; }
```

## Play

Delight is the point. Constraint is what keeps it from becoming noise.

- Type: Familjen Grotesk. Fraunces for one word in the claim, and nowhere else.
- Color: hue 15. One support color at most, and only as a flat block. Three colors is the ceiling, counting ink.
- Shape: radius 12 on controls, 4 on media.
- Density: regular, with one oversized display.
- Motion: one element may use `cubic-bezier(0.2, 1.4, 0.4, 1)` at `--dur-3`. Nothing else overshoots. Lists do not stagger.
- Material: flat shapes, hard edges of color, no gradients, no 3D, no clay.
- Refuse: a rainbow, confetti on load, every element animating, Comic-style faces, more than one joke in the copy.

```html
<link href="https://fonts.googleapis.com/css2?family=Familjen+Grotesk:ital,wght@0,400..700;1,400..700&family=Fraunces:ital,opsz,wght@0,9..144,500;1,9..144,500&display=swap" rel="stylesheet">
```

```css
:root {
  --hue: 15;
  --font-display: "Familjen Grotesk", "Avenir Next", "Segoe UI", sans-serif;
  --font-text: "Familjen Grotesk", "Avenir Next", "Segoe UI", sans-serif;
  --radius-sm: 6px;
  --radius: 12px;
  --radius-lg: 16px;
  --tracking-display: -0.04em;
  --text-md: 1rem;
  --control-h: 2.5rem;
}
.display em {
  font-family: "Fraunces", Georgia, serif;
  font-style: italic;
  font-weight: 500;
}
```

## Fonts you do not reach for

Unless the existing brand uses them: Inter, Roboto, Arial, Helvetica, Open Sans, Lato, Montserrat, Poppins, Nunito, Space Grotesk, and `system-ui` as the designed voice. `system-ui` is a fallback, not a choice.
