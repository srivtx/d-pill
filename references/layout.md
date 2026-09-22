# Layout

Build every region from the primitives in `base.css`. Do not space a page with one-off margins.

| Class | Behavior |
|---|---|
| `.stack` | Vertical. Default gap `--space-4`. `.tight` is `--space-2`. `.loose` is `--space-8`. |
| `.cluster` | Horizontal, wraps, centers on the cross axis. `.between` pushes the ends apart. `.end` aligns to the end. |
| `.split` | Two columns, 1.15 / 0.85, collapses under 720. Children have `min-width: 0` so text can shrink. |
| `.frame` | Centers the page at `--page` (72rem) with gutter. |
| `.measure` | 68ch. Prose only. |
| `.section` | Vertical padding for a marketing band. |
| `.rows` | A list separated by rules. Four tracks: id, name, meta, action. |
| `.shell` | App frame: 14rem side nav, then the work. One column under 720. |

A grid child that holds text needs `min-width: 0`. `.split` already does this. If you write a new grid, set it.

## Density

One density per view. The direction names it. Set the variables. Do not invent a second scale.

| Density | `--text-md` | `--control-h` | In-group gap | Between groups | `--section-pad` | `--row-pad` |
|---|---|---|---|---|---|---|
| compact | 0.875rem | 2rem | `--space-2` (`.stack.tight`) | `--space-4` | `--space-6` | `--space-2` |
| regular | 0.9375rem | 2.25rem | `--space-3` | `--space-5` | `--space-8` | `--space-3` |
| generous | 1.0625rem | 2.5rem | `--space-4` | `--space-6` | `--space-9` | `--space-4` |

The exception is a reading column inside a product: the article sets its own size and measure; the chrome keeps the view density. Broadsheet and Civic already show that override.

`base.css` raises `--control-h` and input type size on coarse pointers, and pads the top bar for the safe area. Do not push those back down.

## Alignment

Pick the left edge and keep it. The wordmark, the claim, the first column of a list, and the form labels share an axis inside the frame.

Center only a short statement (one line) or an empty state. Do not center a paragraph of two or more lines, a form, a nav, or a pricing table.

Optical alignment beats the bounding box for icons, triangles, and arrows. If an icon looks low next to a label, move it up 1px. Do not "fix" it by growing the font.

## Rhythm

Proximity is the grouping. The gap inside a group is at most half the gap between groups. If you need a box to explain that two things belong together, the gap is wrong. Add a border only when the gap cannot say it.

Similarity is the repetition. The same role gets the same treatment: every row, every nav item, every tier.

One focal point per view. Make it by size, by isolation (space around it), or by contrast. Not all three at the maximum.

A page of equal bands is unfinished. Alternate the shape of sections: a split, then a ruled list, then a quote, then a close. Do not alternate background tints as the only rhythm.

## The page box

The shell is `min-height: 100dvh`, not `100vh`. A short page pins the footer with a column flex or a grid row of `1fr` on `main`. Do not `position: fixed` a footer over the work.

The top bar is sticky, short (`--header-h`), and solid `--bg`, with a 1px line. It does not blur the page under it.

The first viewport of a marketing page contains the claim and the action. Proof may be one line. The figure may start there only if the claim still owns the screen.

## Breakpoints

Two, unless a third is forced:

- Under 720px the page is one column. `.split` stacks. `.shell` stacks. The side nav becomes a horizontal bar. If there are more than six destinations, use a Menu disclosure instead of a scrolling strip. `.nav-links` hides and `.nav-menu` shows. The primary action stays visible. Type steps down via the `.display` rule already in `base.css`. Horizontal page padding is `--space-4` or the frame gutter, not both stacked.
- At 1100px and above, a side-by-side figure may sit next to a claim. Do not introduce 640, 768, 1024, and 1280 as four slightly different layouts.

Use a viewport query for the page. Use a container query only when a component must change inside a narrow column it does not control.

Recompose. A table that exists so someone can compare stays a table: wrap it in a region that scrolls horizontally, keep the first column sticky, and show that it scrolls. A table that is really a list of records becomes `.rows`. Pick one and keep the comparison or the record, whichever the job needs.

Text can grow about a third in translation. Do not set a fixed height on a button's label. Use `min-height: var(--control-h)`. Logical properties (`padding-inline`, `margin-inline`) are already the default in `base.css`. Keep using them.

## Navigation

App nav is the objects: Orders, Runs, Invoices. Not Solutions, Resources, Company.

Marketing nav is the product, the price, and a way in. Anything else goes to a short footer.

The logo is a link to the start. The current page is `aria-current="page"` and is indicated by weight plus a mark (the inset line in a top bar, the soft fill in a side nav). Color alone is not the indicator.

Do not add a page the product does not need in order to look complete.

## A directory of objects

Use this only when the objects are peers with their own action: a file, a listing, a product. Not for features, not for plans, not for testimonials.

```css
.directory {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(16rem, 1fr));
  gap: var(--space-4);
}
.directory > article {
  min-width: 0;
  display: flex;
  flex-direction: column;
  gap: var(--space-3);
  padding: var(--space-4);
  border: var(--border);
  border-radius: var(--radius);
  background: var(--surface);
}
```

One treatment. No shadow. The image, if it is the point, bleeds to the edges and the text keeps the padding. Hover changes the border to `--line-strong` or the background to `--bg-subtle`. Do not scale the card.
