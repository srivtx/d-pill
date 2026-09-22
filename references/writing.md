# Writing

The interface has a voice, and it matches the direction. Instrument and Spec are terse. Editorial can be a full sentence. Quiet luxury is calm and specific. Play can be warm. Civic is plain. None of them shout.

Do not claim a behavior the interface does not have. Do not say a change was saved, a file was synced, or a team was notified unless that happened.

## The ban list

Do not use these in headlines, buttons, or empty states. They mark an unset page:

unlock, elevate, seamless, next-gen, cutting-edge, empower, revolutionize, the future of, all-in-one, world-class, delightful, robust, streamline, supercharge, unleash, game-changing, simply, just, easily.

Also refuse the shapes: "Welcome to X", "Your all-in-one platform for Y", "The modern way to Z", "Build faster", "Designed for teams who…". Say what the person does with the product, in its nouns.

No exclamation marks as a personality. One is already too many in a tool. Play may use one, once.

## Buttons and links

A button is a verb, plus the object when the verb alone is ambiguous.

| Unset | Decided |
|---|---|
| Submit | Save changes |
| OK | Keep project |
| Yes | Delete project |
| Click here | Read the issue |
| Learn more | See pricing |
| Get started | Create the first order |

Nav items are nouns: Orders, Pricing, The issue.

A link inside prose says where it goes. "Sign in" is a link. "Sign in to your account by clicking the button below" is not a label.

## Errors

What happened, why if you know, and what to do.

| Unset | Decided |
|---|---|
| Invalid input | That email is missing the @. |
| Something went wrong | The order didn't save. Try again. |
| Error 403 | You don't have access to this oven. Ask an owner. |
| Failed | Card declined. Try another card, or pay by invoice. |

Do not blame the person. Do not say "Oops". Do not use an error code as the sentence. The code may sit in `.quiet.mono` after the sentence when support will ask for it.

## Empty

Name the object, then the action that creates one.

- No orders yet. Create the first order.
- No invoices yet. Create an invoice.
- No matches for “rye”.

Not: "Nothing to see here!", "It's lonely in here", "No data".

The empty search repeats the query. The empty collection does not pretend the person searched.

## Confirm

Title: the consequence, with the object. "Delete this project?"

Body: what goes away that they cannot see from the title. "Deletes the project and its build history."

Safe button first: "Keep project". Destructive button: "Delete project".

## Numbers, dates, money

Pick one date form per product and keep it. A tool may use `2026-09-23` in `.mono`. A magazine uses `23 Sep 2026`. Do not mix them on one screen.

Pick 12-hour or 24-hour and keep it.

Money uses the currency symbol, `.num`, and the precision the currency actually has. Units are `.quiet`. A column of figures shares decimals.

A percentage has a decimal only when that precision is real. "10×" requires the baseline in the same breath, or it is not allowed.

The number in a headline and the number in a figure are the same number.

## Status

Use words. "Late", "Paid", "Draft", "Due today". `--danger`, `--ok`, and `--warn` color the word. Do not invent a second vocabulary of dots and pills that the sentence already covers.

## Loading and pending

The button uses the progressive verb: Saving, Publishing, Sending. A region that is loading does not say "Please wait" if the skeleton is already there. If there is no skeleton, one quiet line: "Loading orders."

## Voice check

Read the screen aloud. If a line could sit on any other product, rewrite it with this product's noun. If a line flatters the product instead of helping the person, cut it.
