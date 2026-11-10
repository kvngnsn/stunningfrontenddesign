# Review before handing over

Run this after the page works. It has three parts: tests that ask for evidence, the tells of generated pages, and the habits of this particular model. Fix what you find by editing the file, not by regenerating it.

## Tests that need evidence

Answer each with something you can point at (a selector, a value, a screenshot region), never a bare yes.

1. **The sentence test.** Describe the page in one sentence to someone who cannot see it. If the sentence would fit another page you could have made, the concept is thin.
2. **The swap test.** Replace the title and nouns with those of an unrelated subject. If the design still fits, it was not designed for this subject. Name three elements that would stop making sense.
3. **The strip test.** Remove all the text. Is the subject still recognisable from what remains?
4. **The first-frame test.** Screenshot at 0 s and at 3 s having touched nothing. Is the first frame composed, and has the signature happened by the second?
5. **The squint test.** Blur the screenshot. One thing should win. Name it.
6. **The removal test.** Take away one decoration at a time. Whatever is not missed, delete.
7. **The honesty test.** Push the signature in a way the brief did not script: drag fast, interrupt mid-animation, resize during it, hold two keys. A true mechanism copes.
8. **The brief test.** Go down the brief line by line. Every hex, duration and behaviour is either in the file or the brief is amended to say what was built instead.
9. **The quiet test.** List every element that moves without being touched. Each needs a reason from the subject. More than the signature and one ambient layer is usually too many.
10. **The phone test.** Look at the 390 px screenshot as its own design. Is it composed, or squeezed?

## Tells of generated pages (as of late 2026)

These shift with each model generation; the list is dated on purpose. Each tell comes with the move to make instead, because a bare ban only sends you to the nearest substitute. All of them are legitimate when the subject calls for them and the brief says so.

| Tell | Instead |
| --- | --- |
| Violet-to-blue gradients, cyan glow on near-black | A palette taken from the subject's materials |
| Cream ground, high-contrast serif, terracotta accent | Any ground the last page did not use; a face from another class |
| Near-black ground with one acid accent | A coloured or light ground; dark only with a stated reason |
| Broadsheet hairlines with italic serif and tracked mono labels | Structure taken from the subject's own documents |
| Flat ink, condensed caps, hard shadows on everything | Hard shadows only inside a tradition that has them |
| Inter, Roboto, system UI as display; then Space Grotesk, DM Sans, Outfit, Plus Jakarta, Playfair, Fraunces | A stack chosen from the subject's world |
| Three equal icon cards; cards inside cards; one radius everywhere | Layout devices from `concepts.md`; elevation only where it means something |
| Hero with a big number, small label and a stat strip | Open with the most characteristic thing in the subject's world |
| An all-caps tracked eyebrow above every heading | Labels only where the object would carry one |
| 01 / 02 / 03 on things that are not a sequence | Number only real sequences, or use the subject's own numbering |
| One italic or coloured word in the headline | Let the whole line's setting carry it |
| Gradient text, frosted glass, coloured side stripes, glow halos | Material surfaces from `surface-and-type.md` |
| Fade-and-rise on every section; hover-scale on every card; pulsing dots | One orchestrated entrance; responses that show what changed |
| Bounce on utility actions | Springs for toys, decelerating curves for tools |
| Emoji as icons | Drawn SVG in the page's own line weight |
| Meta strings joined with middle dots; arrows appended to links | Sentences, or the object's own notation |
| "Seamless", "elevate", "unleash"; "Not X. Y." headings; rows of dashes | Plain claims with a fact in them |
| The usual particle network or starfield behind a hero | A mechanism that belongs to the subject |

## This model's own habits

A study of a large set of showpiece pages produced by Claude Fable 5.2 shows preferences that are fine once and become a signature across a set. If you are that model, these are your defaults; if you are another, they are still common. Each is a choice to make deliberately.

- **Warm paper grounds.** More than a quarter of pages land on cream, ivory or linen. Next most common is near-black. Reach for slate, plaster pink, enamel green, tangerine, blueprint blue, raw concrete, aqua.
- **Gill Sans for every small label.** It is the first label face in most pages. Rotate: a typewriter face, a condensed sign face, a light neutral sans, the display face itself at small size.
- **Tracked small capitals on all labels,** whatever the object. The base skill names all-caps labels as a tell. Keep them for engraved plates and stencils; elsewhere use sentence case.
- **Didone for anything refined, a typewriter face for anything personal.** Both are good and both are overused.
- **The maker's plate.** "Est. 18xx", "No. 14", a founding pair of surnames with an ampersand. One invented maker is charming; ten in a row is a formula. Vary the kind of institution, the era (not always Victorian or mid-century) and how it identifies itself.
- **One dry, wry narrator.** Deadpan specificity is the model's house voice. Let some pages be earnest, exuberant, terse, childlike, bureaucratic or silent.
- **The same two springs.** `cubic-bezier(.34,1.56,.64,1)` and `(.3,1.5,.5,1)` appear across many pages. Tune the curve to the object's weight.
- **A multiply grain overlay on everything.** Some surfaces are clean: enamel, glass, screen, vinyl.
- **Full-bleed canvas with a corner caption** as the layout for anything simulated. Try the simulation inside a document, a diagram or a sheet.
- **Museum and cabinet framings.** Specimen drawers, vitrines and wall labels recur. So do brass instruments.
- **Sound as a bonus.** Roughly half of pages add synthesised audio. Add it when the subject makes sound, not as a habit.

For a single page, check that at most three of these are present and that each was chosen. For a set, the ledger in `concepts.md` is what keeps them from stacking.

## The floor checklist

`scripts/check.py` covers the mechanical part. By eye:

- No console errors; works opened straight from the file system.
- Composed first frame; signature within three seconds; entrance skippable.
- Every gesture has a key; focus ring visible everywhere; tab order follows the page.
- Reduced motion shows a finished composition with every control working.
- No horizontal scroll at 320 px; phone layout recomposed; safe areas respected.
- Silent until asked; sound toggle is a real pressed-state control.
- Text contrast holds over texture; nothing essential is under 12 px.
- The loop pauses when hidden and sleeps when idle.
- Copy is original and in voice; no placeholder text; invented things are plainly invented.
- For product work: nothing invented at all.

## Handing over

Say in two or three sentences what the page is and what to try first, list the keys, and state plainly what was verified (checker, screenshots at which sizes, reduced motion) and what was not. If the brief changed during the build, give the as-built version.
