"""LeWitt-style wall-drawing homage for the "Conceptual art" slide.

This is not a copy of any specific LeWitt work; it is an original
illustration *generated from a specification* — itself an instance of
the idea Sol LeWitt's wall drawings articulated.

Specification (rendered by this file):
  A square wall framed in black.  Inside the frame, draw seven nested
  cat outlines, smallest at the center and largest filling the frame.
  Color each outline by a rainbow rule:
    outermost = red, then orange, amber/yellow, green, blue, indigo,
    innermost = violet.
  All outlines share the same stroke width.
"""

from style import BLACK, GOLDEN, SPOT_HEIGHT, SPOT_WIDTH, WHITE
from lib_svg import (
    main_path,
    rect,
    render,
    svg_close,
    svg_open,
    text,
)


CAT_COLORS = [
    "#6a1b9a",  # violet  (innermost)
    "#3949ab",  # indigo
    "#1e88e5",  # blue
    "#43a047",  # green
    "#f9a825",  # amber/yellow
    "#fb8c00",  # orange
    "#e53935",  # red     (outermost)
]
N_CATS = len(CAT_COLORS)

# Cat-head silhouette: a circular head with two triangular ears.
# Constructed as one closed path so a single stroke draws the outline.
# Head: circle of radius 1 around (0, 0.275); ear tips reach y = -1.275.
# Ear base points sit on the head circle at +5° (inside) and +45°
# (outside) off the 12-o'clock vertical, giving the wide-base / steep-
# outside-edge look of a typical cat ear.
# Centered on its own bounding-box centroid at (0, 0), so concentric
# scaling produces visually-concentric nested cats.
# Bounding box: x in [-1, 1], y in [-1.275, 1.275].
CAT_PATH_D = (
    "M 1 0.275 "
    "A 1 1 0 1 1 -1 0.275 "        # bottom half of head (major arc, sweep CW)
    "A 1 1 0 0 1 -0.707 -0.432 "   # left side up to outside base of left ear
    "L -0.85 -1.275 "              # left ear tip
    "L -0.087 -0.721 "             # left ear inside base
    "A 1 1 0 0 1 0.087 -0.721 "    # short arc across top of head between ears
    "L 0.85 -1.275 "               # right ear tip
    "L 0.707 -0.432 "              # right ear outside base
    "A 1 1 0 0 1 1 0.275 "         # right side back down to start
    "Z"
)

CAT_W = 2.0
CAT_H = 2.55


def _cat(cx: float, cy: float, scale: float, color: str) -> str:
    return (
        f'<g transform="translate({cx},{cy}) scale({scale})">'
        f'<path d="{CAT_PATH_D}" fill="none" stroke="{color}" '
        f'stroke-width="3" stroke-linecap="round" stroke-linejoin="round" '
        f'vector-effect="non-scaling-stroke"/>'
        f'</g>'
    )


def build() -> list[str]:
    W, H = SPOT_WIDTH, SPOT_HEIGHT
    elements = svg_open(W, H)

    # The "wall": a square frame centered horizontally, nudged up to
    # leave a gold-caption line beneath.
    frame = 720
    fx = (W - frame) / 2
    fy = (H - frame) / 2 - 8

    elements.append(
        rect(fx, fy, frame, frame, fill=WHITE, stroke=BLACK, sw=3)
    )

    # Largest cat fills the frame with a small inner padding.
    pad = 18
    s_max = min((frame - 2 * pad) / CAT_W, (frame - 2 * pad) / CAT_H)

    cx = fx + frame / 2
    cy = fy + frame / 2

    # Draw outermost first so each smaller cat lays on top.  (The
    # outlines don't intersect when nested cleanly, but this keeps
    # the layering deterministic.)
    for i in range(N_CATS - 1, -1, -1):
        scale = s_max * (i + 1) / N_CATS
        elements.append(_cat(cx, cy, scale, CAT_COLORS[i]))

    # Caption in the LeWitt voice, just below the frame.
    elements.append(
        text(
            W / 2,
            fy + frame + 38,
            "Wall Drawing  ·  nested cat outlines  ·  red outside → violet inside",
            size=22,
            font="mono",
            anchor="middle",
            fill=GOLDEN,
        )
    )

    elements.append(svg_close())
    return elements


if __name__ == "__main__":
    render(build(), main_path())
