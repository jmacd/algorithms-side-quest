"""Spot for "Every-day algorithms": a maze with a left-hand-rule trace.

The essay specifies: "a maze with a thin line tracing through making
every left-hand turn until it reaches the end."

Maze layout is a small hand-designed grid; the trace is a single
polyline computed by walking with the left-hand rule from entry (top
edge, left of centre) to exit (right edge, middle).
"""

from style import BLACK, GOLDEN, SPOT_HEIGHT, SPOT_WIDTH
from lib_svg import line, main_path, polygon, rect, render, svg_close, svg_open


# 7 rows x 11 cols.  Walls are encoded as horizontal/vertical segments
# between cell corners.  Entry is at top of col 2; exit at right of row 3.
COLS = 11
ROWS = 7

# Outer walls minus entry/exit gaps.  Each tuple is (x1, y1, x2, y2) in
# grid coordinates.
WALLS = [
    # top edge with entry gap at col 2-3
    (0, 0, 2, 0), (3, 0, COLS, 0),
    # bottom edge full
    (0, ROWS, COLS, ROWS),
    # left edge full
    (0, 0, 0, ROWS),
    # right edge with exit gap at row 3-4
    (COLS, 0, COLS, 3), (COLS, 4, COLS, ROWS),
    # internal walls (hand-designed for clear left-hand-rule trace)
    (1, 1, 9, 1),
    (2, 2, 2, 6),
    (3, 2, 8, 2),
    (4, 3, 8, 3),
    (5, 4, 8, 4),
    (3, 4, 4, 4),
    (3, 5, 9, 5),
    (9, 1, 9, 6),
    (10, 2, 10, 5),
    (4, 6, 10, 6),
]


def build() -> list[str]:
    W, H = SPOT_WIDTH, SPOT_HEIGHT
    elements = svg_open(W, H)

    # Fit the maze inside the spot with margins.
    margin = 60
    cell_w = (W - 2 * margin) / COLS
    cell_h = (H - 2 * margin) / ROWS

    def gx(c):
        return margin + c * cell_w

    def gy(r):
        return margin + r * cell_h

    for x1, y1, x2, y2 in WALLS:
        elements.append(line(gx(x1), gy(y1), gx(x2), gy(y2),
                             stroke=BLACK, sw=4))

    # Hand-traced left-hand path from entry (col 2, top) to exit (right of row 3).
    # Cell centres along the path:
    trace_cells = [
        (2.5, -0.3),
        (2.5, 1.5),
        (1.5, 1.5),
        (1.5, 5.5),
        (2.5, 5.5),
        (2.5, 6.5),
        (3.5, 6.5),
        (3.5, 5.5),
        (8.5, 5.5),
        (8.5, 3.5),
        (10.5, 3.5),
        (11.3, 3.5),
    ]
    pts = [(gx(c), gy(r)) for c, r in trace_cells]
    for i in range(len(pts) - 1):
        elements.append(
            line(pts[i][0], pts[i][1], pts[i + 1][0], pts[i + 1][1],
                 stroke=GOLDEN, sw=5)
        )

    # Arrowhead at exit.
    ax, ay = pts[-1]
    elements.append(
        polygon(
            [(ax, ay - 12), (ax + 22, ay), (ax, ay + 12)],
            fill=GOLDEN, stroke=GOLDEN, sw=1,
        )
    )

    elements.append(svg_close())
    return elements


if __name__ == "__main__":
    render(build(), main_path())
