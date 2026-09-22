# Harmony

How colors relate once the hue exists. The token method, the safe band, and dark themes are `color.md`. This is the relationship.

Value does the work. Harmony is which hues you allow in the room. One hue, varied by lightness, is the most reliable way to make a page look finished.

## The relationships

**Monochrome.** One hue. Ground, ink, lines, and accent are lightness and chroma steps of that hue. This is the default d-pill method, and it is the right answer for almost every product. The accent is the same hue, darker or more chromatic, not a second hue.

**Achromatic plus one.** Paper and ink are nearly gray (chroma under 0.01), and one hue carries the accent. Quieter than monochrome-with-a-tint when the brand color must be recognizable. The neutrals still take a whisper of that hue, or they look like a different kit.

**Analogous.** The accent's neighbor, about 20–30 degrees of hue, used as a second note. A leaf accent with a yellower ground. Soft, and still one family. The second hue is a small field or a section, not a second button style. If you cannot tell them apart at a glance, you do not need the second.

**Complementary.** The hue opposite the accent, about 180 degrees. This vibrates if both are saturated and both are large (`taste.md`). The only beautiful use: the complement is a small object (a seal, a single word, a chart mark) on a large quiet ground, and both chromas are under 0.14. Red type on a green field is a costume. A red seal on warm paper is a mark.

**Split complementary.** The two neighbors of the opposite hue, and you use one of them, once. This is "I wanted contrast without the buzz." Same rule: small, dirty, one appearance.

**Triadic.** Three hues about 120 degrees apart. Play, Memphis, Bauhaus, and almost nowhere else. One hue owns 80 percent of the color. The other two are objects. If all three are fields, the page is a flag.

**Spectrum.** A continuous film of hue, like the capsule. Allowed on the mark. Allowed on one poster field in the Psychedelic poster style. Not a UI palette. Not a border. Not a heading. Text that must be read is not set in a spectrum.

## Building the room

From the relationship, assign only the roles you already have. Do not invent `--blue-2`.

- Ground: the hue, lightness near 0.97, chroma near 0.01. Or paper.
- Ink: the hue, lightness near 0.25, chroma near 0.02.
- Muted: the same, lightness near 0.45.
- Line and line-strong: the same hue, the lightnesses in `foundations.md`.
- Accent: the same hue at chroma near 0.12, or the analogous / complement if the relationship says so, and only if it clears the band.
- Status (`--ok`, `--warn`, `--danger`) stay semantic. They are not members of the harmony. They appear on words, rarely. Do not "harmonize" danger into a pretty red that no longer reads as danger, and do not paint the page with them.

## Temperature of the whole

A warm harmony (hues 20–70) feels near, physical, edible, domestic. A cool harmony (hues 200–250) feels measured, far, instrumental. Do not put a cool accent on a warm paper "for balance." Balance is evenness. Pick a temperature and let it be the weather (`taste.md`).

If the photograph brings the opposite temperature, the page chrome stays in its weather and the photograph is allowed to be the exception, because it is a picture of somewhere. Do not recolor the UI to match every photo.

## Checking

Squint to gray. The poster remains. Then look at hue alone: you should be able to name the relationship in one word (monochrome, analogous, complementary, triadic, spectrum). If the honest name is "several," remove a hue.
