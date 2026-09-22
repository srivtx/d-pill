# Sense

This is how to see a page before you decorate it. The tokens, the directions, and the refusal list are elsewhere. Use this to decide what the page should feel like, then let those files specify the parts.

Read it before you write markup. A beautiful interface is mostly proportion, one material, and the nerve to leave things out.

## Look at it as a poster first

Ignore the components. Squint until the page is three or four masses: a dark mass, a light mass, a small sharp mass.

If those masses do not make a shape, no button style will save it. Move something, enlarge something, or delete something until the poster has a shape. Then come back and make it usable.

A tool's poster is quiet: a band of chrome, a field of rows, one dark button. A magazine's poster is a huge line of type and a lot of paper. A gallery's poster is one picture and a name. If you cannot say which poster you are making, you have not committed.

## Evenness is the cheap look

The unset page is even. Same gap everywhere. Same size type. Same weight. Same box. Same radius. Same saturation. Evenness feels unfinished because nothing has been chosen.

Beauty is uneven on purpose.

- One thing is large. The rest is plainly smaller. Adjacent steps on the type ramp (16 next to 18) do not count as a choice. Skip a step.
- One thing is the accent. A large area stays quiet: low chroma, the paper, the ink.
- One gap is tight, because those items are a group. The next gap is obviously wider.
- One edge is shared by almost everything. One element may cross it, once, and that crossing has to be the point (a photograph bleeding off the frame, a caption in the margin).

If you cannot point at the unevenness, the page is still a template.

## Paper, then ink, then one note

Start with the ground, not the brand color.

The ground is a paper. Pure white (`#fff`, lightness 1) looks like an unopened template. Pure black looks like a void. A beautiful ground is slightly warm or slightly cool, at a very low chroma, which is what `--bg` already is. Warm paper (hue around 40–70) feels like a room. Cool paper (hue around 200–230) feels like an instrument. Pick the one the direction names and stop tuning it.

The ink is soft, not `#000`. Soft ink looks printed. Hard black looks like default CSS.

The note is one accent, slightly dirty (chroma around 0.12, not 0.25). It is small. High chroma on a large area turns into a costume. Yellow and lime are notes you write with, not fields you fill with white type. That constraint is in `foundations.md`.

A color changes next to what it sits on. The same brown looks cheap on pure white and expensive on warm paper. Judge the accent on the actual ground, not in a swatch by itself.

Do not encode a meaning in red versus green alone. Status is a word, and the color helps. A person who cannot see that pair still has to get it.

## The headline is a shape

A display line is set, the way a title on a cover is set. You choose the line breaks. Each line is a phrase. The last line is not one short word hanging under a long one.

```html
<h1 class="display">Bread that waits<br>until the room is quiet.</h1>
```

Read it aloud. If you would not say it that way, the break is wrong. If the second line is much shorter than the first, rewrite or rebreak until the two lines have a similar mass, or the short line is a deliberate last beat and not an accident.

Tracking gets tighter only as the type gets larger. At body size, tracking stays 0. Tight tracking on small type looks like a mistake.

Italic is a change of voice for one word or one title, not a style you apply to a paragraph to make it "elegant."

The right edge of a paragraph, the rag, should look like a shoreline. `text-wrap: pretty` is already on. If a line ends in a single short word over and over, rewrite the sentence. Do not justify. Justified text on the web opens rivers of white inside the paragraph.

## Emptiness is a material

On a marketing page, most of the screen is the ground. That emptiness is aligned to the same axis as the type. It is not leftover space around a centered stack.

A full-bleed photograph next to a wide margin is the contrast that feels editorial. The photograph touches an edge. The type does not have to.

In a tool, emptiness is smaller and it means "this is one group, that is the next." Do not pad a tool like a manifesto. Do not pack a manifesto like a table.

When a section feels busy, add space before you add a box. A box is what you use when space has already failed.

## One material

Name the material in the commitment: warm paper and a pencil line, a dark field and one phosphor, a wall with one photograph, clay-colored paper and a soft radius.

Then every surface agrees. A hairline border on paper. No drop shadow pretending the paper is floating. No glass. No gradient mesh. No second illustration style. Depth is reserved for something that is actually above the page: a menu, a dialog, a toast. Those use `--shadow-overlay` and nothing else does.

Mixing materials is the usual way a page starts to look generated. One material, taken seriously, looks expensive even when the layout is simple.

## The one break

Perfect regularity is sterile. The page follows an axis, a scale, and a type ramp, and then it breaks one rule on purpose.

Legal breaks: a line of display type that is much larger than the ramp suggests. A photograph that bleeds. One italic word. A margin caption. A single rust-colored mark in an otherwise ink-and-paper page.

Illegal breaks: a second accent, a second radius family, a shadow on a card, a centered block in an otherwise left-aligned page, a new font "for personality."

One break. If you want a second, remove the first.

## Scroll is a sequence of posters

Each section is its own poster with its own shape. A split, then a ruled list, then a quote, then a short close. The eye should feel a change of pace.

The failure mode is the same band repeated: icon, heading, paragraph, and a tint, four times. Alternating the background color is not a change of pace. Changing the proportion is.

The first screen contains the claim and the way in. What the thing is should be obvious without scrolling. Everything below is evidence, not a second homepage.

## The button is quieter than the sentence

The claim does the persuading. The button is the way through. If the button is a large gradient and the sentence is timid, the page is shouting the wrong word.

In a tool, the button can be the loudest pixel, because there is no claim. It is still small, and there is still only one of it in that region.

## Motion is confidence by being still

A page that is sure of itself does not dance when it loads. Sections do not fade up as you scroll. Nothing bounces.

If something moves, it is the thing that changed, it moves a few pixels, and it settles. A menu coming from its button. A toast. That is the whole vocabulary. Durations live in `base.css`. The judgment is: when in doubt, do not animate.

## The last look

Do this after the critique checklist, with your eyes, in this order.

1. Squint. Point at the first mass, the sections, and the action. If you hesitate, the hierarchy is too even.
2. Read the headline aloud, including the line break.
3. Look at the rag of the longest paragraph.
4. Name the material. Find anything that belongs to a different material and remove it.
5. Cover the accent with your hand. The page should still have a shape. If it collapses, the accent was doing the hierarchy's job.
6. Look at 390 pixels wide. The first screen is still a poster, just a narrower one. The claim is still a claim. The action is still on screen.

Then remove one treatment, as `craft.md` says. The page should feel more sure, not more empty of meaning.
