# Styles

A direction is a starting point. A style is the specific tradition you are working in. When the user names a style, a decade, a material, a movement, or a kind of object (a poster, a label, a paper, a terminal), commit to that style. Do not collapse it back into the nearest generic direction and sand it down.

Floors still hold. The capsule's spectrum stays on the mark. It is not a style for the page unless the style below says so.

## How to use this file

1. Find the style. If they named something that is not here, take the closest one and write the difference as the one borrowed slot.
2. Start from that style's direction so the tokens and the font link already exist.
3. Apply the override in a `<style>` block after `base.css`.
4. Honor the refuse list. It is what keeps the style from turning into a costume.
5. Two named styles: the one that owns the type wins. Borrow one slot from the other.

`faces.md` is how to judge the type. `grids.md` is how to build the page. `harmony.md` is how the colors relate. `proportion.md` is the size relationships. `patterns.md` is the interface arrangement when the style is a product.

## Book and paper

### Old style
Start from Broadsheet. The page is a book.
- Type: an old-style serif (Newsreader, or Literata). Low stroke contrast, angled stress, bracketed serifs. Italic is a true italic, and you may use it for titles of works.
- Color: warm paper, hue 45–70, chroma under 0.01. Ink near 0.22. No accent. Links are underlined ink.
- Shape: radius 0. One column. Folios (the page number) in the margin, `.quiet`.
- Space: generous. Bottom margin larger than the top, the way a page sits in the hand.
- Material: paper. No pictures unless they are plates with captions.
- Refuse: UI chrome, cards, a bright link color, a sans for "modern contrast" unless the notes in the margin need it.

### Rational
Start from Editorial. Baskerville's century: sharper, more contrast, still a book.
- Type: Source Serif 4 or Literata at a serious size. More contrast than old style. Headlines in the same face, not a grotesque.
- Color: cooler paper, hue 80–100, still almost gray. Ink true.
- Shape: radius 0. A thin rule under the title only.
- Space: regular to generous. Measure 62ch.
- Material: a pressed page.
- Refuse: didone hairlines at text size (they break), drop caps, background textures.

### Didone
Start from Quiet luxury. Fashion, perfume, a masthead.
- Type: Bodoni Moda or Libre Bodoni for the name only, at display size. A plain grotesque for every UI label (Instrument Sans or Public Sans). Never Didone at 15px. The hairlines disappear and the letters fill in.
- Color: paper near white or true black. Almost no chroma. The accent is the absence of color, or one metallic line (hue 70, chroma under 0.04).
- Shape: radius 0. Hairline rules. Huge contrast between the word and the ground.
- Space: generous. The word is isolated.
- Material: coated paper, a hard light (`art.md`).
- Refuse: Didone body text, a second display face, rounded buttons, soft shadows.

### Letterpress
Start from Editorial.
- Type: a sturdy serif or a slab (Bitter, or Zilla Slab) because letterpress ink spreads. Slightly loose tracking at text size, the opposite of a digital grotesque.
- Color: ink that is not pure black, paper that is not pure white. Hue 50. One second color from a second pass of ink, used once (a rule or a single word).
- Shape: radius 0. Borders are thick or they are absent. Ornaments only if they are one repeated mark, not a clipart set.
- Space: the bite of the type is the texture. Do not add a paper-grain image. The unevenness is in the spacing and the second color.
- Material: ink on cotton. Flat.
- Refuse: a noise overlay, a fake deboss, a drop shadow under the letters, "vintage" filters.

### Scientific paper
Start from Civic or Broadsheet.
- Type: Source Serif 4 for the article, Public Sans or IBM Plex Sans for the title page labels, IBM Plex Mono for figures and equations' numbers.
- Color: white paper, black ink, one functional blue or none. Figures follow `dataviz.md`.
- Shape: radius 0. Numbered sections. Captions under figures, notes at the bottom.
- Space: compact inside the article, a wide margin for section numbers.
- Material: a journal.
- Refuse: a hero, a marketing lede, icons, a colored header bar.

## Poster and movement

