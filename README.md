# stunningfrontenddesign

A [Claude skill](https://docs.claude.com/en/docs/claude-code/skills) for showpiece web pages: single-file HTML that people stop and play with. Landing pages built round one unforgettable interactive moment, working instruments, toys, small games, generative art, living editorial pieces, and whole galleries where no two pages look alike.

It is an add-on to Anthropic's [`frontend-design`](https://github.com/anthropics/claude-plugins-official/tree/main/plugins/frontend-design) skill and is tuned for Claude Fable 5.2. `frontend-design` teaches distinctive, restrained design for any interface. This skill covers what that one leaves out: what to do when the page itself is the point.

## What it adds

- **A concept method.** Nineteen page archetypes, a list of named traditions to work inside, and four sources of freshness (a real process modelled honestly, a named tradition, an invented world, one twist).
- **A build brief.** Sixteen sections written before any code, specific down to hex values, font stacks, milliseconds and the named algorithm, with a filled example.
- **A catalogue of honest mechanisms.** Springs, rope and soft bodies, flocking, growth, waves and liquids, light compositing, procedural ink, typography engines, exact clockwork, CSS-only state machines, one-triangle WebGL and synthesised sound, each as an idea in a few lines.
- **Type and texture with no network.** System font stacks for seventeen classes of typeface, and recipes for paper, cloth, wood, metal, halftone and print imperfection in CSS, SVG and canvas.
- **Entrance choreography.** The first three seconds as a shot list, named easing tokens, and reduced motion treated as a second design.
- **Engineering floors.** Pixel-ratio-capped canvas, a clamped fixed-step loop that pauses when hidden, pointer events, a key for every gesture, visible focus, live regions, sound that waits to be asked, a recomposed phone layout.
- **Variety for sets.** A ledger with rules, a script that deals random starting points, and a checker that reports sameness across a folder.
- **A review calibrated to the model.** Evidence-based tests, a dated list of the tells of generated pages with what to do instead, and a list of Fable 5.2's own habits to watch for.

## Install

Install Anthropic's `frontend-design` plugin first if you don't have it, then:

```bash
git clone https://github.com/kvngnsn/stunningfrontenddesign ~/.claude/skills/stunningfrontenddesign
```

Restart Claude Code. The skill loads when you ask for a stunning, creative or showcase page, or when you type `/stunningfrontenddesign`.

`check.py` and `deal.py` need only Python 3. `shoot.mjs` needs Node 22 or later and a Chrome, Chromium, Edge or Brave that is already installed; it installs nothing.

## Use

- "Make me a stunning landing page for a neighbourhood bike repair shop."
- "Build an interactive toy about tides. One HTML file."
- "stunningfrontenddesign: twenty pages, zero repetition, full creative freedom. Show me the ledger first."
- "This page looks generic. Give it one moment people will remember."

## Files

| Path | What it is |
| --- | --- |
| `SKILL.md` | The method: request, concept, brief, build, verify, review; sets of pages; notes for Fable 5.2 |
| `references/concepts.md` | Archetypes, traditions, the axes of variety, the ledger |
| `references/brief.md` | The sixteen-section build brief and a filled example |
| `references/surface-and-type.md` | Palette roles, procedural materials, system font stacks, type treatments |
| `references/techniques.md` | Signature mechanisms by family |
| `references/motion.md` | Entrance, easings, durations, reduced motion |
| `references/engineering.md` | The floors, and how to verify them |
| `references/review.md` | Tests, tells, model habits, handover |
| `references/product-work.md` | Carrying this into real product pages and codebases |
| `assets/starter.html` | Single-file plumbing for canvas, loop, input and sound |
| `scripts/deal.py` | Deals random starting hands for concepts |
| `scripts/check.py` | Static floor checks for a page; sameness report for a folder |
| `scripts/shoot.mjs` | Real-time screenshots (first frame, 3 s, phone, reduced motion) with console errors, network requests and overflow |

## Licence

[CC0 1.0](LICENSE). Public domain; use it however you like.
