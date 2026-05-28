"""Shared dynamic-programming grid layout.

Used by:
  * the 5-cent row formation slide (one row, 21 columns),
  * the small "K vs. K+1 coins" recursion-relation diagrams
    (two rows, three columns),
  * the full DP traversal diagram (three rows, 21 columns).

The grid is purely geometric; what's drawn inside each cell (numbers,
emptiness, accent fills) is the caller's job.
"""

from __future__ import annotations

from dataclasses import dataclass

from style import BLACK, FONT_MONO, WHITE
from lib_svg import rect, text


@dataclass(frozen=True)
class GridGeom:
    x0: float
    y0: float
    cell_w: float
    cell_h: float
    rows: int
    cols: int

    def cx(self, col: int) -> float:
        return self.x0 + col * self.cell_w + self.cell_w / 2

    def cy(self, row: int) -> float:
        return self.y0 + row * self.cell_h + self.cell_h / 2

    def left(self, col: int) -> float:
        return self.x0 + col * self.cell_w

    def top(self, row: int) -> float:
        return self.y0 + row * self.cell_h


def draw_grid(
    g: GridGeom,
    values: list[list[str]] | None = None,
    fills: list[list[str]] | None = None,
    text_size: float = 28,
) -> list[str]:
    """Render the grid; ``values[row][col]`` and ``fills[row][col]`` are
    both optional and may be partial (use '' or None for empty cells)."""
    elements: list[str] = []
    for r in range(g.rows):
        for c in range(g.cols):
            fill = WHITE
            if fills and r < len(fills) and c < len(fills[r]) and fills[r][c]:
                fill = fills[r][c]
            elements.append(
                rect(g.left(c), g.top(r), g.cell_w, g.cell_h,
                     fill=fill, stroke=BLACK, sw=2)
            )
            if values and r < len(values) and c < len(values[r]):
                v = values[r][c]
                if v:
                    elements.append(
                        text(
                            g.cx(c),
                            g.cy(r) + text_size / 3,
                            v,
                            size=text_size,
                            font="mono",
                            anchor="middle",
                        )
                    )
    return elements


def draw_col_labels(g: GridGeom, labels: list[str], dy: float = 30,
                    size: float = 24) -> list[str]:
    out = []
    for c, lab in enumerate(labels):
        if not lab:
            continue
        out.append(
            text(g.cx(c), g.y0 - dy, lab, size=size, font="mono",
                 anchor="middle")
        )
    return out


def draw_row_labels(g: GridGeom, labels: list[str], dx: float = 24,
                    size: float = 30) -> list[str]:
    out = []
    for r, lab in enumerate(labels):
        if not lab:
            continue
        out.append(
            text(g.x0 - dx, g.cy(r) + size / 3, lab, size=size,
                 anchor="end")
        )
    return out
