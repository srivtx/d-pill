# Faces

How to look at a typeface and decide. Setting type once you have chosen is `type.md`. The ban list of unset defaults is in `direction.md`. A style in `styles.md` may override that ban on purpose.

## What you are looking at

Judge a face at the size it will be used. A display cut at 72px and the same family at 15px are different tools.

- **Stroke contrast.** The difference between thick and thin. High contrast (Didone) is a display instrument. At text size the thin strokes fail on screens. Low contrast (a grotesque, an old style) is what you read.
- **Stress.** Where the thin part sits. Old style is angled, like a pen. Rational and Didone are vertical. Do not mix an angled old style and a Didone and expect them to feel like one period.
- **X-height.** Tall x-height looks larger and more contemporary at the same point size, and it needs less leading. A small x-height (Cormorant) must be set larger or it looks weak next to a sans.
- **Aperture.** The opening of c, e, a, s. Wide apertures survive small sizes and bad screens. Closed apertures look elegant and disappear at 13px.
- **Terminals.** Ball terminals, sharp cuts, sheared grotesques. This is the personality. If you cannot describe the terminal, you do not have a reason to pick the face.
- **Italic.** A true italic is a different drawing (old style). An oblique is the roman leaned over (most grotesques). Use a true italic when the style is a book. Do not fake an italic with a transform.
- **Figures.** Look for lining and oldstyle, tabular and proportional. If the family has no tabular figures, do not use it for a price column. Use the mono for the numbers.
- **Weight range.** If you only have 400 and 700, do not specify 500 and hope. `direction.md` already says this for Atkinson. It is true of every static family.
- **Optical size.** If the family has an opsz axis (Newsreader, Fraunces, Literata, Source Serif 4), leave `font-optical-sizing` on. Display becomes finer. Text becomes sturdier.

## The classes

Pick a class for the job, then a face inside it. Do not pick a face because it was on a moodboard.

| Class | What it is | Use | Do not use |
|---|---|---|---|
| Old style serif | Low contrast, angled stress | Books, essays, Quiet luxury body | A dense app UI |
| Rational serif | Higher contrast, vertical stress | A serious journal, titles | Tiny captions |
| Didone | Extreme contrast, vertical, hairline serifs | A name, a cover, one line | Body, buttons, nav |
| Slab | Serifs are blocks | Letterpress, packaging, a sturdy title | A long elegant essay |
| Grotesque | 19th-century sans, a little irregular | Editorial display, a blunt headline | If you wanted neutrality |
| Neo-grotesque | Even, high x-height, quiet | Swiss, Instrument, UI | When you wanted a point of view and did not add one elsewhere |
| Geometric sans | Built from circles and lines | Bauhaus, a poster word | Long reading |
| Humanist sans | A pen hiding in a sans | Soft service, Civic, long UI text | A Swiss poster that must be neutral |
| Condensed | Narrow, tall | A newspaper name, a tight label, one poster line | Body text |
| Mono | Fixed width | Code, IDs, figures, a spec | A paragraph |
| Script | A pen or a brush | Never for UI. One signature word if the style is Sign painting or a cover | Anywhere else |
| Blackletter | A manuscript hand | One word on a style that is truly a manuscript or a masthead from that history | Any sentence, any UI, as a joke |

## Pairing, again, as a test

Put the two faces next to each other at their real sizes and say what changed.

- A serif beside a sans: the serif is the voice, the sans is the tool. Good.
- Two serifs: only if one is display and they are the same class. Two classes (Didone plus old style) is two centuries arguing.
- Two sans: only if one is mono, or one is condensed and used as a single display word. A geometric plus a neo-grotesque at the same size looks like a mistake.
- The same family in two weights is usually the right answer. Exhaust it before you add a second family.

## A practical shelf

These are on Google Fonts, so an agent can load them. They are not the only good faces. If the brand has a face, use the brand's face.

- Old style: Newsreader, Literata, Cormorant Garamond (display and titles, it is small at body size).
- Rational text: Source Serif 4.
- Didone, display only: Bodoni Moda, Libre Bodoni.
- Slab: Bitter, Zilla Slab.
- Neo-grotesque: IBM Plex Sans, Inter only inside the Swiss style.
- Humanist: Atkinson Hyperlegible, Public Sans, Source Sans 3.
- Geometric, poster: Outfit, Syne. Not for long text.
- Condensed poster: Oswald, one line.
- Mono: IBM Plex Mono.
- Soft display: Fraunces, optical size on.

## Loading

One family is a few weights, not every weight. 400, 500, 600 is a UI. A display family may be a single weight. Italics only if you will use italics. Extra weights slow the first paint and tempt you to use them all (`taste.md`, typographic color).

`font-display: swap` and a fallback of the same class, so a serif does not flash as a sans. The stacks in `direction.md` already do this. Match that habit for any face you add.
