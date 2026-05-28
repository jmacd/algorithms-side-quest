"""Animated DP-path enumeration for the change-making problem.

Renders a 3-row × 21-column grid for the running example
(total = 20¢, coin set = {1¢, 2¢, 5¢}) and animates a single
highlighted path at a time through all 29 dynamic-programming
solutions.  The caller supplies the coin order (which determines
which denomination labels each row); both coin orderings produce
the same set of (k₁, k₂, k₅) triples in different geometric paths.

The region above and to the left of the grid is rendered with a
light diagonal-stripe pattern (a "thatch") indicating the
no-possibility boundary outside the table.

Animation: SMIL <animate> on per-path opacity, calcMode=discrete,
cycling continuously.  Works in modern browsers when the SVG is
loaded via <img>.
"""

from __future__ import annotations

from style import (
    BLACK,
    GOLDEN,
    INK_FAINT,
    INK_MID,
    WHITE,
    YELLOW,
)
from lib_svg import (
    line,
    rect,
    render,
    svg_close,
    text,
)
from lib_dp_grid import GridGeom, draw_col_labels, draw_grid, draw_row_labels


TOTAL = 20
CYCLE_SECONDS = 22  # 29 paths × ~0.76 s each


def enumerate_paths(coin_order: tuple[int, int, int],
                    total: int = TOTAL) -> list[tuple[int, int, int]]:
    """Every (k0, k1, k2) with c0·k0 + c1·k1 + c2·k2 = total, k ≥ 0.

    Returned sorted by the largest-denomination count first so the
    animation reads as "many big coins → many small coins".
    """
    c0, c1, c2 = coin_order
    paths: list[tuple[int, int, int]] = []
    for k0 in range(total // c0 + 1):
        r0 = total - c0 * k0
        for k1 in range(r0 // c1 + 1):
            r1 = r0 - c1 * k1
            if r1 % c2 == 0:
                paths.append((k0, k1, r1 // c2))
    biggest = max(range(3), key=lambda i: coin_order[i])
    paths.sort(key=lambda t: tuple(-t[i] for i in (biggest,
                                                   *(i for i in range(3)
                                                     if i != biggest))))
    return paths


def _path_points(g: GridGeom,
                 coin_order: tuple[int, int, int],
                 ks: tuple[int, int, int]) -> list[tuple[float, float]]:
    c0, c1, c2 = coin_order
    k0, k1, k2 = ks
    col = 0
    pts: list[tuple[float, float]] = [(g.cx(col), g.cy(0))]
    if k0:
        col += k0 * c0
        pts.append((g.cx(col), g.cy(0)))
    pts.append((g.cx(col), g.cy(1)))
    if k1:
        col += k1 * c1
        pts.append((g.cx(col), g.cy(1)))
    pts.append((g.cx(col), g.cy(2)))
    if k2:
        col += k2 * c2
        pts.append((g.cx(col), g.cy(2)))
    return pts


def _polyline(pts: list[tuple[float, float]]) -> str:
    s = " ".join(f"{x:.1f},{y:.1f}" for x, y in pts)
    return (
        f'<polyline points="{s}" fill="none" stroke="{GOLDEN}" '
        f'stroke-width="7" stroke-linejoin="round" stroke-linecap="round" '
        f'marker-end="url(#arrow-gold)"/>'
    )


def _opacity_animation(idx: int, n: int) -> str:
    """SMIL discrete-mode opacity cycling: 1 during path idx's slot, 0 else."""
    if idx == 0:
        keytimes = f"0;{1 / n:.5f}"
        values = "1;0"
    elif idx == n - 1:
        keytimes = f"0;{idx / n:.5f}"
        values = "0;1"
    else:
        keytimes = f"0;{idx / n:.5f};{(idx + 1) / n:.5f}"
        values = "0;1;0"
    return (
        f'<animate attributeName="opacity" calcMode="discrete" '
        f'values="{values}" keyTimes="{keytimes}" '
        f'dur="{CYCLE_SECONDS}s" repeatCount="indefinite"/>'
    )


def _path_caption(coin_order: tuple[int, int, int],
                  ks: tuple[int, int, int]) -> str:
    parts = []
    for k, c in zip(ks, coin_order):
        if k:
            parts.append(f"{k}\u00d7{c}\u00a2")
    if not parts:
        parts.append("0")
    return "  +  ".join(parts) + f"  =  {TOTAL}\u00a2"


def build(coin_order: tuple[int, int, int]) -> list[str]:
    # Panel canvas: wide and short so two stack neatly on one slide.
    width, height = 1600, 620
    cols = TOTAL + 1
    rows = 3
    cell_w = 64
    cell_h = 110

    grid_w = cols * cell_w
    grid_h = rows * cell_h
    x0 = (width - grid_w) / 2 + 30   # +30 to leave room for row labels
    y0 = 80                          # leaves room for col labels above
    g = GridGeom(x0=x0, y0=y0,
                 cell_w=cell_w, cell_h=cell_h,
                 rows=rows, cols=cols)

    elements: list[str] = []
    elements.append(
        f'<svg xmlns="http://www.w3.org/2000/svg" '
        f'viewBox="0 0 {width} {height}" '
        f'preserveAspectRatio="xMidYMid meet">'
    )
    # Defs: arrow markers + diagonal-stripe thatch pattern for the
    # "no possibility" zone outside the grid.
    elements.append(
        '<defs>'
        '<marker id="arrow-gold" viewBox="0 0 10 10" refX="9" refY="5" '
        'markerWidth="6" markerHeight="6" orient="auto-start-reverse">'
        f'<path d="M0,0 L10,5 L0,10 Z" fill="{GOLDEN}"/>'
        '</marker>'
        '<pattern id="thatch" patternUnits="userSpaceOnUse" '
        'width="14" height="14" patternTransform="rotate(45)">'
        f'<rect width="14" height="14" fill="{WHITE}"/>'
        f'<line x1="0" y1="0" x2="0" y2="14" stroke="{INK_FAINT}" '
        'stroke-width="2"/>'
        '</pattern>'
        '</defs>'
    )
    elements.append(
        f'<rect width="{width}" height="{height}" fill="{WHITE}"/>'
    )

    # Thatch the strip above the grid (between top of canvas and y0) ...
    elements.append(
        f'<rect x="0" y="0" width="{width}" height="{y0}" '
        'fill="url(#thatch)"/>'
    )
    # ... and the strip to the left of the grid.
    elements.append(
        f'<rect x="0" y="{y0}" width="{x0}" height="{grid_h}" '
        'fill="url(#thatch)"/>'
    )

    # Grid itself.  First column highlighted yellow (the DP base case
    # "1 way to make 0").
    fills = [[WHITE] * cols for _ in range(rows)]
    values = [[""] * cols for _ in range(rows)]
    for r in range(rows):
        fills[r][0] = YELLOW
        values[r][0] = "1"
    elements.extend(draw_grid(g, values=values, fills=fills, text_size=22))

    # Column labels 0..20 above the grid.
    elements.extend(
        draw_col_labels(g, [str(c) for c in range(cols)], dy=18, size=20)
    )
    # Row labels = the coin denominations.
    elements.extend(
        draw_row_labels(g,
                        [f"{c}\u00a2" for c in coin_order],
                        dx=22, size=34)
    )

    paths = enumerate_paths(coin_order, TOTAL)
    n = len(paths)

    # Per-path: a <g> wrapping a polyline + its caption + a running
    # path counter ("k / N"), with one SMIL animation cycling
    # opacity 0→1→0 during its time slot.
    caption_y = y0 + grid_h + 60
    counter_y = caption_y + 56
    for idx, ks in enumerate(paths):
        pts = _path_points(g, coin_order, ks)
        caption = _path_caption(coin_order, ks)
        anim = _opacity_animation(idx, n)
        elements.append('<g opacity="0">')
        elements.append(_polyline(pts))
        elements.append(
            f'<text x="{width / 2}" y="{caption_y}" '
            f'font-family="\'Roboto Mono\', monospace" font-size="40" '
            f'fill="{BLACK}" text-anchor="middle">{caption}</text>'
        )
        elements.append(
            f'<text x="{width / 2}" y="{counter_y}" '
            f'font-family="\'Roboto Mono\', monospace" font-size="30" '
            f'fill="{GOLDEN}" text-anchor="middle" font-weight="bold">'
            f'path {idx + 1} / {n}</text>'
        )
        elements.append(anim)
        elements.append('</g>')

    elements.append(svg_close())
    return elements


def emit(coin_order: tuple[int, int, int], output_path: str) -> None:
    render(build(coin_order), output_path)
