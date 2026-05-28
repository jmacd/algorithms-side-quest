"""Animated DP table fill-in for the change-making problem.

Companion to lib_paths.py.  Where the path-counting animation
enumerates the 29 *completed* solutions geometrically, this one shows
the *dynamic program itself* filling the 3 × 21 table cell-by-cell
row-by-row.  For each cell, two transient arrows reveal the
recursion-rule sources (one above, one left by the row's coin value);
the cell's computed value appears at the same instant and stays
forever; a caption underneath narrates ``above + left = value``.
After all 60 cells have been filled the bottom-right cell holds 29 —
the same total the path animation counted geometrically.

The "above" arrow for row 0, and the "left" arrow for any cell where
``c < coin``, both emanate from the thatched zero-possibility region
outside the grid — making it visually obvious those terms contribute
zero, exactly as the recursion's implicit boundary conditions say.

Animation: SMIL <animate> on per-element opacity, calcMode=discrete,
cycling continuously.  60 frames per cycle.
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
from lib_svg import render, svg_close
from lib_dp_grid import GridGeom, draw_col_labels, draw_grid, draw_row_labels


TOTAL = 20
CYCLE_SECONDS = 30   # ~0.5 s per cell


def compute_dp(coin_order: tuple[int, int, int],
               total: int = TOTAL):
    """Run the row-by-row recursion and record every cell's inputs.

    Returns (table, fill_order) where:
      table[r][c]  = final cell value
      fill_order   = list of (r, c, above, left, value) in computation
                     order (skipping column 0 which is the base case).
    """
    rows = len(coin_order)
    cols = total + 1
    table = [[0] * cols for _ in range(rows)]
    fill_order: list[tuple[int, int, int, int, int]] = []
    for r in range(rows):
        table[r][0] = 1
    for r in range(rows):
        coin = coin_order[r]
        for c in range(1, cols):
            above = table[r - 1][c] if r > 0 else 0
            left_c = c - coin
            left = table[r][left_c] if left_c >= 0 else 0
            value = above + left
            table[r][c] = value
            fill_order.append((r, c, above, left, value))
    return table, fill_order


def _opacity_persistent(idx: int, n: int) -> str:
    """Element appears at idx/n and stays at opacity 1 thereafter."""
    if idx == 0:
        return ""  # caller renders the element with static opacity=1
    return (
        f'<animate attributeName="opacity" calcMode="discrete" '
        f'values="0;1" keyTimes="0;{idx / n:.5f}" '
        f'dur="{CYCLE_SECONDS}s" repeatCount="indefinite"/>'
    )


def _opacity_transient(idx: int, n: int) -> str:
    """Element appears at idx/n, disappears at (idx+1)/n; hidden otherwise."""
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


def _arrow(x1: float, y1: float, x2: float, y2: float) -> str:
    return (
        f'<line x1="{x1:.1f}" y1="{y1:.1f}" '
        f'x2="{x2:.1f}" y2="{y2:.1f}" '
        f'stroke="{GOLDEN}" stroke-width="6" stroke-linecap="round" '
        f'marker-end="url(#arrow-gold)"/>'
    )


def _arc_arrow(x1: float, y: float, x2: float, arch: float) -> str:
    """Quadratic-bezier left arrow that dips by ``arch`` px below ``y`` so
    its mid-section misses the intervening cells' value text."""
    cx = (x1 + x2) / 2
    cy = y + arch
    return (
        f'<path d="M {x1:.1f},{y:.1f} Q {cx:.1f},{cy:.1f} {x2:.1f},{y:.1f}" '
        f'stroke="{GOLDEN}" stroke-width="6" stroke-linecap="round" '
        f'fill="none" marker-end="url(#arrow-gold)"/>'
    )


