# Interaction

The control's anatomy is in `components.md`. This file is how it behaves in time.

## Time

- Hover, press, and focus paint within `--dur-1` (color, background, border).
- A menu or dialog may enter in `--dur-2`.
- A drawer, if you truly need one, uses `--dur-3`.
- Exit is faster than enter. Use `--dur-1` and `--ease-in`.
- If work can take longer than about 300ms, the control shows a pending verb immediately.
- Do not animate the height of the page, and do not animate `width`, `height`, `top`, or `left`. Animate opacity and transform. Those stay smooth.
- Duration follows distance. A few pixels is `--dur-1` or `--dur-2`. Something that crosses a large part of the screen is `--dur-3`. Nothing takes longer than `--dur-3` except a skeleton pulse.
- Enter with `--ease-out` (it arrives and settles). Leave with `--ease-in` (it accelerates away). Exit is shorter than enter.
- Do not animate section reveals on scroll. Do not animate the page in on first load.
- Do not stagger a list. Play may stagger at most five items, 30ms apart, and only on that one entrance.
- If an object continues from one view to the next (a thumbnail that becomes the picture), keep it continuous. Do not crossfade two unrelated screens and call it a transition.

Play may put `cubic-bezier(0.2, 1.4, 0.4, 1)` on one element. That curve is not a token, and it is not reused. The press state is a color change in `:active`, not a scale.

The one broad exception is the craft exception, and it belongs to Soft editorial (`soft.md`), committed by name. It buys: section reveals on scroll, once per element, opacity and 8px of translate only, `--dur-3`; a stagger of at most five siblings, 30–60ms apart, that one entrance; media zoom to `scale(1.05)` under an overflow clip; a glyph that animates the state of a running machine (equalizer bars that pause with the audio); one marquee strip, pausable; and a View Transitions wipe for the theme flip, ~450ms, with an instant-swap fallback. Everything else in this file still holds. The recipes and the code are in `soft.md`.

`prefers-reduced-motion` is handled in `base.css`. Do not add a second animation that ignores it.

## Focus

Tab order is visual order. Do not set a positive `tabindex`.

The skip link is the first element in `body`. Every page has one.

`:focus-visible` in `base.css` is the ring. Do not remove it. If a brand color fails as a ring against `--bg`, set `--focus` to `--ink`.

When a dialog closes, focus returns to the control that opened it. `showModal()` does this. Do not call `focus()` on `document.body` afterwards.

Icon buttons have an accessible name. Menus can be escaped. A background that is not the dialog is inert while a modal is open; the native dialog does that.

## Forms

Submit is the moment of first judgment. After that, judge a field on blur. Do not clear the field. Do not move focus in a way that fights the person; move it to the first invalid field on submit only.

A disabled primary button with no explanation is a dead end. Prefer an enabled button that submits and then shows the error. If you must disable it, the hint under it says what unlocks it, and the button remains readable.

The pending state is in `components.md`. Double submits are blocked by disabling during the request, not by hoping.

## Destructive actions

If the action is reversible for a few seconds and it only affects the actor's own work, do it, then offer a toast with Undo. Undo restores the object.

If it is not reversible, or it destroys other people's work, use the confirm dialog in `components.md`. The title names the object. The button repeats the verb and the object. "Delete project", not "Yes" and not "OK".

## Optimistic updates

Use them for a reversible toggle: star, complete, pin. Paint the new state immediately. If the request fails, paint the old state back and show the error. Do not optimistic-delete without the undo toast.

## Five conditions

Every view that shows a collection or a record specifies all five. Do not design only the full one.

| Condition | What the person sees |
|---|---|
| Ideal | The work, the primary action, quiet meta. |
| Empty | What belongs here, and the action that creates the first one. |
| Loading | The shape of the content, as quiet blocks. The chrome stays put. |
| Error | What failed, what to do, the rest of the page still there. |
| Partial | What is showing and what is missing: "Showing 40 of 212." Plus the action to load the rest. |

Stale data that is still safe to read is one quiet line: "Updated 3 hours ago." Stale data that is unsafe to act on is a `.banner` that names the consequence and offers a retry.

Offline copy tells the truth about what you actually built. "You're offline. Changes stay on this device until you reconnect." is allowed only when that queue exists. Otherwise: "You're offline. This page may be out of date."

## Motion and meaning

Animate the thing that changed, from the place it came from. A menu rises 4px from its button. A toast does not fly across the screen. A route change does not fade the whole page.

Hover on a row or a directory item changes background or border. It does not scale, lift, or tilt the object.

## Keyboard

- Buttons and links work with Enter. A button also works with Space.
- A menu closes on Escape and on an outside click. The snippet is in `components.md`.
- Tabs, when you have them, move with the arrow keys.
- Do not invent a shortcut. If the product has one, show it in `.quiet.mono` at the end of the menu item.

## The primary action

It is the largest, or the only filled button, and it sits at the end of the decision: the end of the form, the end of the dialog, the end of the header cluster. In a header, the title is at the start and the action is at the end (`.cluster.between`).

Fewer choices. A region offers one primary. Secondary actions are quiet. Everything else can live in More.
