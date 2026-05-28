"""Spot for "Counting from zero": zoom on a DP grid showing the two
incoming arrows from (x-1, y) and (x, y-1) into (x, y).
"""

from style import BLACK, GOLDEN, SPOT_HEIGHT, SPOT_WIDTH, YELLOW
from lib_svg import (
    line,
    main_path,
    polygon,
    rect,
    render,
    svg_close,
    svg_open,
    text,
)


def build() -> list[str]:
    W, H = SPOT_WIDTH, SPOT_HEIGHT
    elements = svg_open(W, H)

    # Small 3x3 grid centred, with the central cell highlighted.
    cell = 200
    grid_w = cell * 3
    grid_h = cell * 3
    x0 = (W - grid_w) / 2
    y0 = (H - grid_h) / 2

    for r in range(3):
        for c in range(3):
            fill = "#ffffff"
            if (r, c) == (1, 1):
                fill = GOLDEN
            elif (r, c) in ((1, 0), (0, 1)):
                fill = YELLOW
            elements.append(
                rect(x0 + c * cell, y0 + r * cell, cell, cell,
                     fill=fill, stroke=BLACK, sw=4)
            )

    # Cell labels.
    def lab(c, r, s):
        elements.append(
            text(x0 + c * cell + cell / 2,
                 y0 + r * cell + cell / 2 + 14,
                 s, size=42, font="mono", anchor="middle")
        )

    lab(0, 1, "(x−1, y)")
    lab(1, 0, "(x, y−1)")
    lab(1, 1, "(x, y)")

    # Two big arrows into (1,1).
    elements.append(
        line(x0 + cell, y0 + cell + cell / 2,
             x0 + cell + 50, y0 + cell + cell / 2,
             stroke=BLACK, sw=6, marker_end=True)
    )
    elements.append(
        line(x0 + cell + cell / 2, y0 + cell,
             x0 + cell + cell / 2, y0 + cell + 50,
             stroke=BLACK, sw=6, marker_end=True)
    )

    elements.append(svg_close())
    return elements


if __name__ == "__main__":
    render(build(), main_path())
