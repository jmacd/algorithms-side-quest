"""Illustration for the "About the title" slide.

Composition per the essay (§ "Art and Science"):
  a 3D rendering setup with a camera, angle of view and view frustum
  framing a penguin riding a bicycle on a perspective floor inside
  the frustum, plus one of the bees from the title slide.

The axonometric floor grid is the strongest 3D cue: the camera-frustum
side view is otherwise flat, and the explicit X/Z grid receding from
the front of the scene to the back tells the viewer the camera is
looking into a real volume, not at a 2D drawing.

Stdlib-only; deterministic.  The bee body is a simplified version of
the bee in `gen_spot_bees.py` so the family resemblance with the title
slide reads clearly.
"""

import math

from style import (
    BLACK,
    GOLDEN,
    INK_FAINT,
    INK_MID,
    SPOT_HEIGHT,
    SPOT_WIDTH,
    WHITE,
    YELLOW,
)
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
    text,
)


# ---------------------------------------------------------------------------
# Subject: bee (decorative, carried over from the title slide).
# ---------------------------------------------------------------------------

def _bee(cx: float, cy: float, scale: float, tilt: float = 0) -> list[str]:
    s = scale
    elems: list[str] = []
    body_colors = [BLACK, GOLDEN, BLACK, GOLDEN, BLACK]
    section_w = 28 * s
    section_h = 36 * s
    for i, color in enumerate(body_colors):
        ex = (i - 2) * (section_w * 0.85)
        elems.append(
            ellipse(ex, 0, section_w / 2, section_h / 2,
                    fill=color, stroke=BLACK, sw=1.5)
        )
    elems.append(
        ellipse(-10 * s, -28 * s, 38 * s, 18 * s,
                fill="#ffffff", stroke=BLACK, sw=1.5)
    )
    elems.append(line(-38 * s, -28 * s, 18 * s, -28 * s,
                      stroke=BLACK, sw=1))
    elems.append(
        ellipse(-2 * s, -32 * s, 34 * s, 16 * s,
                fill="#ffffff", stroke=BLACK, sw=1.5)
    )
    elems.append(line(-30 * s, -32 * s, 26 * s, -32 * s,
                      stroke=BLACK, sw=1))
    for dx in (-18 * s, 4 * s):
        elems.append(line(dx, 18 * s, dx + 6 * s, 30 * s,
                          stroke=BLACK, sw=1.5))
    head_x = 2 * (section_w * 0.85)
    for ay in (-4 * s, 4 * s):
        elems.append(
            path(
                f"M{head_x},{ay} Q{head_x + 18 * s},{ay - 14 * s} "
                f"{head_x + 26 * s},{ay - 22 * s}",
                stroke=BLACK, sw=1.2,
            )
        )
        elems.append(
            circle(head_x + 26 * s, ay - 22 * s, 2.2 * s,
                   fill=BLACK, stroke=BLACK, sw=0.5)
        )
    return [group(elems, transform=f"translate({cx},{cy}) rotate({tilt})")]


# ---------------------------------------------------------------------------
# Subject: penguin riding a bicycle (side view, facing right).
# Bike origin (0, 0) is the front-wheel ground-contact point projected
# onto the floor — i.e. wheel-bottoms touch y = 0 exactly.
# ---------------------------------------------------------------------------

WHEEL_R = 26
REAR_HUB = (-60, -WHEEL_R)
FRONT_HUB = (60, -WHEEL_R)
CRANK = (0, -WHEEL_R)
SEAT_TOP = (-30, -78)
HEAD_TOP = (35, -82)


def _bike(ox: float, oy: float) -> list[str]:
    elems: list[str] = []

    def L(p):
        return (ox + p[0], oy + p[1])

    # Wheels.
    for hub in (REAR_HUB, FRONT_HUB):
        cx, cy = L(hub)
        elems.append(circle(cx, cy, WHEEL_R, fill=WHITE, stroke=BLACK, sw=3))
        # Spokes (8 evenly spaced).
        for i in range(8):
            ang = i * math.pi / 4 + math.pi / 16
            sx = cx + (WHEEL_R - 1) * math.cos(ang)
            sy = cy + (WHEEL_R - 1) * math.sin(ang)
            elems.append(line(cx, cy, sx, sy, stroke=BLACK, sw=1))
        elems.append(circle(cx, cy, 3, fill=BLACK, stroke=BLACK, sw=1))

    # Frame tubes (diamond shape + chain stay + seat stay + fork).
    tubes = [
        (SEAT_TOP, HEAD_TOP),     # top tube
        (SEAT_TOP, CRANK),        # seat tube
        (HEAD_TOP, CRANK),        # down tube
        (CRANK, REAR_HUB),        # chain stay
        (SEAT_TOP, REAR_HUB),     # seat stay
        (HEAD_TOP, FRONT_HUB),    # fork
    ]
    for a, b in tubes:
        ax, ay = L(a)
        bx, by = L(b)
        elems.append(line(ax, ay, bx, by, stroke=BLACK, sw=3))

    # Seat: short horizontal bar above the seat-tube top.
    sx, sy = L((SEAT_TOP[0] - 2, SEAT_TOP[1] - 3))
    elems.append(ellipse(sx, sy, 14, 4, fill=BLACK, stroke=BLACK, sw=1))

    # Handlebars: vertical stem + horizontal bar above the head tube.
    hx, hy = L(HEAD_TOP)
    elems.append(line(hx, hy, hx + 2, hy - 14, stroke=BLACK, sw=3))
    elems.append(
        line(hx - 8, hy - 14, hx + 16, hy - 14, stroke=BLACK, sw=3)
    )

    return elems


