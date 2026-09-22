# Mobile

The narrow page is a composition, not a squeezed desktop. The breakpoint and the stacking rules are in `layout.md`. Targets and the thumb are started in `behavior.md`. This file is the phone itself.

Design the 390-wide screen on purpose. Do not finish the desktop and then let the columns wrap.

## The first screen

The claim still fits, in two or three set lines, not six wrapped accidents. The action is on screen without a sticky bar covering the paragraph under it. A sticky bottom bar is allowed only for a single action in a flow (pay, save), and it must not hide the field the person is filling. Padding under the content accounts for that bar and for `safe-area-inset-bottom`.

The top bar is the name and one action. Everything else is behind Menu, as `base.css` already does with `.nav-menu`. Do not keep a row of five text links and shrink the type until it fits.

## Type

Body stays at least 16px on a phone. Inputs are already 16px on coarse pointers in `base.css`, because smaller type zooms the page on focus. Do not override that.

Display type drops one step from the desktop clamp. It does not stay at 72px and wrap one word per line. If the headline's line breaks were set with `<br>` for desktop, give the phone its own breaks. A phrase that was beautiful at 1280 can become a tower at 390.

Leading can go slightly tighter on a short phone column (the column is narrower). Do not go below 1.4 for body.

## Touch

Anything tappable is at least 44px on the coarse pointer, which `--control-h` already becomes. Visual size can be quieter than the hit area: padding on a ghost button, not a bigger icon.

Gaps between two tappable things are at least 8px so a thumb does not hit both.

No information that exists only on hover. Tooltips are not a mobile pattern. If the hint matters, it is text.

Do not use a swipe as the only way to delete, archive, or open. A visible button does that. Swipe may be a shortcut.

## Patterns that change

- **Tabs** with more than four items do not shrink. They scroll horizontally inside their own region, or they become a select. The selected tab is still marked by more than color.
- **Tables** follow `layout.md`: a comparison scrolls sideways with a sticky first column. A list of records becomes `.rows`.
- **Dialogs** become full-screen sheets when they contain a form, a picker, or anything taller than half the screen. The title and the close control stay put. The safe action is still first.
- **Side nav** is not a miniature sidebar. It is the top bar plus Menu, or a short horizontal list of five or fewer destinations with labels. Icons alone at the bottom of a marketing site are a puzzle.
- **Galleries** swipe inside their own frame and do not hijack the page scroll. Dots are not the only index. "2 of 6" is clearer.
- **Sticky subheads** inside a long article are allowed if they are one line and they replace themselves rather than stacking under the top bar. Two sticky bars is the desktop mistake again.

## Performance the thumb feels

A phone is often the slow connection. The first screen's type and ground are in the HTML and CSS, not behind a font that never arrives and not behind an image. Hero images are cropped for the narrow ratio, not a desktop photograph scaled down until the subject is a speck. Declare the image's box so the claim does not jump when it loads.

Do not autoplay video with sound. A still from the video is the default. Play is a button.
