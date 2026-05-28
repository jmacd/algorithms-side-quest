"""Stylised Fort Bragg, CA street map placeholder.

Per the essay (§ "Count the houses in town"): "Show a street map of
Fort Bragg, CA".  Per ``AGENTS.md`` we do not embed remote assets and
we do not fabricate a faithful map.  This renders an abstract street
grid (rectilinear blocks + a coast/ocean band on the west, mimicking
Fort Bragg's general shape) with house dots distributed along the
streets, plus a visible credit line explaining what's drawn.
"""

from style import BLACK, GOLDEN, HEIGHT, INK_FAINT, INK_MID, WIDTH, YELLOW
from lib_svg import (
    circle,
    line,
    main_path,
    rect,
    render,
    svg_close,
    svg_open,
    text,
)


def build() -> list[str]:
    elements = svg_open(WIDTH, HEIGHT)

    # Ocean band on the west.
    ocean_w = 200
    elements.append(rect(0, 0, ocean_w, HEIGHT, fill=YELLOW,
                         stroke="none", sw=0))
    # Wavy coastline.
    for i in range(40):
        y = i * (HEIGHT / 40)
        dx = 12 if i % 2 == 0 else -8
        elements.append(
            line(ocean_w + dx, y, ocean_w + dx + 4, y + HEIGHT / 40,
                 stroke=BLACK, sw=1.5)
        )
    elements.append(
        text(ocean_w / 2, HEIGHT / 2, "Pacific", size=32,
             anchor="middle", style="italic", fill=BLACK)
    )

    # Street grid east of the coast.
    grid_x0 = ocean_w + 80
    grid_x1 = WIDTH - 80
    grid_y0 = 120
    grid_y1 = HEIGHT - 160

    # East-west streets.
    n_h = 9
    h_step = (grid_y1 - grid_y0) / n_h
    for i in range(n_h + 1):
        y = grid_y0 + i * h_step
        elements.append(line(grid_x0, y, grid_x1, y,
                             stroke=INK_MID, sw=2.5))

    # North-south streets.
    n_v = 11
    v_step = (grid_x1 - grid_x0) / n_v
    for j in range(n_v + 1):
        x = grid_x0 + j * v_step
        elements.append(line(x, grid_y0, x, grid_y1,
                             stroke=INK_MID, sw=2.5))

    # Highway 1 (thicker, slightly inland).
    hwy_x = grid_x0 + v_step * 1.0
    elements.append(line(hwy_x, grid_y0 - 40, hwy_x, grid_y1 + 40,
                         stroke=BLACK, sw=6))
    elements.append(text(hwy_x + 14, grid_y0 - 50, "Hwy 1",
                         size=22, font="mono"))

    # Houses: a small dot near each street intersection (offset).
    for i in range(n_h):
        for j in range(n_v):
            for dx, dy in ((0.25, 0.25), (0.75, 0.25),
                           (0.25, 0.75), (0.75, 0.75)):
                cx = grid_x0 + (j + dx) * v_step
                cy = grid_y0 + (i + dy) * h_step
                elements.append(
                    circle(cx, cy, 4, fill=GOLDEN, stroke=BLACK, sw=0.6)
                )

    # Label.
    elements.append(
        text(WIDTH / 2, 70, "Fort Bragg, CA — stylised grid",
             size=40, anchor="middle", style="italic")
    )
    elements.append(
        text(WIDTH / 2, HEIGHT - 60,
             "credit: placeholder, not a true map",
             size=22, anchor="middle")
    )

    elements.append(svg_close())
    return elements


if __name__ == "__main__":
    render(build(), main_path())
