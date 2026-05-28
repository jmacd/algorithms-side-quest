"""Single-byte (8-bit) register showing [01101010] = 106.

Per the essay (§ "Bytes"):
  1 * 2^6 + 1 * 2^5 + 1 * 2^3 + 1 * 2^1
  = 64 + 32 + 8 + 2
  = 106

The expansion is shown directly beneath the register cells.
"""

from style import BLACK, GOLDEN, HEIGHT, WIDTH
from lib_svg import main_path, render, svg_close, svg_open, text
from lib_register import bits_from_int, draw_register


def build() -> list[str]:
    elements = svg_open(WIDTH, HEIGHT)

    value = 0b01101010  # 106
    bits = bits_from_int(value, 8)

    cell = 110
    total_w = 8 * cell + 7 * 8
    x = (WIDTH - total_w) / 2 - 60   # leave room for "=  106" on the right
    y = 280

    elements.extend(
        draw_register(bits, x, y, cell=cell, gap=8, decimal=value,
                      decimal_size=72)
    )

    # Expansion: 1*2^6 + 1*2^5 + 1*2^3 + 1*2^1
    line1 = "2⁶  +  2⁵  +  2³  +  2¹"
    line2 = "64  +  32  +   8  +   2"
    line3 = "=  106"

    elements.append(
        text(WIDTH / 2, 580, line1, size=58, font="mono", anchor="middle")
    )
    elements.append(
        text(WIDTH / 2, 680, line2, size=58, font="mono", anchor="middle")
    )
    elements.append(
        text(WIDTH / 2, 800, line3, size=72, font="mono", anchor="middle",
             weight="bold", fill=BLACK)
    )

    # Caption above the register
    elements.append(
        text(WIDTH / 2, 220, "8 bits = 1 byte", size=44,
             anchor="middle", style="italic")
    )

    elements.append(svg_close())
    return elements


if __name__ == "__main__":
    render(build(), main_path())
