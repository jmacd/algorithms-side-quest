"""Row formation: a single row of 21 cells labelled 0..20 for the
"all 5-cent coins" case.  Cells whose amount is divisible by 5 hold 1
(highlighted golden); others hold 0.
"""

from style import BLACK, GOLDEN, HEIGHT, WHITE, WIDTH, YELLOW
from lib_svg import main_path, render, svg_close, svg_open, text
from lib_dp_grid import GridGeom, draw_col_labels, draw_grid, draw_row_labels


def build() -> list[str]:
    elements = svg_open(WIDTH, HEIGHT)

    cols = 21
    rows = 1
    cell_w = 64
    cell_h = 90
    total_w = cols * cell_w
    x0 = (WIDTH - total_w) / 2 + 30   # nudge right for row label
    y0 = HEIGHT / 2 - cell_h / 2

    g = GridGeom(x0=x0, y0=y0, cell_w=cell_w, cell_h=cell_h,
                 rows=rows, cols=cols)

    values = [[("1" if c % 5 == 0 else "0") for c in range(cols)]]
    fills = [[(GOLDEN if c % 5 == 0 else WHITE) for c in range(cols)]]

    elements.extend(draw_grid(g, values=values, fills=fills,
                              text_size=36))

    # Column labels 0..20 above the row.
    elements.extend(
        draw_col_labels(g, [str(c) for c in range(cols)], dy=24, size=24)
    )

    # Row label to the left.
    elements.extend(draw_row_labels(g, ["5¢"], dx=28, size=42))

    # Caption above.
    elements.append(
        text(WIDTH / 2, 240,
             "ways to make A using only 5¢ coins",
             size=44, anchor="middle", style="italic")
    )

    # Footnote below.
    elements.append(
        text(WIDTH / 2, HEIGHT / 2 + 220,
             "amount A  =  0, 1, 2, … 20",
             size=32, font="mono", anchor="middle")
    )

    elements.append(svg_close())
    return elements


if __name__ == "__main__":
    render(build(), main_path())