### Swiss
Start from Instrument for a product, Editorial for a poster.
- Type: a neo-grotesque. Inter is allowed only here, because the style is the neo-grotesque, not an unset default. Alternative: IBM Plex Sans. One weight for text, a heavier weight for the one word that matters. Flush left. Ragged right.
- Color: white or a single flat hue used as a field, black type. If the field is color, the type is black or white, whichever clears 4.5, and there is no second hue.
- Shape: radius 0. A grid you can see: columns, a heavy rule, or none. Alignment is the whole style.
- Space: the grid's gutter is constant. Elements snap to it. Asymmetric is allowed. Centered is not, except a single poster word.
- Material: ink on a flat sheet.
- Refuse: gradients, shadows, rounded cards, a second typeface "for warmth," photography with a color grade that fights the flat field.

### Swiss poster
Start from Editorial. This is the concert poster, not the app.
- Type: one grotesque, set so large it is architecture. One word or one name. A fact (date, place) in a small size on the same grid.
- Color: one field of flat color, type in ink or paper. Black, white, and one hue is the whole palette.
- Shape: radius 0. The grid is 3 or 4 columns. Type crosses columns on purpose.
- Space: huge. The empty cells are the design.
- Material: a printed sheet. Flat. No photograph unless the photograph is also flat and cropped to the grid.
- Refuse: a subtitle in a script face, a ticket-shaped button, more than three sizes.

### Bauhaus
Start from Play, then remove the joke.
- Type: a geometric sans (Outfit or Syne) for the headline, a plain grotesque for text. Geometry is circles, squares, triangles drawn as themselves.
- Color: red, yellow, blue, and black, but dirty them (chroma near 0.14, not 0.25) so they sit on paper. One of the three dominates. The others are small.
- Shape: radius 0 on the page. Circles are circles, not pills. The primary geometry is the composition.
- Space: asymmetric, weighted to one corner, the way a poster balances a heavy circle with a small square.
- Material: gouache on paper. Flat shapes. No 3D.
- Refuse: a rainbow, a gradient mesh, cute illustrations, using all three primaries at full size.

### De Stijl
Start from Editorial.
- Type: a geometric sans, horizontal or, rarely, one vertical label. Almost no italics.
- Color: paper, black, and red (hue about 25, chroma 0.16). Nothing else.
- Shape: black bars of two thicknesses, rectangles, radius 0. The bars are the layout.
- Space: the bars divide the page into rectangles. Text sits in a rectangle. It does not cross a bar.
- Material: painted wood and paper. Flat.
- Refuse: diagonals (that is constructivism), curves, a fourth color, photographs.

### Constructivist
Start from Editorial.
- Type: a heavy grotesque or a condensed gothic (Oswald), angled only as a block, not as a sentence rotated for decoration. One diagonal is the composition. A second diagonal is a mess.
- Color: black, paper, and red. A photograph may be stark, high contrast, cropped hard.
- Shape: radius 0. Thick rules. A block of color behind one word.
- Space: crowded on purpose in one zone, empty in another. The density is the contrast.
- Material: print, ink, halftone. If you use a photo, it can be contrasty. Do not add a paper texture image.
- Refuse: a full-page diagonal of body text (unreadable), three accents, a clean SaaS hero with a red button and calling it constructivist.

### Art Deco
Start from Quiet luxury.
- Type: a high-contrast display (Bodoni Moda) or a geometric with small caps for the name. Labels in a plain sans. Rules are part of the letters' world: sunbursts only as one drawn mark, not a pattern fill.
- Color: black, a warm off-white, and one metal (hue 80, low chroma, used as a line or a small field).
- Shape: symmetry is allowed here, on a poster or a title. Radius 0 or a very small radius. Stepped lines, a frame.
- Space: the frame is inset. The name is centered in the frame. The rest of the site, if it is a product, goes asymmetric again. Do not center the app.
- Material: lacquer, brass, paper. Hard.
- Refuse: a gold gradient, a repeating fan pattern behind everything, geometric clipart in every section.

