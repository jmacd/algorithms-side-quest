"""Spot for "Counting exercises": person at a chalkboard with n! = n·(n-1)!.

Simple line-art figure facing a chalkboard; thought-bubble shape above
the head indicating thinking.  All elements are deterministic.
"""

from style import BLACK, GOLDEN, SPOT_HEIGHT, SPOT_WIDTH, YELLOW
from lib_svg import (
    circle,
    ellipse,
    line,
    main_path,
    path,
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

    # Chalkboard on the left, framed with golden border.
    bx, by, bw, bh = 80, 120, 720, 520
    elements.append(rect(bx - 16, by - 16, bw + 32, bh + 32,
                         fill=GOLDEN, stroke=BLACK, sw=3))
    elements.append(rect(bx, by, bw, bh, fill="#ffffff",
                         stroke=BLACK, sw=2))
    # Chalk equation
    elements.append(
        text(bx + bw / 2, by + bh / 2 + 30,
             "n! = n · (n − 1)!", size=88, font="mono",
             anchor="middle", weight="bold")
    )

    # Person on the right.  Head, body, arms, legs.
    px = W - 360
    head_y = 220
    elements.append(circle(px, head_y, 60, fill=YELLOW, stroke=BLACK,
                           sw=2.5))
    # Eyes
    elements.append(circle(px - 22, head_y - 6, 4, fill=BLACK,
                           stroke=BLACK, sw=1))
    elements.append(circle(px + 22, head_y - 6, 4, fill=BLACK,
                           stroke=BLACK, sw=1))
    # Mouth
    elements.append(path(f"M{px - 18},{head_y + 24} q18,12 36,0",
                         stroke=BLACK, sw=2))
    # Body
    elements.append(
        path(
            f"M{px - 60},{head_y + 70} Q{px},{head_y + 60} "
            f"{px + 60},{head_y + 70} L{px + 90},{head_y + 320} "
            f"L{px - 90},{head_y + 320} Z",
            fill=YELLOW, stroke=BLACK, sw=2.5,
        )
    )
    # Arm pointing toward the board (left)
    elements.append(
        line(px - 60, head_y + 100, px - 220, head_y + 70,
             stroke=BLACK, sw=4)
    )
    elements.append(circle(px - 230, head_y + 65, 10, fill=YELLOW,
                           stroke=BLACK, sw=2))
    # Other arm at side
    elements.append(line(px + 70, head_y + 100, px + 110, head_y + 260,
                         stroke=BLACK, sw=4))
    # Legs
    elements.append(line(px - 40, head_y + 320, px - 60, head_y + 480,
                         stroke=BLACK, sw=4))
    elements.append(line(px + 40, head_y + 320, px + 60, head_y + 480,
                         stroke=BLACK, sw=4))
    # Shoes
    elements.append(ellipse(px - 60, head_y + 488, 24, 8, fill=BLACK,
                            stroke=BLACK, sw=1))
    elements.append(ellipse(px + 60, head_y + 488, 24, 8, fill=BLACK,
                            stroke=BLACK, sw=1))

    # Thought bubble above head (3 ellipses).
    for cx, cy, r in ((px + 80, head_y - 80, 14),
                      (px + 110, head_y - 130, 22),
                      (px + 160, head_y - 200, 36)):
        elements.append(circle(cx, cy, r, fill="#ffffff", stroke=BLACK,
                               sw=2))
    elements.append(text(px + 160, head_y - 192, "?", size=44,
                         font="mono", anchor="middle", weight="bold"))

    elements.append(svg_close())
    return elements


if __name__ == "__main__":
    render(build(), main_path())
