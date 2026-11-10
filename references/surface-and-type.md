# Palette, surface and type

Everything here works with no network: no font files, no images, no libraries. That constraint is part of the look. Pages that draw their own paper and choose their type from what is already on the machine load instantly and never break.

## Palette

- **Four to seven colours, declared once in `:root`, named for materials or jobs.** `--paper --ink --brass --glaze --thread --danger`. A name like `--primary` tells you nothing about where the colour is allowed to go; `--thread` does.
- **One rationed accent with a stated job.** It marks one kind of thing only: the value being changed, today's date, the exhibit number, the single warm window in a night scene. If the accent appears in more than about five percent of the pixels it has stopped being an accent.
- **Darker and lighter tones are mixed from the palette**, never new hues. Metals and glazes get a triple: body, highlight, shadow (`--brass --brass-hi --brass-lo`).
- **Decide the ground on purpose.** Roughly three pages in four in the strongest work sit on a light or coloured ground: paper, linen, plaster, slate, tangerine, blueprint blue. Use a dark ground when the subject needs darkness to work (additive light, night sky, a lit diner at 3 a.m.) and write that reason in the brief.
- **No pure black or white unless the two values are the concept.** Blacks are warm or tinted toward the palette (`#17110D`, `#07131F`, `#0E0B10`); whites are papers (`#EFE6CF`, `#FBF3E0`). Say which way the dark leans ("dark green, not navy").
- **Check contrast as numbers.** Body text at 4.5:1 or better against its actual background, including over texture. When colours are interpolated over time, interpolate in OKLab and enforce a contrast floor at each step.

## Surface

A flat fill reads as a screen. A surface reads as a thing. One texture layer is usually enough; build it procedurally.

**Grain from SVG noise, as a data URI.** The workhorse. A small tile of fractal noise laid over the page:

```css
.grain{position:fixed;inset:0;pointer-events:none;z-index:9;opacity:.3;mix-blend-mode:multiply;
  background:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='180' height='180'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='.9' numOctaves='2' stitchTiles='stitch'/%3E%3CfeColorMatrix values='0 0 0 0 .2  0 0 0 0 .15  0 0 0 0 .1  0 0 0 .6 -.15'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)'/%3E%3C/svg%3E")}
```

The colour matrix sets the grain's tint in its first three rows and turns noise into alpha in the fourth. On light grounds use `multiply`; on dark use `overlay` or `soft-light` at a much lower opacity (.05 to .1).

**Fibre and brushing from anisotropic noise.** Two different base frequencies stretch the noise into strands: `baseFrequency=".035 .6"` for parchment, `".012 1.3"` for brushed metal, `".006 .28"` for wood grain. Swap the pair to turn the grain ninety degrees.

**Grain from a canvas tile.** Fill a small ImageData (160 to 220 px square) with seeded random values at low alpha, optionally stroke a few dozen faint fibre curves, export with `toDataURL()` and tile it as a background. Seeded, so the paper is the same on every load.

**Materials from gradients alone.**

| Material | Recipe |
| --- | --- |
| Laid paper | `repeating-linear-gradient` 1 px line every 3 px one way, a heavier line every 96 px the other |
| Woven cloth | two or three `repeating-linear-gradient` layers of 1 px lines at 3 to 9 px spacing, alpha .02 to .3 |
| Wood | three repeating gradients a degree or so apart (179°, 180°, 180.5°) over a base tone |
| Brushed enamel | a 90° repeat with uneven stops (1/3/4/7 px) under a diagonal sheen |
| Brass | a five-stop linear gradient at about 158°; rings from `conic-gradient` |
| Aluminium, knurling | `conic-gradient` with alternating light and dark stops; `repeating-conic-gradient(#111 0 6deg,#3a3a3a 6deg 12deg)` for a knurled edge |
| Vinyl record | `repeating-radial-gradient` of hairlines |
| Halftone | `radial-gradient(circle, var(--ink) 1.15px, transparent 1.5px) 0 0/5px 5px` |
| Drafting grid | four linear gradients, fine at 5 mm and heavy at 25 mm |
| Rivets, perforations | a small `radial-gradient` repeated with `repeat-x` along an edge |
| Depth of a tray or well | four or five stacked inset `box-shadow`s |
| Torn or pinked edge | a zigzag `clip-path: polygon(...)` |

**Printed imperfection.** What makes print look printed:

- Hand wobble on edges: `feTurbulence baseFrequency=".02 to .035"` into `feDisplacementMap scale="3 to 5"`, applied to stamps, seals and hand-cut shapes.
- Off-register colour: a duplicate layer offset 1.5 to 2.5 px in the second ink.
- Overprint: plates composited with `mix-blend-mode:multiply` so two inks make a third where they cross.
- Patchy ink: a turbulence alpha mask pushed through `feColorMatrix` (alpha row around `-2 1.85`) and composited `in`, with a faint offset ghost underneath.
- Halftones as SVG `<pattern>` dots at different screen angles per ink (15°, 75°).

**Light as a layer.** A lamp pool and vignette from stacked radial gradients; window light as a blurred, skewed grid of pale panes drifting slowly; reflections on glass shifted by pointer position through custom properties; a day-to-night wash as one full-size `multiply` layer whose colour is interpolated, with lit windows drawn above it so only they glow.

