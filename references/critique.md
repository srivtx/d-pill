# Critique

Run this on the real markup after it exists. A fail is fixed before you call the UI done. Do not paste this list back to the user. In the reply, name the direction and one sentence on what changed.

The gate has two halves and they run in order. First the machine: `python3 scripts/critique.py` on every HTML and CSS file you wrote — it checks the scales, the floors, and the tells, and exits 2 with `file:line:col [rule]` findings until they are fixed. The registry behind each rule is `references/rules.json`. Then this list, which is the judgment half: direction, focal point, one weather. The machine cannot see those, and a clean machine pass buys the review, not the pass.

Check a wide window (around 1280) and a 390-wide window. If the page runs and a browser is available, tab from the skip link through the primary action, fire that action, and fire one error. A screenshot of the first paint is not this gate.

The safe band for token lightness is in `foundations.md`. The ratios below are the floor when a color sits outside that band or when you are unsure.

## Direction

- The committed direction, or the named style in `styles.md`, is visible in the type, the color, and the radius. A named style was not sanded back into a generic app.
- The refusal list in `craft.md` is honored, or a real brand explicitly overrides a specific item.
- One accent. Status colors are only on status.
- One material, as named in the commitment. Nothing on the page belongs to a second material (a shadow on paper, a glow on a tool, glass on a document).
- The page looks like it did not try. One weather, the work louder than the chrome, the finish pass in `taste.md` done. The mark's spectrum has not leaked onto the interface.
- The accent is not doing the hierarchy's job. Cover it, and the poster still has a shape.

## Hierarchy

- One focal point. Squinting still separates the first thing, the sections, and the action.
- The page uses about four type sizes, from the ramp.
- Weights are only the ones in `foundations.md`.
- The line under a display claim is a `.lede`, not a full-width paragraph.
- A display headline is broken into phrases, as in `sense.md`. The last line is not one stranded word.
- Neighboring text sizes are not adjacent steps on the ramp. One size is obviously larger.
- Body leading fits the measure. Display leading is tight. Prose is not justified. Emphasis follows `type.md`.
- In gray, the poster still has a shape. Accent is a note, not a second ground (`color.md`).
- Rounded boxes that contain rounded boxes use a larger outer radius (`geometry.md`). Icons and labels align on the cap height, not the em box.
- Vertical space comes from stack, section, or rows. There is no second rhythm of random margins.

## Color and type

- Roles come from `base.css`. No stray hex.
- Body text, labels, and hints that carry meaning clear 4.5:1 against their background.
- Text at 24px or larger, and bold text at 19px or larger, clears 3:1.
- `--line-strong` edges, the focus ring, and essential marks clear 3:1 against the adjacent color.
- `--ink-muted` is inside the safe band. It is not disabled-gray.
- The focus ring is visible on every interactive element. `:focus-visible` has not been removed.
- Two families at most, and the second changes the voice. The faces actually load.

## Structure

- Edges share an axis. Nothing is centered that `layout.md` tells you not to center.
- Under 720 the layout recomposes: one column, the action still visible, no sideways scroll except a declared table or code block.
- A directory treatment appears only for peer objects with their own action.
- Chrome is one treatment deep. No object carries a border, a shadow, and a tint.
- The first viewport of a marketing page has the claim and the action.
- The container matches the job in `arrange.md`. A carousel is not carrying the argument. Labels are not clipped by a fixed width (`world.md`).

## States

- Every control has hover, focus-visible, and disabled or pending where the action can be unavailable.
- The view specifies ideal, empty, loading, error, and partial where it shows a collection.
- A destructive action either undoes or confirms, using the pattern in `components.md`.
- The primary action does something. Pending keeps the width and changes the verb.
- The action sits on the object it changes. One primary per region (`behavior.md`).
- A selling page argues in the order in `narrative.md`. Proof is real or absent. The first and last actions share a destination.

## AI surfaces

For a chat, copilot, or agent surface; the rules are in `ai-interfaces.md`. Fire the stream and the tools before judging.

- The view pins only while the person is at the bottom. Scroll up during a stream: the pin releases, and a "Jump to latest" affordance appears when content lands below.
- Nothing below a streaming block moves between two frames. Fire the stream and watch the button row and the composer.
- The stop control is reachable while streaming. Stopping keeps the partial answer and says "Stopped," styled quiet, not as an error.
- The stream writes at the frame budget, not per token. The caret is a 1px block, not a spinner.
- Every citation marker resolves, is numbered, and opens the cited source. No marker the model did not produce.
- An approval card names the object and the verb. Anything destructive or external waits for the person.
- No tool-call theater: rendered steps all ran. No fake typing delay on a finished answer. One mark for the model's presence, not sparkles on every heading.

## Writing

- No word from the ban list in `writing.md`, unless it is the product's actual name.
- Buttons are verbs. Errors say what to do. Empty states name the object.
- The interface does not claim a behavior it does not have.
- No invented customers, logos, testimonials, or metrics. Sample data is consistent with itself.

## Access

The design half of this list is `a11y.md`. These are the fails.

- `html` has the right `lang`. The title is the view and the product.
- One `h1`. Heading levels do not skip.
- Inputs have visible labels. Icon buttons have accessible names. Images that mean something have alt; decorative images have empty alt.
- Tab order matches the visual order. The skip link is first and becomes visible on focus.
- A modal traps focus, closes on Escape, and returns focus.
- `prefers-reduced-motion` is intact.
- On a coarse pointer, targets meet the floor already set in `base.css`.

## Truth in the figure

- Numbers in a screenshot or chart match the copy.
- A chart has a unit, a labeled axis or an end label, and no decoration that changes the reading.
- Links go where the words say. Buttons that look primary are primary.

## The last pass

Remove one treatment, as `craft.md` describes. Then look again at 390 and at 1280. If the action, the hierarchy, or a floor got worse, put that treatment back. Otherwise leave it off.
