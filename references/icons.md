# Icons

A small drawing system. Using an icon in the interface is in `components.md` and `details.md`. This file is how the drawings are made so a set feels like one hand.

## Grid

Draw on a 24px grid. The live area is 20px, with 2px of padding inside the grid. Strokes sit on whole or half pixels at the size they ship, so a 1.5px stroke stays sharp.

Ship only 16, 20, and 24. 16 is for dense meta, inside a table. 20 is the default beside a label. 24 is an empty state or a nav icon with a word under it. Do not scale a 24 icon to 13, and do not invent 28.

## Stroke

One weight for the whole set. 1.5px at 24. Round caps and round joins for grotesque directions (Instrument, Soft, Civic, Play). Butt caps and miter joins for sharp ones (Editorial, Spec, Atelier, Quiet luxury, Broadsheet). Signal can go either way, but only one.

Corners in the metaphor match the product's radius family. A rounded button set does not get sharp, brittle icons.

Filled icons and stroked icons are two sets. Pick one. A single filled icon for "warning" inside a stroked set is how sets fall apart. Draw the warning as a stroke too.

## Optical corrections

Geometry lies at this size.

- A circle looks smaller than a square of the same box. Let circles and triangles overshoot the live area by about 1px.
- A square stays inside the live area.
- Horizontal strokes look heavier than vertical ones. If a plus looks clumsy, thin the horizontal arm a hair, do not change the nominal weight of the set.
- Arrowheads and carets are visually centered toward their point, as in `geometry.md`.
- An icon beside type aligns to the cap height. Nudge the whole glyph. Do not redraw it shorter to cheat the alignment.

## Metaphors

Use the metaphor people already know. Search is a magnifier. Close is an ×. Menu is lines or the word Menu. Trash is a bin. Do not invent a clever synonym for a common action.

If the idea has no common metaphor, use a word. An icon that needs a tooltip to mean anything should have been a label. The tooltip can still exist for an icon-only button, and the accessible name is required either way.

Do not put an icon in a colored circle to make a feature list. The drawing is enough, in `--ink` or `--ink-muted`.

## Files

Inline SVG, `currentColor`, `aria-hidden="true"` when a label is next to it. No fixed fill in the file. No extra whitespace in the viewBox. A set shares one viewBox, so swapping an icon does not move the label.

If the project already has a set, draw new icons into that set. Do not import a second pack for three missing pictures.
