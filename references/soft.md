# Soft editorial

The craft-site style: quiet cards with a hairline border and a soft shadow, a grotesk for the page, a display serif for the one quote that matters, mono for the machine facts, dashed rules between sections, and motion that rewards a person who pays attention. Commit it by name from `styles.md`. This file is the recipe. The motion allowance it relies on is the craft exception in `interaction.md`. Pixel drawing and glyph tiles are in `icons.md`. The sources are in `reading.md`.

People point at a site built this way and say "neumorphism." The 2019 meaning of that word — extruded dents in the same gray, no borders, text in the shadow color — failed contrast, failed focus, and died inside a season. What survived is the corrected revival, and the correction is the whole recipe: the border carries the edge, the shadow only lifts, text stays at `--ink`, and the focus ring depends on neither. Drop any one line and the surface goes back to failing. Every ratio below was checked with `scripts/contrast.py`.

## Start from

Editorial for a front page with a point of view. Atelier for a small set of work. Play only when the mascot or the marquee is the point. The soft surface and the status strip work in any of the three.

## The soft surface

One written exception to the chrome law: a hairline border and a soft shadow, together, on the same surface. Both, because the shadow alone loses the edge on dark, and the border alone loses the lift on light. The exception is for cards and slabs. Not for rows, not for inputs, not for the page itself.

- Ground: `--bg`, untouched. The card sits at `--surface`, one step off the page, never two.
- Border: `var(--border)`, 1px, visible in both themes. Ink (0.62 L) on the ground clears the 3:1 edge floor.
- Shadow: on light, `0 1px 2px` and `0 8px 24px` at ink around 5% — ink-based, not black-based. On dark, one wider black shadow at 30–40%. The shadow lifts; it never carries meaning.
- Radius: 12–16px on cards. Controls inside keep `--radius`.
- Text: `--ink` and `--ink-muted`. Ink on surface clears 4.5:1 by a wide margin (≈14:1 at the base palette). Text is never set in the shadow color.
- Focus: the standard `:focus-visible` ring from `base.css`. A control never signals focus by swapping shadows.
- Hover: the shadow deepens one step at `--dur-1`, or the border warms. Not both. Press is an `:active` color change, not a scale.

## Type and meta

- Body: a grotesk with personality — Space Grotesk, Bricolage Grotesque. The page speaks in it.
- Display: a serif with a true italic — Instrument Serif, Newsreader. It sets the one quote over the banner and at most one heading per page. The second family has to change the voice; if it does not, use one family.
- Meta: mono at `--text-xs` for labels, timestamps, and counts. A fact set in mono reads as a measurement, which is the point.
- Rules: dashed hairlines (`1px dashed`, `--line-strong`) between sections, and between a card and a strip it opens. Solid for tables, dashed for the journal.

## The status strip

The signature block: what the person is listening to, watching, or where they are — two or three small cards under the headline, not a widget farm.

- Each card: the soft surface, one 64px tile, a caps or mono label, a name, a quiet detail, one quiet action at the end.
- The tile is the same box in every card, so the row reads as one object, not three designs.
- A live thing may pulse: one 6px dot, ~2s ping. One pulse per strip.
- An audio card may open a seek strip under the whole row — the row's full width, not one card's — so the cards never change size while it plays. The cards stretch to equal height; the strip is a separate element and collapses when the sound stops. The label degrades honestly: "last played" with a link out beats a dead embed.

## Motion

These are the craft exception's allowances, from `interaction.md`. What they buy:

