# When the page is for a real product

Most of this skill is tuned for showpieces: pages whose job is to be experienced. Real work is usually mixed. A company's landing page wants one showpiece moment and then needs to be clear; its settings screen wants none. This file is how to carry the showpiece craft into real work without spoiling it.

## Set the ambition by surface

Ask what the visitor is there to do.

| The visitor is there to | Ambition | What this skill contributes |
| --- | --- | --- |
| Be shown something (launch page, campaign, portfolio piece, event, 404, about page) | Full | Everything: concept, brief, signature moment, entrance |
| Be persuaded (product landing page, pricing story) | One moment | A signature that demonstrates the product truthfully, then quiet, legible sections |
| Read (docs, articles, changelogs) | Surface and type only | Palette, paper, typography, perhaps one living figure |
| Operate (apps, dashboards, forms, settings) | Craft only | Engineering floors, states, in-voice copy; no entrance, no ambient motion |

The surface decides, not the industry. A developer tool's landing page is still a place to be shown something. Its console is still a place to operate.

**The frequency gate.** Anything a person does many times a day gets no animation at all beyond instant feedback. Delight belongs to what is rare: first run, completion, an empty state, a milestone.

## The showpiece moment for a real product

The strongest move for a product page is to let the visitor use a small true piece of the product in the hero. Not a screenshot, not a looping video of the interface, but a working miniature: the scheduler that actually schedules three sample meetings, the formatter that formats what they type, the scale that weighs. Apply the same tests as any signature moment: it is an honest mechanism, it demonstrates itself within three seconds, and it works by keyboard and under reduced motion.

Then stop. One moment per page. Sections after the hero are calm and are not each given a trick.

## What changes from the showpiece rules

- **Facts are real.** Use the product's actual name, numbers, customers and words. Never invent testimonials, statistics, logos or awards. If something is missing, ask for it or leave a clearly marked gap. Invented worlds are for studies.
- **No real business named?** When the request is for a kind of business with no details, build for a plainly fictional stand-in (invented name, a reserved-range phone number, an `.example` address) and list what to replace in the handover. Opening hours, prices and services may be plausible placeholders; proof (reviews, counts, awards, press) is never invented.
- **Brand first.** Existing brand colours, fonts and tone are the brief. Find the tradition inside the brand (what trade, material or era does it already point at) and push that, instead of bringing a foreign one.
- **The project's stack rules.** Use its framework, components, tokens and fonts. The single-file and no-network rules are for standalone pages.
- **Web fonts are allowed** when the project has them: at most two families, preloaded, `font-display: swap`, with a fallback stack from `surface-and-type.md` tuned to similar metrics.
- **Images are allowed** when they are real: with `width` and `height`, lazy-loaded below the fold, meaningful `alt`.
- **Dark and light.** Decide from the scene of use (where is this person, in what light, doing what), not from the product category. If both themes ship, compose each one; the dark one is not the light one inverted. Set `color-scheme` and `theme-color`.

## Craft floor for product surfaces

Borrowed from what careful interface teams agree on. Check these in addition to `engineering.md`.

**States.** Every interactive element has default, hover, focus-visible, active, disabled and loading; every view has empty, error and success. Interaction raises contrast, never lowers it. Design with empty, short and very long content.

**Feedback timing.** Wait 150 to 300 ms before showing a spinner so fast responses never flash one; once shown, keep it at least 300 ms. Skeletons mirror the final layout. Press feedback under 160 ms; menus and popovers 150 to 250 ms and growing from their trigger; dialogs up to 500 ms; exits faster than entrances. Never start from `scale(0)`; .95 is plenty.

**Type.** Body at least 16 px. Measure 45 to 75 characters. Each level at least 1.25 times the next. More space above a heading than below it. Tabular numerals in tables. Real ellipses and quotation marks, non-breaking spaces inside "10 MB".

**Space.** One spacing scale. Tight within a group, generous between groups. One focal point per view: squint and check that one thing wins.

**Depth.** Shadows in two layers (a tight contact shadow and a soft ambient one), tinted toward the background hue, never a zero-offset glow. Nested corners concentric: the inner radius is the outer minus the gap. Cards only when elevation means something; never a card inside a card.

**Forms.** Visible labels. Correct `type`, `inputmode` and `autocomplete`. Never block paste. Do not disable the submit button in advance; validate on submit, show errors inline beside the field, and move focus to the first one. An error says what happened and how to fix it.

**Targets.** 24 px minimum, 44 px on touch. Never disable zoom.

**The browser's own surfaces.** Theme `::selection`, `caret-color`, `accent-color`, scrollbars, the focus ring and link underline offset. It takes six lines and is the detail most often left at default.

**Copy.** The headline says what the thing is and for whom. Buttons are a verb and its object. An action keeps one name through the whole flow. See the base skill's section on writing.

## Reviewing an existing page

When asked to improve or critique rather than build, report findings as `file:line`, most serious first, each with the fix. Separate floors that are broken (contrast, focus, overflow, missing states) from defaults that could be choices (the tells in `review.md`). Then propose at most one showpiece idea, sized to the surface.
