"""Fort Bragg, CA street map with an *approximate* house-counting route.

Per the essay (§ "Count the houses in town"):

> Show a street map of Fort Bragg, CA.  Pull data from OpenStreetMap for
> Fort Bragg, CA and render the image (from leaflet, maybe) with some
> approximate path tracing through all the north-south streets in
> westward sequence then all the east-west streets in northward
> sequence, then render the image with real map and traced route.

We honour the AGENTS.md "stdlib only" and "no remote assets at build
time" rules by checking in a snapshot of the OSM data at
``diagram/static/fort-bragg-streets.json`` and re-projecting it here.
The snapshot was fetched once via the Overpass API; the query, bbox,
and source attribution travel with the file.

Two layers:

1. **Real map** — actual OSM ways for residential, tertiary, and
   primary roads, clipped to the bbox.  Main Street / Highway 1 is
   rendered thicker in black as a landmark.
2. **Approximate route** — *very* approximate.  We don't trace every
   real street; we lay a clean lawnmower scan over the central
   residential grid: a handful of evenly-spaced vertical sweeps east
   → west (phase 1), then evenly-spaced horizontal sweeps south →
   north (phase 2).  The point is the *shape* of the algorithm —
   "walk every street, count every house" — not a faithful tour.
"""

from __future__ import annotations

import json
import math
import os

from style import BLACK, GOLDEN, HEIGHT, INK_MID, WIDTH
from lib_svg import (
    circle,
    main_path,
    path,
    render,
    svg_close,
    svg_open,
    text,
)

DATA_PATH = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "static",
    "fort-bragg-streets.json",
)

# A tight box around the regular residential grid (Fir St / Pudding
# Creek inland, between the coast bluff and Main / Hwy 1, then a few
# blocks east of Main).  This is where the "count the houses" lawnmower
# scan lives.  The full data bbox is wider so background context (Old
# Haul Rd, Pudding Creek Rd, the eastern subdivisions) still draws.
ROUTE_BBOX = {
    "south": 39.4385,
    "north": 39.4515,
    "west":  -123.8090,
    "east":  -123.7960,
}

# Lawnmower density: a small number of lines so the scan reads as a
# clean pattern rather than a smear.  Counts are chosen so start (NE
# corner) and end (NW corner) sit on different corners of the route
# bbox: 9 verticals (odd → phase 1 ends at SW), then 8 horizontals
# (even, starting W→E so phase 2 starts at SW and ends at NW).
N_VERTICAL = 9
N_HORIZONTAL = 8


def _load() -> dict:
    with open(DATA_PATH, encoding="utf-8") as f:
        return json.load(f)


def _projector(bbox: dict, mx: float, my: float, mw: float, mh: float):
    """Return a (lat, lon) → (svg_x, svg_y) function with preserved aspect."""
    lat0 = (bbox["south"] + bbox["north"]) / 2.0
    coslat = math.cos(math.radians(lat0))
    m_per_deg_lat = 111_000.0
    m_per_deg_lon = 111_000.0 * coslat
    geo_w_m = (bbox["east"] - bbox["west"]) * m_per_deg_lon
    geo_h_m = (bbox["north"] - bbox["south"]) * m_per_deg_lat
    scale = min(mw / geo_w_m, mh / geo_h_m)
    used_w = geo_w_m * scale
    used_h = geo_h_m * scale
    off_x = mx + (mw - used_w) / 2.0
    off_y = my + (mh - used_h) / 2.0

    def proj(lat: float, lon: float) -> tuple[float, float]:
        x_m = (lon - bbox["west"]) * m_per_deg_lon
        y_m = (bbox["north"] - lat) * m_per_deg_lat
        return (off_x + x_m * scale, off_y + y_m * scale)

    return proj


def _polyline_d(points: list[tuple[float, float]]) -> str:
    return "M " + " L ".join(f"{x:.1f},{y:.1f}" for x, y in points)


