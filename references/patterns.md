# Patterns

Interface arrangements that are not the page types in `surfaces.md` and not the containers in `arrange.md`. Use the one that matches the job. Do not invent a second way to do the same job.

## Master and detail

A list on one side, the open record on the other. The list is `.rows`, narrow. The detail is the well, wide. Selecting a row sets `aria-current` and shows the record. On a phone the list is the page and the record is the next page, with a way back. Do not show a tiny detail under a list on a phone.

The detail has one `h1` (the record's name) and one primary action. The list does not have its own competing primary. Creating a new record is the list's action, or the detail's empty state, not both.

## Inspector

A third region, 16–20rem, for properties of the thing in the well: name, status, dates, a few actions. It is a definition list, not a form, until the person edits. The inspector can close. The page makes sense without it. Do not put the only copy of the name in the inspector.

## Split view

Two peers side by side (a diff, a translation, a before and after). They scroll together if the comparison is line by line. They scroll apart if they are two documents. Label each pane. On a phone, stack them and repeat the labels.

## Command palette

A dialog opened from the keyboard, for people who live in the tool. The input is "Jump to…", the results are a list of destinations and actions, the current row is marked. Escape closes. It does not replace the visible navigation. If there is no keyboard culture in the product, do not add one as decoration.

## Filter bar

Filters are labeled controls in a cluster, above the list they change. The active filters are visible as words the person can remove, not only as a hidden state of a dropdown. The count of results sits in the same band. Clearing is a text button, "Clear filters", shown when a filter is on.

## Bulk actions

When the person can select rows, the actions that apply to the selection appear only when something is selected, in a bar that names the count: "3 selected." The actions are verbs. They go away when the selection is cleared. Do not show disabled bulk buttons on every row.

## Pagination

Use pages when the total is known and the person may need a specific page (a catalog, a log). Show the range: "1–40 of 212." The current page is weight plus a mark. Next and previous are words.

Use "Load more" when the stream is the point and a page number is meaningless. Keep the count.

Do not use infinite scroll for something the person must find again later. It throws away the place they were.

## Calendar

A month is a grid of days. The day number is the content. Events are one line, or a count, not six colored bars. Today is a mark (weight, or a ring), not a filled rainbow. A selected day is `--accent-soft`. Keyboard: arrows move the day. A list of the selected day's events sits beside or below the month, as rows. On a phone, the list is the primary and the month can collapse.

Do not use a calendar widget to display a single date the person will not change. Write the date.

## Media row

A thumbnail, a name, a meta line, an action. This is `.rows` with an image in the first track. The image has a fixed ratio so the rows do not jump. The thumbnail is 40px in a dense list and up to 96px if the picture is the point. If the picture is the point, you are in a gallery, not a media row.

## Definition list

A term and its value, stacked or in two columns. Settings, inspectors, receipts, spec sheets. The term is `--ink-muted` or small. The value is ink. Do not card each pair. A receipt groups them: items, then totals, with the amount due larger (`proportion.md`).

## Wizard

Named steps, from `arrange.md`. Show the step you are on and the number of steps. The way back keeps the answers. The last step says what will happen and repeats the irreversible facts (the amount, the deletion). Do not use a wizard for two fields.

## Consent

If you must ask: one sentence that says what you store and why, in plain language, and two actions of equal visual weight, accept and refuse. The refuse path is a real choice, not a maze. Do not pre-check a pile of purposes. Do not use a dark pattern (`behavior.md`). If you do not need consent for the page to function, do not ask.

## Pagination of a document

A long doc has a contents list (`surfaces.md`). At the end, the next document, with its real title. "Next" alone is not a name.

## What a pattern is not

A pattern is not a card with an icon, a title, and two lines of lorem. That is the unset layout. If you cannot find the job above, use a stack and a heading.