### Streamline
Start from Soft service or Quiet luxury.
- Type: a rounded-but-not-cute geometric, or a mid-century grotesque. Generous x-height. Script only for one signature word.
- Color: cream, a muted teal or clay, and a dark green or brown. Chroma under 0.08. Think painted metal, not candy.
- Shape: long radii on large forms (a poster panel), small radii on controls. Horizontal speed lines only as one graphic.
- Space: regular. Low, wide compositions. Photographs are horizontal.
- Material: bent wood, aluminum, enamel. A soft shadow is allowed on a physical object in a photo, not on a button.
- Refuse: pastel gradients, 1950s clipart, a fake wood texture.

### Psychedelic poster
Start from Play. This is the one style that may use a spectrum on the page. It is still a poster, not a dashboard.
- Type: one bulbous or high-contrast display face for a single line (Fraunces at a huge optical size, or a similar soft display). Body, if any, is a plain sans at a readable size and color. The filled letterforms may be the art.
- Color: a spectrum is allowed on one field or one letter, in the same spirit as the capsule: continuous, film-like, not six flat stripes. The text that people must read is ink on a quiet ground, not spectrum on spectrum.
- Shape: radius is the letter, not a card system. One poster. The page below the poster returns to a readable column.
- Space: the poster is full-bleed. Then the page calms down.
- Material: ink, a light show, paper. Flat. No 3D chrome.
- Refuse: making the app UI psychedelic, unreadable melted body text, a rainbow button, using this style for a bank or a medical tool.

### Punk and zine
Start from Editorial.
- Type: a raw grotesque or a mono for the notes. One photocopied headline, cut out, which you may rotate a degree or two. Not every line. Body stays straight and readable.
- Color: black on cheap paper (hue 70, lightness 0.94). One fluorescent note, once, or red from a stamp.
- Shape: radius 0. Borders are uneven on purpose only if the misregister is one element. A hairline grid of chaos is noise.
- Space: tight, cheap, a margin that is not precious.
- Material: photocopy, staple, stamp. No grunge texture image. The style is the cropping and the one rotated scrap.
- Refuse: a distress filter on the whole page, graffiti on a SaaS hero, unreadable body.

### Risograph
Start from Editorial or Play.
- Type: a sturdy sans or slab. Overprint is the look: two inks, not ten.
- Color: paper, plus two inks (for example hue 25 and hue 230, chroma 0.12). Where they cross, let the third color happen. Do not simulate it with a blend mode on every div. One overlap is enough.
- Shape: radius 0. Registration slightly off, once, on a single shape, not on the text.
- Space: poster-like.
- Material: soy ink, misregistered on purpose, once.
- Refuse: a noise overlay, CMYK gradients, more than two inks.

### Memphis
Start from Play.
- Type: a geometric sans. The pattern is the decoration: squiggles, triangles, dots, as a small number of flat shapes.
- Color: a bright set, capped at four, one of them dominant. Dirty the chroma slightly so it does not burn.
- Shape: the shapes are the style. Controls stay simple so the pattern does not also have to be the button.
- Space: busy in one band (the pattern), quiet in the band where people read.
- Material: laminate, flat color. No gradients, no 3D.
- Refuse: pattern behind body text, every section patterned, neon on white at full chroma.

### Supergraphics
Start from Editorial.
- Type: one word so large it is cropped by the viewport. The rest of the sentence is a normal size. You read the fragment, then the line.
- Color: one field, one type color.
- Shape: the letter is the architecture. Radius follows the type, not a card.
- Space: the letter may bleed off the edge (`geometry.md`, the one break).
- Material: paint on a wall, flat.
- Refuse: three cropped words competing, a paragraph set at the same giant size.

### Magazine cover
Start from Editorial.
- Type: one cover line, set, broken by hand. The masthead is a constant (the name, always the same place, every issue). Cover lines do not cover the face of a person if a person is the cover.
- Color: the photograph's grade plus ink. The masthead is always the same color, even when the photo changes, unless a single issue inverts it on purpose.
- Shape: full bleed photo, type in the quiet zones of the photo or, better, in a band that is not the photo.
- Space: the top band is the masthead. The cover line owns the lower half or one side.
- Material: coated paper.
- Refuse: a list of features with checkmarks, a button that says "read more" on the cover, more than three cover lines.