def build(coin_order: tuple[int, int, int]) -> list[str]:
    width, height = 1600, 620
    cols = TOTAL + 1
    rows = 3
    cell_w = 64
    cell_h = 110

    grid_w = cols * cell_w
    grid_h = rows * cell_h
    x0 = (width - grid_w) / 2 + 30
    y0 = 80
    g = GridGeom(x0=x0, y0=y0,
                 cell_w=cell_w, cell_h=cell_h,
                 rows=rows, cols=cols)

    elements: list[str] = []
    elements.append(
        f'<svg xmlns="http://www.w3.org/2000/svg" '
        f'viewBox="0 0 {width} {height}" '
        f'preserveAspectRatio="xMidYMid meet">'
    )
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
    # Thatched zero-possibility margins.
    elements.append(
        f'<rect x="0" y="0" width="{width}" height="{y0}" '
        'fill="url(#thatch)"/>'
    )
    elements.append(
        f'<rect x="0" y="{y0}" width="{x0}" height="{grid_h}" '
        'fill="url(#thatch)"/>'
    )

    # Static grid: column 0 filled yellow with "1"; rest blank.
    fills = [[WHITE] * cols for _ in range(rows)]
    values = [[""] * cols for _ in range(rows)]
    for r in range(rows):
        fills[r][0] = YELLOW
        values[r][0] = "1"
    elements.extend(draw_grid(g, values=values, fills=fills, text_size=28))

    elements.extend(
        draw_col_labels(g, [str(c) for c in range(cols)], dy=18, size=20)
    )
    elements.extend(
        draw_row_labels(g,
                        [f"{c}\u00a2" for c in coin_order],
                        dx=22, size=34)
    )

    _, fill_order = compute_dp(coin_order, TOTAL)
    n = len(fill_order)

    caption_y = y0 + grid_h + 60
    counter_y = caption_y + 56

    for idx, (r, c, above, left, value) in enumerate(fill_order):
        coin = coin_order[r]

        # Persistent cell value: appears at idx/n and stays.
        opacity_attr = '1' if idx == 0 else '0'
        elements.append(f'<g opacity="{opacity_attr}">')
        elements.append(
            f'<text x="{g.cx(c):.1f}" y="{g.cy(r) + 32 / 3:.1f}" '
            f'font-family="\'Roboto Mono\', monospace" font-size="32" '
            f'fill="{BLACK}" text-anchor="middle" font-weight="bold">'
            f'{value}</text>'
        )
        anim_p = _opacity_persistent(idx, n)
        if anim_p:
            elements.append(anim_p)
        elements.append('</g>')

        # Transient overlay: cell border + two arrows + caption + counter.
        elements.append('<g opacity="0">')

        # Golden stroke around the cell currently being computed.
        elements.append(
            f'<rect x="{g.left(c):.1f}" y="{g.top(r):.1f}" '
            f'width="{cell_w}" height="{cell_h}" '
            f'fill="none" stroke="{GOLDEN}" stroke-width="5"/>'
        )

        # "Above" arrow — from the cell above (or from thatched zone for r=0)
        # down into the top of the current cell.
        ax = g.cx(c)
        if r > 0:
            ay1 = g.top(r) - cell_h / 2 + 16   # near bottom of cell above
        else:
            ay1 = y0 - 44                       # in thatched zone above grid
        ay2 = g.top(r) + 12                     # just inside the top edge
        elements.append(_arrow(ax, ay1, ax, ay2))

        # "Left" arrow — from the cell coin-columns to the left
        # (or from thatched zone if c < coin) into the left edge of cell.
        # Curved so its mid-section dips below the row's value text and
        # doesn't overstrike the intervening cells.
        left_c = c - coin
        if left_c >= 0:
            lx1 = g.left(c) - cell_w * (coin - 1) - 12  # near right of source
        else:
            lx1 = x0 - 44                                # in thatched zone
        lx2 = g.left(c) + 12                             # just inside left edge
        arch = 14 + 8 * (coin - 1)                       # gentler for coin=1
        elements.append(_arc_arrow(lx1, g.cy(r), lx2, arch))

        # Caption narrating the recursion-rule arithmetic.
        caption = (
            f"row\u202f{r + 1}  col\u202f{c}  :  "
            f"above\u202f{above}  +  left\u202f{left}  =  {value}"
        )
        elements.append(
            f'<text x="{width / 2}" y="{caption_y}" '
            f'font-family="\'Roboto Mono\', monospace" font-size="36" '
            f'fill="{BLACK}" text-anchor="middle">{caption}</text>'
        )

        # Cell counter (so the audience can see the 60 ticks accumulate).
        elements.append(
            f'<text x="{width / 2}" y="{counter_y}" '
            f'font-family="\'Roboto Mono\', monospace" font-size="30" '
            f'fill="{GOLDEN}" text-anchor="middle" font-weight="bold">'
            f'cell {idx + 1} / {n}</text>'
        )

        elements.append(_opacity_transient(idx, n))
        elements.append('</g>')

    elements.append(svg_close())
    return elements


def emit(coin_order: tuple[int, int, int], output_path: str) -> None:
    render(build(coin_order), output_path)
