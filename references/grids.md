# Grids

How the page is divided before any card exists. The CSS primitives are in `layout.md`. This is which grid, and why.

## Kinds

**Manuscript.** One column. The measure is `--measure` or narrower. Margins are what's left. This is a book, a doc, a form, a letter. Do not put a manuscript inside a 12-column frame and then only use the middle. Just set the measure.

**Column.** Two or more columns for peers or for a text-plus-figure split. Gutters come from the space scale, and they are smaller than the outer margin. Two columns: a split. Three: a catalog or a newspaper front, only if each column is still at least 28ch. If a column drops under that, you have too many.

**Modular.** Columns and rows, the cells equal. Swiss poster, a wayfinding board, a spec sheet of peers. An element may span cells. It may not sit in the gutter. The empty cell is allowed to stay empty. That is the style.

**Hierarchical.** The columns are not equal. A narrow rail for labels or a contents list, a wide well for the work. The rail is 12–16rem or it is a margin, not a second page. This is the app shell and the docs layout. Do not make three hierarchies. Two regions is the maximum unless the third is a quiet inspector (`patterns.md`).

## The page, in pieces

On a screen the top is already eaten by the bar. Do not also pad the content as if it were a printed page with a huge top margin, or the work starts too low. Printed-page habit that still holds: the bottom wants air, the sides want a margin you can feel, and the margin is larger than the gutter.

A useful screen construction, not a religion:

- Side margin: `--space-6` to `--space-8` on a large screen, `--space-4` on a phone.
- Top of the content, under the bar: `--space-6` in a tool, `--space-8` or more on a poster.
- Text block: the measure, not the viewport.
- Bottom: at least as much as the top of the content, often more, so the page does not feel cut off.

The Van de Graaf idea (the text block is a page within the page, with a generous outer margin) is this, and only this. Do not overlay a geometric diagram on the design and call it a canon. If the text block looks like a column floating in a field of margin, you have it.

## Twelve columns

A 12-column grid is a measuring tool. It is not a look. Use it when elements must span 3, 4, 6, or 8 columns and align across sections. Do not draw the columns. Do not put a one-column article on a 12-column grid with empty tracks on both sides if a manuscript grid is what you meant.

Gutters are `--space-4` or `--space-5`. If you need a smaller gutter, the thing is a table, not a layout grid.

## Rows and baseline

Body leading is the beat. A heading's margin, in a stack, should be a multiple of that beat when you can do it without fighting the space scale. Do not build a baseline-grid framework. Do check that a heading doesn't collide with the next line, and that two columns of body beside each other share a cap line at the top. If they drift, fix the heading size or the gap, not the whole page with a plugin.

## Hang and optical margin

Punctuation at the start of a display line (an opening quote) should hang outside the measure so the letters align. `hanging-punctuation` is already on. If the browser ignores it, pull the quote with a negative margin on that element only.

A column of text next to an image: align the cap height of the first line with the top of the image, or align the top of the image with the top of the heading. Do not align the image to the border-box of a heading that has padding you forgot about.

## Breaking the grid

Break it once, on purpose (`sense.md`). A figure that spans the margin. A word that crosses two cells. A full-bleed image. The break is visible because everything else sits on the grid. If everything breaks the grid, you do not have a grid, and the page will look accidental.

## Phone

Under 720 the grid becomes one column. A modular poster becomes a stack in the same order a person would read the poster: the large word, then the fact, then the picture. Do not keep four columns and shrink the type.