### Album cover
Start from Atelier.
- Type: the name of the work and the artist. Almost nothing else. Type can be tiny and still be the whole idea, or one word.
- Color: from the image, not from a brand palette you impose on top.
- Shape: a square, treated as an object. On a page, give it room. Do not put a card shadow under it.
- Space: the square is the poster.
- Material: print, a sleeve.
- Refuse: a tracklist as the hero, a play-button overlay you cannot resist adding, mockups of the vinyl unless the object is the point.

### Film title
Start from Editorial or Quiet luxury.
- Type: a custom-feeling display, used as a title sequence: one line, then a fact. Wide tracking is allowed on a single caps title because the style is the credit. It is not allowed on buttons.
- Color: black, or a still from the picture with type off to the side.
- Shape: a frame. Letterbox only if the work is a film and the frame is the content, not a CSS trick on a paragraph.
- Space: slow. A lot of ground. The title arrives alone.
- Material: light on a screen, or ink. Stillness (`taste.md`).
- Refuse: animated letter-by-letter on a product page, a trailer playing by itself.

## Object and place

### Scandinavian
Start from Quiet luxury or Soft service.
- Type: a humanist sans. Quiet. No drama in the italic.
- Color: pale wood, whitewash, a muted blue-gray or a forest hue at low chroma. Black used sparingly, as a small object (a hook, a word).
- Shape: small radius or none. Honest joins. Photographs of real rooms and real light.
- Space: generous, but the objects are useful, not floating in a void for effect. A chair is a chair.
- Material: ash, wool, paper, daylight.
- Refuse: hygge as a word on the page, fake candlelight filters, a cream gradient, stock people in matching cream sweaters.

### Japanese editorial
Start from Atelier or Editorial.
- Type: a grotesque for Latin, with real care for the Japanese or Chinese face if that script is present (`world.md`). Latin is small, often. The grid is strict. Vertical Latin is a label, not a paragraph.
- Color: paper, ink, and one red seal's worth of accent (hue 25), used as a stamp once.
- Shape: radius 0. A clear column. Lots of margin. The margin is the point.
- Space: asymmetric, a heavy block and a void. Do not fill the void.
- Material: paper, ink, a photograph with air in it.
- Refuse: a bamboo texture, a fake brush font for English, oriental ornaments, centering everything and calling it zen.

### Gallery wall
Start from Atelier.
- Type: the wall label is `.caps` or small roman: artist, title, year, material. The work is unlabeled in the sense that the label does not sit on it.
- Color: the wall is `--bg`. The work brings the color.
- Shape: radius 0. Frames are the work's, not the page's.
- Space: more than you think. Two works do not crowd.
- Material: a wall, a light from above. `art.md`.
- Refuse: a carousel, a price in the hero, a testimonial under the work.

### Lookbook
Start from Quiet luxury.
- Type: the name of the piece, the price or the season, and almost no adjectives.
- Color: from the clothes and the room. Page chrome disappears.
- Shape: full-bleed sequences. One image, then the name, then the next image. Not a grid of twelve equals.
- Space: a breath between looks.
- Material: the photograph (`art.md`). Hard light or window light, chosen once.
- Refuse: a lifestyle paragraph, "shop the look" repeated under every image as the design, rounded thumbnails.

### Packaging label
Start from Spec or Quiet luxury, depending on whether the object is a tool or a jar.
- Type: the name large, the facts (weight, origin, ingredients) small and complete. This is a label. It tells the truth in order: what it is, what is in it, who made it, how much.
- Color: one ground, one ink, maybe one printed color. Think a tin or a paper label.
- Shape: the page can be a narrow column, like a label. Radius follows the object: 0 for a paper label, small for a tin.
- Space: tight, even, like type set on a die-cut. Alignment is strict.
- Material: paper, ink, a simple rule.
- Refuse: a hero photograph plus a fake label on top of it, marketing lines where the ingredients should be, icons for every ingredient.

