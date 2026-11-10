# Motion and entrance

The base skill says to keep unprompted motion rare and orchestrate one moment. This file is how to build that moment and the small responses round it. If a general motion-principles skill is installed, it covers timing and easing fundamentals; this file covers the choreography specific to showpiece pages.

## Mood decides the physics

Decide once, in the brief, how things in this world move, and hold to it.

| Temperament | Motion |
| --- | --- |
| Toys, sweets, play | springs with visible overshoot, squash and stretch, pops |
| Instruments, luxury, clinical | slow decelerating curves, nothing bounces, long holds |
| Heavy machinery, concrete, vaults | in-out curves with a delay before moving, a settle bump at the end |
| Print and paper | wipes, stamps, `steps()` jitter, things placed rather than flown |
| Living things | continuous simulation, never a tween |

## Easings are named tokens

Declare two to four curves in `:root`, named for what they are in this piece (`--settle`, `--brush`, `--pour`, `--pop`), and use only those. Bare `ease` and `ease-in-out` are the default and read as one.

| Job | Curves |
| --- | --- |
| Settle (most entrances and reveals) | `cubic-bezier(.16,.84,.24,1)`, `(.2,.8,.2,1)`, `(.16,1,.3,1)`, `(.22,1,.3,1)` |
| Spring pop (overshoot) | `(.34,1.56,.64,1)`, `(.3,1.5,.5,1)`, `(.3,1.7,.5,1)`; squish `(.2,1.9,.4,.9)` |
| Wipe, brush, weight (in-out) | `(.77,0,.18,1)`, `(.65,0,.2,1)`, `(.62,.02,.18,1)`, `(.7,0,.2,1)` |
| Falling, closing (accelerating) | `(.55,0,.95,.45)`, `(.6,0,.9,.5)` |
| Mechanical, precise | `(.3,0,.2,1)`, `(.4,0,.1,1)` |
| Ambient sway (loops) | `(.45,0,.55,1)` on `alternate` |
| Shake | `(.36,.07,.19,.97)` |

A spring written as `linear(...)` behind `@supports` gives several bounces where the bezier gives one. Anything a hand can interrupt should be a spring in code instead (see `techniques.md`).

## Durations and staggers

| Band | Range |
| --- | --- |
| Press, hover, toggle | 120 to 350 ms |
| Interface changes | 450 to 900 ms |
| Reveals | 0.7 to 1.6 s |
| Atmosphere (a lamp warming, glare fading) | 1.5 to 2.8 s |
| Ambient loops | 9 to 48 s, layers given different periods and negative delays so they never line up |

Staggers by `--i`: about 30 ms per letter, 40 to 70 ms per small item, 70 to 130 ms per large one. `animation-delay: calc(var(--i) * 55ms + 250ms)`. Order the stagger by something real (reading order, distance from an origin, printing order), not DOM order by accident.

## The entrance

Write the first three seconds as a shot list. Three rules:

1. **Follow the object's real order.** A print is laid down block by block and sealed last. A terminal warms to a line, counts memory, then draws its panels. A blueprint is drafted centre lines first, then tubes, then dimensions. A building is poured storey by storey. The order is information about the thing.
2. **Show the payoff unprompted.** By three seconds the signature has happened once by itself: the board cascades, a few drops fall and a comb passes through them, the flags spell a word, the scale rocks. A demo replaces an instruction.
3. **Stay skippable and short.** 1.5 to 3 seconds. Any input cuts to the ready state.

### Vocabulary

Reach for these before a fade.

- **Clip wipe**: `clip-path: inset(0 100% 0 0)` to `inset(0 -3% 0 0)`, often with a small translate that settles. Brushes, glazes, ink.
- **Rule draw**: `transform: scaleX(0)` to `1` from one end.
- **Self-drawing line**: `pathLength="1"`, `stroke-dashoffset` 1 to 0.
- **Sticker slap**: from `scale(1.6) rotate(8deg)` to rest on a spring curve.
- **Drop with squash**: multi-stop keyframes, each stop with its own timing function.
- **Tracking settle**: letter-spacing easing from wide to set (or the reverse for something dissolving).
- **Focus pull**: `filter: blur(3px)` to `0` over a couple of seconds, for things emerging from fog or dark.
- **Stutter on**: uneven opacity steps for a tube or filament catching; one element may keep failing.
- **Stepped feed**: `steps(14,end)` for paper and tape.
- **Stamp**: scale down from large with a shake and a roughened edge filter.
- **Time warp**: run the simulation fast at first and decelerate to real time, `speed = 1 + 21 * e^(-(t-1)/1.05)`, so the scene is established when the visitor arrives.
- **Circular reveal**: `clip-path: circle(0 at X Y)` growing from the light source.

Fade-and-rise on every section as it scrolls into view is the default, and the base skill names it as a tell. If sections must reveal, use one of the above tied to the tradition, and only once per section.

## Responses to the hand

- Buttons that press into a hard offset shadow on `:active`.
- Ink-fill hovers: a pseudo-element scaling from an edge.
- Cards that tilt toward the pointer while their shadow slides the other way.
- A hint that demonstrates (one canister rocks, one key depresses) and then disappears for good once the thing has been used.
- Hover effects only under `@media (hover:hover)`; on touch the same information appears on tap.

## Reduced motion is a second design

Write it into the brief and build it as carefully as the first. Listen for the setting changing while the page is open. Every control keeps working.

| The piece does this | With reduced motion it does this |
| --- | --- |
| Builds itself in an entrance | appears finished |
| Drives a figure by scroll | steps through stages with previous and next |
| Flies, flips or morphs between states | crossfades, or changes at once with a brief highlight |
| Runs an ambient simulation | runs at a quarter to a third speed with fewer agents, or shows a composed still that redraws on input |
| Springs and rocks to a value | moves there in one short step |
| Loops forever | holds its best frame |
| Shakes, flashes, strobes | does not |

Functional motion stays: a timer still counts, a game still moves its pieces, a dragged thing still follows the finger.

In CSS, disable under the media query and then set the end state explicitly; an animation that is simply removed can leave things at their starting opacity of zero.

```css
@media (prefers-reduced-motion: reduce){
  .in{animation:none;opacity:1;transform:none;clip-path:none}
}
```
