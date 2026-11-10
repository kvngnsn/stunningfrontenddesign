#!/usr/bin/env python3
"""Static checks for single-file HTML studies.

    python3 check.py page.html            # one page
    python3 check.py folder/              # every .html in a folder, plus a sameness report

It reads files and prints findings. It never runs the page and never touches the network.
FAIL means the page breaks a floor the skill promises. WARN means look and decide.
Exit status is 1 when any page has a FAIL.

Standard library only.
"""
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

HEX = re.compile(r"#([0-9a-fA-F]{6}|[0-9a-fA-F]{3})\b")
URL_USE = re.compile(
    r"""(?:src|href|action|poster)\s*=\s*["']?\s*(?:https?:)?//|"""
    r"""url\(\s*["']?\s*(?:https?:)?//|@import|"""
    r"""\bfetch\s*\(|XMLHttpRequest|new\s+WebSocket|sendBeacon|EventSource\s*\(|importScripts""",
    re.I,
)
EMOJI = re.compile("[\U0001F300-\U0001FAFF\U00002700-\U000027BF\U0001F000-\U0001F2FF]")
FONT_DECL = re.compile(r"font-family\s*:\s*([^;}{]+)", re.I)
VAR_DECL = re.compile(r"--[\w-]+\s*:\s*((?:\"[^\"]+\"|'[^']+'|[\w -]+)(?:\s*,\s*(?:\"[^\"]+\"|'[^']+'|[\w -]+)){2,})\s*[;}]")
GENERIC = {"serif", "sans-serif", "monospace", "cursive", "fantasy", "system-ui", "inherit",
           "ui-serif", "ui-sans-serif", "ui-monospace", "ui-rounded", "math", "emoji"}
DEFAULT_FACES = {"inter", "roboto", "arial", "helvetica", "open sans", "poppins", "montserrat",
                 "space grotesk", "system-ui", "-apple-system", "blinkmacsystemfont", "segoe ui"}


def norm_hex(h):
    h = h.lower()
    return "".join(c * 2 for c in h) if len(h) == 3 else h


def rgb(h):
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


def hsl(h):
    r, g, b = (v / 255 for v in rgb(h))
    mx, mn = max(r, g, b), min(r, g, b)
    l = (mx + mn) / 2
    if mx == mn:
        return 0.0, 0.0, l
    d = mx - mn
    s = d / (2 - mx - mn) if l > 0.5 else d / (mx + mn)
    if mx == r:
        hh = ((g - b) / d) % 6
    elif mx == g:
        hh = (b - r) / d + 2
    else:
        hh = (r - g) / d + 4
    return hh * 60, s, l


def first_faces(text):
    """First named face of every font stack, lower-cased."""
    faces = []
    stacks = [m.group(1) for m in FONT_DECL.finditer(text)]
    stacks += [m.group(1) for m in VAR_DECL.finditer(text)]
    for stack in stacks:
        if "var(" in stack:
            continue
        parts = [p.strip().strip("\"'").lower() for p in stack.split(",")]
        parts = [p for p in parts if p and not p.startswith("!")]
        if len(parts) >= 1 and parts[0] not in GENERIC and re.match(r"^[a-z0-9 .-]+$", parts[0]):
            faces.append(parts[0])
    return faces


def ground_colour(text):
    m = re.search(r"(?:html\s*,\s*)?body\s*\{[^}]*?background(?:-color)?\s*:\s*([^;}]+)", text, re.I)
    if not m:
        return None
    val = m.group(1)
    hx = HEX.search(val)
    if hx:
        return norm_hex(hx.group(1))
    v = re.search(r"var\((--[\w-]+)", val)
    if v:
        d = re.search(re.escape(v.group(1)) + r"\s*:\s*#([0-9a-fA-F]{3,6})\b", text)
        if d:
            return norm_hex(d.group(1))
    return None