### Wayfinding
Start from Civic or Instrument.
- Type: a grotesque designed to be read at a distance and at a glance. Short words. Icons from `icons.md`, always with the word, except a few learned ones inside a station you control.
- Color: high contrast. A color codes a line only if the name of the line is also there. Never color alone (`a11y.md`).
- Shape: radius small. Arrows are simple, optically aligned (`geometry.md`). The arrow and the word are one unit.
- Space: consistent. The same information sits in the same place on every "sign" (every header, every card that is actually a sign).
- Material: enamel, paint, a backlit panel. Flat. Durable, not delicate.
- Refuse: a unique layout for every page, clever icons with no words, a pastel system people cannot read from the doorway.

### Architectural drawing
Start from Spec.
- Type: a mono or a narrow grotesque for labels. The drawing is the content. Labels sit in the margin, leader lines in `--line-strong`.
- Color: paper, ink, one red for the dimension or the cut line.
- Shape: radius 0. Thin lines and one heavier line for the cut or the focus.
- Space: the drawing has room. Dimensions align.
- Material: tracing paper, ink.
- Refuse: a 3D render with a lens flare, a gradient sky, decorative line weights you cannot explain.

### Blueprint
Start from Signal, but the ground is a blueprint blue only if the user asked for a blueprint. Otherwise it is paper and a blue line.
- Type: mono, small, labels.
- Color: either paper and blue ink, or a blue ground (hue 230, lightness about 0.35) and lighter lines. Text must clear 4.5 against that ground. If it cannot, the ground is paper.
- Shape: radius 0. A title block in the corner: name, date, sheet.
- Space: grid visible, light.
- Material: a sheet.
- Refuse: a blueprint background image, white text that fails contrast, a fake aged edge.

### Sign painting
Start from Editorial.
- Type: one painted word, a slab or a heavy grotesque, slight imperfections only in that one word. The rest of the page is clean type. Do not distress the paragraph.
- Color: a dark board, a light letter, or the reverse. One color of paint.
- Shape: the word is the sign. A simple underline or a period painted on.
- Space: isolated, like a sign on a wall with the wall around it.
- Material: paint. Flat. A little brush drag is the one break, once.
- Refuse: a texture of wood on the whole site, a script face for every heading, fake rust.

## Screen-native

### Flat
Start from Instrument or Civic.
- Type: the direction's sans. Hierarchy by size and weight only.
- Color: flat roles. No gradient, no shadow. Elevation is a lightness step (`color.md`).
- Shape: the direction's radius, small. Borders or fills, not both on everything.
- Space: regular.
- Material: paper and ink, on a screen.
- Refuse: adding a shadow "so it has depth," a long gradient, neumorphic dents.

### Dense terminal
Start from Spec or Signal.
- Type: IBM Plex Sans and IBM Plex Mono. Figures in mono. Labels in the sans, or all mono if it is truly a console.
- Color: dark or paper. One phosphor or amber if it is Signal. No decoration.
- Shape: radius 2 or 0. Rules between rows. The cursor is a block only in an actual input.
- Space: compact. Row height is `--control-h` or tighter.
- Material: a screen, a spec sheet.
- Refuse: a fake CRT scanline overlay, bloom, a blinking prompt on a marketing page, green-on-black as a costume when the product is not a console.

### Raw document
Start from Broadsheet, and the face may be the browser's default serif or sans on purpose.
- Type: the user agent's face, or a single system stack, because the style is "this is a document, not a brand." Set it explicitly so it is a choice. Sizes in a simple ramp. Links blue and underlined is allowed here, and only here, because the convention is the style.
- Color: white, black, one link color that clears 4.5. Default focus outline stays.
- Shape: no radius tokens. Almost no classes. The structure is the HTML.
- Space: the browser's rhythm, cleaned up only enough to set a measure and a margin.
- Material: a document.
- Refuse: restyling it halfway into a brand, a CSS reset that removes the focus outline, a font that sneaks in "to make it nicer" and breaks the point.

