# Concepts and variety

A stunning page starts as a premise that would be interesting described in one sentence to someone who will never see it. The visual work then has something to be faithful to. This file is for the moment before the brief: choosing the premise, and (for a set of pages) making sure no two share one.

## Where freshness comes from

Four sources, and the strongest pages use all four.

1. **A real process, modelled honestly.** The maths of paper marbling, the kinematics of a pen plotter, a wave equation, a damped spring with the right mass, the actual light curve of an eclipse. A faked effect looks like every other faked effect; a true mechanism has behaviour nobody designed, and people feel the difference when they push on it.
2. **A named tradition.** Not "retro" but "Solari split-flap board", "Memphis-Milano", "1931 Art Deco lift lobby", "two-colour risograph zine", "cyanotype blueprint", "Attic black-figure pottery", "mid-century tin lithography", "Swiss mathematics poster", "X-Y vector arcade display". A tradition comes with its own palette, type, ornament and imperfections, so it makes a hundred decisions that would otherwise fall to habit.
3. **An invented world with proper nouns.** A maker, a place, a founding year, a serial number, a narrator with a temperament. "Station 03-117, est. 1884" does more than a paragraph of atmosphere.
4. **One twist.** A single thing that is slightly wrong or alive: the thirteenth floor that should not be there, the one specimen that still moves, the pot that collapses if you get greedy, the letter in the neon sign that never quite catches.

When the request is for a real product, sources 1 and 2 still apply (what does this product actually do, shown truthfully; what trade or material does it belong to) and source 3 is replaced by the product's real names and facts. See `product-work.md`.

## Archetypes

Pick one as the frame. These are structures, not themes; any subject can sit inside any of them.

| Archetype | What it is | The interaction |
| --- | --- | --- |
| Working instrument | A real measuring or calculating device that actually computes | Operate it and read true answers |
| Object as interface | One physical thing owns the viewport; its parts are the controls | Handle it the way you would the real one |
| Craft bench | A process you perform with tools: marbling, throwing a pot, setting type | Make something and keep it |
| Mechanical display | A board, dial wall or indicator belonging to an invented institution | Watch it update; change its inputs |
| Brand built round one toy | A landing page for an invented maker where one control demonstrates the product | Play with the toy; the page reacts |
| Product is the interface | The thing sold is what the cursor or the page becomes | Use the page and you have used the product |
| Specimen cabinet | A generated collection with catalogue numbers and curatorial text | Browse, inspect, re-seed |
| Museum of small exhibits | Several tiny pieces under one roof, each with a wall label | Wander between rooms |
| Editorial with a living figure | Long-form text beside a diagram that scroll or reading drives | Read; the figure keeps pace |
| Medium as subject | The page is read through the thing it is about (fog, print error, phosphor) | Push the medium aside to read |
| Scroll as travel | Scrolling is time, depth, floors or distance | Scroll and arrive somewhere |
| Data as people | A dataset where every unit stays an individual you can name | Regroup the crowd |
| Dashboard without rectangles | Live values shown on drawn instruments, never in tiles | Read needles and drums |
| Ambient scene | An ecosystem with nothing to win | Disturb it gently |
| One-mechanic game | An arcade or puzzle piece with a single verb | Play; lose; play again |
| Maths as specimen | A sequence, attractor or tiling presented as a living thing | Change a parameter and watch it regrow |
| Old medium, real physics | ASCII, vector CRT, line printer, with a true simulation underneath | Type or steer within its limits |
| Diorama | A small built world seen from above or in section | Flip the switches |
| No-script piece | Illustration and state done entirely in CSS | Click; nothing but stylesheets responds |

## Traditions to draw from

A starter list. Name one precisely in the brief; mixing two works when one governs layout and the other governs surface.

Print and paper: letterpress broadside, wood type, risograph, tin lithography, fine-press book, parish newsletter, Sunday-supplement editorial, technical drawing sheet, cyanotype, field notebook, museum wall label, lab manual, public-information leaflet, fan-fold computer printout, airmail stationery.

Movements: Bauhaus, Swiss/International, Memphis-Milano, op art, Art Deco, 1970s supergraphics, mid-century picture book, constructivist poster, Arts and Crafts, Vienna Secession.

Hardware: split-flap board, vector CRT, brass scientific instrument, hi-fi catalogue, toy camera, typewriter, slide rule, model railway, pen plotter, lighthouse optics, telephone exchange.

Crafts and materials: ceramics and glaze, weaving drafts, stained glass, cross-stitch, marbling, beeswax, enamel signage, cut vinyl, neon (only where the neon is literal).

Natural history: entomology drawer, conchology cabinet, herbarium sheet, core-logging sheet, tide table, star chart, aquarium panel.

## The axes of variety

Two pages feel different when they differ on most of these, and feel the same when they share three or more.

1. **Archetype** (table above)
2. **Tradition**
3. **Ground**: light paper, saturated colour field, dark, or shifting
4. **Hue family** of the ground and of the accent
5. **Lead typeface class**: didone, book serif, slab, geometric sans, humanist sans, condensed poster, typewriter, script, drawn lettering
6. **Rendering medium**: DOM and CSS only, inline SVG, Canvas 2D, WebGL, or a mix
7. **Signature technique family**: spring, particles, flocking, field, growth, wave, rigid bodies, cloth or rope, raymarch, procedural drawing, typography engine, audio engine, state machine
8. **Layout device**: single object, sticky figure beside text, full-bleed canvas with a corner plate, paged book, drawing sheet, scatter, bands, rooms
9. **Interaction verb**: drag, pour, type, scroll, steer, arrange, flick, tune, breathe on, wait
10. **Density and temperament**: maximal and loud, or sparse and exact; funny or solemn
11. **Sound**: none, percussive, tonal, textural

## The ledger, for sets of pages

When making more than one page, keep a ledger and consult it before each new brief. One line per page:

```
#   title                 archetype      tradition        ground        lead face   medium   technique       verb
01  Tea by the Ounce      object as UI   Victorian shop   slate field   book serif  svg+2d   torsion spring  pour
02  ...
```

Rules for the ledger:

- A new page may share at most two columns with any earlier page, and never the pair (ground, lead face).
- No more than a quarter of the set on dark grounds, and each dark page says why its subject needs the dark.
- No more than a fifth of the set leading with the same typeface class.
- Spread the mediums: a set that is all full-bleed canvas reads as one page repeated. Include documents, no-script pieces and pages where the browser's own layout is the star.
- Alternate temperament. After a loud page, a quiet one.
- Plan the whole ledger first, as titles and one-line concepts, before writing any brief. Sameness is cheapest to fix while the pages are still titles.

`scripts/check.py <folder>` reports shared grounds, lead faces, main colours and technique mixes across a finished set.

## Testing a concept before you commit

- Say it in one sentence to an imaginary friend. Would they ask to see it?
- Could the same sentence describe a page you have already made, or one you would make for any similar request? Then it is the default; turn one axis.
- Is there a true mechanism in it, or only an appearance? Add the mechanism.
- Does the subject justify every loud choice? "The neon is literal here" is a reason. "It looks cool" is the default speaking.
