# Information

Design for understanding: diagrams, steps, comparisons, and finding your way. Charts of numbers are in `dataviz.md`. Navigation chrome is in `layout.md`.

## Diagrams

A diagram explains one relationship. Write the sentence first ("The order moves from bake to bag to door"). Then draw the least picture that carries that sentence.

Label the objects on the objects. A legend is a second place to look. Use one only when the marks are too small to name.

Lines are `--line-strong` when they mean a connection and `--line` when they are just structure. Arrowheads are simple, one size, and they point at the dependent thing. Do not decorate a diagram with the product's illustration style. It is type and lines.

Three to seven nodes. Past that, split into two diagrams or the sentence was two sentences.

No isometric scenes, no people-as-circles org charts with photos, no tangled connectors that cross more than once. If lines must cross, a small gap in the lower line is enough. It does not need a bridge illustration.

## Steps

Number steps only when order matters. The number is `.num`, muted, and the verb is ink. "1. Mix" not "Step one: the mixing phase of your journey."

If order does not matter, it is a list, not a process. Unnumbered, parallel grammar.

On a phone a horizontal stepper becomes a vertical stack. Do not shrink eight circles onto one row.

A stepper that is also navigation shows the current step with weight and a mark, and completed steps are quiet, not a trail of green checkmarks, unless completion is the point of the tool.

## Comparison

A comparison is a table or a set of aligned rows. The thing being compared is the header. The criteria are the first column, in parallel grammar ("Ships", "Price", "Lead time"), not a paragraph in each cell.

Highlight a column only if you are honestly recommending it, with the same restraint as pricing in `surfaces.md`: one filled button or one quiet label, not a scale and a ribbon.

Empty cells say "None" or "—" and mean it. A blank cell looks like a mistake.

## Wayfinding

If the place is more than two levels deep, show where the person is. Breadcrumbs are links, separated by a quiet slash or a middot, the current crumb is text, not a link: `Journal / Night bake / Temperatures`. They sit above the `h1`, in `--text-sm`.

Do not breadcrumb a flat marketing site. Depth you invented for the crumbs is not depth.

The current page in the nav is still `aria-current`, as in `components.md`. Breadcrumbs do not replace that.

A help article ends with a real next step: the related task, or back to the group. "Was this helpful?" is optional and easy to ignore. It is not the heading.

## Timelines

A timeline is a list with a date in `.num` or `.mono` and one sentence of what happened. A vertical rule may connect them. Dates align. Do not alternate cards left and right down the page. That is a poster trick that breaks on a phone and makes comparison harder.

Future items are quiet. Past items are ink. The current one is the accent, once.

## Maps and places

A map is for a spatial question. If the question is "what's the address," the address as text plus a link is better than an embedded map. If you embed one, it is large enough to use, it has a text address next to it, and it does not steal scroll (`behavior.md` and the page box in `layout.md`: give it a fixed height and do not let it trap the page).

Do not use a map as a decorative hero.

## The sentence test

Cover the picture. If the headings and labels still explain it, the diagram is helping. If they don't, the picture was carrying words it cannot hold. Add the words. Do not add more drawing.