def _clip_polyline(geom: list[list[float]], bbox: dict) -> list[list[list[float]]]:
    """Liang-Barsky clip of a polyline against the bbox.  Returns a list of
    sub-polylines; a single way that exits and re-enters the bbox yields
    more than one sub-polyline."""
    s, w, n, e = bbox["south"], bbox["west"], bbox["north"], bbox["east"]
    subs: list[list[list[float]]] = []
    current: list[list[float]] = []
    for i in range(len(geom) - 1):
        lat1, lon1 = geom[i]
        lat2, lon2 = geom[i + 1]
        x1, y1, x2, y2 = lon1, lat1, lon2, lat2
        dx, dy = x2 - x1, y2 - y1
        p_arr = [-dx, dx, -dy, dy]
        q_arr = [x1 - w, e - x1, y1 - s, n - y1]
        u1, u2 = 0.0, 1.0
        out = False
        for p, q in zip(p_arr, q_arr):
            if p == 0:
                if q < 0:
                    out = True
                    break
            else:
                t = q / p
                if p < 0:
                    if t > u2:
                        out = True
                        break
                    if t > u1:
                        u1 = t
                else:
                    if t < u1:
                        out = True
                        break
                    if t < u2:
                        u2 = t
        if out:
            if current:
                subs.append(current)
                current = []
            continue
        cp1 = [y1 + u1 * dy, x1 + u1 * dx]
        cp2 = [y1 + u2 * dy, x1 + u2 * dx]
        if not current:
            current.append(cp1)
        elif u1 > 0:
            subs.append(current)
            current = [cp1]
        current.append(cp2)
        if u2 < 1:
            subs.append(current)
            current = []
    if current:
        subs.append(current)
    return [s for s in subs if len(s) >= 2]


def _route_path(d: str, sw: float, dash: str | None = None) -> str:
    extra = f' stroke-dasharray="{dash}"' if dash else ""
    return (
        f'<path d="{d}" stroke="{GOLDEN}" fill="none" stroke-width="{sw}" '
        f'stroke-linecap="round" stroke-linejoin="round" '
        f'stroke-opacity="0.9"{extra}/>'
    )


def _arrow_triangle(cx: float, cy: float, dx: float, dy: float,
                    size: float = 16.0) -> str:
    """Filled triangle of `size` long, centred at (cx,cy), pointing along
    (dx,dy)."""
    mag = math.hypot(dx, dy)
    if mag == 0:
        return ""
    ux, uy = dx / mag, dy / mag
    px, py = -uy, ux
    half_h = size * 0.5
    half_w = size * 0.55
    tip = (cx + ux * half_h, cy + uy * half_h)
    b1 = (cx - ux * half_h + px * half_w, cy - uy * half_h + py * half_w)
    b2 = (cx - ux * half_h - px * half_w, cy - uy * half_h - py * half_w)
    return (f'<path d="M {tip[0]:.1f},{tip[1]:.1f} '
            f'L {b1[0]:.1f},{b1[1]:.1f} L {b2[0]:.1f},{b2[1]:.1f} Z" '
            f'fill="{GOLDEN}" stroke="{BLACK}" stroke-width="1.5"/>')


def _trim_end(a: tuple[float, float], b: tuple[float, float],
              amount: float) -> tuple[float, float]:
    """Move point `b` back toward `a` by `amount` pixels along the segment."""
    dx, dy = b[0] - a[0], b[1] - a[1]
    mag = math.hypot(dx, dy)
    if mag <= amount:
        return b
    ux, uy = dx / mag, dy / mag
    return (b[0] - ux * amount, b[1] - uy * amount)


def _trim_start(a: tuple[float, float], b: tuple[float, float],
                amount: float) -> tuple[float, float]:
    """Move point `a` forward toward `b` by `amount` pixels along the segment."""
    dx, dy = b[0] - a[0], b[1] - a[1]
    mag = math.hypot(dx, dy)
    if mag <= amount:
        return a
    ux, uy = dx / mag, dy / mag
    return (a[0] + ux * amount, a[1] + uy * amount)


