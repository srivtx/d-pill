# Details

The small decisions that make a finished interface feel finished. Components and states are in `components.md`. If a detail below is already a rule in `base.css`, do not reinvent it. Extend the stylesheet.

## Lines

Hairlines are 1px, solid, `--line` or `--line-strong`. A 0.5px line disappears on a non-retina display and jumps on a retina one. A control's edge is `--line-strong` because it has to clear 3:1. A row divider may be `--line`.

A divider runs the width of the content, not the viewport, unless it is the one editorial rule in `geometry.md`. Do not put a rule tight against a heading. The heading sits outside the list. The list's first row owns the first rule.

## Type in the box

Buttons already center with `line-height: 1`. Trust that, then the 1px nudge in `geometry.md` if the word still sits low.

The gap between an icon and its label is `--space-2`. If the SVG has padding inside the viewBox, the pair will look separated. Crop the viewBox to the glyph instead of adding a negative margin.

Icons are one set. Stroke 1.5, round caps and joins for a grotesque, butt caps for a sharp direction (Editorial, Spec, Atelier). 20px in the UI. 24px only in an empty state. Filled and stroked icons do not mix.

A count is a number. A red circle is not a personality. Use `--danger` on the word or the number only when the person must act.

Avatars are circles from the space scale (24, 32, or 40). A light photo gets a 1px `--line` or it dissolves. Initials use `--font-text`.

## Focus, press, selection

These are three different pictures.

- Focus is the 2px offset ring. It appears for keyboard, not for a mouse click. Do not replace it with a glow.
- Press (`:active`) is a darkening of the fill, already in `base.css`. The control does not move, scale, or sink.
- Selection is `--accent-soft` and `--ink`. Do not style selection as the accent fill with light text. People select text to read it.

Current-item (where you are in the nav) is weight plus a mark. It is not the focus ring and not the selection color.

## Scroll, caret, overscroll

The page ground is on `html` and `body`, so the overscroll bounce is `--bg` and not white. Scrollbars are thin and `--line-strong`.

Headings clear the sticky bar when jumped to (`scroll-padding` and `scroll-margin` are in `base.css`). Do not let a fragment link hide the title under the bar.

The caret in a field is `--accent` when that accent is visible on `--surface`. Otherwise it is `--ink`.

## Truncation and numbers

Ellipsis is for a column whose width is the constraint, and only when the full string exists on the next surface. Never ellipsis an error. A title may wrap to two lines instead of truncating. Two lines is a choice. Three lines of truncation is a paragraph in a box that should have been a paragraph.

Money and metrics in a column share a baseline, use `.num`, and put the unit in `.quiet` at the body's size, not a second display size. The decimal places match down the column.

## Empty geometry

A skeleton is the outline of the real layout: the same rows, the same title width, the same image ratio, in `--bg-subtle`. A stack of generic gray bars will be replaced by a different shape and the page will jump. Reduced motion keeps the skeleton still.

Images declare `width` and `height` or `aspect-ratio`. The frame is stable before the bytes arrive.

## Groups of fields

Inside a field, the label, the control, and the hint are `--space-1` apart. Between fields, use a stack gap from the density table. An error replaces the hint in the same slot. It does not appear to the side and it does not shift the next field horizontally.

Related fields (a date range, a city and a postal code) share a group label. Unrelated fields do not sit in one flat list of forty. Chunk them under headings. The chunking rule is in `behavior.md`.

## Z-order

Use the named layers in `base.css`: sticky, dropdown, drawer, dialog, toast. Do not invent `z-index: 9999`. A new layer means you have two things competing to be on top, and one of them should not be there.
