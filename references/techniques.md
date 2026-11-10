# Signature techniques

The signature moment is the one thing a visitor will describe to someone else. It should be an honest mechanism: something that actually computes, so that it behaves well when pushed in ways you did not script. This file is a catalogue of mechanisms that fit in one file with no libraries, each with the idea in a few lines. Choose by asking what the subject really does, then find its family here.

Idioms are sketches, not drop-in code. Write the real thing for the piece.

## Contents

- Springs and settling
- Bodies: rope, cloth, soft, rigid
- Crowds and fields
- Growth and pattern
- Waves and liquids
- Light and compositing
- Drawing by procedure
- Typography engines
- Mechanisms and exact maths
- Scroll-driven figures
- CSS-only state
- WebGL in one triangle
- Sound

## Springs and settling

Most "feel" comes from here. Anything that responds to a hand should be a spring in code, not an eased transition, because a spring can be interrupted mid-flight.

```js
// damped spring, substepped so stiff springs stay stable
for (let s = dt; s > 0; s -= 0.008){ const h = Math.min(0.008, s);
  v += (k*(target - x) - c*v) * h;  x += v*h; }
```

- Give every moving part its own `(k, c)`. A heavy barometer needle (6.5, .62) and a nervous wind vane (30, .2) on the same page is characterisation.
- **Stiction**: move the target only when the input has changed by more than a threshold, so needles stick and jump.
- **Chase without a spring**: `x += (target - x) * (1 - Math.exp(-rate*dt))`. Frame-rate independent; use it for scroll smoothing, doors, cameras. Never `x += (target - x) * 0.1`, which changes speed with refresh rate.
- **Closed-form overshoot** for scripted moves: `s(t) = 1 - e^(-8t) * (cos 7.8t + 1.03 sin 7.8t)` gives about four percent overshoot with no state.
- **Damped bounce** for recoil: `offset = -A * e^(-13t) * cos(40t)` for the first half second.
- **Drag with momentum**: take velocity from the last several pointer samples, coast with exponential friction, resist past the ends (scale the overdrag by about .3) and spring back.
- **One value drives many**: write a slider value into custom properties (`--amp`, `--rate`) and let keyframes multiply by them, so a single control agitates the whole page.
- **Impulse kicks**: a click or beat adds to velocity rather than setting position; the spring does the rest.
- **Sleep**: stop the loop when everything is within epsilon of rest and wake on input.

## Bodies: rope, cloth, soft, rigid

- **Towed chain** (fish, tails, hoses): each node is pulled to a fixed distance from the one ahead. Add a travelling sine whose amplitude grows toward the tail. Define markings in spine coordinates so they bend with the body.
- **Thread with slack**: smooth the polyline with two rounds of Chaikin corner-cutting, then offset along the normal by a sum of sines keyed to arc length, scaled by a slack value and eased to zero at both ends. Tighten by animating slack to zero.
- **Verlet soft body**: fixed step 1/120 s with an accumulator capped at about five substeps. Each step: integrate, shape-match (blend the best-fit rotation with an area-normalised linear fit so a squashed shape bulges), then edge and cross springs, then damp relative to rigid motion so thrown shapes keep tumbling.
- **Angular spring chain** (a leaning stack): for each joint sum the mass above; torque = gravity * mass * lever - K*θ - C*ω with C = 2ζ√(K*I). Integrate from the base up so the top lags.
- **Rigid pieces**: separating-axis tests for convex polygons; for puzzles, snap by scoring how many vertices coincide, and detect a win by sampling a grid inside the target silhouette and checking coverage.
- **Lathe profile** (pottery, turned wood): the object is a radius array. A push adds a Gaussian, neighbours are smoothed, and volume is conserved so narrowing makes it taller. Shade each strip with a gradient computed from Lambert, specular and rim terms.

## Crowds and fields

- **Flocking at thousands**: positions and velocities in typed arrays; a uniform grid built by counting sort (count, prefix sum, scatter); sample at most seven neighbours; use per-cell sums for long-range cohesion. Batch drawing into a handful of paths by depth and state.
- **Agitation wave**: each agent has an excited state with a refractory period, passed to neighbours, so a disturbance travels through the flock.
- **Field-aligned marks** (filings, grass, hatching): field = sum of softened point sources. For headless marks wrap the angle difference modulo π: `d -= Math.PI * Math.round(d / Math.PI)`.
- **Thousands of springs**: one stiffness, phase and velocity per element in Float32Arrays, driven by a moving gust front; draw the nearest few hundred in detail and the rest as strokes bucketed by colour.
- **Pheromone trails**: two scalar fields that agents deposit into and steer by with three forward sensors; diffuse and decay each step.
- **Steering**: seek, flee, wander and arrive cover most ambient creatures.

## Growth and pattern

