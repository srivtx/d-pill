# Brand

How a mark, a name, and a palette stay one thing. Page color is in `color.md`. Words are in `writing.md`. Pictures are in `narrative.md`. This file is the identity those have to obey.

## The mark

A mark is simple enough to recognize at a glance. It is one object. It is not a miniature illustration of the product, and it is not a button.

d-pill's mark is only the capsule, in `assets/mark.svg`. No plate, no badge, no rounded square behind it. The fill is a thin-film spectrum, the way a capsule looks under a hard light: magenta through violet, blue, cyan, green, gold, and back to rose, with a gloss along the top and a seam where the two halves meet. That rainbow belongs to the object. It does not become the interface. Pages still follow the direction. Do not paint a product in the mark's spectrum.

Do not restyle the capsule per page. Do not put it inside another shape to "make a logo."

## Lockups

Three arrangements, and no others:

- **Mark alone.** Favicon, avatar, a tight nav. No word beside it.
- **Wordmark alone.** When the name is set in the product's display face and the place is quiet (a footer, a colophon).
- **Horizontal lockup.** Mark, then a gap the width of the mark's inner padding, then the name in the text face at a size that matches the mark's height. Aligned on the optical center, not the bounding box.

Do not stack the name under the mark unless the place is a poster and you have set it as type, with the line-break rules in `type.md`. Do not put the mark inside a sentence.

## Clear space and size

Clear space on every side is at least one quarter of the mark's height. Nothing enters it: no type, no edge of a photo, no button.

Smallest mark: 16px if the strokes still read. If they collapse, use a simpler one-color version, not a scaled-down blur. Smallest wordmark: the name at `--text-sm` or larger. Below that, use the mark.

## Color versions

- The full mark is the spectrum capsule. Use it at sizes where the film still reads, about 64px wide and up.
- Below that, the gradient turns to mud. Use the silhouette: the capsule and the seam, one color, ink on paper or paper on ink.
- Do not recolor the film to match a campaign, and do not replace it with flat stripes. The spectrum is continuous.

Do not put the capsule on a busy photograph. If the film will not read, use the silhouette on a solid `--bg` block.

## Misuse

Refuse these, including when a template suggests them:

- Rotate, skew, or italicize the mark.
- Put it in a circle, a colored badge, a button, or a rounded square.
- Add a second shadow or a glow around it. The gloss is already in the file.
- Replace the film with flat rainbow stripes, or with a single brand color, except the small silhouette.
- Recreate it in type ("a pill icon from a font").
- Crowd it with a tagline in the lockup. The tagline is a line of type somewhere else, or it does not exist.

## Favicon and platform

The favicon is the silhouette of the capsule, not a letter you typed into a generator. Clear space sits outside the drawing. The viewBox has a little air so the stroke does not clip. Do not add your own plate behind it, and do not let a platform circle it and then also draw your own circle.

`theme-color` is `--bg`, not the accent. The browser chrome should disappear into the page.

## Name

The name is set the way the product writes it. d-pill is lowercase, with a hyphen. Do not capitalize it for emphasis, and do not drop the hyphen. Other products: use their real spelling, once, the same way everywhere. Do not invent a stylistic casing ("dPill", "D·PILL") as a design move.

## What brand does not include

A brand is not a stock of gradients, mascots, and "brand shapes" scattered behind sections. If a shape is not the mark and not the interface, it does not go on the page. Personality lives in the direction: type, hue, density, and what you refuse.
