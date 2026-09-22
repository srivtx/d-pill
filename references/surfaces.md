# Surfaces

The primitives are in `layout.md`. The words are in `writing.md`. Each surface below is the structure, not a skin. Commit a direction first; these structures work inside all ten.

The first element in `body` is the skip link. The title element is the view, then the product.

## Marketing

Nav: wordmark, a few links, one action that stays visible under 720.

Pick one opening. Do not combine them.

**Typographic.** A `.caps` eyebrow only if it adds a fact. An `h1.display`. A `.lede`. One `button.primary` (or `button.ink` where the direction says so) and one quiet link. No figure in the first viewport.

**Split.** The claim column on the left, the figure on the right, bleeding toward the edge. Under 720 the claim comes first and the figure follows.

**Masthead.** The claim owns the first viewport. A full-width figure starts below it, with a caption.

Then two to four sections, each one idea, each a different shape: a split, a `.rows` list of facts, a `blockquote`, a close. The close repeats the action and states the cost or the next step in one line.

Do not open with a claim, a figure, three cards, and a logo row in the same viewport.

Proof is one line ("Used by 40 bakeries in the city") only when it is true. Otherwise skip proof.

## Pricing

An `h1` that says who it is for. Two or three tiers in a `.split` or a simple grid with shared edges. Each tier: the name, the price in `.num` at `--text-3xl`, the period in `.quiet`, a list of features in parallel grammar, one button.

The tier you recommend uses `button.primary` or `button.ink`. The others use the bordered button. A `.caps` label ("Fits most teams") is allowed when it is true. Do not scale the column, float a ribbon, and shadow it.

Prices share a baseline. Features use the same part of speech. The difference between tiers is obvious without a color legend.

## Auth

One column, 22rem, inside `.frame`. The product's name, one sentence if the form needs it, the form, the alternate path as a text link ("Have an account? Sign in"). No illustration panel. No carousel of benefits.

Errors follow `components.md`. After success, go to the place the person was trying to reach, not to a generic home, when you know that place.

## App shell

```html
<a class="skip" href="#work">Skip to orders</a>
<div class="shell">
  <nav class="nav-side" aria-label="Primary">
    <a href="/" class="wordmark">Oven</a>
    <a href="/today" aria-current="page">Today</a>
    <a href="/orders">Orders</a>
  </nav>
  <main id="work" class="work stack">
    <!-- the view -->
  </main>
</div>
```

The side nav is the objects. The work region is the largest and the quietest. Chrome uses `--ink-muted` and `--text-sm`. There is no welcome banner and no card around the whole page.

A view header is `.cluster.between`: an `h1` with the view's name, and the one action for this view.

## A list of work

The default inside an app. Instrument or Spec.

```html
<header class="cluster between">
  <div class="stack tight">
    <h1>Today</h1>
    <p class="quiet">14 open · 3 late</p>
  </div>
  <button class="primary">New order</button>
</header>
<ul class="rows interactive">
  <li>
    <span class="num">1842</span>
    <span>Rye, two loaves</span>
    <span class="quiet">Due 14:00</span>
    <button class="ghost">Mark out</button>
  </li>
</ul>
```

"3 late" may use `--danger` if lateness is the thing to act on. It is a word, not a badge. The row opens the record. One ghost action is allowed on the row; anything else goes in More.

Empty, loading, error, and partial follow `interaction.md`.

## Dashboard

A dashboard answers a question. It is not a grid of equal cards.

Lead with the number that matters, in `--text-3xl` and `.num`, with its unit and its comparison in `.quiet` ("212 orders · 18 fewer than last Tuesday"). Under it, the breakdown: one chart or one table, not both saying the same thing, plus the list of items the person can act on.

Chart rules:

- One series: the accent, no legend, the label at the end of the line.
- Categories: four at most. The mark clears 3:1 against `--bg`. The label is `--ink` or `--ink-muted` and clears 4.5.
- Gridlines use `--line`. Axis labels are `--text-xs`, `.num` where they are values.
- The title is a claim ("Signups fell after Tuesday") or a plain noun ("Revenue"). The unit is in the title or the axis.
- No 3D, no gradient fill, no dual axis.
- A chart with no data is the empty state, not a flat line of zeros with no sentence.

## Settings

Groups of rows. Each row: the label, a one-line description in `.quiet`, the control at the end. The control is a checkbox, a native select, or a link to a subpage when the choice is a long form.

The destructive group is last, separated by `--space-8` and an `h2`. Its button is `danger`, and it confirms through the dialog.

Do not put every setting on one endless page if they cluster into a few objects. Then the side nav lists those objects.

## Docs and long reading

Broadsheet, or Civic with the essay override. Three regions at most: a contents list, the article at 62–68ch, and an optional "next". The article `h1` is the document's title. Links inside prose are underlined. Code is `.mono` on `--bg-subtle`. The contents list highlights the current section with `aria-current="true"` and the side-nav treatment.

Do not put a card around a paragraph.

## First run

The empty product is a design, not a placeholder. Show the shape of the list faintly if it helps the person understand what will appear, and put one action in the empty state that creates the first object. The words are in `writing.md`. Do not show a tour that covers the page in modals.

## Editorial opening

A worked structure for Editorial, Atelier, or Quiet luxury. One `h1`, one rule, one figure or one paragraph. Not both fighting.

```html
<main class="frame stack loose section">
  <p class="caps">Issue 04 · The night bake</p>
  <h1 class="display">Bread that waits until the room is quiet.</h1>
  <p class="lede">A notebook from the oven we run after midnight, when the dough is the only schedule.</p>
  <p><a class="btn ink" href="/issue/04">Read the issue</a></p>
</main>
```

The `.btn` class on an anchor is allowed because it navigates and should look like the action. It is still an `<a>`.
