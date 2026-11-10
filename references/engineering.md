# Engineering floors

A showpiece that stutters, blurs on a dense screen, ignores the keyboard or dies on a phone is not stunning. These floors are what let an ambitious page be shipped without a second look. `assets/starter.html` has the plumbing for most of them; `scripts/check.py` tests the ones a script can see.

## One file, no network

- One `.html` with inline `<style>` and `<script>`. No external scripts, stylesheets, fonts, images, analytics or `fetch`. Graphics are inline SVG, data URIs, CSS, or drawn on canvas.
- No frameworks or libraries. Everything in `techniques.md` is a few dozen lines when written for one purpose.
- Forms do not submit anywhere; they answer locally with an in-world confirmation.
- Storage is rarely needed. If used, wrap it in try/catch and work without it.
- When a project has its own stack (React, a build step, a design system), these single-file rules give way to the project's conventions. The rest of this file still applies.

## Canvas

- Size the backing store at CSS size × `Math.min(devicePixelRatio || 1, 2)` and scale the context to match. Uncapped pixel ratios on phones cost three times the fill for nothing visible.
- Re-lay out on resize through one `requestAnimationFrame` (or a ResizeObserver), and re-bake any static layers. Listen to `visualViewport` when an on-screen keyboard can cover the piece.
- Static art (paper, sky, glass, sprites, glyph atlases) is drawn once to an offscreen canvas and blitted.
- Expensive light (caustics, haze, glow, shadow masks) is computed at a quarter or an eighth of the size and scaled up.
- Batch strokes: one path per colour-and-width bucket, not one `stroke()` per item.
- Above about a thousand of anything, use typed arrays and preallocate. No allocation inside the frame.
- Write whole images through a `Uint32Array` view of ImageData.

## The loop

- One `requestAnimationFrame` loop. Clamp `dt` to 50 ms so a stalled tab does not explode the simulation. Physics on a fixed step (1/120 s) with an accumulator and a cap on substeps.
- Pause on `visibilitychange`; on resume reset the clock before the first frame.
- Run on demand where you can: a dirty flag skips drawing when nothing changed, and a sleeping loop wakes on input. IntersectionObserver pauses work that is off screen.
- Watch frame time with a moving average. After sustained slowness, degrade in steps: lower internal resolution, thin the agent count, drop the costliest layer. Recover slowly so it does not oscillate.
- DOM writes only on change: compare before `setAttribute` or `textContent`; update custom properties every few frames if every frame is not needed.
- Seed all randomness (mulberry32 or a hash). Show the seed as content when re-creating a piece matters: a drawer number, an opus number, an edition.

## Input

- Pointer Events only, with `setPointerCapture` and `pointercancel` handled. No separate mouse and touch code paths.
- `touch-action: none` on a surface that is dragged; `pan-y` where the page must still scroll under a figure. Never trap the wheel: at the edge of a zoom range let it pass through to the page.
- Hover behaviours sit behind `@media (hover:hover) and (pointer:fine)`. A custom cursor likewise, and it never hides the real pointer on touch.
- On touch, anything that follows the finger (a loupe, a tool) floats above it, not under it.
- Tap targets at least 44 px, whatever the drawn object's size; a transparent button over a small drawn control is fine.
- `-webkit-tap-highlight-color: transparent`, `overscroll-behavior: none` on full-screen toys, `user-select: none` on the play surface only.

## Keyboard and assistive tech

- Every gesture has a key. Arrows nudge (Shift for coarse or fine), Home and End jump, Space or Enter acts, Escape dismisses or releases, number or letter keys select tools. Do not steal keys while focus is in a text field.
- Show the keys somewhere in the piece's own voice, with `<kbd>`.
- Real controls underneath the drawing: native `<button>`, `<input type="range">`, links. A drawn lever is a styled button. Where a canvas has regions that act, lay transparent focusable buttons over them.
- `:focus-visible` always has a visible ring, in the palette and in-world: a dashed pencil box, inverse video on a terminal, a brass outline. Never `outline: none` without a replacement.
- Toggles carry `aria-pressed`; custom sliders are `role="slider"` with `aria-valuenow` and an `aria-valuetext` in words ("6 of 10, properly hot").
- A decorative canvas is `aria-hidden`. A canvas that is the content has `role="img"` and an `aria-label` that says what is shown, and state changes are announced in a visually hidden `aria-live="polite"` region.
- A real `<h1>` (visually hidden if the title is drawn), `lang` on `<html>`, a `<title>`, landmark elements for pages with sections, a skip link on long documents.
- Text contrast 4.5:1 or better, measured against the texture it actually sits on.

## Reduced motion

Read the setting in CSS and in script, and listen for it changing. What each kind of motion becomes is in `motion.md`. The floor here: with the setting on, the page is complete, nothing is stuck at opacity zero, and every control works.

## Sound

- Silent on load, always. The `AudioContext` is created inside the first click on a visible sound control, and resumed if suspended.
- The control is a real toggle with `aria-pressed`, drawn as something from the world (a bell, a tuning fork, a lamp switch).
- A master gain, changed only with `setTargetAtTime`. Suspend the context shortly after muting and when the tab is hidden.
- Nothing essential is carried by sound alone.

## Phone

- Write the phone composition in the brief. Recompose: stack the stage above the text, turn a rail into a swipe strip, cut the agent count, drop secondary panels. A desktop layout scaled down is not a phone layout.
- `min-height: 100dvh` with a `100vh` fallback; `env(safe-area-inset-*)` padding where the piece runs to the edges; `viewport-fit=cover`.
- No horizontal page scroll at 320 px wide. `overflow-x: clip` on the root is a guard, not a fix.
- Type sized with `clamp()`; body text never under 16 px on phones for anything that is read.
- State counts in the brief per breakpoint ("8,000 stalks on desktop, 3,400 on phones").

## Fallbacks

- WebGL: handle context loss and restoration, probe for the texture formats you need, and keep a Canvas 2D or CSS version with the same interactions.
- Guard newer CSS with `@supports` (`linear()`, `@property`, `:has()`, scroll timelines) and give the plain path a finished look.
- A short in-world `<noscript>` line when the piece needs script.

## CSS hygiene

- Tokens in `:root`: palette, type roles, easings, a few lengths. Everything else refers to them.
- Animate `transform`, `opacity`, `clip-path` and `filter`; name the properties in every `transition` (never `all`).
- Keep selector specificity flat so section rules and component rules do not cancel each other.
- Layer order declared once (`z-index` tokens or DOM order), with the grain overlay on top and `pointer-events: none`.
- `box-sizing: border-box` globally; `-webkit-font-smoothing: antialiased` on dark-on-light display type where it helps.

## Verify before handing over

1. `python3 scripts/check.py page.html` and clear every FAIL.
2. `node scripts/shoot.mjs page.html` for screenshots at 1440 × 900 (first frame and after three seconds), 390 × 844 and reduced motion, with console errors, network requests and overflow reported. Look at the screenshots; a picture finds what reading code does not. Headless Chrome's own `--screenshot` flag is not a substitute: it cannot go narrower than 500 px and starves animation frames.
3. If a browser tool is available, capture the signature moment mid-interaction as well.
4. Tab through it. Use it with keys only.
5. Emulate reduced motion and confirm the still is a finished composition.
6. Narrow to 320 px and look for overflow.

If the environment cannot open a browser, say so in the handover instead of claiming it was checked.
