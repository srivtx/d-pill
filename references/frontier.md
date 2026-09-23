# Frontier

The moves at the edge, 2025–26: barely-there chrome, anti-grid layouts, exaggerated letters, shader surfaces, dense dark tools, pages that adapt. Catalogued here because agents get asked for them by name. None of them is endorsed by being listed. Each carries a gate — what must be true before you commit it — and a refuse list, because a frontier move worn as decoration is the fastest way to make a page look generated.

A frontier move is a direction. If it cannot carry the whole surface, it is a costume. The floors hold under every gate, unchanged.

## Barely-there UI

Chrome dissolving: near-invisible borders, flat ground, lightness steps doing all the separation, the content as the only object. The page looks like it is not trying, on purpose.

- Gate: the type system alone can hold the page — a committed ramp, real hierarchy, one focal point — because nothing else will. Lightness steps stay inside the safe band; `--bg-subtle` is the deepest quiet step.
- Gate: a low-light surface does not mean low contrast. `--ink` and `--line-strong` still clear their floors.
- Use it for: reading surfaces, portfolios, editorial work that trusts itself.
- Refuse: hiding focus, dissolving edges so touch targets vanish, "barely-there" as an excuse for no direction. A page that is nothing is not minimal; it is unset (`craft.md`).

## Anti-grid and broken structure

Deliberately off-grid composition: exposed structure, uneven fields, one violent alignment decision. It extends Brutalist web in `styles.md`, not the meme.

- Gate: one axis still governs. The break is one decision, repeated — a huge margin, a rule through the page, one column that refuses the rail — not a random rotation per block.
- Gate: it still reads. Squint, find the first thing, the sections, the action.
- Use it for: campaigns, posters, one-off landing moments.
- Refuse: overlapping unreadable text, low-contrast gray on a bright field, "ugly on purpose" without an axis. If they cannot read it, it failed, including as anti-grid.

## Expressive letters

Type as the image: exaggerated display faces, huge serif italics, ink-trap grotesques, a single word carrying the whole first viewport. The 2026 graphic-design wave.

- Gate: display only. Body, labels, and controls stay on the direction's text face at readable sizes.
- Gate: the family-count law holds — the expressive face is one of the two allowed, and it must change the voice, or it is decoration.
- Use it for: a masthead, a campaign claim, a personal site's one word.
- Refuse: expressive letters at body size, three display faces fighting, stretched or outlined type as a substitute for scale (`craft.md`).

## Shader and 3D surfaces

WebGL, shaders, and 3D scenes as a hero material: a flowing field, a lit object, a generative backdrop. The Awwwards end of the frontier.

- Gate: one viewport, the hero. Content pages stay documents.
- Gate: a static fallback ships, and the page is complete without the canvas.
- Gate: the frame budget is kept (60fps on mid hardware), `prefers-reduced-motion` gets the still image, and type never sits on the brightest band of the scene.
- Use it for: a product whose subject is visual (a renderer, a game, a tool for makers), a launch moment.
- Refuse: scroll-jacking to drive a scene, 3D for a pricing page, an interactive scene the person cannot pause, a canvas replacing a document. The craft exception in `interaction.md` still governs any motion; a shader does not suspend it.

## Dense dark tools

The Linear school: dense, dark, keyboard-first product UI — compact rows, quiet borders, speed as the aesthetic. It reads "designed" because nothing in it performs.

- Gate: it is a tool a person uses daily, with real density — rows, records, a command palette. On a marketing page this look is a costume.
- Gate: keyboard hints shown are shortcuts that actually work. Dark theme contrast holds (`--ink` in the dark band, edges over 3:1).
- Use it for: consoles, dashboards, agent UIs (see `ai-interfaces.md`). Start from Spec or Dense terminal in `styles.md`.
- Refuse: glow, gradients-as-depth, hint chrome with no behavior, dark mode with unmapped roles.

## Adaptive and generative pages

Pages that change with the person or compose themselves: personalized content, model-composed layouts. The AI-native frontier.

- Gate: the default state is a complete, committed design. Adaptation is a layer on a decided page, never a substitute for one.
- Gate: generated composition comes from a fixed vocabulary of components, and every generated element passes the same floors (`ai-interfaces.md`, Generative UI).
- Gate: the person can tell what was composed for them and turn it off.
- Use it for: feeds, digests, surfaces where the model's output is the content.
- Refuse: personalization as the design ("AI will make it good"), a layout system that only works when the model is right, dark patterns wearing adaptive clothing.

## Motion at the frontier

The tooling got cheaper and the discipline matters more. GSAP went fully free in 2025 (Webflow), so orchestrated timelines cost nothing to ship and everything to restrain. Motion (ex-Framer Motion) is the React spring engine. Native CSS took scroll-driven animations, view transitions, and anchored positioning into baseline.

- CSS first: two properties or fewer, no library. Springs belong to the one magnetized control row in `soft.md`, fine pointer only.
- A timeline library earns its place for one orchestrated sequence, not for hover effects.
- The durations, easings, and refusals in `interaction.md` are the law regardless of engine. A library being free is not a reason.

## Native-CSS frontier

Popover, anchor positioning, container queries, `:has()`, scroll-driven animations, view transitions: baseline in the current browsers, and Interop 2026 is closing the rest. Use them where they replace a script:

- Anchor a tooltip or menu to its trigger with CSS before shipping a positioning library.
- A dialog is `<dialog>`. A toggletip is popover. A component's own sizing is a container query, not a viewport media query.
- Every gated feature degrades: `@supports` or a fallback state, and the page works with the feature off. The pattern to copy is `soft.md`'s scroll-progress hairline.
- Refuse: shipping a polyfill bundle for what the page can live without, and using a new feature where an old one was already the right tool (`:has()` is not a layout system).

## Committing one

When the ask is a trend word — "aurora," "glassy," "anti-grid," "shader hero," "Linear-style" — route through here:

1. Find the move above. Read its gates. If the gates do not pass, say so and commit the nearest honest style from `styles.md`.
2. Write the commitment with the move named, its one viewport or surface, and what it refuses.
3. The critique gate runs unchanged, both themes, both widths.

A trend that cannot write its own commitment paragraph is a vibe, and vibes are what `direction.md` exists to refuse.
