# Components

Use the element that already does the job. Style the classes in `base.css`. Do not rebuild a control the platform provides.

- It navigates: `<a href>`.
- It acts: `<button>`.
- It chooses one of a few filters and loads another view: a link, or tabs only if the panels are already on the page.
- It confirms something destructive or blocks the page: `<dialog>` opened with `showModal()`.
- It discloses a short menu: `<details class="menu">`.

Never a `div` with a click handler.

There is no card class. A repeated object with its own action uses the directory pattern in `layout.md`. Everything else is a stack, a split, or `.rows`.

## Button

Three levels in one region, and usually only two:

- `primary` — the accent fill. One per region.
- the unclassed button — a border, the ink. The alternative.
- `ghost` — no border. A tertiary action in a toolbar or a row.

`ink` replaces `primary` in Editorial, Atelier, and Quiet luxury.

`danger` is the destructive fill. In a menu, `danger ghost` is text in `--danger` with no fill.

Heights and padding come from `--control-h` and `--space-3`. Do not set a one-off height. On coarse pointers `--control-h` is already 44px.

An icon button is `button.icon` with an `aria-label` that names the object: "Delete invoice 1842". The SVG is 20px, `currentColor`, one stroke. No circle behind it.

A button that is working keeps its width, sets `aria-busy="true"`, and changes the verb: "Save" becomes "Saving". It is disabled for the duration so it cannot fire twice.

Do not show a primary action that does nothing. If the feature is not built, omit the control.

## Field

Label above the control, always visible, tied with `for` and `id`. Placeholder is an example ("ava@oven.test"), never the label, never the only instructions.

```html
<label class="field">
  <span>Email</span>
  <input type="email" name="email" autocomplete="email" required
         aria-invalid="true" aria-describedby="email-error">
  <span class="error" id="email-error">That email is already on an account. Sign in instead.</span>
</label>
```

Hint (`.hint`) sits under the control. The error replaces the hint, uses `.error`, and sets `aria-invalid`. Do not signal an error by color alone; the sentence is the signal.

One column. Under 720, every field is full width. Above that, a short pair (city, postal code) may sit in a `.cluster`. Related choices go in a `fieldset` with a `legend`.

Required is the word "Required" on the label, or one line for the whole form ("All fields required") when that is true. An asterisk alone is not the label.

Checkboxes and radios use `label.choice` so the hit area is the row, with `accent-color` already set. A switch is a checkbox that takes effect immediately in settings. A checkbox is a choice submitted with the form. Do not draw a switch out of divs.

Do not validate on the first keystroke. Validate on submit, then on blur. Keep what the person typed.

## The current item

Top-bar links use `aria-current="page"`. Side-nav links do too. Both are styled in `base.css`: weight plus a mark, not color alone.

## Rows and tables

`.rows` is the default list of records. The tracks are id (`.num` or `.mono`), name, quiet meta, one action.

A table is for comparison across columns. Header text is `--ink-muted`, weight 500. Numeric columns are `.num` and end-aligned. Give the table a name with `<caption>` or an `h2` just above it. A row hover belongs on a row the person can open.

## Dialog

```html
<dialog id="delete-project">
  <form method="dialog" class="stack">
    <h2>Delete this project?</h2>
    <p>Deletes the project and its build history.</p>
    <div class="cluster end">
      <button value="cancel">Keep project</button>
      <button class="danger" value="confirm">Delete project</button>
    </div>
  </form>
</dialog>
```

The page keeps its `h1`. The dialog title is an `h2`. The safe action is the first button, so Enter does not destroy. `method="dialog"` closes and sets `returnValue`. `showModal()` traps focus and returns it on close. Escape closes. A click on the backdrop closes:

```js
dialog.addEventListener("click", (event) => {
  if (event.target === dialog) dialog.close();
});
```

Do not open a dialog from a dialog. A form dialog uses `dialog.wide`. A confirm stays narrow.

## Menu

```html
<details class="menu">
  <summary>More</summary>
  <div class="menu-panel">
    <a href="/projects/1842/copy">Duplicate</a>
    <hr>
    <button class="danger ghost">Delete</button>
  </div>
</details>
```

```js
document.addEventListener("click", (event) => {
  document.querySelectorAll("details.menu[open]").forEach((menu) => {
    if (!menu.contains(event.target)) menu.removeAttribute("open");
  });
});
document.addEventListener("keydown", (event) => {
  if (event.key !== "Escape") return;
  document.querySelectorAll("details.menu[open]").forEach((menu) => {
    menu.removeAttribute("open");
  });
});
```

Items are verbs. A destructive item is last, after a rule. Do not put a primary action inside a menu.

## Tabs

Use tabs when the panels are alternate views of the same object and they are all present. The tab is a `button` with `role="tab"`, `aria-selected`, and a roving tabindex. The panel is `role="tabpanel"`, labelled by the tab. Arrow keys move selection. Do not use tabs as the site nav.

## Toast

`.toasts` is `aria-live="polite"`. One toast at a time. A success may leave after a few seconds. An error that needs a decision is a `.banner` or an inline `.error`, not a toast. The undo pattern is in `interaction.md`.

## Banner

`.banner` is for a condition of the whole view: offline, a failed save, a permission. One sentence and, when there is a next step, one action. `.banner.danger` for something that blocks the work.

## Empty, loading, error

Empty is a stack: one sentence that says what belongs here, one action that creates it. No illustration unless the direction is Play or Soft service, and then only in the palette.

Loading that replaces a region uses blocks of `--bg-subtle` in the shape of the content that is coming, with a slow opacity pulse. Reduced motion is already forced to a static block by `base.css`. Do not use a shimmer gradient.

An error names the failure and the next step, in the region that failed, with the rest of the page still usable.

## Search

An input with a real label ("Search orders"), results as `.rows`, the query echoed in the empty line: No matches for “rye”. Highlight the match with `<mark>` styled as `--accent-soft` and `--ink`. Do not return card grids from search.

## Footer

A short cluster or stack: the name, the few real links, the year. Not four columns of places the product does not have.
