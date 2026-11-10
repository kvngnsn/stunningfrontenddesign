---
name: stunningfrontenddesign
description: Builds showpiece web pages - single-file HTML that people stop and play with - landing pages with one unforgettable interactive moment, interactive toys, small games, generative art, living editorial pieces, and whole galleries of pages where no two look alike. An add-on to Anthropic's frontend-design skill, tuned for Claude Fable 5.2. Use it whenever someone asks for a page that is stunning, beautiful, fancy, impressive, creative, award-worthy, a showcase or a "wow" page; asks for an HTML experiment, demo, toy, game, visual study or creative-coding piece; wants many pages or designs with no repetition; says the result looks generic, templated or AI-made and wants it pushed further; or says "stunningfrontenddesign". Also use it to add one showpiece moment to a real product page. Not for routine app screens, forms or dashboards, where frontend-design alone is the right tool.
---

# stunningfrontenddesign

Pages that make people stop are not better-decorated versions of ordinary pages. They start from a premise worth describing, model something real, and are specified to the millisecond before a line of code exists. This skill is the working method for that kind of page.

It extends Anthropic's `frontend-design` skill. If that skill is available and not yet loaded, load it first; what it says about grounding in the subject, typography, structure, copy and restraint is assumed here and not repeated. This skill adds what a showpiece needs on top: a concept method, a build brief, a catalogue of honest mechanisms, entrance choreography, engineering floors, a way to keep a set of pages from repeating, and a review calibrated to this model's own habits.

When the two differ, the person's own words win first. After that, `frontend-design` governs surfaces people operate or read, and this skill governs surfaces people come to experience. `references/product-work.md` says how to tell which is which.

## What you make

By default, one self-contained `.html` file: inline CSS and JavaScript, no network requests, no libraries, no font files, no images. Type comes from system font stacks chosen to land on the right class of face, and every texture and illustration is drawn in CSS, SVG or canvas. This is a design position as much as a technical one: the page loads at once, works from a double-click, and cannot rot.

Inside an existing project, follow the project's stack and conventions instead, and bring everything else here with you.

## The method

### 1. Read the request for what is fixed and what is free

Whatever the person specified (subject, brand, colours, tone, a reference) is settled; build on it exactly. Everything they left open is yours to decide, and the point of this skill is to not spend that freedom on defaults.

Decide the ambition by what visitors are there to do. A page to be experienced gets the full method. A page that persuades gets one showpiece moment and calm sections. Screens people operate get craft and no spectacle. See `references/product-work.md` for real products.

If the subject is open ("make something beautiful"), choose one yourself and say what you chose in a sentence. Don't stop to ask; a concrete proposal that can be redirected is more useful than a question.

If the request names a kind of business but no actual one ("a landing page for a bike repair shop"), build for a plainly fictional stand-in: an invented name, an address that cannot exist, a phone number from a reserved range, an `.example` email. Say so when handing over and list the facts to replace. Never invent reviews, awards, customer counts or statistics, for a stand-in or for a real business.

### 2. Find the concept

Read the first half of `references/concepts.md` (the ledger half is for sets). A concept is one sentence someone could disagree with, and it draws on a real process modelled honestly, a named tradition, an invented world with proper nouns (for studies) or the product's true facts (for real work), and one twist.

Your first idea is the idea everyone gets. Write it down, then set it aside and find a second and third. When nothing in the request points anywhere, run `python3 scripts/deal.py` for a random hand of archetype, tradition, ground, typeface class, medium, technique and verb, and let the cards push you somewhere you would not have gone. The subject outranks the cards.

### 3. Write the brief

Read `references/brief.md` and write the brief in its sixteen sections before any code: format, concept, mood, palette, surface, typography, composition, method, signature moment, interaction, entrance, motion, sound, reduced motion, voice, traps. It should contain hex values, font stacks, durations, easing curves, counts and sample copy. Wherever a line reads like a mood ("smooth", "modern", "bold"), replace it with a number, a name or an example.

A showpiece gets every section in full, 400 to 900 words. A page with one showpiece moment and calm sections after it gets the moment's sections in full (method, signature, interaction, entrance, reduced motion) and a line or two for the rest; skip sound and the invented world when they do not apply.

Pull specifics from the references as you need them, not all up front: `references/surface-and-type.md` for palette roles, texture recipes and font stacks; the one family in `references/techniques.md` that matches your mechanism (it opens with a contents list); `references/motion.md` for the entrance and easings.

Then check the brief against `references/review.md` before building: run the sentence and swap tests on it, and count how many of the listed habits it leans on. Changing a brief costs a paragraph. Changing a built page costs the page.

Show the person the brief when they are present and the build is large or the direction is a gamble. Otherwise keep going; they asked for a page.

### 4. Build

Start from `assets/starter.html` for anything with a canvas, a loop or sound. It carries the plumbing (seeded randomness, pixel-ratio-capped canvas, a clamped fixed-step loop that pauses when hidden, unified pointer input, live reduced-motion handling, sound that waits for a gesture) so your attention goes to the piece. It is plumbing only and has no layout or look of its own: the full-size canvas is there to be resized, moved into a figure or deleted.

