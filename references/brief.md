# The build brief

The brief is where the page is designed. Code written from a vague brief comes out as the average of every page you have seen; code written from a brief with hex values, milliseconds and a named algorithm comes out as that page and no other. Write the brief before any code, in this order, and keep it in the conversation (or in a `.txt` beside the page when the person wants the prompts kept).

A brief for a full showpiece runs 400 to 900 words. If it is shorter, some section is still a mood and has not become a decision.

For a page that has one showpiece moment and is otherwise an ordinary, clear page (most real product pages), write sections 8 to 11 and 14 in full for the moment, and give the others a line or two each. Sound is optional everywhere. Section 15's invented proper nouns are for studies; for a real product, voice means the product's own tone and its real names.

## The sections, in order

**1. Format line.** One sentence naming the artefact and its medium. "A landing page for an invented umbrella maker, drawn as a rain-streaked shop window." "A CSS-only illustration with no JavaScript." "A one-mechanic arcade game on a vector display."

**2. Concept.** One sentence that states the idea, with no visuals in it. It should be something a person could disagree with. "The thread is the map, the memory and the way home." "Statistics that never stop being people." "Everything is a dial." If the concept sentence would fit a different page, it is a theme and not yet a concept.

**3. Mood.** Three adjectives, chosen so that the third rules something out. "Quiet, exact, slightly funny" rules out grandeur.

**4. Palette.** Four to seven hex values. Each has a role named for a material or a job (`paper`, `glaze`, `brass`, `danger`), never `primary` or `accent-2`. One of them is the rationed accent, and the brief says where it may appear ("only on the value being changed"). State the ground outright: light page, dark page, or colour field. A dark ground needs a reason in the subject.

**5. Surface.** What the page is made of and how that is drawn: paper tooth, enamel, clay grain, phosphor, cut vinyl. Name the method (see `surface-and-type.md`).

**6. Typography.** The stack for each role, written out in full, plus the treatment: size range, tracking, case, numerals. Include the exact title string and one or two real lines of copy.

**7. Composition.** What owns the viewport and where the rest sits. Draw an ASCII wireframe when the layout is not obvious. Say how the phone layout re-composes (what moves, what is dropped), because shrinking the desktop layout is not a phone layout.

**8. Method.** The real algorithm behind the piece, named, with its parameters: "depth-first maze on concentric rings, cell count doubling outward, a few loops added", "fifteen pendulums, pendulum i completes 51 + i swings a minute", "boids on a uniform grid, seven sampled neighbours". If the page is a document with no simulation, this section is the content structure and the scroll behaviour.

**9. Signature moment.** The longest paragraph. It is written as choreography: what the person does, what happens first, what follows, how it resolves, how long each beat takes. One moment per page. Everything else stays quieter than this.

**10. Interaction.** Pointer, touch and keyboard, each named. Every gesture has a key. Say what a first-time visitor sees that tells them the thing can be touched.

**11. Entrance.** The first three seconds, beat by beat with timings. The entrance should show the payoff of the page happening once by itself, so that a visitor who touches nothing still sees what it does.

**12. Motion.** Two to four easing curves with names and values, the duration bands, the stagger step. Say which motion is physical (springs in code) and which is declared (CSS).

**13. Sound.** Optional. Always off until asked, always synthesised. Name each voice and how it is made ("a sine dropping from 165 to 43 Hz", "filtered noise through a resonant bandpass").

**14. Reduced motion.** A second design, described as fully as the first: the finished still, the stepper that replaces the scroll figure, the crossfade that replaces the flight. "Animations off" is not a design.

**15. Voice.** Who is speaking and three sample lines. Invented proper nouns: the maker, the place, the year, a serial number.

If a mechanism in the brief turns out not to work on screen, change it and amend the brief, so the brief kept beside the page describes what was built.

**16. Traps.** One line naming the default this brief is steering away from. "The opposite of a tasteful dark SaaS page." "No real brand's markings."

## How specific is specific enough

Each of these is a decision someone could check in the finished file:

- "seven drops fall one after another, each ring easing out over 600 ms"
- "each pops in with its shadow, 35 ms apart"
- "only letters that differ roll; the rest hold perfectly still"
- "the needle is heavy: it overshoots once and settles in about a second"
- "yellow appears only on the dimension being changed"