def check(path):
    text = path.read_text(encoding="utf-8", errors="replace")
    low = text.lower()
    fails, warns = [], []

    # --- floors -----------------------------------------------------------
    for m in URL_USE.finditer(text):
        line = text.count("\n", 0, m.start()) + 1
        fails.append(f"line {line}: network or external resource ({m.group(0).strip()[:40]})")
    if "<script" in low and re.search(r"<script[^>]+\bsrc\s*=", text, re.I):
        fails.append("external script tag: inline everything")
    if "prefers-reduced-motion" not in low:
        fails.append("no prefers-reduced-motion handling")
    if "name=\"viewport\"" not in low and "name=viewport" not in low:
        fails.append("no viewport meta")
    if not re.search(r"<title>\s*\S", text, re.I):
        fails.append("no <title>")
    if not re.search(r"<html[^>]*\blang\s*=", text, re.I):
        fails.append("no lang on <html>")
    interactive = bool(re.search(r"pointerdown|mousedown|touchstart|onclick|addEventListener\(\s*['\"]click", text))
    if interactive and ":focus-visible" not in low and ":focus" not in low:
        fails.append("interactive but no visible focus style")
    if re.search(r"outline\s*:\s*(none|0)\b", low) and ":focus-visible" not in low:
        fails.append("outline removed with no :focus-visible replacement")
    if re.search(r"\.play\(\)|new\s+Audio\(", text) and "autoplay" in low:
        fails.append("media autoplay: sound must wait for a gesture")
    if re.search(r"<h1[\s>]", text, re.I) is None:
        warns.append("no <h1>: give the page a real title element (visually hidden is fine)")

    # --- judgement calls --------------------------------------------------
    if interactive and "keydown" not in low and not re.search(r"<(button|input|select|a)\b", low):
        warns.append("pointer interaction with no keyboard path")
    if re.search(r"mousedown|mousemove", text) and "pointerdown" not in text and "touchstart" not in text:
        warns.append("mouse-only events: use pointer events so touch and pen work")
    if "getcontext(" in low:
        if "devicepixelratio" not in low:
            warns.append("canvas without devicePixelRatio sizing will be soft on dense screens")
        if "requestanimationframe" in low and "visibilitychange" not in low:
            warns.append("animation loop does not pause when the tab is hidden")
        if "aria-" not in low and "role=" not in low:
            warns.append("canvas piece with no accessible name, label or live region")
    if "audiocontext" in low and not re.search(r"aria-pressed|type=\"checkbox\"|role=\"switch\"", low):
        warns.append("sound without an obvious toggle control")
    if "setinterval(" in low and "requestanimationframe" not in low:
        warns.append("setInterval-driven animation: prefer requestAnimationFrame")
    if EMOJI.search(text):
        warns.append("emoji used as graphics: draw it instead")
    if "backdrop-filter" in low:
        warns.append("backdrop-filter (frosted glass): a default look unless the subject calls for it")
    if re.search(r"lorem ipsum|your (text|title|content) here|placeholder text", low):
        warns.append("placeholder copy")
    if re.search(r"(?<![-\w])height\s*:\s*100vh", low) and "dvh" not in low and "svh" not in low:
        warns.append("100vh without a dvh/svh companion: mobile browser bars will crop it")
    if re.search(r"transition\s*:\s*all\b", low):
        warns.append("transition: all (name the properties)")

    faces = first_faces(text)
    lead = [f for f, _ in Counter(faces).most_common()]
    if lead and lead[0] in DEFAULT_FACES:
        warns.append(f"lead typeface is a default ({lead[0]}): choose a face for this subject")
    if not faces:
        warns.append("no named typeface anywhere: type is undesigned")

    colours = Counter(norm_hex(h) for h in HEX.findall(text))
    purple = [c for c in colours if 250 <= hsl(c)[0] <= 290 and hsl(c)[1] > .45 and .35 < hsl(c)[2] < .75]
    if len(purple) >= 2 and "gradient" in low:
        warns.append("saturated violet plus gradients: the stock generated look, keep only if it is the subject")
    ground = ground_colour(text)

    size = len(text.encode("utf-8"))
    if size > 400_000:
        warns.append(f"{size // 1024} KB: large for one file")

    return {
        "path": path, "fails": fails, "warns": warns, "ground": ground,
        "top": [c for c, _ in colours.most_common(6)], "faces": lead[:3],
        "tech": sorted(k for k, v in {
            "canvas2d": "getcontext('2d')" in low or 'getcontext("2d")' in low,
            "webgl": "webgl" in low, "svg": "<svg" in low, "svg-filter": "<filter" in low,
            "audio": "audiocontext" in low, "dom-only": "getcontext(" not in low and "<svg" not in low,
        }.items() if v),
    }


def hue_bucket(hexcode):
    h, s, l = hsl(hexcode)
    if l < .12:
        return "dark"
    if s < .12:
        return "light-neutral" if l > .8 else "grey"
    names = ["red", "orange", "yellow", "green", "teal", "blue", "violet", "pink"]
    edges = [20, 45, 70, 160, 200, 255, 300, 345]
    for name, edge in zip(names, edges):
        if h < edge:
            return name + ("-light" if l > .8 else "")
    return "red" + ("-light" if l > .8 else "")


def sameness(results):
    n = len(results)
    out = []
    grounds = defaultdict(list)
    for r in results:
        if r["ground"]:
            grounds[hue_bucket(r["ground"])].append(r["path"].name)
    for bucket, names in sorted(grounds.items(), key=lambda kv: -len(kv[1])):
        if len(names) > max(2, n * .25):
            out.append(f"{len(names)}/{n} pages share a {bucket} ground: {', '.join(names[:6])}")
    faces = defaultdict(list)
    for r in results:
        if r["faces"]:
            faces[r["faces"][0]].append(r["path"].name)
    for face, names in sorted(faces.items(), key=lambda kv: -len(kv[1])):
        if len(names) > max(2, n * .2):
            out.append(f"{len(names)}/{n} pages lead with '{face}': {', '.join(names[:6])}")
    exact = defaultdict(list)
    for r in results:
        if len(r["top"]) >= 3:
            exact[tuple(sorted(r["top"][:3]))].append(r["path"].name)
    for key, names in exact.items():
        if len(names) > 1:
            out.append(f"same three main colours in: {', '.join(names)}")
    tech = Counter(tuple(r["tech"]) for r in results)
    for combo, count in tech.items():
        if count > max(3, n * .5):
            out.append(f"{count}/{n} pages use the same technique mix ({'+'.join(combo)})")
    return out


def main(argv):
    if len(argv) != 2:
        print(__doc__)
        return 2
    target = Path(argv[1])
    files = sorted(target.glob("*.html")) if target.is_dir() else [target]
    if not files:
        print("no .html files found")
        return 2
    results = [check(f) for f in files]
    bad = 0
    for r in results:
        status = "FAIL" if r["fails"] else ("WARN" if r["warns"] else "ok")
        bad += bool(r["fails"])
        print(f"{status:4}  {r['path'].name}")
        for f in r["fails"]:
            print(f"      FAIL  {f}")
        for w in r["warns"]:
            print(f"      warn  {w}")
    if len(results) > 1:
        print("\nSameness across the set")
        notes = sameness(results)
        for line in notes or ["nothing repeated past the thresholds"]:
            print(f"  {line}")
    print(f"\n{len(results)} page(s), {bad} failing")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
