# Foundations

`base.css` is the only list of token names and the only default values. Edit by overriding. Do not invent a parallel set (`--gray-7`, `--blue`, a hex beside an OKLCH role).

Load the direction's font stylesheet, then `base.css`, then a `<style>` block with that direction's override. Overrides come after `base.css` so they win. `--hue` is inherited by both themes. If you replace a derived color with a fixed `oklch()`, set it on `:root` and again on `html[data-theme="dark"]`.

Ship the direction's primary theme. Signal is dark-first: put `data-theme="dark"` on `<html>` in the document, not after JavaScript. Add the other theme only when the product needs both. Do not auto-invert a paper page because the OS is dark.

## Roles

| Token | Role |
|---|---|
| `--bg` | The page. The largest area. |
| `--bg-subtle` | A row hover, a code block, a quiet band. |
| `--surface` | Dialogs, menus, inputs. A step toward the reader from `--bg`. |
| `--ink` | Primary text. |
| `--ink-muted` | Secondary text that is still text: hints, meta, captions. |
| `--line` | Dividers that are not the only edge of a control. |
| `--line-strong` | The edge of an input, a secondary button, a checkbox boundary. |
| `--accent`, `--accent-ink` | The primary action's fill and the text on it. Also the current-item mark and the focus ring. |
| `--accent-soft` | A selected row. Not a section background. |
| `--danger`, `--danger-ink`, `--danger-soft` | Destructive actions and errors. Not a second brand color. |
| `--ok`, `--warn` | Status text and icons. Not decoration. |
| `--focus` | The ring. Defaults to `--accent`. |

Status colors are not accents. A screen has one accent.

## Color

Neutrals are the accent's hue at a very low chroma, so the page is tinted rather than dead gray. Change `--hue` before you change anything else.

Pick the hue from the material of the thing: bread 28, clay 25, leaf 145, sea 200, steel 215, bronze 70. If you cannot name a material, use 215. Do not pick 265–300 unless that is already the brand.

Chroma for an accent starts at 0.12. If the color flattens (a channel is clipping), lower chroma by 0.02 until it sits in gamut. Do not raise lightness to buy neon.

Hues 70–110 (yellow, lime) never carry light text. Use them as a mark or as a soft fill with `--ink` on top. The primary button in those hues is `button.ink`.

`--ok` and `--warn` are for words like "Paid" and "Due". They are dark enough to be text on `--bg` in the light theme and light enough in the dark theme.

### Safe band

Checked against the default `--bg` lightness (0.985 light, 0.17 dark). If you move `--bg` by more than 0.03, recheck with `scripts/contrast.py`.

Light:

- `--ink` lightness ≤ 0.30
- `--ink-muted` lightness ≤ 0.52
- An accent fill with light text: lightness ≤ 0.50, except hues 70–110
- `--line-strong` lightness ≤ 0.64

Dark:

- `--ink` lightness ≥ 0.92
- `--ink-muted` lightness ≥ 0.74
- `--line-strong` lightness ≥ 0.54
- Accent used as text: lightness ≥ 0.78

Outside the band, run:

```bash
python3 scripts/contrast.py text 0.46 0.016 215 0.985 0.008 215
python3 scripts/contrast.py ui   0.62 0.016 215 0.985 0.008 215
```

`text` must clear 4.5. `ui` (edges, rings, essential marks) must clear 3. The floors themselves are enforced in `critique.md`.

There is no hex in the stylesheet. A brand hex gets converted to OKLCH and stored as a role.

## Type

Two families, and only if the second changes the voice. Mono is the second family when the product shows code, IDs, or money. Otherwise one family.

Weights, and only these:

- 400 body and long text
- 500 labels, table headers, nav, display
- 600 buttons and the current nav item

Do not set UI to 700. Play may set a single display word to 700. A newspaper masthead may too, if the face needs it.

A screen uses about four sizes, from the ramp in `base.css`: meta (`--text-sm` or `--text-xs`), body (`--text-md`), title (`--text-xl` or `--text-lg`), and, on a marketing page, `.display`. A fifth size means the hierarchy is doing two jobs.

- Display tracking is `--tracking-display` (default `-0.02em`). Body, UI, and buttons stay at 0.
- `.caps` is 12px, weight 500, tracking `0.06em`, muted. One eyebrow per region. Not on buttons.
- Body line-height is `--leading-body`. UI and labels use `--leading-ui`. Display uses `--leading-display` and `text-wrap: balance`.
- Prose measure is `--measure` (68ch). The line under a display claim uses `.lede` (36ch). A pull quote maxes out at 28ch.
- Figures in columns use `.num` (tabular). Identifiers and code use `.mono`. Do not set tabular numbers on body copy.
- `text-wrap: pretty` is already on paragraphs. Do not justify.

Element headings are the UI scale (`h1` is `--text-xl`). The marketing claim is one `h1.display`. Do not use `.display` inside an app shell.

## Space

The scale is `--space-1` (4px) through `--space-10` (128px): 4, 8, 12, 16, 24, 32, 48, 64, 96, 128. There is no 13, 18, 20, or 22.

Vertical space comes from `.stack`, `.section`, or `.rows`. Headings and paragraphs have no margin of their own. Do not mix margins and gaps to invent a third rhythm.

Within one density, most of a screen uses three steps: a tight gap inside a group, a normal gap between groups, a large gap between regions. Which steps belong to which density is in `layout.md`.

## Shape and elevation

One radius family per direction, already set by its override: `--radius-sm`, `--radius`, `--radius-lg`. `--radius-full` is only for a round avatar or a single pill control, not for buttons in a square system.

Elevation is a lightness step plus `--line`. `--shadow-overlay` is only for dialog, menu, and toast. No other shadow.

## Motion

Three durations, already in `base.css`. Which one to use is in `interaction.md`. Do not add a fourth. Do not add bounce or elastic easing outside Play, and Play overrides one element, not the token.

## Font loading

In `<head>`, before the stylesheet:

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
```

Then the direction's font link. `display=swap` is already on those URLs. The fallback in the font stack is a sans under a sans and a serif under a serif, so the first paint does not reflow into a different voice.

## Document

```html
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Today · Oven</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <!-- direction font link -->
  <link rel="stylesheet" href="base.css">
  <style>/* direction override */</style>
</head>
<body>
  <a class="skip" href="#work">Skip to content</a>
  <!-- surface -->
</body>
</html>
```

The title is the view, then the product: "Today · Oven". One `h1`. `lang` matches the page.

If the repo already uses Tailwind, map these roles into the existing theme and stop. Do not introduce a second naming scheme. The class names in `base.css` are the implementation when you are writing plain CSS.