**Keep glow honest.** Bloom only where something physically emits light, and faint. Halos on everything is the default, not a choice.

## Type without font files

Choose a stack whose first available face on each platform lands in the same class. Put stacks in `:root` tokens named for their role in this piece (`--plate`, `--label`, `--ticket`).

| Class | Stack |
| --- | --- |
| Didone display | `Didot,"Bodoni MT","Bodoni 72","Playfair Display",Georgia,"Century Schoolbook","Times New Roman",serif` |
| Book serif | `Baskerville,"Baskerville Old Face","Hoefler Text",Palatino,"Palatino Linotype","Book Antiqua",Georgia,serif` |
| Old-style text | `"Iowan Old Style","Adobe Garamond Pro",Garamond,"Palatino Linotype",Palatino,Georgia,serif` |
| Slab | `Rockwell,"Rockwell Nova","Roboto Slab",Clarendon,Georgia,"Times New Roman",serif` |
| Fat display | `"Cooper Black","Cooper Std Black","Bookman Old Style","Rockwell Extra Bold",Georgia,serif` |
| Geometric sans | `Futura,"Century Gothic","Avenir Next",Avenir,"URW Gothic","Trebuchet MS",sans-serif` |
| Engraved humanist | `"Gill Sans","Gill Sans MT","Gill Sans Nova",Optima,Candara,"Trebuchet MS",sans-serif` |
| Light neutral | `"Helvetica Neue","Gill Sans Light","Segoe UI Light","Segoe UI",sans-serif` |
| Condensed sign | `"Arial Narrow","Helvetica Neue Condensed","HelveticaNeue-CondensedBold","Roboto Condensed","Liberation Sans Narrow","Nimbus Sans Narrow",Impact,sans-serif` |
| Poster heavy | `Impact,Haettenschweiler,"Arial Black","Franklin Gothic Condensed","Arial Narrow",sans-serif` |
| Rounded | `"Arial Rounded MT Bold","Trebuchet MS","Gill Sans",sans-serif` |
| Stencil, show card | `"Stencil","Stencil Std",Impact,"Arial Narrow",sans-serif` · `"Playbill","Bodoni MT Condensed",Georgia,serif` |
| Typewriter | `"American Typewriter","Courier Prime",Courier,"Courier New","Nimbus Mono PS",monospace` |
| Technical mono | `"SF Mono",Menlo,Consolas,"DejaVu Sans Mono","Liberation Mono",monospace` |
| Chancery script | `"Apple Chancery","Lucida Calligraphy","Z003","URW Chancery L",Palatino,serif` |
| Roundhand | `"Snell Roundhand","Segoe Script","Brush Script MT","Z003",cursive` |
| Handwriting | `"Bradley Hand","Segoe Print","Ink Free","Marker Felt",Noteworthy,cursive` |

The base skill's limit of one or two families is about the page's own text. An object in the scene that carries writing (a handwritten repair tag, a printed ticket, an engraved plate) may use the face that object would have; that is a prop, not a third text family. Keep it to the prop.

Rotate through the classes. If the last page led with a didone on cream, this one does not.

When the lettering matters too much to leave to whatever is installed, draw it: a title built from SVG bars and arcs, a stroke font of your own for a vector display, glyphs cut from a grid. Then nothing depends on the machine.

For a real product that has brand fonts, use them and skip this table.

### Treatments

- **Extreme contrast of scale.** One display element at 11 to 16 vw (line-height around .88, tracking slightly negative) against small text. One giant thing per page: a numeral, a word, a wordmark.
- **Labels set small because the object would have them small**: engraved plates, museum labels, ticket print. 9.5 to 12 px, tracked .17 to .4em. Use capitals where the tradition does (an engraved plate, a stencil) and sentence case otherwise; an all-caps eyebrow above every heading is a tell. When centring tracked text, add `text-indent` equal to the tracking so it sits true.
- **Numerals.** `font-variant-numeric: tabular-nums` wherever a number changes; old-style figures (`"onum"`) in running text for bookish or luxury pieces.
- **Outlined and shadowed display type.** `-webkit-text-stroke` with `paint-order: stroke fill`, plus a hard offset `text-shadow` with no blur. Stack several hard shadows in palette colours at .028em steps for 1970s fat type.
- **Per-letter setting.** Wrap letters in spans carrying `--r` and `--o` for rotation and offset; animate with `--i` for stagger.
- **Fit a line to its measure.** Measure the string at 100 px with canvas `measureText` (use the actual bounding box for ink-tight fitting), set the size to `100 * width / measured * .985`, cap by viewport height, and run again on `document.fonts.ready` and on resize. Or use SVG `textLength` with `lengthAdjust` so a label keeps its footprint in any fallback face.
- **Aliasing a face across platforms.** `@font-face{font-family:"House Cond";src:local("Impact"),local("Arial Narrow Bold"),local("Roboto Condensed Bold")}` gives one name to whichever is present.
- **Text on a path.** SVG `<textPath>` for arched banners and rim lettering; animate `startOffset` to make text flow.
- **Finish.** `text-wrap: balance` on headings, `text-wrap: pretty` on paragraphs, `hanging-punctuation: first` where supported, body measure under about 70 characters, real quotation marks and dashes.
