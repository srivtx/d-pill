# Type

`foundations.md` owns the ramp, the weights, and the measure. This file is how the type is set so it looks considered. Read it whenever the page has a headline, a paragraph, or a pair of faces.

## The levers, in order

Make hierarchy with size first, then weight, then space, then color. If you desaturate a screenshot and the order disappears, color was doing the job size should do. Gray is not a smaller font. A quiet line is a smaller size or a lighter weight, and it still clears the contrast floor.

Skip a step on the ramp between a parent and a child. 15px next to 18px looks like a mistake. 15 next to 24 looks like a decision.

Bold is for a button, the current nav item, or one phrase in a paragraph. A whole sentence in 600 looks like shouting. A whole paragraph in 500 looks like nothing was chosen.

## Pairing

Two families only when the second changes the voice. Pair a high-contrast serif with a plain grotesque. Do not pair two display serifs, two geometric sans, or a face with itself in a "different style" that is just a weight.

Match the body size to the serif's x-height. A serif with a small x-height (Cormorant) needs to be set larger than the grotesque beside it or it looks weak. Quiet luxury already sets the display very large. The UI face stays at `--text-md`.

If the face has an optical-size axis (Newsreader, Fraunces, Literata), leave `font-optical-sizing: auto` on. Display cuts have thinner joints and tighter spacing. Text cuts are sturdier. Do not force a display cut at 15px.

## Line length and leading

`--measure` is 68ch. That is the article. A lede is 36ch. A pull quote is 28ch. A headline is as wide as its own phrase, not as wide as the viewport.

Leading follows the length. At a full measure, body leading stays `--leading-body`. If you narrow a column to about 45ch, you may drop leading toward `--leading-ui`. Display leading stays near 1.0 to 1.1. Do not use body leading on a headline. The lines of a headline should feel like they belong to one shape, not three separate lines floating apart.

## The rag, widows, line breaks

The right edge of a paragraph is a shoreline. Do not justify. Justification opens rivers.

`text-wrap: pretty` and `widows` / `orphans` are in `base.css`. They are not enough on their own. If the last line of a paragraph is one short word, rewrite the sentence. If a heading breaks so the last line is one word, rebreak it. The headline rule in `sense.md` still holds: each line is a phrase.

Break headlines with `<br>` at the phrase. Do not trust the browser to break a display line.

## Caps, italics, figures

`.caps` is for an eyebrow or a group label: small, tracked out, muted, and short. Never a sentence. Never a button. Tracking on caps is `--tracking-caps`. Tracking on lowercase body is 0. Tight tracking belongs only on large type.

Italic is one word or one title. It is a change of voice. It is not a way to make a paragraph look expensive.

UI figures are lining figures. Columns of figures use `.num` (tabular). In a Broadsheet or Editorial article, set `font-variant-numeric: oldstyle-nums` on the prose so the numbers sit with the lowercase. Do not set oldstyle on prices, tables, or IDs. `.num` on a child wins over the article.

Fractions, when the face has them and the text is a real recipe or a measurement: `font-variant-numeric: diagonal-fractions`. Do not fake precision with superscripts.

Use real quotation marks (“ ” and ‘ ’), an apostrophe (’), and an ellipsis (…). Straight quotes from a keyboard look like code. An ampersand in the display face, once, is allowed in Editorial. It is not a logo.

## Links and underlines

Prose links are underlined. The underline skips the descenders (`text-decoration-skip-ink` is on). Nav links are not underlined. Do not invent a second link style (a colored pill, a gradient underline, an animated underline).

## What not to set

- No drop cap. It fights the leading and it looks like a costume on a product page. A pull quote does the job.
- No outlined type, no gradient type, no text shadow.
- No negative leading on body.
- No all-caps headline. A caps eyebrow above a normal headline is the cap moment.
- No third size of a single sentence (a bold italic accent word inside an already accented line). One emphasis per line.