- **Reaction-diffusion**: Gray-Scott on ping-pong float textures; vary feed and kill with a noise map so the pattern differs across the surface. Probe float and half-float render targets and fall back to Canvas 2D.
- **Dendrites and frost**: tips that curve, side branches at ±60°, an occupancy grid to stop collisions. Stroke only the new segments onto an offscreen canvas; melt with `destination-out`.
- **Mazes**: depth-first or Wilson's algorithm on a grid or on concentric rings whose cell count doubles outward; knock out a few walls for loops; breadth-first search for a pursuer.
- **Sandpiles and cellular automata**: integer grids, double-buffered active lists, a time budget per frame; write through a `Uint32Array` view of ImageData and scale up with `image-rendering: pixelated`.
- **Voronoi mosaics**: assign each pixel or cell to its nearest seed; colour from a per-cell property.
- **Rule-based ornament** (rose windows, tracery, tiling): generate from a seed and print the seed as the piece's catalogue number, so a number always returns the same piece.
- **Symmetric specimens**: paint one half, then the mirror under `scale(-1,1)` with the PRNG reseeded to the same value; add asymmetric wear afterwards with `destination-out`.

## Waves and liquids

- **1-D surface** (liquid in a vessel): heights and velocities per column, `hv += (c*(l + r - 2h) - k*h) * dt`, remove the mean each step. Tilt the rest level with a spring that seeks the container's angle.
- **2-D wave equation** in WebGL: one float texture holds current, previous and averaged energy; nine-point Laplacian; a damped border absorbs reflections; shade by curvature.
- **Metaballs**: for each blob add `(1 - q)^3` where `q = dist²/R² < 1`; threshold with a width proportional to gradient magnitude for clean edges. Move the blobs with a simple thermal model (heat at the base, buoyancy, drag). SVG fallback: blur, then push alpha contrast with `feColorMatrix`.
- **Sharpened swell**: `h = A * (2 * (.5 + .5*sin(θ - skew*cos θ))^sharp - 1)`; raise `sharp` for rougher seas.
- **Mathematical marbling**: a drop displaces every existing vertex outward by `sqrt(1 + area/dist²)`; a comb stroke shifts vertices along its direction with exponential falloff. Resample polylines under a vertex budget.
- **Caustics and haze**: compute on a buffer an eighth of the size, scale up, blend with `lighter`.
- **Ribbon material** (honey, paint): three offset ribbons along the path's normals (deep edge, body, a thin specular line), width varying per point.

## Light and compositing

Canvas compositing modes do most of the work.

- **Beam with shadows**: draw a light mask at half resolution, cut shadows out with `destination-out`, matte the true-colour scene with `destination-in`, add the mask again with `lighter` for bloom.
- **Light through glass**: copy the glass, `multiply` a radial tint centred on the sun, `color-dodge` a hotspot, `destination-in` the glass mask. Project onto a floor by drawing rows of a blurred copy sheared by the sun's angle.
- **Persistence** (phosphor, long exposure, slit-scan): each frame fade an offscreen layer with `destination-out` at alpha `1 - e^(-dt/τ)`, then draw the new samples.
- **Vector display**: stroke every line three times (wide dim glow, thin bright core, vertex dots), then screen a quarter-size blurred copy on top.
- **Line accumulation**: scale per-line alpha to the number of lines so any density lays down the same ink; jitter width and alpha per line for a hand-hatched look.
- **Day and night**: one `multiply` overprint whose colour is interpolated; emitters drawn above it.
- **CSS 3D lighting**: dot each face normal with a sun vector and pick from a tone ramp; cast a ground shadow by projecting corners and taking the convex hull.
- **Raymarched solids**: signed distance fields in a fragment shader with Fresnel and absorption; drop resolution when a frame-time average rises and recover slowly.
- **Sphere shading on canvas**: per-pixel normal from the disc, Lommel-Seeliger `μ0/(μ0+μ)` for a dusty body, shadows from a horizon sweep.

## Drawing by procedure

- **Ink ribbon**: resample a path with Catmull-Rom, give it a half-width that varies with value noise and tapers at the ends, wobble along the normal. Reads as brush or woodblock line.
- **Halftone**: walk a lattice rotated 45°, sample tone, radius ≈ `pitch * .635 * tone^.47`; hash jitter for misregistration.
- **Stamped glyphs** (typewriter, letterpress): draw the glyph offscreen, knock holes with a noise mask via `destination-in` or `destination-out`, add an offset slur at low alpha, then `multiply` onto the sheet so overstrikes darken. A persistent hashed quirk per character (the e sits high) makes it a machine.
- **Plotter drawing**: order paths by nearest endpoint, remove hidden lines with a running horizon, plan pen speed with corner limits, thin the ink where the pen is fast.
- **Stitches and weave**: draw each stitch as a short shaded strand with a twist highlight; cache sprites by parameter in a Map and clear it past a few hundred entries.
- **Point markers in SVG**: a zero-length subpath (`M x y h0`) with a round or square line cap draws a dot or a square.
- **Self-drawing lines**: set `pathLength="1"` and animate `stroke-dashoffset` from 1 to 0.
- **Sprite and glyph atlases**: paint each variant once to an offscreen canvas and `drawImage` from it per cell.

## Typography engines