def _penguin(ox: float, oy: float) -> list[str]:
    """Side-view penguin sitting on the bike seat (origin = seat-top center)."""
    elems: list[str] = []

    def L(x, y):
        return (ox + x, oy + y)

    # Body — large vertical oval, black.
    bx, by = L(0, -32)
    elems.append(ellipse(bx, by, 22, 36, fill=BLACK, stroke=BLACK, sw=1.5))

    # White belly — smaller oval offset forward (right) and slightly down.
    wx, wy = L(6, -30)
    elems.append(ellipse(wx, wy, 12, 28, fill=WHITE, stroke="none", sw=0))

    # Head — black oval atop the body, slightly forward.
    hx, hy = L(4, -76)
    elems.append(ellipse(hx, hy, 16, 18, fill=BLACK, stroke=BLACK, sw=1.5))

    # Beak — orange triangle pointing right (the riding direction).
    bkx, bky = L(18, -76)
    elems.append(
        polygon(
            [(bkx, bky - 3), (bkx + 13, bky), (bkx, bky + 3)],
            fill="#fb8c00", stroke=BLACK, sw=1,
        )
    )

    # Eye — small white circle with a black pupil.
    ex, ey = L(9, -80)
    elems.append(circle(ex, ey, 3, fill=WHITE, stroke=BLACK, sw=0.8))
    elems.append(circle(ex + 0.8, ey - 0.3, 1.4,
                        fill=BLACK, stroke=BLACK, sw=0))

    # Forward flipper reaching toward the handlebars.
    fx, fy = L(18, -42)
    elems.append(ellipse(fx, fy, 14, 4, fill=BLACK, stroke=BLACK, sw=1))

    return elems


# ---------------------------------------------------------------------------
# Whole-scene composition.
# ---------------------------------------------------------------------------