def _build_route_d(sweeps_p1: list, sweeps_p2: list,
                   bulge_v: float, bulge_h: float,
                   corner_r: float) -> tuple[str, list]:
    """Build the SVG d= string for the lawnmower route and return the list
    of (a, b, orientation) sweep segments actually drawn (with corner
    trimming applied), so arrows can be placed at their midpoints."""
    sweeps: list[tuple[tuple[float, float], tuple[float, float], str]] = []
    # Trim the last phase-1 sweep so a smooth quarter-circle corner can
    # join it to the (likewise trimmed) first phase-2 sweep.
    for i, (a, b) in enumerate(sweeps_p1):
        if i == len(sweeps_p1) - 1:
            b = _trim_end(a, b, corner_r)
        sweeps.append((a, b, "v"))
    for i, (a, b) in enumerate(sweeps_p2):
        if i == 0:
            a = _trim_start(a, b, corner_r)
        sweeps.append((a, b, "h"))

    parts: list[str] = []
    a0, b0, _ = sweeps[0]
    parts.append(f"M {a0[0]:.1f},{a0[1]:.1f}")
    parts.append(f"L {b0[0]:.1f},{b0[1]:.1f}")
    for i in range(1, len(sweeps)):
        prev_a, prev_b, prev_o = sweeps[i - 1]
        a, b, curr_o = sweeps[i]
        if prev_o == curr_o == "v":
            # 180° U-turn: bulge in the direction the prev sweep was moving.
            sgn = 1.0 if (prev_b[1] - prev_a[1]) > 0 else -1.0
            c1 = (prev_b[0], prev_b[1] + sgn * bulge_v)
            c2 = (a[0], a[1] + sgn * bulge_v)
        elif prev_o == curr_o == "h":
            sgn = 1.0 if (prev_b[0] - prev_a[0]) > 0 else -1.0
            c1 = (prev_b[0] + sgn * bulge_h, prev_b[1])
            c2 = (a[0] + sgn * bulge_h, a[1])
        else:
            # 90° corner (phase change): cubic with both control points at
            # the would-be corner — gives a smooth quarter-bend.
            if prev_o == "v":
                corner = (prev_b[0], a[1])
            else:
                corner = (a[0], prev_b[1])
            c1 = corner
            c2 = corner
        parts.append(
            f"C {c1[0]:.1f},{c1[1]:.1f} {c2[0]:.1f},{c2[1]:.1f} "
            f"{a[0]:.1f},{a[1]:.1f}"
        )
        parts.append(f"L {b[0]:.1f},{b[1]:.1f}")
    return " ".join(parts), sweeps