### Brutalist web
Start from Editorial. This is not an excuse for a mess.
- Type: a heavy grotesque, or the raw document's face, set with intent. Huge heading, plain body, one mono for facts. Alignment is still an axis. Brutalist is blunt, not broken.
- Color: black, white, and one violent accent used as a field or a single word, checked for contrast. No palette of eight brights.
- Shape: radius 0. Visible borders, thick, on one element. Default-looking controls are allowed if they are deliberate.
- Space: tight or oddly large, but consistent. The oddness is one decision (a huge margin, a border on the whole page), repeated.
- Material: a browser. Honest.
- Refuse: overlapping unreadable text, a random rotation on every block, low-contrast gray on yellow, "ugly on purpose" without an axis. If they cannot read it, it failed, including as brutalism.

### Soft product
Start from Soft service.
- Type: a humanist sans with a real x-height. Atkinson if clarity is the point.
- Color: warm ground, one clay or leaf accent, chroma moderate.
- Shape: radius 12 on controls. Shadows none. Elevation by a lighter surface.
- Space: regular. Room to breathe, not a toy.
- Material: paper, a rounded object, daylight.
- Refuse: a squircle on every div, a mascot, baby colors, an illustration of people hugging a phone.

### Soft editorial
Start from Editorial, or Atelier when it is a portfolio. The craft site: quiet, personal, precise. The full recipe, the status strip, and the override are in `soft.md`.
- Type: a grotesk with personality for the page (Space Grotesk, Bricolage Grotesque), a display serif with a true italic for the one quote and at most one heading (Instrument Serif), mono for facts.
- Color: the base neutrals. One scarce accent. A dark pixel banner may hold the one serif italic quote, contrast-checked.
- Shape: radius 12–16 on cards. The soft surface: hairline border and soft shadow together, the one written exception to the chrome law.
- Space: regular. A status strip of two or three small cards under the headline, equal heights.
- Motion: the craft exception in `interaction.md` — reveal once, media zoom, live glyphs, the theme wipe.
- Material: a desk, a journal, a machine that is on.
- Refuse: same-gray dents, text in the shadow, focus by shadow, glass and soft on one page, a mascot per section, pixel art as the whole material.

### Agent console
Start from Spec, or Dense terminal when it is dark. A surface where a person talks to a model or supervises an agent. The full anatomy, message states, streaming laws, and approval patterns are in `ai-interfaces.md`.
- Type: the direction's sans and its mono. The transcript is body size. Meta (model, cost, context left) is `.quiet` `.mono` at one edge.
- Color: light or dark. One accent for the person's actions and the send control. Status colors only for tool-call states.
- Shape: the direction's small radius. The transcript is a document, not bubbles: author-side for the person, full-width `--surface` or plain for the machine.
- Space: compact. Composer at the bottom edge, transcript above, one conversation per view. A conversations sidebar is desktop only and it is a list.
- Motion: the craft exception does not apply by default — a stream is motion enough. Enter and exit follow `interaction.md`; the streaming laws are in `ai-interfaces.md`.
- Material: a console, a workbench with a machine on it.
- Refuse: bubble alternation for person and machine, a mascot, sparkles on every heading, chrome between turns, a spinner where streaming text would be.

### Maximal campaign
Start from Play or Editorial.
- Type: one display face at extreme scale, one text face. The campaign line is the page.
- Color: a bold field. Type in ink or paper. A photograph full-bleed is allowed if the type has a quiet place.
- Shape: the campaign owns the first viewport. The rest of the site may calm into the direction.
- Space: the first screen is full. After it, return to a measure.
- Material: print advertising. One idea.
- Refuse: maximum volume on every section, three campaigns on one page, autoplay sound.

### Data ink
Start from Spec. Tufte, as rules.
- Type: the smallest type that still clears the floor. Labels on the data. No chartjunk.
- Color: ink and the accent for the one series. Gridlines `--line` or absent.
- Shape: no boxes around charts. The data is the shape.
- Space: compact, aligned, small multiples when there are many series (`dataviz.md`).
- Material: a journal figure.
- Refuse: 3D, gradients in the fill, a legend when a label will do, dual axes, icons on bars.

