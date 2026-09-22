# Commerce

A page where someone spends money. Trust is the material. The selling argument is in `narrative.md`. Dark patterns are refused in `behavior.md`. This file is the shop itself.

## The product

One product, one `h1` (its name), the price in `.num` at a size you can see without hunting, and one primary action: "Add to bag" or "Buy", with the price on the button if there is any chance of surprise ("Pay $48").

The photograph follows `narrative.md`: one light, the object large, no fake shadow on the floor unless the photo really has one. A second view is a second photograph in the same light, not a zoom gimmick. Give each image an `aspect-ratio` so the name does not jump.

Specifics (size, material, what is included) are a stack of plain rows, not a tabbed marketing essay. The thing that changes the decision sits above the fold with the price. Long care instructions can follow.

## Variants

Size, color, and edition are real controls: a radio group or a native select, with a visible label. The selected one is weight plus a mark, not color alone. If a variant is unavailable, it stays visible and says "Sold out". Do not hide it, and do not let someone add it.

Color variants show a swatch that is the actual color, with the name in text. A swatch alone fails when two browns are close. The name is the accessible name.

## Price

The price the person pays is the largest number. A compare-at price, if true, is `.quiet`, smaller, and not a fake inflation. The currency is written once, the same way as the rest of the product (`writing.md`). Tax and shipping are stated before the pay button, not after it. "Calculated at checkout" is acceptable only if you then show the number before they pay.

A sale is a word ("Ends Sunday") you can stand behind. No countdown that resets.

## The bag

A list of rows: thumbnail, name, variant, quantity, line price. Quantity is an input the person can edit, plus remove as a text button. The subtotal is a row they can find, not a sticky carnival. One action: "Checkout".

Empty bag: "Your bag is empty." and a way back to the goods. No illustration of a sad cart.

## Checkout

Short. Contact, delivery, payment. Each group has a heading. The pay button repeats the amount. Errors sit on the field that failed. Do not clear the card number's neighbors when one field fails.

Show the order beside the form on a wide screen, and above the pay button on a phone, so the person sees what they are buying at the moment they pay.

Trust is the merchant name, the amount, and a readable return policy one click away. It is not a row of badge clipart ("secure", "guaranteed", padlocks you drew).

## A catalog

A directory of peer products uses the directory rule in `layout.md`: one treatment, the photograph as the point, the name and the price always present. Do not hide the price until hover. Hover does not scale the card.

Sort and filter are real controls with labels. The result count is a quiet line: "14 loaves". Filters that define the list belong in the URL when the stack allows it (`behavior.md`).

## After payment

Say what happened and what happens next. "Paid. We bake this tonight. A receipt is on its way to ava@oven.test." The order number is `.mono` so they can read it back. Do not dump them on a generic home.
