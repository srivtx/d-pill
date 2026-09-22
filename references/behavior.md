# Behavior

How a person actually moves through a page. The wiring of focus, forms, and confirmations is in `interaction.md`. This file is the judgment those patterns come from.

## The action is close and few

A control is easier when it is larger and closer to where the person already is. Put the action on the object it changes. "Mark out" sits on the order row. "Delete" sits in that object's menu or dialog, not in a toolbar at the other edge of the screen.

The time to choose grows with the number of equal options. One primary per region. The rest go behind More, or they are quiet buttons. Twelve pills of the same weight is not a menu. It is a stall.

On a phone, the bottom of the screen is easy to reach and the top corners are not. That does not mean a sticky bar glued over the page. It means the submit of a form sits at the end of the form, and the top bar stays a short name plus one action.

## Recognition, scent, disclosure

People recognize a thing they can see. They struggle to remember an icon they saw three screens ago. Label the icon, except for a very small set the whole product treats as words: close, menu, search. Even those prefer the word when there is room.

A link tells you what you will get. "Pricing", "The night bake", "Order 1842". "Learn more" and "Click here" have no scent. The wording rules are in `writing.md`.

The first view holds the decision. The rest is available, not dumped. Advanced fields live in a `<details>` with a label that says what is inside ("Delivery notes", not "Advanced"). Hidden has to be findable.

A settings page is groups of three to seven rows under headings. A long undifferentiated list is not "simple." It is unreadable. Phone numbers and card numbers are grouped as they are spoken.

## Response

Every successful action changes something the person can see. A save that leaves the button looking idle feels broken. Use the pending verb, then a past-tense quiet word ("Saved") or a toast, then return the button to its name.

If the result happens somewhere else, say where. "Added to today's orders."

The control acknowledges the press on `:active` in the same frame. Waiting for the network before any change makes the interface feel dead. The pending state starts immediately when the work may take longer than about 300ms.

Chrome paints immediately. Data may skeleton. A blank white page while JavaScript boots is a failure. The ground and the type are HTML and CSS, so they are there before the data.

## Trust

The default is the safe, common choice. Do not pre-select a purchase, a subscription, or a destructive option.

Do not invent urgency. "Only 2 left" is allowed when it is true and you are prepared for it to be checked. A countdown you reset on refresh is a lie, and the page will look like one.

Do not confirmshame. The decline button is "No thanks" or the specific refusal, not "No, I hate saving money."

Do not trap the back button. A dialog is not a new history entry. A step in a flow has a URL or an obvious way back. Refresh restores the view the person thinks they are on, or it explains why it cannot.

Filters that define what you're looking at belong in the URL when the stack can do it. A list the person cannot share or refresh is a list they do not trust.

## Performance the person feels

Perceived speed is a design decision.

- The skeleton matches the final geometry (`details.md`).
- Images reserve their box.
- Fonts swap onto a fallback of the same genre (sans for sans, serif for serif), which the stacks in `direction.md` already do.
- Do not load a second illustration library, a second icon pack, and a motion library for one page.
- A long list paginates or loads more with a count ("Showing 40 of 212"). Do not mount a thousand rows because the array exists.

## Patterns, not inventions

People arrive knowing how a checkbox, a link, a back button, and a search field behave. Use that. Invent the composition, the type, and the material. Do not invent a new way to select one of three options when a radio group will do.

A new gesture (swipe to delete, drag to reorder) is extra, never the only way. The labeled button still exists.
