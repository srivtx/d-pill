# Data

Pictures of numbers. Dashboards as a page are in `surfaces.md`. This file is how a single chart, table, or figure tells the truth and still looks quiet.

## One question

Every figure answers one question. Write that question before you pick a form. "Did orders fall after Tuesday?" wants a line. "Which loaf sold" wants a bar or a table. "The exact invoice" wants a table and no chart.

The title is the claim ("Orders fell after Tuesday") or the plain noun ("Orders"). The unit is in the title or on the axis. "Overview" is not a title.

## Form

- **Table** when the person needs the number. Align figures with `.num`. Header in `--ink-muted`. A caption or an `h2` names it.
- **Bar** to compare categories. The axis includes zero. A bar chart that doesn't start at zero exaggerates. Horizontal bars when the names are long.
- **Line** for change over time. A line may start above zero if the subtitle says what the baseline is and the crop does not flip the story. If cropping changes a fall into a cliff, start at zero or plot the change itself.
- **Big number** when one value is the whole answer. `--text-3xl`, `.num`, the unit and the comparison in `.quiet` beside or under it. Not inside a card with a sparkline, an icon, and a badge.
- **Small multiples** when there are several series. Four small charts people can compare beat one chart with eight lines.
- **Pie** only for two or three parts that sum to a whole, each labeled with its name and value on the slice. No legend, no 3D, no exploded slice. If you need a fourth part, use a bar.

No dual axis. No 3D. No gradient fills. No decorative grid. Gridlines are `--line`, or they are absent and the direct labels do the work.

## Color and labels

One series: `--accent`, no legend, the label at the end of the line or on the bar.

Categories: four at most, as steps of lightness of the same hue, each mark clearing 3:1 against the ground. The labels are ink, not the same color as the mark. Do not use `--danger` and `--ok` as a palette. Those words are status, and they belong on a word ("Late"), not on a series you thought should be red.

Label the thing itself. A legend across the top forces the eye to bounce. Use a legend only when the marks are too small to hold a word, and then it sits in the same order as the marks.

Missing data is a gap, not a zero, unless zero is true. Say "No data for Wednesday" rather than dropping a line to the axis.

## Annotation

One note is allowed, pointing at the event that explains the shape ("Oven down Tuesday"). The note is `--text-sm`, ink, with a 1px leader. It is not a tooltip the person must hover to find. Hover may show the exact value. The story has to be visible without it.

## Source and sample

If the numbers come from somewhere other than this product, one quiet line under the figure names the source and the date. If the numbers are sample, they are obviously sample and they match any number written in the prose. A chart that contradicts the headline is a broken page.

## Empty

No data is the empty state from `writing.md`, in the figure's place. Not a chart of zeros. Not a ghost of last month's curve.
