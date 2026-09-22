# Arrange

Which container the information wants. Primitives are in `layout.md`. Charts are in `dataviz.md`. Pick here before you draw boxes.

## Decide from the job

| The person needs to | Use |
|---|---|
| Open one record and act on it | `.rows`. Name, meta, one action. |
| Compare values across columns | A table. Numeric columns `.num` and end-aligned. |
| See the object | A gallery or the directory in `layout.md`. The picture is the point. Name and price always visible. |
| Read in order | A single column at `--measure`. |
| Follow a sequence that must happen in order | A numbered stack (`information.md`). |
| Choose one of a few peers | A `.split` or a short row of peers. Pricing, plans, two paths. |
| Watch something change over time | One chart, or a big number and a quiet comparison. |
| Scan a stream that keeps growing | A feed of rows, newest first, with a time. Not cards. |
| Fill something in | One column of fields (`components.md`). The primary action at the end. |

If two rows of the table both seem true, the job is not named yet. Name it, then pick again.

## What not to reach for

- A board of cards (kanban) only when the columns are real states the person moves work between. Not for features, not for plans, not for a homepage.
- A bento grid (uneven tiles for decoration) is wallpaper with extra steps. Unevenness comes from scale of type and pictures, not from a mosaic of boxes.
- Tabs only when the panels are alternate views of the same object and they are already on the page (`components.md`). Tabs are not site navigation.
- An accordion only when each header is a real question and the page would be too long if they were all open. Do not hide the answer to the main question in one.
- A carousel only for peer pictures of one object (a product's views), with a count ("2 of 6") and a way that is not only dots. Never for the argument of the page. People do not see slide two.

## A form is a page

A form is a column, about 28rem, labels above, one idea per group. Groups have headings when there are more than one: Contact, Delivery, Payment. The gap inside a field is tight. The gap between fields is a density step. The gap between groups is a section step.

The primary button is the last thing in the column, full width on a phone, content width on a desktop. It says the verb and, when money is involved, the amount.

A long form is named steps, not one scroll with forty fields. Each step has a title, a way back that keeps what they typed, and a visible count of steps ("2 of 3") in `.quiet`. Do not use a progress bar as the only indicator.

Optional fields are few. If most fields are optional, the form is a record the person is editing, and the empty ones can wait. Do not star a field. Write Required, or say "All fields required" once when that is true.

## A feed

Time is the spine. Each item is one sentence or one object, the time in `.quiet` or `.mono`, the action on the item. Avatars only if the person is the point (a message), at the sizes in `details.md`. Do not give every event a card, an icon in a circle, and a relative time you cannot parse ("3mo"). Absolute when it matters ("23 Sep"), relative only for today ("2 hours ago") and then still have the absolute time available.

## Search results

The query is in the field and repeated in the heading or the empty line. Results are `.rows` or articles with a title and one line, not cards. The match can be `<mark>` in `--accent-soft`. "No matches for “rye”." Offer to clear the query. Do not show unrelated "you might like" items under a failed search unless they are honestly related and labeled as such.

## Empty, missing, and wrong pages

- **Empty collection.** What belongs here, and the action that creates the first one (`writing.md`).
- **No matches.** The query, and a way to clear it.
- **404.** The name of the product, one sentence ("That page is gone."), one link to a real place (home, or search). Do not make a joke the only content. Do not dump the whole sitemap.
- **Down.** What is broken, whether their work is safe, what to do. "Checkout is down. Your bag is saved on this device. Try again in a few minutes." Only claim the bag is saved if that is true.
- **No permission.** Who can open it, and what the person can do instead. Not a lock illustration.

These pages use the same type and the same frame as the rest of the product. A 404 that looks like a different brand is a second website.
