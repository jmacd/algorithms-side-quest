"""Spot for "Art and Science": a painter on a ladder sketching lines
on a wall.

Composition per the essay (§ "Spot illustrations"):
  painter on a ladder with art materials sketching lines on the wall.

The wall on the right shows a partial grid of lines being installed
following a written specification — a LeWitt-style wall-drawing in
progress.  Paint cans sit at the foot of the ladder.

Deterministic: all positions are pinned constants.
"""

from style import BLACK, GOLDEN, INK_FAINT, SPOT_HEIGHT, SPOT_WIDTH, YELLOW
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


def build() -> list[str]:
    W, H = SPOT_WIDTH, SPOT_HEIGHT
    elements = svg_open(W, H)

    floor_y = H - 60

    # ---- Wall on the right ------------------------------------------------
    wall_x, wall_y, wall_w, wall_h = 540, 80, 760, 600
    elements.append(
        rect(wall_x, wall_y, wall_w, wall_h, fill="#ffffff",
             stroke=BLACK, sw=3)
    )
    # Finished portion: dense parallel diagonals in the upper-left half.
    finished_clip_x2 = wall_x + 440
    finished_clip_y2 = wall_y + 360
    # Draw diagonals at 45° (top-right going to bottom-left direction).
    spacing = 28
    # Diagonals: parametrized as y = -x + c.  c ranges so lines fall
    # within the finished region.
    cs = [wall_x + i * spacing for i in range(-6, 22)]
    for c in cs:
        # Clip to rect [wall_x, wall_y] - [finished_clip_x2, finished_clip_y2]
        # Compute intersections of line y - wall_y = -(x - c) (i.e. y = -x + c + wall_y)
        # with the rectangle.
        # Using simpler parametrisation: line from (c, wall_y) going down-right
        # at 45°, i.e. (c + t, wall_y + t).
        # Range of t such that point stays in finished rect:
        t_min = max(0, wall_x - c)
        t_max_x = finished_clip_x2 - c
        t_max_y = finished_clip_y2 - wall_y
        t_max = min(t_max_x, t_max_y)
        if t_max <= t_min:
            continue
        x1, y1 = c + t_min, wall_y + t_min
        x2, y2 = c + t_max, wall_y + t_max
        elements.append(line(x1, y1, x2, y2, stroke=BLACK, sw=1.6))

    # In-progress portion: a few faint guide ticks in the bottom-right
    # half of the wall, indicating where the next lines will go.
    for i in range(8):
        gx = wall_x + 460 + i * 36
        gy = wall_y + 380 + (i % 2) * 6
        elements.append(line(gx, gy, gx + 10, gy + 10,
                             stroke=INK_FAINT, sw=1.2, dash="4,4"))

    # ---- Ladder -----------------------------------------------------------
    ladder_top_x = 280
    ladder_top_y = 140
    ladder_bot_x = 220
    ladder_bot_y = floor_y
    rail_offset = 36
    # Two rails (slightly angled, foot wider than top).
    left_top = (ladder_top_x - rail_offset, ladder_top_y)
    left_bot = (ladder_bot_x - rail_offset - 10, ladder_bot_y)
    right_top = (ladder_top_x + rail_offset, ladder_top_y)
    right_bot = (ladder_bot_x + rail_offset + 10, ladder_bot_y)
    elements.append(line(*left_top, *left_bot, stroke=BLACK, sw=5))
    elements.append(line(*right_top, *right_bot, stroke=BLACK, sw=5))
    # Rungs.
    n_rungs = 6
    for i in range(1, n_rungs + 1):
        t = i / (n_rungs + 1)
        lx = left_top[0] + t * (left_bot[0] - left_top[0])
        ly = left_top[1] + t * (left_bot[1] - left_top[1])
        rx = right_top[0] + t * (right_bot[0] - right_top[0])
        ry = right_top[1] + t * (right_bot[1] - right_top[1])
        elements.append(line(lx, ly, rx, ry, stroke=BLACK, sw=4))

    # ---- Painter standing on the second rung from the top -----------------
    stand_t = 2 / (n_rungs + 1)
    stand_x = ladder_top_x + stand_t * (ladder_bot_x - ladder_top_x) + 10
    stand_y = ladder_top_y + stand_t * (ladder_bot_y - ladder_top_y)

    # Body (yellow torso polygon).
    body_top = stand_y - 180
    elements.append(
        polygon(
            [
                (stand_x - 36, body_top),
                (stand_x + 36, body_top),
                (stand_x + 52, stand_y - 4),
                (stand_x - 52, stand_y - 4),
            ],
            fill=YELLOW, stroke=BLACK, sw=2.5,
        )
    )
    # Legs.
    elements.append(line(stand_x - 22, stand_y - 4, stand_x - 18, stand_y + 18,
                         stroke=BLACK, sw=5))
    elements.append(line(stand_x + 22, stand_y - 4, stand_x + 18, stand_y + 18,
                         stroke=BLACK, sw=5))
    # Head.
    head_cx, head_cy, head_r = stand_x, body_top - 50, 44
    elements.append(circle(head_cx, head_cy, head_r, fill=YELLOW,
                           stroke=BLACK, sw=2.5))
    # Eyes (looking right toward wall).
    elements.append(circle(head_cx + 10, head_cy - 4, 3.5, fill=BLACK,
                           stroke=BLACK, sw=1))
    elements.append(circle(head_cx + 22, head_cy - 4, 3.5, fill=BLACK,
                           stroke=BLACK, sw=1))
    # Mouth.
    elements.append(path(f"M{head_cx + 4},{head_cy + 16} q12,8 24,0",
                         stroke=BLACK, sw=2))
    # Beret-ish cap on top of head.
    elements.append(
        path(
            f"M{head_cx - head_r + 6},{head_cy - head_r + 10} "
            f"Q{head_cx},{head_cy - head_r - 30} "
            f"{head_cx + head_r - 6},{head_cy - head_r + 10} "
            f"L{head_cx + head_r - 14},{head_cy - head_r + 18} "
            f"L{head_cx - head_r + 14},{head_cy - head_r + 18} Z",
            fill=BLACK, stroke=BLACK, sw=1.5,
        )
    )

    # ---- Right arm extended toward wall with a brush ----------------------
    sh_x, sh_y = stand_x + 32, body_top + 20      # shoulder
    elbow_x, elbow_y = stand_x + 130, body_top + 6
    hand_x, hand_y = wall_x - 30, body_top - 10
    elements.append(line(sh_x, sh_y, elbow_x, elbow_y, stroke=BLACK, sw=5))
    elements.append(line(elbow_x, elbow_y, hand_x, hand_y, stroke=BLACK, sw=5))
    elements.append(circle(hand_x, hand_y, 8, fill=YELLOW, stroke=BLACK, sw=2))
    # Brush: shaft from hand into the wall, golden tip.
    brush_tip_x = wall_x + 16
    brush_tip_y = hand_y - 4
    elements.append(line(hand_x + 4, hand_y - 2, brush_tip_x, brush_tip_y,
                         stroke=BLACK, sw=4))
    elements.append(
        polygon(
            [
                (brush_tip_x, brush_tip_y - 6),
                (brush_tip_x + 18, brush_tip_y),
                (brush_tip_x, brush_tip_y + 6),
            ],
            fill=GOLDEN, stroke=BLACK, sw=1.5,
        )
    )
    # A fresh stroke just laid on the wall, extending the diagonal grid.
    elements.append(
        line(brush_tip_x + 2, brush_tip_y, brush_tip_x + 110,
             brush_tip_y + 110, stroke=BLACK, sw=2.4)
    )

    # ---- Left arm holding a scroll (the "specification") ------------------
    lsh_x, lsh_y = stand_x - 32, body_top + 20
    lhand_x, lhand_y = stand_x - 100, body_top + 80
    elements.append(line(lsh_x, lsh_y, lhand_x, lhand_y, stroke=BLACK, sw=5))
    # Scroll: small rectangle with a couple of horizontal text lines.
    scroll_w, scroll_h = 86, 110
    sx, sy = lhand_x - scroll_w / 2, lhand_y
    elements.append(rect(sx, sy, scroll_w, scroll_h, fill="#ffffff",
                         stroke=BLACK, sw=2))
    for i in range(5):
        ty = sy + 18 + i * 18
        elements.append(line(sx + 10, ty, sx + scroll_w - 10, ty,
                             stroke=INK_FAINT, sw=1.5))
    # Scroll corner curl.
    elements.append(
        path(
            f"M{sx + scroll_w},{sy} "
            f"q-14,2 -18,18 q14,-2 18,-18 z",
            fill="#ffffff", stroke=BLACK, sw=1.5,
        )
    )

    # ---- Floor and paint supplies at the base of the ladder ---------------
    elements.append(line(40, floor_y, W - 40, floor_y, stroke=BLACK, sw=2))
    # Paint can (cylinder) to the left of the ladder.
    can_x, can_y, can_w, can_h = 80, floor_y - 70, 80, 70
    elements.append(rect(can_x, can_y, can_w, can_h, fill=GOLDEN,
                         stroke=BLACK, sw=2.5))
    elements.append(ellipse(can_x + can_w / 2, can_y, can_w / 2, 8,
                            fill=GOLDEN, stroke=BLACK, sw=2.5))
    elements.append(ellipse(can_x + can_w / 2, can_y + can_h, can_w / 2, 8,
                            fill=GOLDEN, stroke=BLACK, sw=2.5))
    # Handle.
    elements.append(
        path(
            f"M{can_x + 6},{can_y + 6} q{can_w / 2 - 6},{-26} "
            f"{can_w - 12},0",
            stroke=BLACK, sw=2,
        )
    )
    # A second smaller can to the right of the ladder.
    can2_x = ladder_bot_x + rail_offset + 80
    can2_y = floor_y - 50
    can2_w, can2_h = 60, 50
    elements.append(rect(can2_x, can2_y, can2_w, can2_h, fill="#ffffff",
                         stroke=BLACK, sw=2.5))
    elements.append(ellipse(can2_x + can2_w / 2, can2_y, can2_w / 2, 6,
                            fill="#ffffff", stroke=BLACK, sw=2.5))
    # Three brushes leaning against can2.
    for i, (bx_off, blen) in enumerate([(48, 110), (60, 130), (72, 100)]):
        bx0 = can2_x + bx_off
        by0 = can2_y + can2_h - 4
        bx1 = bx0 + 28 + i * 4
        by1 = by0 - blen
        elements.append(line(bx0, by0, bx1, by1, stroke=BLACK, sw=3))
        # Tip (golden on first and third, dark on middle).
        tip_color = GOLDEN if i != 1 else BLACK
        elements.append(
            polygon(
                [
                    (bx1 - 6, by1 + 4),
                    (bx1 + 6, by1 - 12),
                    (bx1 + 12, by1 - 2),
                ],
                fill=tip_color, stroke=BLACK, sw=1.2,
            )
        )

    elements.append(svg_close())
    return elements


if __name__ == "__main__":
    render(build(), main_path())