### Exhibition
Start from Atelier.
- Type: wall text is large enough to read standing up. On a screen that means the article size, not a caption size, for the introductory line. Labels of works stay small.
- Color: the wall. Works punctuate it.
- Shape: a sequence of rooms, which on a page is a sequence of full sections with a breath between.
- Space: generous. A work, then text, then a work.
- Material: a room, quiet.
- Refuse: a sidebar of related products, a chat bubble, a sticky discount bar.

## Only when they ask, and then like this

These are the styles people request by their meme name. The crude version is why interfaces look generated. If they ask, do the version below.

### Glass
A panel may be translucent only when there is something real behind it (a photograph, a map) and the text still clears 4.5 against the worst frame of that background. Add a solid fallback. One panel, not a page of frosted cards. Border is a hairline, not a white glow. Blur is slight. If you cannot guarantee contrast, do not use glass. Use a solid `--surface`.

### Neumorphism
The 2019 meaning — extruded dents in the same gray, no borders, text in the shadow color — is refused: it fails contrast, fails focus, and dates the page in a season. When people point at a site they like and say this word, they almost always mean Soft editorial, above, with its border-and-shadow correction in `soft.md`. Commit that. If they truly want the dent: one raised surface, a visible border as well as the shadow, text at `--ink`, and a focus ring that does not depend on either. Prefer Flat.

### Chrome and Y2K
Start from Play. One metallic object (the hero mark, a single frame), not a page of bevels. Type stays flat and readable. Highlights are a gradient on that one object, the way the capsule has a gloss. The rest of the page is flat. Refuse: lens flare, starfields, beveled navigation, unreadable metallic body text.

### Clay and 3D characters
Do not use them as the interface. If the product is a game or Play and they asked: one character, one light, the page's palette, no gloss on the type. The UI under the character is still a normal layout with real contrast.

### Aurora and mesh gradients
A mesh is a background pretending to be a picture. Refuse it for the ground. A single quiet wash between two neighbors of the same hue, low chroma, is not an aurora. It is a tinted paper, and it must not push text off the safe band. If they asked for an aurora: one hero field, type not on the brightest part, the rest of the page returns to `--bg`.

### Brutalist meme
Random fonts, marquee tags, and a shaking button are not the brutalist style above. If they ask for "brutalist" without a reference, use Brutalist web: blunt, aligned, readable, one accent, radius 0.

## Mapping a vague ask

| They say | You commit |
|---|---|
| Clean, modern, startup | Instrument or Flat. Not a gradient. |
| Premium, elegant, luxury | Didone or Quiet luxury or Lookbook. |
| Editorial, magazine | Magazine cover or Swiss poster or Editorial. |
| Tech, developer, dark | Dense terminal or Signal. |
| Friendly, human | Soft product. Not a mascot. |
| Soft, tactile, cozy, craft | Soft editorial. Not the dent. |
| Personal site, portfolio with warmth | Soft editorial from Atelier. |
| Bold, wild, fun | Play, Memphis, or Maximal campaign. One of them. |
| Old, classic, book | Old style or Rational. |
| Fashion | Didone or Lookbook. |
| Art, museum | Gallery wall or Exhibition. |
| Local, handmade | Letterpress, Sign painting, or Packaging label. |
| Government, public | Wayfinding or Civic. |
| Data | Data ink or Spec. |
| Trippy, psychedelic | Psychedelic poster. Read the refuse line. |
| Swiss, minimal, grid | Swiss. |
| Brutal, raw, ugly-on-purpose | Brutalist web, not the meme. |
| AI-native, agentic, a copilot, "like ChatGPT" | Agent console above; the rules in `ai-interfaces.md`. |
| "Like Linear," dense, dark, keyboard-first | Spec or Dense terminal, gated by Dense dark tools in `frontier.md`. |
| Trend words: glassy, aurora, barely-there, anti-grid, shaders, expressive type | The gates in `frontier.md` first, then the matching entry above. |
