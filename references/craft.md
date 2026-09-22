# Craft

This is the difference between a page that fills a template and a page that was decided. The refusals apply when nobody has supplied a brand. A real brand wins, and these fixes still apply to structure.

## If you were about to

| The tell | The fix |
|---|---|
| Inter, Roboto, or `system-ui` as the voice | The direction's face. The ban list is in `direction.md`. |
| A purple or indigo gradient, a mesh, a dot grid | `--bg`, and one accent used on the action. |
| A centered hero, a centered form, a centered nav | One left edge. Center only a one-line empty state. |
| Three equal feature cards with icons in tinted circles | One feature, shown large, then a ruled list for the rest. |
| `rounded-2xl` and a shadow on every box | The direction's radius. Shadow only on dialog, menu, toast. |
| A border plus a shadow plus a tint on the same object | One treatment. |
| Gradient text, outlined text, text with a glow | `--ink`. One word in the accent is already a lot. |
| Gray text around `#999` or `text-gray-400` | `--ink-muted`, inside the safe band in `foundations.md`. |
| A hover that scales a card | A background or border change. |
| Pill badges for New, AI, Beta, Popular | One status, as words. A recommended tier gets a quiet label, not a ribbon and a scale. |
| A marquee of logos you do not have | One true proof line, or nothing. |
| A tilted screenshot inside a fake browser | A real crop of the product on `--bg`, with a 1px `--line` if it would otherwise melt into the page. Or no figure. |
| Invented testimonials, invented people, stock handshakes | Omit them. |
| Four columns of footer links | The name, the real links, the year. |
| The same 8px gap between everything | Tight inside a group, wide between groups. The density table is in `layout.md`. |
| Every weight from 400 to 700 on one screen | The three weights in `foundations.md`. |
| Two accents, plus green, plus orange | One accent. `--ok` and `--warn` are status, and they are rare. |
| A welcome banner above the work | The work. The title is the view's name. |
| Glass, noise overlays, blob backgrounds | The direction's material. Flat. |
| A skeleton shimmer that looks like an ad | A still or slowly pulsing block of `--bg-subtle`. |
| Icons in colored circles as a feature list | A 20px icon in `--ink` or `--ink-muted`, or no icon. |

## Hierarchy

Squint. You should still be able to point at the first thing, the sections, and the action.

The claim is at least twice the body size on a marketing page. In a tool, the title is `--text-xl` and the meta is `--text-sm`; the gap between them is `--space-1` or `--space-2`, and the gap before the work is a density step larger.

Do not give the eyebrow, the claim, the lede, the button, and the proof the same contrast. The claim is ink and large. The lede is ink and short. The proof is `.quiet`. The button is the accent. The eyebrow, if you need one, is a single `.caps`.

## Optical details

Edges, crops, radius, and visual weight are in `geometry.md`. Hairlines, focus versus press versus selection, truncation, and figures are in `details.md`. Type setting is in `type.md`. Color judgment is in `color.md`.

## Imagery

One ratio per region. Crop with an intent. `object-fit: cover` with an explicit aspect ratio, so the layout does not jump when the file arrives.

If you do not have a photograph, use type and space. Do not generate a photograph of a person, a customer logo, or a 3D clay illustration to fill the hole.

When the direction allows an image and you are generating one: flat light or the direction's real material, the page's hue, no gradient backdrop, no floating UI, no fake logos. Atelier gives the photograph the size and gets the chrome out of it. Signal and Spec usually need no photograph at all.

A product figure shows the decision the page is about, cropped tight. The numbers in the figure match the numbers in the copy.

## Icons

One set, one stroke, 20px, `currentColor`. 24px only in a large empty state. If the project has no icon set, use inline SVG for the few you need. Do not import a pack to use four icons.

An icon without a text label needs an accessible name. An icon next to a label is `aria-hidden="true"`.

## Restraint

After the page works, remove one treatment. The page should still hold. If it does, the treatment was not earning its place. Do this once. The things that usually go: a second border, a background tint on a section, an eyebrow, an icon, a shadow.

Stop when removing the next thing would hide the action or the structure.
