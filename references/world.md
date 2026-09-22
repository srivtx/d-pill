# World

The page will be read in more than one language, on more than one script, by people whose text is longer than yours. Design for that from the start. It is the same discipline as the phone: recompose, do not squeeze.

## Expansion

Translation runs about a third longer than English, and sometimes twice, for a short label. German, Finnish, and French buttons are where fixed widths break.

- Buttons size to their label. `min-height: var(--control-h)`, padding inline, no fixed width except a full-width phone button.
- Nav items wrap or move into Menu. They do not shrink the type below the body size.
- Headings wrap. A `<br>` you set for English is wrong in another language. Prefer a width constraint and `text-wrap: balance`, and only force breaks in a language you are actually setting.
- Do not truncate translated labels. Truncation is for user-generated strings in a known column (`details.md`).

Test one long language if you ship more than one. If you cannot, leave the room anyway.

## Direction

For right-to-left languages, mirror the layout. The name starts at the inline start. The action sits at the inline end. Use the logical properties already in `base.css` (`padding-inline`, `margin-inline`, `text-align: start`). Do not set `left` and `right` for layout.

What does not mirror:

- Numbers and the decimal separator stay in the locale's own rules, but a column of figures still aligns.
- Media controls: a play mark still points the way the playback goes. Do not flip the glyph if the direction of time is the point.
- Logos and the d-pill capsule. The mark is an object. Do not mirror the spectrum or the seam.
- Charts: time still moves in the direction the locale reads, which usually means the axis flips. Labels follow the script.

`dir="rtl"` on the document, or on the section that is in that language. Do not implement RTL by pasting flipped margins.

## Punctuation and marks

These are part of the finish in `taste.md`.

- Hyphen `-` joins a compound word or breaks a word.
- En dash `–` is a range: `Mon–Fri`, `12–14`. Not a hyphen.
- Em dash `—` is a break in a sentence, used rarely. Do not use it as a bullet.
- Minus for negative money is `−` or the locale's sign, and it aligns with the figures.
- Quotation marks are the language's marks, not always “ ”. French and German have their own. Straight "quotes" still look like code.
- Percent, currency, and the order of the symbol follow the locale (`48 $` versus `$48`). One locale per page. Do not mix.

## Names and numbers

A name field is at least two logical fields only if you truly need them apart. Many cultures use one given name, or a family name first. The display order is the locale's. Do not force "First / Last" as the model of a person.

Postal addresses are not one US-shaped block. City, region, and code change shape. Stack the fields and let the address be longer.

Phone numbers are `type="tel"` and grouped as spoken. Do not validate them against one country's pattern if the product is not one country.

Dates in the UI say the month as a word when the audience is mixed (`23 Sep 2026`), so `03/04/2026` is not guessed. A tool that has chosen ISO keeps ISO (`type.md` and `writing.md`). One choice per product.

## Scripts

Line-height that is comfortable in Latin can clip Arabic, Thai, or Devanagari. Do not set a fixed height on a line of text. Body leading of about 1.5 survives most scripts. Display leading near 1.0 may clip accents and marks above the letter. If the script needs more air, add it. Do not solve it by shrinking the type.

A font stack that only covers Latin will show tofu. The direction's face, then a stack that includes a face for the script in use. Do not fall through to a different personality (a whimsical fallback for Arabic). A plain system face for that script is better than the wrong voice.

## A second language on the same page

A quote in the original language can sit beside its translation. The original is the display face or italic, the translation is the text face, and both are labeled if it is not obvious which is which. Do not auto-translate a person's name.
