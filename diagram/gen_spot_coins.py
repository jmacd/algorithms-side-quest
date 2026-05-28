"""Spot for "Change the problem": a pile of coins.

A loose mound of overlapping circular coins.  Coin denominations
(1¢, 5¢, 10¢, 25¢) are labelled mono-numeric inside each coin.  Outer
rims alternate the accent colours.
"""

from style import BLACK, GOLDEN, SPOT_HEIGHT, SPOT_WIDTH, YELLOW
from lib_svg import circle, main_path, render, svg_close, svg_open, text


# Hand-placed pile.  (cx, cy, r, value, fill) — drawn back-to-front.
COINS = [
    (760, 600, 100, 25, YELLOW),
    (640, 580, 90, 10, GOLDEN),
    (880, 590, 88, 10, GOLDEN),
    (560, 520, 78, 5, YELLOW),
    (740, 500, 82, 25, GOLDEN),
    (920, 510, 78, 1, YELLOW),
    (470, 600, 70, 1, GOLDEN),
    (980, 600, 70, 5, YELLOW),
    (660, 430, 70, 1, GOLDEN),
    (820, 410, 72, 5, YELLOW),
    (560, 380, 60, 1, YELLOW),
    (720, 340, 66, 25, GOLDEN),
    (880, 330, 62, 10, YELLOW),
    (770, 240, 56, 5, GOLDEN),
]


def build() -> list[str]:
    W, H = SPOT_WIDTH, SPOT_HEIGHT
    elements = svg_open(W, H)

    for cx, cy, r, val, fill in COINS:
        elements.append(circle(cx, cy, r, fill=fill, stroke=BLACK, sw=3))
        # Inner rim
        elements.append(
            circle(cx, cy, r - 10, fill="none", stroke=BLACK, sw=1.5)
        )
        label = f"{val}¢"
        elements.append(
            text(cx, cy + r * 0.22, label, size=max(24, r * 0.55),
                 font="mono", anchor="middle", weight="bold")
        )

    elements.append(svg_close())
    return elements


if __name__ == "__main__":
    render(build(), main_path())
