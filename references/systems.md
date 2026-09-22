# Systems

How to grow a design system without dissolving it. The tokens you already have are in `foundations.md` and `base.css`. This file is the discipline of adding to them.

## Add a token only when the role repeats

A value used once is a local decision. A value used the same way three times is a token. Name the role (`--warning-soft`), not the paint (`--amber-200`) and not the place (`--card-border`).

If you cannot say the role in a few words, you do not have a token. You have a one-off. Keep it next to the component.

Do not add a step to the space scale. The scale is done. If 20px feels necessary, the layout is between two steps and one of them is the right one.

## Add a component only when the behavior repeats

The third time you build the same control with the same states, it becomes a component. Before that, copy the markup. A component library of one is how pages get abstract and ugly.

A new component ships with every state it can actually be in: default, hover, focus-visible, active, disabled, and the ones that apply (loading, error, empty, selected). A component with a default state only is a picture.

It uses the existing roles. It does not bring its own hex, its own radius, or its own shadow.

## Naming

Names are the language of the product plus the role. `OrderRow`, `Price`, `Quiet`. Not `CustomCard2`, not `BlueButton`, not `Wrapper`.

Variants are few and named for intent: primary, quiet, danger. Not for look: rounded, large, purple. Size, if you truly need two, is a density choice from `layout.md`, not a new variant ladder (xs, sm, md, lg, xl) on every component.

## Dark and brand

A new role is designed in both themes if the product has both. Check it against the safe band. A component that only works on paper is unfinished if Signal, or a dark toggle, is in scope.

When a brand arrives later, map their type and color onto the roles. Do not fork a second stylesheet called `brand-overrides.css` full of unrelated hex. `color.md` says how a hex becomes an accent and a neutral.

## What you write down

For each new component, four lines are enough:

- What it is for, and what it is not for.
- The states.
- The token roles it uses.
- What it refuses (a card that refuses a shadow, a chart that refuses a pie).

If the note is a page long, the component is doing too much. Split the behavior, not the documentation.

## Do not theme by scattering

A theme is a set of role values. Swapping themes means swapping those values, not rewriting components. If a component has a color inside it that is not a role, it will be wrong in the next theme. That color is the bug.

## Version by commitment

Change the system when the direction changes or a real repeated need appears. Do not restyle the tokens because a page felt boring. Boredom is usually evenness. Fix the poster (`sense.md`) before you invent a new color.