- Reveal on scroll, once per element: opacity 0→1, translateY 8px→0, `--dur-3`, `--ease-out`. Never the whole page at once, never twice.
- Stagger: at most five siblings, 30–60ms apart, that one entrance only.
- Media hover zoom: `scale(1.05)` cap, `--dur-2`, `transform-origin: center`, inside an overflow clip. The chrome does not zoom.
- One spring curve per surface, on one element: `cubic-bezier(0.2, 1.4, 0.4, 1)`. Not a token. Not reused.
- The theme flip: View Transitions API, a circle that wipes from the toggle in ~450ms. No support: instant swap. `prefers-reduced-motion` already collapses it in `base.css`.
- A machine that runs may animate its own glyph: equalizer bars while audio plays. It stops when the thing stops, because it is a state, not a decoration.
- One marquee strip, 30–70s, pause on hover. A second marquee is a costume.
- One mascot, at most 40px, on the bottom edge, out of the flow, never over a target. It is Play borrowed for the last 40 pixels of the page.
- An inline text link may grow an underline on hover: one 1px `currentColor` line drawn from the middle outward (`background-size`, no extra element), `--dur-1`. Pick one hover answer per link — a row that already answers with color does not also get the underline. Headings and buttons never carry it.
- A 2px reading-progress hairline at the top edge may track the scroll through the CSS scroll-driven animations module: `animation-timeline: scroll()`, `@supports`-gated, no script, hidden where unsupported and under `prefers-reduced-motion`. It is a ruler, not a performance.
- One control row may magnetize: each control leans toward the pointer a few pixels on springs (stiffness ~350, damping ~28, pull ≤ 6px) and releases home on leave. Fine pointers only — nothing happens on touch — and it is off under `prefers-reduced-motion`. Controls only: never rows, never text, never cards. One row per page.

## Pixel art and glyph tiles

One pixel object per surface: the banner or the tile, not both. A banner sits dark (L ≤ 0.3) so a serif italic quote in paper clears 4.5:1 on its worst pixel — checked, not assumed. Pixel drawing rules are in `icons.md`.

A repo, an org, or a side project with no mark gets a glyph tile, not a colored circle with an initial: a tone gradient (two steps of one hue, low chroma) with the glyph in `currentColor`. Light theme gets the pastel step, dark theme the real hue. Rules in `icons.md`.

## Refuse

Same-gray dents, text in the shadow color, focus by shadow, a squircle on every div, glass and soft on the same page, three stat cards where one sentence would do, a marquee per section, animation on page load, a mascot per section, pixel art as the whole material, an underline on a heading, a progress hairline on a three-screen page, a magnetized card, a second magnetized row.

## The override

Paste after `base.css`. This is the style, as code. It renders as written — `scripts/soft-check.html` is the proof page, checked in both themes:

