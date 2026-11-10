#!/usr/bin/env python3
"""Deal starting points for page concepts, so the first idea is not always the same idea.

    python3 deal.py                      # one hand
    python3 deal.py -n 12                # twelve hands with the columns spread out
    python3 deal.py -n 5 --seed 41       # repeatable
    python3 deal.py --avoid dark,didone  # leave out anything containing these words

A hand is a prompt for thinking, not a specification. Take it as dealt, or keep the
columns that fit the subject and redeal the rest. The subject always outranks the cards:
if the request names a tradition, a ground or a typeface, that column is already decided.

Standard library only.
"""
import argparse
import random

DECK = {
    "archetype": [
        "working instrument", "object as interface", "craft bench", "mechanical display",
        "brand built round one toy", "product is the interface", "specimen cabinet",
        "museum of small exhibits", "editorial with a living figure", "medium as subject",
        "scroll as travel", "data as people", "dashboard without rectangles", "ambient scene",
        "one-mechanic game", "maths as specimen", "old medium, real physics", "diorama",
        "no-script piece",
    ],
    "tradition": [
        "letterpress broadside", "wood type poster", "two-colour risograph", "tin lithography",
        "fine-press book", "technical drawing sheet", "cyanotype blueprint", "field notebook",
        "lab manual", "public-information leaflet", "fan-fold computer printout",
        "airmail stationery", "Bauhaus", "Swiss/International poster", "Memphis-Milano",
        "op art", "Art Deco", "1970s supergraphics", "mid-century picture book",
        "constructivist poster", "Vienna Secession", "split-flap board", "vector CRT",
        "brass scientific instrument", "hi-fi catalogue", "toy camera", "model railway",
        "pen plotter", "enamel signage", "cut vinyl", "ceramics and glaze", "weaving draft",
        "stained glass", "cross-stitch sampler", "woodblock print", "entomology drawer",
        "herbarium sheet", "tide table", "star chart", "black-figure pottery",
        "screenprinted gig poster", "transit map", "seed packet", "matchbox label",
        "ship's log", "knitting pattern", "board-game box", "pharmacy label",
    ],
    "ground": [
        "light paper", "light paper, cool", "plaster or blush", "saturated warm colour field",
        "saturated cool colour field", "mid-tone slate or stone", "raw material (kraft, concrete, linen)",
        "dark, because the subject emits light", "shifting through the page",
        "pure white with one ink", "two flat colours split",
    ],
    "lead face": [
        "didone", "book serif", "old-style text serif", "slab", "fat display serif",
        "geometric sans", "humanist sans", "light neutral sans", "condensed sign",
        "poster heavy", "rounded", "stencil", "typewriter", "technical mono", "script",
        "handwriting", "drawn lettering (SVG or canvas)",
    ],
    "medium": [
        "DOM and CSS only", "inline SVG", "Canvas 2D", "WebGL", "SVG with a canvas layer",
        "CSS 3D", "text itself (character cells or type engine)",
    ],
    "technique": [
        "springs and settling", "rope or thread", "soft bodies", "rigid pieces", "flocking",
        "field-aligned marks", "growth (dendrite, lichen, coral)", "maze or graph",
        "cellular automaton", "wave or liquid surface", "metaballs", "light compositing",
        "persistence and trails", "procedural ink line", "halftone or print process",
        "typography engine", "exact clockwork or astronomy", "scroll-driven figure",
        "CSS state machine", "audio engine", "software 3D", "raymarched solid",
    ],
    "verb": [
        "drag", "pour", "type", "scroll", "steer", "arrange", "flick", "tune", "wind",
        "breathe on", "wait and watch", "trace", "stack", "cut", "press and hold", "sort",
    ],
    "temperament": [
        "sparse and exact", "loud and maximal", "funny", "solemn", "tender", "bureaucratic",
        "childlike", "clinical", "eerie", "exuberant",
    ],
    "sound": ["none", "none", "none", "percussive", "tonal", "textural"],
}


def deal(n, rng, avoid):
    columns = {}
    for name, cards in DECK.items():
        pool = [c for c in cards if not any(a in c.lower() for a in avoid)] or cards
        picks = []
        while len(picks) < n:            # go through the whole pool before repeating any card
            round_ = pool[:]
            rng.shuffle(round_)
            picks.extend(round_)
        columns[name] = picks[:n]
    return [{name: columns[name][i] for name in DECK} for i in range(n)]


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("-n", type=int, default=1, help="number of hands")
    ap.add_argument("--seed", type=int, default=None, help="seed for a repeatable deal")
    ap.add_argument("--avoid", default="", help="comma-separated words to leave out")
    args = ap.parse_args()

    seed = args.seed if args.seed is not None else random.SystemRandom().randrange(1, 10**6)
    rng = random.Random(seed)
    avoid = [a.strip().lower() for a in args.avoid.split(",") if a.strip()]
    print(f"seed {seed}\n")
    for i, hand in enumerate(deal(max(1, args.n), rng, avoid), 1):
        print(f"hand {i}")
        for name, card in hand.items():
            print(f"  {name:12} {card}")
        print()


if __name__ == "__main__":
    main()
