"""Four-byte (32-bit) register with arbitrary bits and a decimal display.

Per the essay (§ "Counting to 4,294,967,296"): "draw four bytes with
random 0-1 values side by side, slight spacing between the bytes."
Deterministic constant pattern is used in place of randomness.
"""

from style import BLACK, HEIGHT, WIDTH
from lib_svg import main_path, render, svg_close, svg_open, text
from lib_register import bits_from_int, draw_register


def build() -> list[str]:
    elements = svg_open(WIDTH, HEIGHT)

    # Deterministic 32-bit value: 0xC3A91B6E
    value = 0xC3A91B6E
    bits = bits_from_int(value, 32)

    cell = 38
    gap = 4
    byte_gap = 22
    total_w = 32 * cell + 28 * gap + 3 * (byte_gap - gap)
    x = (WIDTH - total_w) / 2
    y = 360

    elements.extend(
        draw_register(bits, x, y, cell=cell, gap=gap,
                      byte_gap=byte_gap)
    )

    # Caption
    elements.append(
        text(WIDTH / 2, 260, "4 bytes  =  32 bits",
             size=56, anchor="middle", style="italic")
    )

    elements.append(
        text(WIDTH / 2, 620, "2³² = 4,294,967,296",
             size=72, font="mono", anchor="middle", weight="bold")
    )
    elements.append(
        text(WIDTH / 2, 720, "≈ 4 billion", size=52, anchor="middle",
             style="italic")
    )

    elements.append(svg_close())
    return elements


if __name__ == "__main__":
    render(build(), main_path())
