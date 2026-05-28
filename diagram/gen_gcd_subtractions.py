"""Placeholder for the cited GCD-by-successive-subtraction illustration.

Essay reference:
  https://en.wikipedia.org/wiki/File:GCD_through_successive_subtractions.svg

The slide reads "An algorithm is..." with this image on the right.  We
do not reproduce the cited SVG.  Instead we draw a small, original
trace of Euclid's subtraction algorithm on two integers so the slide
illustrates the concept without copying the source.  Source is cited
beneath the image.
"""

from style import BLACK, GOLDEN, HEIGHT, WIDTH, YELLOW
from lib_svg import (
    line,
    main_path,
    rect,
    render,
    svg_close,
    svg_open,
    text,
)


def bar(x: float, y: float, units: int, unit_w: float = 36,
        h: float = 50, fill: str = GOLDEN) -> list[str]:
    out = []
    for i in range(units):
        out.append(rect(x + i * unit_w, y, unit_w, h, fill=fill,
                        stroke=BLACK, sw=1.5))
    return out


def build() -> list[str]:
    elements = svg_open(WIDTH, HEIGHT)

    # Trace gcd(48, 18) by repeated subtraction.
    # Steps: (48, 18) -> (30, 18) -> (12, 18) -> (12, 6) -> (6, 6) -> done.
    pairs = [(48, 18), (30, 18), (12, 18), (12, 6), (6, 6)]

    x0 = 220
    y0 = 200
    row_h = 130
    unit_w = 22

    elements.append(
        text(WIDTH / 2, 110, "gcd(48, 18) by subtraction",
             size=44, anchor="middle", weight="bold")
    )

    for i, (a, b) in enumerate(pairs):
        y = y0 + i * row_h
        elements.append(
            text(x0 - 50, y + 32, f"{a:>2}, {b:>2}",
                 size=30, font="mono", anchor="end")
        )
        elements.extend(bar(x0, y, a, unit_w=unit_w, h=40, fill=GOLDEN))
        elements.extend(
            bar(x0, y + 50, b, unit_w=unit_w, h=40, fill=YELLOW)
        )
        if i < len(pairs) - 1:
            # Arrow indicating subtraction step.
            elements.append(
                text(x0 + 48 * unit_w + 30, y + 50,
                     "→ subtract smaller", size=22, anchor="start",
                     style="italic")
            )

    # Final answer.
    elements.append(
        text(WIDTH / 2, y0 + len(pairs) * row_h + 40,
             "→ gcd = 6", size=44, anchor="middle", weight="bold")
    )

    # Credit.
    elements.append(
        text(
            WIDTH / 2, HEIGHT - 60,
            "credit: Wikipedia (File:GCD_through_successive_subtractions.svg)",
            size=22, anchor="middle",
        )
    )

    elements.append(svg_close())
    return elements


if __name__ == "__main__":
    render(build(), main_path())
