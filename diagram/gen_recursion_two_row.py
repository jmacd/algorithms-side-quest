"""Two-row, three-column recursion-relation diagram.

The essay (§ "Recursion relation in words") describes two rows
(``K coins`` and ``K+1 coins``) and three columns (``A'``, ..., ``A``)
with values ``N`` (row 1, col 3) and ``N'`` (row 2, col 1) and an
arrow labelled ``C`` from ``N'`` rightward two cells to (row 2, col 3),
indicating that ``A' + C = A``.

A second variant, used by the "again" slide, additionally fills
(row 2, col 3) with ``N + N'`` and shows two arrows whose contributions
are summed.
"""

import sys

from style import BLACK, GOLDEN, HEIGHT, WHITE, WIDTH, YELLOW
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
from lib_dp_grid import GridGeom, draw_col_labels, draw_grid, draw_row_labels


def build(filled: bool) -> list[str]:
    elements = svg_open(WIDTH, HEIGHT)

    cols = 3
    rows = 2
    cell_w = 220
    cell_h = 180
    total_w = cols * cell_w
    x0 = (WIDTH - total_w) / 2 + 40
    y0 = (HEIGHT - rows * cell_h) / 2 + 40

    g = GridGeom(x0=x0, y0=y0, cell_w=cell_w, cell_h=cell_h,
                 rows=rows, cols=cols)

    # Values and fills.
    values = [[""] * cols for _ in range(rows)]
    fills = [[WHITE] * cols for _ in range(rows)]
    values[0][2] = "N"
    values[1][0] = "N'"
    if filled:
        values[1][2] = "N + N'"
        fills[1][2] = YELLOW

    elements.extend(draw_grid(g, values=values, fills=fills,
                              text_size=68))

    # Column headers: A', (ellipsis), A
    elements.extend(
        draw_col_labels(g, ["A'", "…", "A"], dy=28, size=44)
    )

    # Row labels.
    elements.extend(
        draw_row_labels(g, ["K coins", "K+1 coins"], dx=36, size=38)
    )

    # Arrow from (row1, col2) = N to (row2, col2) = N+N' down (only filled).
    # And arrow from N' across two cells with label C.
    # Bottom-row arrow N' → cell(row=1,col=2): horizontal.
    src_x = g.cx(0) + cell_w * 0.30
    dst_x = g.cx(2) - cell_w * 0.30
    by = g.cy(1) - 70
    elements.append(
        line(src_x, by, dst_x, by, stroke=GOLDEN, sw=6, marker_end=True)
    )
    elements.append(
        text((src_x + dst_x) / 2, by - 18, "+ C",
             size=42, font="mono", anchor="middle", fill=BLACK,
             weight="bold")
    )

    if filled:
        # Down arrow from N (row 0 col 2) into row 1 col 2.
        dx = g.cx(2)
        dy1 = g.top(0) + cell_h - 4
        dy2 = g.top(1) + 6
        elements.append(
            line(dx, dy1, dx, dy2, stroke=GOLDEN, sw=6, marker_end=True)
        )

    # Bottom legend.
    legend = "A' + C = A"
    elements.append(
        text(WIDTH / 2, HEIGHT - 80, legend,
             size=44, font="mono", anchor="middle", style="italic")
    )

    if filled:
        elements.append(
            text(WIDTH / 2, HEIGHT - 30,
                 "count to A with new coin  =  N + N'",
                 size=34, anchor="middle", style="italic")
        )

    elements.append(svg_close())
    return elements


if __name__ == "__main__":
    out = main_path()
    filled = "filled" in out
    render(build(filled), out)
