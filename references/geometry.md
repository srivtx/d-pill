# Geometry

Where things sit, and why the mathematical center often looks wrong. `layout.md` owns the primitives and the breakpoints. `sense.md` owns the poster. This file owns the eye for edges, crops, and curves.

## Visual weight

Align to what the eye sees, not to the bounding box.

- A mixed-case word has more mass above the baseline. Centered in a button it looks low. `base.css` uses flex centering and `line-height: 1`. If the label still looks low, nudge it up 1px. Do not fix it by raising the font size.
- A triangle, a play mark, or a chevron is optically centered toward its heavy side. A play mark usually needs 1px in the direction it points.
- An icon next to a label aligns to the cap height, not the em box. If the glyph looks low, nudge the icon up 1px.
- In a row of a label, a button, and a price, align their centers on the x-height, or align all of them to one baseline. Do not mix the two in one row.
- Vertical centering in a tall hero leaves the type looking low, because optical center is slightly above mathematical center. Bias the type up, or don't vertically center at all. Top alignment with a generous margin is usually the better poster.

## One axis, peers when they are peers

Everything that is text shares a left edge. The action sits at the end of that same band.

Equal columns are for peers: three prices, two comparable plans. A claim beside a figure is unequal. `.split` is already 1.15 / 0.85. You may push it to something like 1.3 / 0.7 if the figure needs more, or the reverse if the type is the picture. Do not "fix" it back to 50/50 out of habit.

Margins are larger than gutters. The space outside the content is quieter than the space between columns. `--page` caps the width so a three-column layout never becomes three novels.

## Radius

One radius family per direction, from the override.

When a rounded box contains a rounded thing, the outer radius equals the inner radius plus the padding. A 6px button inside a 16px pad wants an outer radius near 22px. The same radius on both looks like the inner shape is floating off the corner.

A circle is for a person (an avatar) or a single round control the direction already asked for. A circle used as a bullet, a badge, and a button, next to rounded cards, is three shapes. Sharp corners are one voice (print, spec, editorial). Large radii are another (soft, play). They do not share a page.

Do not scale a box that has a 1px border. The border blurs. Animate opacity or color instead.

## Frames and bleed

A 1px line is a frame. A border plus a shadow plus a tint is three frames. Use one.

Bleed is for the photograph: it may run to the viewport edge. Type stays in the frame. Do not bleed the headline off the edge and box the photo. The exception is Play, and only if the break is the one break in `sense.md`.

A full-bleed rule (a line from edge to edge) is an editorial device. One per page, not between every section.

## Crops

Give every image an `aspect-ratio` and `object-fit: cover`, and reserve the space so the page does not jump when the file arrives.

The subject looks into the page, toward the type or the action, not out of the frame. Leave room in front of a gaze. A face centered in a small circle is an avatar. A face centered in a hero is a poster, and only Atelier does that on purpose.

Pick one ratio per region and repeat it. 3:2 and 16:10 feel like pictures. 4:5 and 3:4 feel like posters. 1:1 feels like a thumbnail. Do not mix all of them on one page.

Crop tighter than the source. The decision, the hands, the object. A wide shot of a room with the product in the corner wastes the poster.

## How people scan

In a left-to-right page the eye hits the top left, moves across the first band, then down the left edge. Put the name at the start of the band and the action at the end. The paragraph is read after the largest type, not before.

People scan headings and the starts of lines. Front-load the noun. A heading that begins with "Our" or "The best" throws away the first glance.

This is not permission to center everything on a mobile screen. The left edge still works on a phone. Centering is still reserved for a one-line empty state.

## Grouping

- Things closer than their neighbors are a group. If you need a box to explain the group, the gap is wrong.
- The same role looks the same. If two buttons do the same kind of job, they share a style.
- An axis is a line the eye follows. Break it once, in `sense.md`'s one break, or not at all.
- You do not need four borders to imply a region. A top rule, or a change of ground, is enough. Closure does the rest.
- Things that move together belong together. Do not put unrelated blocks on one shared animation.

## Sticky and fixed

A sticky bar is part of the ground: solid `--bg`, a 1px line, no shadow at rest. A shadow under a bar that has not moved looks like the bar is floating above an empty page.

Do not pin a second bar, a chat bubble, and a cookie strip over the work. One sticky region. On a phone, a bar glued to the bottom covers the job the person came to do. The action lives with the claim or at the end of the form.
