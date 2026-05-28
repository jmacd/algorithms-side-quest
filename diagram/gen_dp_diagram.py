"""Full dynamic-programming diagram: 3 rows × 21 columns.

Rows correspond to coin denominations 1¢, 2¢, 5¢ (top → bottom).  The
first column (amount = 0) is all 1s.  Coloured arrows trace one
particular path from (1¢, 0) to (5¢, 20):

  * row 1 (1¢): four arrows of length 1, ending at column 4;
  * down to row 2;
  * row 2 (2¢): three arrows of length 2, ending at column 10;
  * down to row 3;
  * row 3 (5¢): two arrows of length 5, ending at column 20.

Reflects the essay's claim that this path corresponds to
"4 one-cent coins, 3 two-cent coins, and 2 five-cent coins to reach
20".  The essay's parenthetical "three arrows" for the 1¢ row is read
as a typo; using four arrows preserves the 4+6+10 = 20 arithmetic the
essay explicitly states.
"""

from style import BLACK, GOLDEN, HEIGHT, WHITE, WIDTH, YELLOW
from lib_svg import (
    line,
    main_path,
    polygon,
    render,
    svg_close,
    svg_open,
    text,
)
from lib_dp_grid import GridGeom, draw_col_labels, draw_grid, draw_row_labels


def colored_arrow(g: GridGeom, r1: int, c1: int, r2: int, c2: int,
                  color: str, sw: float, dash: str | None = None,
                  inset: float = 14) -> str:
    """Arrow between cell centres, slightly inset from the cell edges."""
    x1, y1 = g.cx(c1), g.cy(r1)
    x2, y2 = g.cx(c2), g.cy(r2)
    # Slight vertical offset so multiple arrows in the same row don't sit on
    # the cell numbers.  Always nudge up to avoid clipping.
    if r1 == r2:
        y1 -= 18
        y2 -= 18
    return line(x1, y1, x2, y2, stroke=color, sw=sw, marker_end=True,
                dash=dash)


def build() -> list[str]:
    elements = svg_open(WIDTH, HEIGHT)

    cols = 21
    rows = 3
    cell_w = 64
    cell_h = 140
    total_w = cols * cell_w
    x0 = (WIDTH - total_w) / 2 + 30
    y0 = (HEIGHT - rows * cell_h) / 2 + 40

    g = GridGeom(x0=x0, y0=y0, cell_w=cell_w, cell_h=cell_h,
                 rows=rows, cols=cols)

    # First column all 1s (highlight in light yellow); other cells blank.
    fills = [[WHITE] * cols for _ in range(rows)]
    values = [[""] * cols for _ in range(rows)]
    for r in range(rows):
        fills[r][0] = YELLOW
        values[r][0] = "1"

    elements.extend(draw_grid(g, values=values, fills=fills,
                              text_size=30))

    # Column labels 0..20.
    elements.extend(
        draw_col_labels(g, [str(c) for c in range(cols)], dy=22, size=22)
    )
    # Row labels.
    elements.extend(
        draw_row_labels(g, ["1¢", "2¢", "5¢"], dx=24, size=40)
    )

    # Arrows.  Three coin colours/styles: 1¢ black solid, 2¢ golden solid,
    # 5¢ black thick dashed.  All within the only-two-accent palette.
    # 1¢ row: arrows (0,0)->(0,1)->(0,2)->(0,3)->(0,4)
    for c in range(4):
        elements.append(
            colored_arrow(g, 0, c, 0, c + 1, BLACK, sw=3)
        )
    # Down (0,4) -> (1,4)
    elements.append(
        line(g.cx(4), g.top(0) + cell_h - 8,
             g.cx(4), g.top(1) + 8,
             stroke=BLACK, sw=3, marker_end=True)
    )
    # 2¢ row: (1,4)->(1,6)->(1,8)->(1,10)
    for k in range(3):
        c1 = 4 + 2 * k
        c2 = c1 + 2
        elements.append(
            colored_arrow(g, 1, c1, 1, c2, GOLDEN, sw=5)
        )
    # Down (1,10) -> (2,10)
    elements.append(
        line(g.cx(10), g.top(1) + cell_h - 8,
             g.cx(10), g.top(2) + 8,
             stroke=BLACK, sw=3, marker_end=True)
    )
    # 5¢ row: (2,10)->(2,15)->(2,20)
    for k in range(2):
        c1 = 10 + 5 * k
        c2 = c1 + 5
        elements.append(
            colored_arrow(g, 2, c1, 2, c2, BLACK, sw=5, dash="14,8")
        )

    # Caption.
    elements.append(
        text(WIDTH / 2, 100,
             "ways to make A  using {1¢, 2¢, 5¢}",
             size=44, anchor="middle", style="italic")
    )
    elements.append(
        text(WIDTH / 2, HEIGHT - 90,
             "one path:  4 × 1¢  +  3 × 2¢  +  2 × 5¢   =   20¢",
             size=32, font="mono", anchor="middle")
    )

    elements.append(svg_close())
    return elements


if __name__ == "__main__":
    render(build(), main_path())
