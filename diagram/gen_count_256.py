"""Counting to 256: a strip of three register snapshots (0, 127, 255).

The essay describes an animation; we render three static snapshots in
a left-to-right progression so the slide deck communicates the same
idea without requiring Lottie playback.  Each snapshot shows a 3-digit
decimal counter and the corresponding 8-bit register.
"""

from style import BLACK, GOLDEN, HEIGHT, WIDTH
from lib_svg import line, main_path, polygon, render, svg_close, svg_open, text
from lib_register import bits_from_int, draw_register


SNAPSHOTS = (0, 127, 255)


def build() -> list[str]:
    elements = svg_open(WIDTH, HEIGHT)

    elements.append(
        text(WIDTH / 2, 160, "1 byte counts 0 → 255",
             size=56, anchor="middle", style="italic")
    )

    cell = 56
    gap = 5
    reg_w = 8 * cell + 7 * gap
    spacing = 80
    rows_y0 = 260
    row_h = 240

    # Decimal counter column on the left of each row, register on right.
    for i, v in enumerate(SNAPSHOTS):
        y = rows_y0 + i * row_h
        # Decimal display
        elements.append(
            text(280, y + 70, f"{v:>3}",
                 size=120, font="mono", anchor="end", weight="bold")
        )
        # Register
        x = 360
        bits = bits_from_int(v, 8)
        elements.extend(
            draw_register(bits, x, y, cell=cell, gap=gap)
        )
        # Down arrow between snapshots
        if i < len(SNAPSHOTS) - 1:
            ax = 220
            ay1 = y + cell + 30
            ay2 = y + row_h - 10
            elements.append(line(ax, ay1, ax, ay2, stroke=BLACK, sw=3))
            elements.append(
                polygon(
                    [(ax - 10, ay2 - 16), (ax + 10, ay2 - 16), (ax, ay2)],
                    fill=BLACK, stroke=BLACK, sw=1,
                )
            )

    elements.append(svg_close())
    return elements


if __name__ == "__main__":
    render(build(), main_path())
