# AI interfaces

Surfaces where a person talks to a model, or a model acts for them: chat, copilots, agents, generators, streaming answers. The rest of this repo's laws hold unchanged. This file is the part the frontier added, and it is mostly restraint.

## Anatomy

- One conversation per view. The transcript is the page. The composer is the bottom edge. A sidebar of other conversations is desktop only, and it is a list, not a card grid.
- The transcript is a document, not a feed of bubbles. Alternating left/right bubbles are for two people. The person's messages sit author-side and compact; the machine's answer is full width, either plain on `--bg` or on one `--surface` block, never both.
- The composer grows to about six lines, then scrolls inside itself. Attachments are chips above the text. Enter sends; Shift+Enter breaks the line; the send button is the one primary on the surface.
- Model name, token cost, and context left are `.quiet` `.mono` at one edge. They are gauges, not a header bar.
- Nothing sits between turns. No divider, no avatar per message, no timestamp on every line. A timestamp appears on hover or on turn boundaries only.

## Message states

A machine message has more conditions than a static one, and every one is designed:

| Condition | What the person sees |
|---|---|
| Queued | Accepted, not started. The send control turns pending; the turn's place is reserved. |
| Streaming | Text arriving, caret visible, stop reachable. |
| Complete | The full answer, sources settled, actions offered. |
| Stopped | The partial answer kept, one quiet line: "Stopped." |
| Failed | What failed and what to do: "The model didn't answer. Retry." Never a stack trace. |

- Streaming is the baseline. A blank wait for a finished answer reads as broken.
- The streaming caret is a 1px ink block that pulses at most as slowly as a skeleton. It is not a spinner; a spinner claims progress the interface cannot see.
- Stopping is immediate, keeps the partial text, and is not styled as an error.
- Retrying replaces the failed turn in place. The transcript does not fork.

## Streaming stability

Three failure modes come with streaming, and all three are design bugs, not engine bugs:

1. Scroll. Pin the view to the bottom only while the person is already at the bottom. The moment they scroll up, the pin releases. A "Jump to latest" affordance appears when new content lands below. The interface never decides where attention goes.
2. Shift. Reserve the space a growing block will take: a `min-height` on the streaming turn, an aspect ratio on incoming media. Nothing below a stream moves. A button the person was about to click does not travel.
3. Frames. Write the DOM at the frame budget (a rAF or a 30–60ms batch), not per token. The stream can outrun the screen; the screen is the contract.

- Markdown renders progressively. A code block or table takes its final shape as it closes; an unclosed fence shows as code, not as raw syntax.
- Smooth scrolling during a stream is off. The follow is a jump to bottom, not an animation fighting the reader.
- The scroll pin and the jump affordance are keyboard reachable.

## Tool calls and agent actions

When the machine does more than answer, its work is shown as it happens:

- A tool call is one row: verb, object, state (running, done, failed). Collapsed by default, expandable on demand. Only real calls are shown; steps that did not run are theater, and theater is refused.
- An action that changes anything outside the conversation is an approval card: what will change, in the person's vocabulary; the verb and the object on the button; reject and edit as quiet actions. Approve-then-run, not run-then-tell.
- The ask-first default covers money, sends, writes to other systems, and anything destructive. Reversible local toggles may run first and offer undo, under the toast rules in `interaction.md`.
- After an approved action runs, the result is stated in one line with a link to the object. The transcript is a log, not a ceremony.
- Errors from tools keep the tool's real words, translated: "The calendar API refused the write: the event overlaps." Not "Something went wrong."

## Citations and sources

- A claim that rests on a source carries a numbered marker. Markers resolve when clicked; a link that exists before it resolves is not shipped.
- Sources are numbered in order and open in a new tab. The marker is `--ink-muted` until hover, then ink; it clears 3:1 either way.
- Never render a citation the model did not produce. A fabricated source is a fabricated testimonial.

## Generative UI

When the model composes the interface from components, it composes from a vocabulary, not from freedom:

- The vocabulary is a small set of elastic primitives you shipped: a text block, a list, a key-value table, a media block, a chart, an action row. The model picks and fills; it does not invent markup.
- Every generated element uses the tokens and classes in `base.css`. Generated chrome is still one treatment, the direction's radius, the scale's spacing.
- The floors apply to generated UI identically. A model-made low-contrast chip fails the gate the same as a hand-made one.
- Each primitive handles its own empty, error, and partial state, so the model cannot compose a dead end.
- When a person might mistake generated copy for editorial copy, it carries one quiet mark. One, not a border of badges.

## Trust

- The person can tell what is theirs, what is the model's, and what the model did on its own. Authorship is visible without forensics.
- Memory use is named when it changes the answer: "Using the preferences you saved." Not a settings archaeology dig.
- Confidence is reported only when the model reports it. "I'm 99% sure" with no such number is a lie with a decimal.
- One mark for the model's presence: a glyph, a name, a border color. Sparkles, if they are that mark, appear once per surface — never on every heading, never on content.
- "AI" is said once, where the product explains itself. Pills for New, AI, and Beta are refused in `craft.md` and they are refused here.

## Refuse

- A spinner where streaming text would be.
- A fake typing delay on a finished answer.
- Tool-call theater: rendered steps that did not run.
- A mascot with expressions, or a persona costume per turn.
- Bubbles alternating for a person and a machine.
- Confirmations on reversible actions — trust friction is a cost, not a feature.
- Auto-running anything that writes outside the conversation.
- A "regenerate" that silently discards the previous answer.

The critique gate for these surfaces is in `critique.md` under "AI surfaces."
