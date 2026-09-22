# Brand

How a mark, a name, and a palette stay one thing. Page color is in `color.md`. Words are in `writing.md`. Pictures are in `narrative.md`. This file is the identity those have to obey.

## The mark

A mark is simple enough to hold at 16px and specific enough to recognize at a glance. It is one shape, or one shape and one note. It is not a miniature illustration of the product.

Build it on the same material as the interface: one fill, one cut, one accent at most. If the mark needs a gradient, a shadow, or a mockup to look like something, it is not finished.

d-pill's own mark is the reference for this rule, in `assets/mark.svg`: a capsule, ink on one side and paper on the other, a single clay square on the cut. Mass, emptiness, one note. Do not restyle it per page.

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

- On paper: ink mark, paper ground, accent note.
- On ink: paper mark, ink ground. The accent stays, or drops out if it fails contrast.
- One color: ink only, the accent becomes a cut (a gap), not a gray.

Do not recolor the mark to match a campaign. Do not put it on a photograph unless the photograph has a quiet field and the one-color version still clears 3:1 against that field. When it does not, the mark sits on a solid `--bg` block.

## Misuse

Refuse these, including when a template suggests them:

- Rotate, skew, or italicize the mark.
- Add a shadow, a glow, an outline, or a gradient.
- Put it in a circle, a colored badge, or a rounded square it was not drawn for.
- Recreate it in another typeface.
- Crowd it with a tagline in the lockup. The tagline is a line of type somewhere else, or it does not exist.

## Favicon and platform

The favicon is the mark, not a letter you typed into a generator. Apple touch icon and social avatar use the same drawing, with the clear-space padding already inside the file (the plate in `assets/mark.svg` is that padding). Do not let a platform round it into a different shape and then also add your own circle.

`theme-color` is `--bg`, not the accent. The browser chrome should disappear into the page.

## Name

The name is set the way the product writes it. d-pill is lowercase, with a hyphen. Do not capitalize it for emphasis, and do not drop the hyphen. Other products: use their real spelling, once, the same way everywhere. Do not invent a stylistic casing ("dPill", "D·PILL") as a design move.

## What brand does not include

A brand is not a stock of gradients, mascots, and "brand shapes" scattered behind sections. If a shape is not the mark and not the interface, it does not go on the page. Personality lives in the direction: type, hue, density, and what you refuse.