```css
/* Soft editorial. Paste after base.css. */
:root {
  --font-display: "Instrument Serif", Georgia, serif;
  --font-text: "Space Grotesk", "Instrument Sans", system-ui, sans-serif;
  --font-mono: "JetBrains Mono", "IBM Plex Mono", ui-monospace, monospace;
  --radius-lg: 16px;
  --soft-lift:
    0 1px 2px oklch(0.25 0.02 var(--hue) / 0.05),
    0 8px 24px oklch(0.25 0.02 var(--hue) / 0.05);
  --soft-lift-hover:
    0 1px 2px oklch(0.25 0.02 var(--hue) / 0.06),
    0 12px 32px oklch(0.25 0.02 var(--hue) / 0.08);
}
html[data-theme="dark"] {
  --soft-lift: 0 8px 24px oklch(0.05 0.01 var(--hue) / 0.35);
  --soft-lift-hover: 0 12px 32px oklch(0.05 0.01 var(--hue) / 0.45);
}

/* the surface. Border and shadow together: the one written exception. */
.card-soft {
  background: var(--surface);
  border: var(--border);
  border-radius: var(--radius-lg);
  box-shadow: var(--soft-lift);
  transition:
    box-shadow var(--dur-1) var(--ease-out),
    border-color var(--dur-1) var(--ease-out);
}
.card-soft:hover { box-shadow: var(--soft-lift-hover); }

/* the one quote */
.quote {
  font-family: var(--font-display);
  font-style: italic;
  font-size: var(--text-2xl);
  line-height: 1.1;
  max-width: 28ch;
}

/* the journal rules */
.rule-dashed { border: 0; border-top: 1px dashed var(--line-strong); }

/* the status strip */
.strip {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(16rem, 1fr));
  gap: var(--space-3);
  align-items: stretch;
}
.strip .card-soft { display: flex; align-items: center; gap: var(--space-3); padding: var(--space-3); }
.tile {
  flex: none;
  width: 4rem; height: 4rem;
  border-radius: var(--radius);
  overflow: hidden;
  border: var(--border);
  background: var(--bg-subtle);
}

/* one live dot per strip */
.dot-live { position: relative; width: 6px; height: 6px; border-radius: var(--radius-full); background: var(--ok); }
.dot-live::after {
  content: ""; position: absolute; inset: 0; border-radius: inherit;
  background: var(--ok);
  animation: ping 2s var(--ease-out) infinite;
}
@keyframes ping { from { transform: scale(1); opacity: 0.6; } to { transform: scale(2.4); opacity: 0; } }

/* equalizer bars — a state, paused with the audio */
.eq { display: flex; gap: 3px; height: 14px; align-items: flex-end; }
.eq span { width: 3px; border-radius: 1px; background: var(--ok); animation: eq 1s ease-in-out infinite; }
.eq span:nth-child(2) { animation-delay: 0.15s; }
.eq span:nth-child(3) { animation-delay: 0.3s; }
.eq span:nth-child(4) { animation-delay: 0.45s; }
.eq[data-idle] span { animation-play-state: paused; }
@keyframes eq { 0%, 100% { height: 30%; } 50% { height: 100%; } }

/* reveal once. The .js class is set by a script before paint;
   without it nothing is ever hidden. */
.js .reveal { opacity: 0; transform: translateY(8px); }
.reveal.in { opacity: 1; transform: none; }
.reveal { transition: opacity var(--dur-3) var(--ease-out), transform var(--dur-3) var(--ease-out); }

/* media zoom under a clip; the chrome stays still */
.media { overflow: hidden; border-radius: var(--radius-lg); }
.media img, .media video { transition: transform var(--dur-2) var(--ease-out); }
.media:hover img, .media:hover video { transform: scale(1.05); }

/* one marquee strip. Duplicate the list for the -50% loop. */
.marquee { overflow: hidden; }
.marquee ul { display: flex; gap: var(--space-4); width: max-content; animation: marquee 48s linear infinite; }
.marquee:hover ul { animation-play-state: paused; }
@keyframes marquee { to { transform: translateX(-50%); } }

/* inline links grow an underline from the middle — one hover answer */
.link-underline {
  background-image: linear-gradient(currentColor, currentColor),
    linear-gradient(currentColor, currentColor);
  background-size: 0% 1px, 0% 1px;
  background-position: left bottom, right bottom;
  background-repeat: no-repeat;
  padding-bottom: 1px;
  transition: background-size var(--dur-1) var(--ease-out);
}
.link-underline:hover,
.link-underline:focus-visible {
  background-size: 50% 1px, 50% 1px;
}

/* reading-progress hairline — scroll-driven, no script, no support = no bar */
.scroll-progress {
  position: fixed;
  inset: 0 0 auto 0;
  height: 2px;
  background: var(--ink);
  opacity: 0.3;
  transform-origin: 0 50%;
  transform: scaleX(0);
  pointer-events: none;
  z-index: 60;
  display: none;
}
@supports (animation-timeline: scroll()) {
  .scroll-progress {
    display: block;
    animation: progress linear both;
    animation-timeline: scroll(root block);
  }
}
@keyframes progress { from { transform: scaleX(0); } to { transform: scaleX(1); } }
@media (prefers-reduced-motion: reduce) {
  .scroll-progress { display: none; }
}
```

The theme flip is four lines of script, not CSS:

```js
const flip = (root, next, x, y) => {
  const vt = document.startViewTransition(() => { root.dataset.theme = next; });
  const r = Math.hypot(Math.max(x, innerWidth - x), Math.max(y, innerHeight - y));
  vt.ready.then(() => root.animate(
    { clipPath: [`circle(0px at ${x}px ${y}px)`, `circle(${r}px at ${x}px ${y}px)`] },
    { duration: 450, easing: "ease-in", pseudoElement: "::view-transition-new(root)" }
  ));
};
```

The magnetized control row is a few more. Give the control `transition: transform var(--dur-1) var(--ease-out)` so the follow eases; springs if the stack has them:

```js
const magnet = (el, pull = 4) => {
  if (!matchMedia("(hover: hover) and (pointer: fine)").matches) return;
  if (matchMedia("(prefers-reduced-motion: reduce)").matches) return;
  el.addEventListener("pointermove", (e) => {
    const r = el.getBoundingClientRect();
    el.style.transform =
      `translate(${(e.clientX - r.left - r.width / 2) / r.width * pull}px,` +
      ` ${(e.clientY - r.top - r.height / 2) / r.height * pull}px)`;
  });
  el.addEventListener("pointerleave", () => { el.style.transform = ""; });
};
```

`prefers-reduced-motion` is already handled globally in `base.css`; nothing here fights it.
