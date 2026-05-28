"""Title spot: three bumble bees in flight over poppies on bare ground.

Composition per the essay (§ "Spot illustrations"):
  * three bees, similar size with +/- 5% variation;
  * each bee: 1 head + 4 body sections in alternating black/golden/...
    /black/golden/black, two lobe-shaped wings (black outline, one
    vein each), pair of legs, pair of antennae;
  * level ground with indistinct cover and 4 clusters of yellow
    California Poppy flowers.

Deterministic: bee jitter and poppy positions are hand-picked constants,
not random.
"""

import sys

from style import BLACK, GOLDEN, SPOT_HEIGHT, SPOT_WIDTH, YELLOW
from lib_svg import (
    circle,
    ellipse,
    group,
    line,
    main_path,
    path,
    polygon,
    rect,
    render,
    svg_close,
    svg_open,
)


def bee(cx: float, cy: float, scale: float, tilt: float = 0) -> list[str]:
    s = scale
    elems: list[str] = []
    # Body: head + 4 sections, drawn as 5 stacked ellipses, alternating
    # black / golden / black / golden / black (head + 4 sections).
    body_colors = [BLACK, GOLDEN, BLACK, GOLDEN, BLACK]
    section_w = 28 * s
    section_h = 36 * s
    # Lay body along x-axis from head (right) to tail (left).
    for i, color in enumerate(body_colors):
        ex = (i - 2) * (section_w * 0.85)
        elems.append(
            ellipse(ex, 0, section_w / 2, section_h / 2,
                    fill=color, stroke=BLACK, sw=1.5)
        )
    # Wings: two lobes, outline only.
    for sign in (-1, 1):
        wx = -10 * s
        wy = -22 * s * (1 if sign < 0 else 1)
        elems.append(
            ellipse(wx, -28 * s, 38 * s, 18 * s,
                    fill="#ffffff", stroke=BLACK, sw=1.5)
        )
        # vein
        elems.append(
            line(wx - 28 * s, -28 * s, wx + 28 * s, -28 * s,
                 stroke=BLACK, sw=1)
        )
        break  # two wings overlap; draw second offset
    elems.append(
        ellipse(-2 * s, -32 * s, 34 * s, 16 * s,
                fill="#ffffff", stroke=BLACK, sw=1.5)
    )
    elems.append(
        line(-30 * s, -32 * s, 26 * s, -32 * s, stroke=BLACK, sw=1)
    )
    # Legs: 2 short lines under the body
    for dx in (-18 * s, 4 * s):
        elems.append(
            line(dx, 18 * s, dx + 6 * s, 30 * s, stroke=BLACK, sw=1.5)
        )
    # Antennae: 2 thin curves from head (rightmost ellipse).
    head_x = 2 * (section_w * 0.85)
    for ay in (-4 * s, 4 * s):
        elems.append(
            path(
                f"M{head_x},{ay} Q{head_x + 18 * s},{ay - 14 * s} "
                f"{head_x + 26 * s},{ay - 22 * s}",
                stroke=BLACK, sw=1.2,
            )
        )
        # antenna tip
        elems.append(
            circle(head_x + 26 * s, ay - 22 * s, 2.2 * s, fill=BLACK,
                   stroke=BLACK, sw=0.5)
        )
    return [group(elems, transform=f"translate({cx},{cy}) rotate({tilt})")]


def poppy_cluster(cx: float, cy: float, scale: float = 1.0) -> list[str]:
    """A small cluster of 3 California poppies on stems."""
    s = scale
    elems: list[str] = []
    # Stems
    for dx, h in ((-22, 80), (0, 100), (24, 70)):
        elems.append(
            line(cx + dx * s, cy, cx + dx * s, cy - h * s,
                 stroke=BLACK, sw=1.5)
        )
        # Single leaf
        elems.append(
            path(
                f"M{cx + dx * s},{cy - h * s * 0.55} "
                f"q{8 * s},{-4 * s} {16 * s},{-2 * s} "
                f"q{-8 * s},{6 * s} {-16 * s},{2 * s} z",
                fill=YELLOW, stroke=BLACK, sw=1,
            )
        )
    # Flower heads: 4 petals each, simple lobes.
    for dx, h in ((-22, 80), (0, 100), (24, 70)):
        head_x = cx + dx * s
        head_y = cy - h * s
        for ang in (0, 90, 180, 270):
            import math
            rad = math.radians(ang)
            px = head_x + math.cos(rad) * 8 * s
            py = head_y + math.sin(rad) * 8 * s
            elems.append(
                ellipse(px, py, 11 * s, 6 * s, fill=GOLDEN, stroke=BLACK,
                        sw=1)
            )
        elems.append(
            circle(head_x, head_y, 4 * s, fill=BLACK, stroke=BLACK, sw=1)
        )
    return elems


def build() -> list[str]:
    W, H = SPOT_WIDTH, SPOT_HEIGHT
    elements = svg_open(W, H)

    # Ground line, two thirds down.
    ground = H * 0.78
    elements.append(line(40, ground, W - 40, ground, stroke=BLACK, sw=2))
    # Indistinct ground cover: scattered short ticks.
    cover_x = [80, 140, 210, 280, 360, 450, 540, 640, 760, 880, 1000,
               1100, 1190, 1280, 1340]
    for x in cover_x:
        elements.append(line(x, ground + 4, x + 14, ground + 4,
                             stroke=BLACK, sw=1))
        elements.append(line(x + 6, ground + 4, x + 6, ground + 14,
                             stroke=BLACK, sw=1))

    # Four poppy clusters distributed along the ground.
    for cx, scl in ((220, 1.05), (560, 0.95), (920, 1.0), (1240, 0.9)):
        elements.extend(poppy_cluster(cx, ground - 2, scale=scl))

    # Three bees in the upper half, +/- 5% scale, slight tilt variation.
    bee_specs = (
        (380, 280, 1.05, -8),
        (760, 200, 1.00, 4),
        (1140, 320, 0.95, -3),
    )
    for cx, cy, scl, tilt in bee_specs:
        elements.extend(bee(cx, cy, scl, tilt))

    elements.append(svg_close())
    return elements


if __name__ == "__main__":
    render(build(), main_path())
