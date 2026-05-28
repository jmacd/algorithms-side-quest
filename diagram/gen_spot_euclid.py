"""Spot for "I ❤️ Algorithms": Euclid's GCD as a left-to-right flow chart.

Per the essay: left-to-right structure of Euclid's GCD with variables
``a`` and ``b``, symbolic expressions in nodes, and a recursion loop
arrow back to the start.
"""

from style import BLACK, GOLDEN, SPOT_HEIGHT, SPOT_WIDTH, YELLOW
from lib_svg import (
    circle,
    group,
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


def diamond(cx: float, cy: float, w: float, h: float,
            label: str) -> list[str]:
    pts = [(cx, cy - h / 2), (cx + w / 2, cy),
           (cx, cy + h / 2), (cx - w / 2, cy)]
    return [
        polygon(pts, fill=YELLOW, stroke=BLACK, sw=2.5),
        text(cx, cy + 10, label, size=30, font="mono", anchor="middle"),
    ]


def node(cx: float, cy: float, w: float, h: float,
         label: str, fill: str = GOLDEN) -> list[str]:
    return [
        rect(cx - w / 2, cy - h / 2, w, h, fill=fill, stroke=BLACK, sw=2.5,
             rx=14),
        text(cx, cy + 10, label, size=30, font="mono", anchor="middle"),
    ]


def arrow(x1: float, y1: float, x2: float, y2: float,
          sw: float = 2.5) -> str:
    return line(x1, y1, x2, y2, stroke=BLACK, sw=sw, marker_end=True)


def build() -> list[str]:
    W, H = SPOT_WIDTH, SPOT_HEIGHT
    elements = svg_open(W, H)

    cy = H * 0.5

    # Start: (a, b)
    elements.extend(node(180, cy, 200, 110, "(a, b)"))

    # Diamond: b == 0 ?
    elements.extend(diamond(480, cy, 240, 160, "b = 0 ?"))

    # Yes branch -> return a
    elements.extend(node(840, cy - 180, 220, 110, "return a"))

    # No branch -> recurse with (b, a mod b)
    elements.extend(node(900, cy, 320, 110, "(b, a mod b)"))

    # Arrows
    elements.append(arrow(280, cy, 360, cy))
    elements.append(arrow(480, cy - 80, 840, cy - 130))
    elements.append(text(640, cy - 110, "yes", size=26, anchor="middle"))
    elements.append(arrow(600, cy, 740, cy))
    elements.append(text(670, cy - 12, "no", size=26, anchor="middle"))

    # Loop back from (b, a mod b) under the diagram back to (a, b)
    loop_y = cy + 230
    elements.append(line(900, cy + 55, 900, loop_y, stroke=BLACK, sw=2.5))
    elements.append(line(900, loop_y, 180, loop_y, stroke=BLACK, sw=2.5))
    elements.append(line(180, loop_y, 180, cy + 55, stroke=BLACK,
                         sw=2.5))
    # arrowhead on the up-leg
    elements.append(
        polygon([(180, cy + 55), (170, cy + 75), (190, cy + 75)],
                fill=BLACK, stroke=BLACK, sw=1)
    )
    elements.append(text(540, loop_y - 14, "recurse", size=26,
                         anchor="middle", style="italic"))

    elements.append(svg_close())
    return elements


if __name__ == "__main__":
    render(build(), main_path())