def build() -> list[str]:
    data = _load()
    bbox = data["bbox"]
    ways = data["ways"]

    TOP, BOTTOM = 80, 90
    PADX = 60
    mx, my = PADX, TOP
    mw, mh = WIDTH - 2 * PADX, HEIGHT - TOP - BOTTOM
    proj = _projector(bbox, mx, my, mw, mh)

    elements = svg_open(WIDTH, HEIGHT)

    # --- Background street network (clipped to map bbox) -----------------
    def draw_clipped(w, stroke, sw):
        for sub in _clip_polyline(w["geometry"], bbox):
            pts = [proj(lat, lon) for lat, lon in sub]
            if len(pts) >= 2:
                elements.append(path(_polyline_d(pts), stroke=stroke, sw=sw))

    for w in ways:
        if w["highway"] != "primary":
            draw_clipped(w, INK_MID, 2.0)
    for w in ways:
        if w["highway"] == "primary":
            draw_clipped(w, BLACK, 5.0)

    # --- Approximate lawnmower route over the residential grid ----------
    rb = ROUTE_BBOX

    # Phase 1: vertical sweeps from east → west.  Each sweep is a
    # (start_point, end_point) pair in SVG coords; we alternate direction
    # so consecutive sweeps connect at the near endpoint.
    sweeps_p1: list[tuple[tuple[float, float], tuple[float, float]]] = []
    for i in range(N_VERTICAL):
        t = i / (N_VERTICAL - 1)
        lon = rb["east"] + t * (rb["west"] - rb["east"])
        if i % 2 == 0:
            sweeps_p1.append((proj(rb["north"], lon), proj(rb["south"], lon)))
        else:
            sweeps_p1.append((proj(rb["south"], lon), proj(rb["north"], lon)))

    # Phase 2: horizontal sweeps from south → north.
    sweeps_p2: list[tuple[tuple[float, float], tuple[float, float]]] = []
    for i in range(N_HORIZONTAL):
        t = i / (N_HORIZONTAL - 1)
        lat = rb["south"] + t * (rb["north"] - rb["south"])
        if i % 2 == 0:
            sweeps_p2.append((proj(lat, rb["west"]), proj(lat, rb["east"])))
        else:
            sweeps_p2.append((proj(lat, rb["east"]), proj(lat, rb["west"])))

    # Bulge sizes are derived from the actual projected sweep spacing so
    # the U-turns read as half-circles regardless of the map's pixel
    # scale.  0.55 ≈ cubic-Bezier control offset for a half-circle.
    spacing_v_px = abs(sweeps_p1[1][0][0] - sweeps_p1[0][0][0])
    spacing_h_px = abs(sweeps_p2[1][0][1] - sweeps_p2[0][0][1])
    bulge_v = spacing_v_px * 0.55
    bulge_h = spacing_h_px * 0.55
    corner_r = min(bulge_v, bulge_h) * 0.6

    route_d, drawn_sweeps = _build_route_d(
        sweeps_p1, sweeps_p2, bulge_v, bulge_h, corner_r,
    )
    elements.append(_route_path(route_d, sw=4.0))

    # Direction arrows: one per straight sweep, placed at 40 % along the
    # sweep (toward the start) so alternating sweeps put arrows on
    # opposite sides of the midline rather than all clustering in a row
    # at dead centre.
    for a, b, _ in drawn_sweeps:
        t = 0.4
        cx = a[0] + t * (b[0] - a[0])
        cy = a[1] + t * (b[1] - a[1])
        elements.append(
            _arrow_triangle(cx, cy, b[0] - a[0], b[1] - a[1], size=18.0)
        )

    # Start / end markers.
    sx, sy = sweeps_p1[0][0]
    elements.append(circle(sx, sy, 13, fill=GOLDEN, stroke=BLACK, sw=2.5))
    elements.append(text(sx + 20, sy + 8, "start", size=26, weight="bold"))
    ex, ey = sweeps_p2[-1][1]
    elements.append(circle(ex, ey, 13, fill=BLACK, stroke=BLACK, sw=2.5))
    elements.append(text(ex - 20, ey + 8, "end", size=26, weight="bold",
                         anchor="end"))

    # --- Highway 1 label (Main Street) -----------------------------------
    main_ways = [w for w in ways if w["highway"] == "primary"]
    if main_ways:
        all_main_pts: list[list[float]] = []
        for w in main_ways:
            for sub in _clip_polyline(w["geometry"], bbox):
                all_main_pts.extend(sub)
        if all_main_pts:
            # Place the label on a quiet southern stretch of Main St,
            # well clear of the title and the route's start corner.
            south_pt = min(all_main_pts, key=lambda p: p[0])
            tx, ty = proj(south_pt[0], south_pt[1])
            elements.append(text(tx + 14, ty - 14, "Hwy 1 / Main St",
                                 size=22, font="mono", fill=BLACK))

    # --- North arrow (top-left, inside the map area) ---------------------
    nax, nay = mx + 30, my + 70
    elements.append(path(
        f"M {nax},{nay} L {nax},{nay - 44} L {nax - 9},{nay - 32} "
        f"M {nax},{nay - 44} L {nax + 9},{nay - 32}",
        stroke=BLACK, sw=2.2,
    ))
    elements.append(text(nax + 16, nay - 22, "N", size=22, weight="bold"))

    # --- Title and credit -------------------------------------------------
    elements.append(text(
        WIDTH / 2, 50,
        "Fort Bragg, CA — N-S sweeps westward, then E-W sweeps northward",
        size=30, anchor="middle",
    ))
    elements.append(text(
        WIDTH / 2, HEIGHT - 30,
        "street data: © OpenStreetMap contributors (ODbL) · "
        "route is illustrative, not literal",
        size=20, anchor="middle", style="italic", fill=INK_MID,
    ))

    elements.append(svg_close())
    return elements


if __name__ == "__main__":
    render(build(), main_path())