def build() -> list[str]:
    W, H = SPOT_WIDTH, SPOT_HEIGHT
    elements = svg_open(W, H)

    # ---- Camera (left) ---------------------------------------------------
    cam_cx, cam_cy = 200, H / 2 - 20
    body_w, body_h = 150, 110
    bx = cam_cx - body_w / 2
    by = cam_cy - body_h / 2
    elements.append(rect(bx, by, body_w, body_h, fill="#ffffff",
                         stroke=BLACK, sw=3, rx=10))
    # Lens cylinder pointing right.
    lens_x = bx + body_w
    elements.append(rect(lens_x, cam_cy - 28, 48, 56, fill="#ffffff",
                         stroke=BLACK, sw=3, rx=4))
    elements.append(circle(lens_x + 48 + 14, cam_cy, 32, fill="#ffffff",
                           stroke=BLACK, sw=3))
    elements.append(circle(lens_x + 48 + 14, cam_cy, 20, fill=INK_FAINT,
                           stroke=BLACK, sw=2))
    elements.append(circle(lens_x + 48 + 14, cam_cy, 8, fill=BLACK,
                           stroke=BLACK, sw=1))
    # Viewfinder bump on top of body.
    elements.append(rect(bx + 20, by - 16, 40, 18, fill="#ffffff",
                         stroke=BLACK, sw=2, rx=3))
    # Tripod underneath.
    cam_bottom = by + body_h
    foot_y = H - 60
    for dx in (-60, 0, 60):
        elements.append(line(cam_cx, cam_bottom + 4, cam_cx + dx, foot_y,
                             stroke=BLACK, sw=4))
    # Floor line.
    elements.append(line(40, foot_y, W - 40, foot_y, stroke=BLACK, sw=2))

    # ---- View frustum ----------------------------------------------------
    apex_x = lens_x + 48 + 14 + 32      # right edge of lens
    apex_y = cam_cy
    far_left = apex_x + 460
    far_top = apex_y - 200
    far_bot = apex_y + 200
    near_left = apex_x + 60
    near_top = apex_y - 36
    near_bot = apex_y + 36
    # Dashed sight lines from the apex out past the far plane.
    elements.append(line(apex_x, apex_y, far_left, far_top,
                         stroke=GOLDEN, sw=2.4, dash="6,6"))
    elements.append(line(apex_x, apex_y, far_left, far_bot,
                         stroke=GOLDEN, sw=2.4, dash="6,6"))
    # Solid frustum edges (near → far on top and bottom).
    elements.append(line(near_left, near_top, far_left, far_top,
                         stroke=BLACK, sw=2.4))
    elements.append(line(near_left, near_bot, far_left, far_bot,
                         stroke=BLACK, sw=2.4))
    # Near and far planes (vertical lines).
    elements.append(line(near_left, near_top, near_left, near_bot,
                         stroke=BLACK, sw=2.4))
    elements.append(line(far_left, far_top, far_left, far_bot,
                         stroke=BLACK, sw=2.4))
    # Angle-of-view arc + label.
    arc_r = 80
    ang_top = math.atan2(far_top - apex_y, far_left - apex_x)
    ang_bot = math.atan2(far_bot - apex_y, far_left - apex_x)
    ax1 = apex_x + arc_r * math.cos(ang_top)
    ay1 = apex_y + arc_r * math.sin(ang_top)
    ax2 = apex_x + arc_r * math.cos(ang_bot)
    ay2 = apex_y + arc_r * math.sin(ang_bot)
    elements.append(
        path(
            f"M{ax1:.2f},{ay1:.2f} A{arc_r},{arc_r} 0 0 1 {ax2:.2f},{ay2:.2f}",
            stroke=GOLDEN, sw=2.4,
        )
    )
    elements.append(
        text(apex_x + arc_r + 8, apex_y + 4, "angle of view",
             size=22, font="sans", anchor="start", fill=GOLDEN)
    )

    # ---- 3D scene floor inside the frustum ------------------------------
    # Axonometric (cabinet) projection of a horizontal plane in the scene:
    #   screen_x = FX + d * DX_DEPTH + w * DX_WIDTH
    #   screen_y = FY + d * DY_DEPTH + w * DY_WIDTH
    # where d ∈ [0,1] is scene depth (front→back into the camera's view)
    # and w ∈ [0,1] is scene width (the axis perpendicular to the camera
    # axis; tilted up-and-slightly-right so we see the floor as a plane).
    # All four corners are kept inside the frustum so the camera really
    # is looking at the scene.
    FX, FY = 510, 432
    DX_DEPTH, DY_DEPTH = 290, 96
    DX_WIDTH, DY_WIDTH = 22, -42

    def floor_xy(d: float, w: float) -> tuple[float, float]:
        return (FX + d * DX_DEPTH + w * DX_WIDTH,
                FY + d * DY_DEPTH + w * DY_WIDTH)

    fc0 = floor_xy(0.0, 0.0)
    fc1 = floor_xy(1.0, 0.0)
    fc2 = floor_xy(1.0, 1.0)
    fc3 = floor_xy(0.0, 1.0)
    elements.append(polygon([fc0, fc1, fc2, fc3], fill="#f7f1e3",
                            stroke=INK_MID, sw=1.6))
    # Grid lines parallel to the front edge (constant scene-depth).
    n_depth = 5
    for i in range(1, n_depth):
        t = i / n_depth
        a = floor_xy(t, 0.0)
        b = floor_xy(t, 1.0)
        elements.append(line(a[0], a[1], b[0], b[1],
                             stroke=INK_FAINT, sw=1))
    # Grid lines parallel to the depth axis (constant scene-width).
    n_width = 5
    for j in range(1, n_width):
        t = j / n_width
        a = floor_xy(0.0, t)
        b = floor_xy(1.0, t)
        elements.append(line(a[0], a[1], b[0], b[1],
                             stroke=INK_FAINT, sw=1))

    # ---- Penguin riding bicycle on the floor -----------------------------
    bike_d = 0.55            # depth fraction (deeper = further from camera)
    bike_w = 0.45            # width fraction (centered on the floor)
    ground_x, ground_y = floor_xy(bike_d, bike_w)

    # Subtle shadow under the bike.
    elements.append(
        ellipse(ground_x, ground_y + 2, 78, 7,
                fill=INK_FAINT, stroke="none", sw=0)
    )

    elements.extend(_bike(ground_x, ground_y))

    # Penguin sits on the seat (seat-top in bike local coords = SEAT_TOP).
    seat_x = ground_x + SEAT_TOP[0]
    seat_y = ground_y + SEAT_TOP[1]
    elements.extend(_penguin(seat_x, seat_y))

    # ---- Bee flying above the scene --------------------------------------
    bee_cx = 740
    bee_cy = 248
    elements.extend(_bee(bee_cx, bee_cy, scale=0.7, tilt=-12))

    # ---- Labels ----------------------------------------------------------
    elements.append(
        text(cam_cx, foot_y + 30, "camera",
             size=24, font="sans", anchor="middle", fill=INK_MID)
    )
    scene_label_x, _ = floor_xy(0.5, 0.5)
    elements.append(
        text(scene_label_x, foot_y + 30, "scene",
             size=24, font="sans", anchor="middle", fill=INK_MID)
    )

    elements.append(svg_close())
    return elements


if __name__ == "__main__":
    render(build(), main_path())