Each of these is a mood, and will be filled in with a default:

- "smooth animations", "modern typography", "a bold palette", "delightful micro-interactions", "clean layout"

When a line in your brief reads like the second list, replace it with a number, a name or a sample.

## A filled example

> **A weighing page for an invented tea merchant, drawn as the brass counter scale in the shop.**
>
> Concept: you do not browse tea, you weigh it; the price is whatever the pan says.
>
> Mood: unhurried, exact, faintly stern.
>
> Palette: counter slate #2E3A3A (ground, a colour field and not a dark theme), pan brass #B8893A with highlight #E6C67A and shadow #6E4E1C, tea-paper #EFE6CF for labels and text panels, leaf green #4F6B3A, ticket red #B3261E used only for the price ticket and the tare warning. Colour-field page.
>
> Surface: honed slate drawn with two low-frequency turbulence layers and a faint diagonal sheen; brass as a five-stop linear gradient with a conic highlight on the pans; labels on laid paper (1 px rule every 3 px, heavier every 96 px).
>
> Typography: labels in an engraved caps stack ("Gill Sans","Gill Sans MT",Optima,"Trebuchet MS",sans-serif), 11 px, tracked .2em, because they are engraved plates; tea names in a book serif (Baskerville,"Hoefler Text",Palatino,Georgia,serif) at clamp(1.6rem,3.4vw,2.8rem), italic; weights and prices in the same serif with tabular old-style figures. Title string: "Harrow & Finch, Tea by the Ounce". Sample line: "Second flush. Smells of the tin it came in, which is a compliment."
>
> Composition: the scale stands centre, two thirds of the viewport tall, beam across the upper third. Six tea canisters sit on a shelf along the bottom edge. The price ticket hangs from the right pan's hook. No header, no nav; the maker's plate on the scale base is the title. On a phone the shelf becomes a horizontal strip you swipe, and the scale fills the width.
>
> Method: the beam is a damped torsion spring. Angle seeks the value set by the difference in pan loads; stiffness 9, damping 1.1, so it rocks three or four times. Pans hang from the beam ends on two-link pendulums so they stay level and swing a beat behind. Leaf is poured as particles that settle into a heap whose height is computed from mass, not simulated.
>
> Signature moment: drag a canister over the left pan and tip it. Leaf pours for as long as you hold, the pan sinks, the beam swings past level and comes back, and the ticket on the other side flips its digits one column at a time as the weight is read, always a moment late, the way a person reads a swinging scale. Let go and the beam takes about two seconds to come to rest; only then does the ticket print its final price with a small stamp and a click.
>
> Interaction: drag or touch a canister to pour; a brass weight tray on the right lets you add counterweights by tapping. Keys: 1 to 6 choose a canister, hold Space to pour, W adds a weight, Backspace empties the pan. A canister rocks once on load to show it can be picked up.
>
> Entrance: the slate fades up from black over 400 ms; the beam draws in from the pivot outward (600 ms); the pans drop on their chains and swing to rest (1.2 s, physical); the plate's lettering is revealed left to right by a clip wipe; one canister rocks.
>
> Motion: settle cubic-bezier(.16,.84,.24,1) for wipes; pop cubic-bezier(.34,1.56,.64,1) for the ticket stamp; everything on the scale is simulated, never eased. Digit flips 140 ms each, 60 ms apart.
>
> Sound: off by default, toggled by a shop bell drawn on the counter. Leaf is filtered noise whose level follows pour rate; the stamp is a short noise burst through a low bandpass; the beam at rest gives one soft sine tick.
>
> Reduced motion: the beam moves to its final angle in a single 200 ms step with no rocking, leaf appears as a heap without particles, the ticket changes without flipping. Everything still weighs and prices correctly.
>
> Voice: a shopkeeper who has opinions and no patience for adjectives. "Enough for a week, if you are sensible." "That is too much. I will sell it to you anyway." Plate: "Harrow & Finch, est. 1887, Scale No. 14".
>
> Traps: not a product grid with a cart; nothing here is a card.

Notice what the example never says: "elegant", "modern", "smooth", "premium".