Read `references/engineering.md` before writing the script. In order:

1. Tokens in `:root` straight from the brief: palette, type roles, named easings.
2. The static composition, finished and good-looking with no script at all. This is also most of the reduced-motion design.
3. The mechanism, honest and minimal, with real controls underneath anything drawn.
4. The signature moment, then the entrance that demonstrates it unprompted within three seconds.
5. Keyboard paths, focus styles, labels and live announcements, as part of the build and not after it.
6. The phone composition and the reduced-motion design, as written in the brief.
7. Sound last, if the brief has it.

Write the file once, completely. No placeholders, no "rest of the code here", no TODOs. Then improve it with targeted edits; do not regenerate the whole file to change a part.

### 5. Verify

```bash
python3 scripts/check.py page.html      # floors a script can see; clear every FAIL
node scripts/shoot.mjs page.html        # first frame, 3 s, phone and reduced-motion screenshots,
                                        # plus console errors, network requests and overflow
```

`check.py` only reads the source, so a clean result means the floors are present, not that the page is good. Look at the screenshots. Most of what goes wrong (overflow, an empty first frame, text over texture that cannot be read, a phone layout that was only shrunk) is obvious in a picture and invisible in code. If a browser tool is available, also open the page and use it by keyboard, and screenshot the signature moment mid-interaction, which the script cannot reach. If nothing can render the page, say so when handing over instead of implying it was seen.

### 6. Review and hand over

Run the evidence tests and the tell lists in `references/review.md`, fix by editing, and hand over with two or three sentences on what it is and what to try first, the keys, and what was and was not verified.

## Sets of pages

When asked for several pages, or a gallery, variety is the job.

1. Plan the whole set first as a ledger (`references/concepts.md`): one line per page with archetype, tradition, ground, lead typeface class, medium, technique and verb. `python3 scripts/deal.py -n 20` deals spread-out starting hands.
2. Enforce the ledger rules before writing any brief: no two pages share more than two columns, at most a quarter on dark grounds, at most a fifth with the same typeface class, mediums and temperaments mixed.
3. Write each brief in full. A brief this specific can be built by a separate agent with no other context, so briefs can be built in parallel, and each builder needs only its brief, `assets/starter.html`, `references/engineering.md` and `references/techniques.md`.
4. Keep each brief beside its page as `NNN-slug.txt`.
5. Run `python3 scripts/check.py folder/` for floors and the sameness report, run `shoot.mjs` on every page, and look at the contact sheet as a whole. Pages that look like siblings get one axis turned.

State the size of the job before starting a large set. A finished page is roughly twenty to thirty thousand output tokens including its brief, so fifty pages is over a million. Get a yes for anything past a handful.

## Working as Claude Fable 5.2

This skill was calibrated on what Fable 5.2 can do in a single pass, which changes what is worth asking of yourself.

- **Ask for the real mechanism.** A wave equation, a soft-body solver, a gear train phase-locked to the clock, a reaction-diffusion shader with a fallback: each fits in one file and can be written correctly the first time. Do not settle for an animation that imitates the behaviour when the behaviour itself is within reach.
- **Spend the thinking on the concept and the brief.** That is where pages are won. Once the brief is exact, the build is execution; write it straight through.
- **Hold the whole file.** Seven hundred to a thousand lines in one file is normal for these pages. Keep one loop, one state object, one place where the canvas is sized.
- **Know your habits.** `references/review.md` lists the choices this model makes when not paying attention: warm paper grounds, one humanist sans for every label, tracked capitals, a maker's plate with a founding year, a dry narrator, the same spring curve, grain on everything. Each is good once. Check every brief and every set against the list.
- **Be economical.** Tokens here cost about twice what they do on Opus. One complete write and a few precise edits, not repeated rewrites. In a set, the concept ledger and briefs are the high-leverage part; the builds can be handed to agents on a less expensive model with the brief as their full instruction.

On Claude Opus the whole method applies as written. On smaller models (Sonnet, Haiku), keep the method and narrow the build: one technique from the catalogue, Canvas 2D or SVG instead of WebGL, no sound, and a brief at the same level of detail.

## Reference files

| File | Read it when |
| --- | --- |
| `references/concepts.md` | choosing a premise; planning a set; the variety ledger |
| `references/brief.md` | writing the build brief (always) |
| `references/surface-and-type.md` | choosing palette, drawing materials and texture, picking font stacks |
| `references/techniques.md` | choosing and implementing the signature mechanism |
| `references/motion.md` | writing the entrance, easings and the reduced-motion design |
| `references/engineering.md` | before writing script; before verifying |
| `references/review.md` | checking the brief; reviewing the finished page |
| `references/product-work.md` | the page is for a real product, or lives in an existing codebase |
| `assets/starter.html` | starting any page with a canvas, a loop or sound |
| `scripts/deal.py` | the subject is open, or a set needs spread-out starting points |
| `scripts/check.py` | after building one page or a folder of them |
| `scripts/shoot.mjs` | to see the page at desktop, phone and reduced motion, and catch console errors and overflow (Node 22+, an installed Chrome) |
