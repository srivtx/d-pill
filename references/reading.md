# Reading

The judgments in this repo condense; they do not appear from taste alone. Each entry below is a source a judgment traces to. Read the one that touches the work in front of you. Nothing here overrides the floors — the floors are the law, the sources are the reasons.

## Names and history

- **Invisible Details of Interaction Design** — Rauno Freiberg, Every, 2023. https://every.to/context-engineering/invisible-details-of-interaction-design — The craft-site school in one piece: focus states, cursor behavior, scroll feel, continuity, the frame budget. `soft.md`'s motion and `details.md`'s tells trace here. The Hacker News thread on it is the field commentary.
- **Rauno's web interface guidelines** — rauno.me, ongoing. A designer's working rules for interfaces; the practical end of the same school.
- **detail.design** — a curated index of craft articles and tools. Where the school keeps its reading.
- **What Is Neumorphism?** — IxDF, updated. https://ixdf.org — "New skeuomorphism," also sold as "soft UI": the definition, and the low-contrast failure mode that got it written up.
- **Neumorphism: Its Origin Story & Influence on UI Design** — SVGator, 2023. https://www.svgator.com — The 2019 coinage, the Dribbble wave, the two-opposing-shadows recipe on the ground color.
- **Neumorphism: Its rise and fall in UI design** — Webflow. https://webflow.com — Why it died: WCAG contrast failures, invisible focus, a trend that aged in one season. The reason `styles.md` refuses the dent and `soft.md` carries the correction.

## Motion

- **ViewTransition — MDN Web Docs**. https://developer.mozilla.org/en-US/docs/Web/API/ViewTransition — The API contract, including the documented `ready`-promise circular reveal. The theme flip in `soft.md` is this pattern, not an invention.
- **Full-page theme toggle animation with View Transitions API** — Akash Hamirwasia, 2023. https://akashhamirwasia.com — The original walk-through of the circular theme wipe.
- **Some practical examples of view transitions** — Piccalil (Andy Bell), 2025. https://piccalil.li — View transitions used with restraint: what they are for, and what they are not.
- **15 best microinteraction examples** — Webflow. https://webflow.com — Purposeful restraint: each animation confirms, reveals, or guides. `interaction.md`'s "motion does not perform" in practice.
- **20 Motion Design Principles** — Mockplus, 2025. https://www.mockplus.com — Duration, easing, and distance as the working vocabulary behind `--dur-1` through `--dur-3`.
- **A guide to Scroll-driven Animations with just CSS** — WebKit, 2025. https://webkit.org — `scroll()` and `view()` timelines in pure CSS, and the Safari 26 landing that closed the support gap. The progress hairline in `soft.md` is this module, `@supports`-gated.
- **CSS scroll-driven animations — MDN Web Docs**. https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_scroll-driven_animations — The module contract: an animation's progress bound to a scroll timeline instead of a clock.
- **Two approaches to fallback CSS scroll driven animations** — Cyd Stumpel, 2025. https://cydstumpel.nl — Progressive enhancement for scroll timelines: the feature ships or the page simply stays still. Why `soft.md` gates the hairline behind `@supports` instead of scripting it.
- **Animating Underlines** — css-irl.info, 2021. https://css-irl.info — The `background-size` technique behind `soft.md`'s `.link-underline`: two half-width gradients that grow from the middle, no extra elements.
- **CSS Line Hover Styles for Links** — Codrops (Tympanus). https://tympanus.net — The whole family of underline hovers. Read it to choose one and ship one; a site that mixes three underline behaviors has no behavior.
- **Motion for React** — motion.dev. The spring library a React build uses for the magnetic follow; the physics vocabulary (stiffness, damping, mass) behind the allowance's "a few pixels on springs."
- **Framer Motion Tutorial: 5 Advanced Animation Patterns** — uiTheFactory, 2026. https://uithefactory.com — Magnetic buttons done on springs. Read the pattern, keep the budget: the pull is single-digit pixels, controls only, fine pointers only.

## Type

- **Font Trends 2026** — Gleam Studio. https://www.gleamstudio.design — The expressive-serif revival (Fraunces, Instrument Serif) and grotesques with ink traps (Bricolage Grotesque): the faces `soft.md` and `faces.md` point at, named in the wild.
- **50 fonts that will be popular with designers in 2025** — Creative Boom. https://www.creativeboom.com — The screen-optimized serif revival from the editorial side.

## Layout

- **Revolutionizing UI/UX with Bento UI grid design** — Stan, 2024. https://www.stan.vision — The bento-box metaphor and its uptake in SaaS marketing. Why `arrange.md` still refuses it as decoration: the boxes carry features, not vibes.
- **Bento Grid: Explained with Examples and Code** — Banani. https://www.banani.co — Origins in the compartmentalized lunch box, and the one honest rule the trend forgot: tile sizes follow content importance, or the grid is wallpaper.
- **Best Bento Grid Design Examples** — Mockuuups Studio. https://mockuuups.studio — The gallery. Look for the ones that stop being grids and become charts; that is the failure mode `grids.md` guards against.

## Access

- **WCAG 2.2** — W3C. https://www.w3.org/TR/WCAG22/ — The 4.5:1 and 3:1 floors this repo enforces before any direction is committed.
- **Neumorphism accessibility write-ups** — the UX Design Institute and IxDF entries above both carry the failure analysis: same-gray surfaces cannot pass 1.4.11 (non-text contrast), and shadow-swapped focus cannot pass 2.4.7. The correction in `soft.md` (border + ink + independent ring) exists to pass these.

## Books

- **The Visual Display of Quantitative Information** — Edward Tufte. Data-ink, chartjunk, small multiples. `dataviz.md` is these rules applied to the web.
- **The Elements of Typographic Style** — Robert Bringhurst. Pairing, measure, rhythm. The backbone of `type.md` and `proportion.md`.
