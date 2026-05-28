"""Travelling Salesman: 5 cities with all connecting roads, and a
hypothetical shortest circuit highlighted in golden.
"""

import math

from style import BLACK, GOLDEN, HEIGHT, INK_FAINT, WIDTH, YELLOW
from lib_svg import (
    circle,
    line,
    main_path,
    render,
    svg_close,
    svg_open,
    text,
)


# Five city positions, deterministic.
CITIES = [
    ("A", 380, 280),
    ("B", 960, 240),
    ("C", 1260, 600),
    ("D", 880, 920),
    ("E", 360, 760),
]

# A "hypothetical" shortest circuit visiting each city exactly once
# and returning to start: A → B → C → D → E → A.
CIRCUIT = ["A", "B", "C", "D", "E", "A"]


def build() -> list[str]:
    elements = svg_open(WIDTH, HEIGHT)

    by_name = {name: (x, y) for name, x, y in CITIES}

    # All pairwise edges in faint grey.
    n = len(CITIES)
    for i in range(n):
        for j in range(i + 1, n):
            a = CITIES[i]
            b = CITIES[j]
            elements.append(
                line(a[1], a[2], b[1], b[2],
                     stroke=INK_FAINT, sw=2, dash="6,8")
            )

    # Highlight the circuit on top.
    for i in range(len(CIRCUIT) - 1):
        a = by_name[CIRCUIT[i]]
        b = by_name[CIRCUIT[i + 1]]
        elements.append(
            line(a[0], a[1], b[0], b[1], stroke=GOLDEN, sw=8)
        )

    # Cities on top.
    for name, x, y in CITIES:
        elements.append(circle(x, y, 36, fill=YELLOW, stroke=BLACK,
                               sw=3.5))
        elements.append(
            text(x, y + 14, name, size=44, font="mono",
                 anchor="middle", weight="bold")
        )

    # Caption.
    elements.append(
        text(WIDTH / 2, 100, "5-city circuit", size=44,
             anchor="middle", style="italic")
    )

    elements.append(svg_close())
    return elements


if __name__ == "__main__":
    render(build(), main_path())
