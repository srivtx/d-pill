# Color

`foundations.md` owns the tokens, the hue method, and the safe band. This file is how to judge color. Run `scripts/contrast.py` when a value leaves the band.

## Value first

Squint, or imagine the page in gray. The poster still needs a shape. Light and dark do that. Hue is the note on top.

The split that holds a page:

- Most of the area is ground (`--bg`). About three fifths.
- Structure is ink, muted ink, and lines. About a third.
- Accent is the action and one mark. A tenth, often less.

If the accent covers a hero, it is no longer a note. It is a second ground, and the page has two materials.

## Temperature

Warm grounds (hue about 40–70, chroma under 0.02) feel near and physical. Cool grounds (hue about 200–230) feel precise. The direction already picks. Do not "balance" a warm page with a cold blue accent. The accent stays in the same family of hue, or it is ink.

A neutral that does not share `--hue` looks dirty or disconnected. That is why the grays are tinted. A pure gray next to a warm paper looks bluish. Let the token do it. Do not "correct" it back to hex gray.

## What sits on what

A color is judged on its neighbor, not in a palette swatch. Check the accent on `--bg`, the ink on `--surface`, the button label on the button.

On a light theme, a raised surface is lighter than the page. On a dark theme, a raised surface is also lighter than the page. Dark themes do not go "deeper" by getting blacker. They step up in lightness: page, then surface, then dialog.

Shadows are the hue at low opacity, and only on things that float. A gray shadow on warm paper looks like soot. `base.css` already tints `--shadow-overlay`.

Large fields do not gradient. A gradient is a second material. A photograph may contain a gradient of light. The CSS behind it does not add another.

## Dark, as its own picture

`html[data-theme="dark"]` is not an invert of the light theme.

- Ink is off-white, not `#fff`. Pure white vibrates on a dark ground.
- Lines get lighter, not a translucent white smear.
- The accent gets lighter so it still reads, and its text gets dark.
- Photographs get a 1px `--line` if their edge melts into the page. Do not dim them with a black overlay unless the type is sitting on the photo, which it should not.
- Test both themes if you ship both. A token that works on paper can fail on the dark field. The safe band has two halves.

Signal is dark-first. Do not design it in light and flip the attribute at the end.

## Meaning

`--danger`, `--ok`, and `--warn` are words' companions. They are never decoration, never a second brand, never the way a chart gets "colorful."

Red against green is not a message. The word ("Late", "Paid") is the message. The color helps people who can see it.

A focus ring has to clear 3:1 against the color it sits on. The ring is offset onto the ground, so judge it against `--bg`, not against the button fill.

## Charts and images

Chart color lives in `surfaces.md`: one series in the accent, categories as steps of lightness, four at most. Do not import a categorical rainbow.

A duotone treatment on a photo is a material change. It is allowed in Play, and only if you commit the whole page to flat color. A CSS multiply overlay on a stock photo is not a duotone. It is a filter.

## When the brand arrives with a hex

Convert it to OKLCH and store it as `--accent` or as ink, whichever role it actually plays. Then rebuild the neutrals from that hue at low chroma. Do not keep their gray and their brand color as two unrelated systems. Check the safe band. If their accent is too light for white text, the button is `button.ink` and the brand color becomes the note, the rule, or the word.
