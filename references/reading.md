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

## Type

- **Font Trends 2026** — Gleam Studio. https://www.gleamstudio.design — The expressive-serif revival (Fraunces, Instrument Serif) and grotesques with ink traps (Bricolage Grotesque): the faces `soft.md` and `faces.md` point at, named in the wild.
- **50 fonts that will be popular with designers in 2025** — Creative Boom. https://www.creativeboom.com — The screen-optimized serif revival from the editorial side.

## Access

- **WCAG 2.2** — W3C. https://www.w3.org/TR/WCAG22/ — The 4.5:1 and 3:1 floors this repo enforces before any direction is committed.
- **Neumorphism accessibility write-ups** — the UX Design Institute and IxDF entries above both carry the failure analysis: same-gray surfaces cannot pass 1.4.11 (non-text contrast), and shadow-swapped focus cannot pass 2.4.7. The correction in `soft.md` (border + ink + independent ring) exists to pass these.

## Books

- **The Visual Display of Quantitative Information** — Edward Tufte. Data-ink, chartjunk, small multiples. `dataviz.md` is these rules applied to the web.
- **The Elements of Typographic Style** — Robert Bringhurst. Pairing, measure, rhythm. The backbone of `type.md` and `proportion.md`.