- **Diffed text**: when a string changes, animate only the letters that differ and hold the rest perfectly still.
- **Character-cell displays**: keep a `chars[row][col]` buffer, build each row's markup and touch the DOM only when the row's string changed. Solve font size from a hidden probe of repeated "M".
- **Text flowing on a path**: a Catmull-Rom path with an arc-length table and binary search; animate `startOffset`. Morph to plain reading by lerping the path to a baseline.
- **Solid justified blocks**: fit every line to the full measure by ink bounds; search line breaks exhaustively for short texts.
- **Letters as bodies**: outline points become soft-body nodes or point clouds that morph between words with per-point stagger.
- **Editable glyphs**: store letters as point data, let handles be dragged, and switch page-wide rendering modes with one `data-mode` attribute on the root.

## Mechanisms and exact maths

Where a formula exists, use it. Closed forms are scrub-exact, pause-proof and identical for every viewer.

- **Clockwork**: derive everything from `Date.now()`. For meshing gears, driven angle = `-(zA/zB) * (θA - φ) + φ + 180 + 180/zB` (degrees), so teeth interlock.
- **Pendulum wave**: `θ = θ0 * cos(2π n t / 60)` per pendulum; fire a chime when `floor(2nt/60 + .5)` changes.
- **Eclipses and phases**: lit fraction from circle-overlap area.
- **Daylight and sky**: solar declination and hour angle for a date and latitude.
- **Log scales, stereographic projection, nomograms**: generate the instrument's scales from the function, as SVG.
- **Shared randomness from the clock**: seed events from the hour (`rng(hour * 7919 + 13)`) so everyone sees the same weather.
- **Mechanical flip**: draw half-faces scaled by `cos(angle)` and darkened by `sin(angle)`; cycle forward only, like the real drum.
- **Lookahead scheduler** for rhythm: a 25 ms timer schedules notes 120 ms ahead on audio time; never trust `setTimeout` for the beat itself.
- **Bezier in JS**: solve `cubic-bezier` by Newton iteration so canvas tweens match the CSS easings exactly.
- **Long computations**: work in slices under about 10 ms, yield, and cancel stale jobs by id.

## Scroll-driven figures

- A tall track (`height: 1400vh`) with a fixed or sticky stage; progress through the track drives the stage. Smooth progress with the exponential chase, never by hijacking the scroll itself.
- A sticky figure column beside flowing text; each section sets a target state.
- Scroll as depth, floors, hours or miles, with a single huge readout in the margin.
- Render only while the figure is on screen (IntersectionObserver), and stop the loop when progress has settled.
- Reduced motion: quantise into stages with previous and next buttons.

## CSS-only state

A piece with no script at all is a strong change of register within a set.

- Hidden inputs first in the DOM; state through `:checked ~` chains or `:has()`.
- `@property` registered numbers animate inside `calc()`.
- Start a continuous spin without a jump by transitioning a wrapper while the inner loop unpauses.
- Freeze a value by retargeting its transition with a huge delay.
- Retrigger a one-shot by alternating two identical keyframe names per state.
- Counters and custom-property strings (`content: var(--hint)`) write status text.
- `steps()` with a synced `clip-path` for mechanical feeds.
- Size everything in the object's own `em` so one font-size scales or nests the whole drawing.
- Isometric scenes from `rotateX(55deg) rotateZ(45deg)` with `preserve-3d`; each box one element, sides on its pseudo-elements.

## WebGL in one triangle

- One buffer holding (-1,-1), (3,-1), (-1,3), drawn as three vertices, covers the screen. All state arrives as uniforms.
- Points: per-point attributes for two positions and a random stagger; morph in the vertex shader; additive blending into a half-float target, then a tone ramp. Cut round sprites with `gl_PointCoord` and `discard`.
- Dither gradients with a hash so they do not band.
- Always: handle `webglcontextlost` and `webglcontextrestored`, probe for float targets, and ship a Canvas 2D or CSS fallback that keeps the same interactions.

## Sound

Every sound is synthesised, and every piece is complete in silence. See `engineering.md` for when the context may start.

| Voice | Recipe |
| --- | --- |
| Tick, click, key | a short burst from one shared noise buffer through a bandpass, exponential decay |
| Thud, kick, drop | a sine falling in pitch (about 165 to 43 Hz) over 150 to 200 ms |
| Bell, chime | three or four sine partials with separate exponential decays; a struck bar adds a partial at 2.756× |
| Pluck | triangle plus sines at 2× and 3.01×, fast decay |
| Wind, rain, pour | noise through a bandpass whose frequency or gain is driven by an LFO or by the simulation's energy |
| Brown noise | `b = (b + .02 * white) / 1.02` |
| Horn | two detuned saws and a sub sine through a lowpass |
| Terminal beep | a square wave, 60 ms |

Use `StereoPannerNode` to place a sound where it happens on screen, a compressor on the master for dense pieces, and `setTargetAtTime` for every gain change so nothing clicks. Envelopes ramp exponentially from and to a small positive value, never zero. An `AnalyserNode` with a zero-crossing trigger gives a steady oscilloscope trace.
