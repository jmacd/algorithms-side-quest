"""Half-filled Sudoku board.

The fill pattern is fixed (deterministic) and uses a recognisably
partial puzzle — about half the cells filled.
"""

from style import BLACK, GOLDEN, HEIGHT, WIDTH, YELLOW
from lib_svg import line, main_path, rect, render, svg_close, svg_open, text


PUZZLE = [
    "53..7....",
    "6..195...",
    ".98....6.",
    "8...6...3",
    "4..8.3..1",
    "7...2...6",
    ".6....28.",
    "...419..5",
    "....8..79",
]


def build() -> list[str]:
    elements = svg_open(WIDTH, HEIGHT)

    board = 880
    bx = (WIDTH - board) / 2
    by = (HEIGHT - board) / 2 + 30
    cell = board / 9

    # Thin lines for every cell.
    for i in range(10):
        sw = 5 if i % 3 == 0 else 1.6
        # Verticals
        elements.append(
            line(bx + i * cell, by, bx + i * cell, by + board,
                 stroke=BLACK, sw=sw)
        )
        # Horizontals
        elements.append(
            line(bx, by + i * cell, bx + board, by + i * cell,
                 stroke=BLACK, sw=sw)
        )

    # Given cells get a yellow background; numerals in mono.
    for r, row in enumerate(PUZZLE):
        for c, ch in enumerate(row):
            if ch == '.':
                continue
            elements.append(
                rect(bx + c * cell + 3, by + r * cell + 3,
                     cell - 6, cell - 6, fill=YELLOW, stroke="none", sw=0)
            )
            elements.append(
                text(bx + c * cell + cell / 2,
                     by + r * cell + cell / 2 + 22,
                     ch, size=60, font="mono", anchor="middle",
                     weight="bold")
            )

    # Caption.
    elements.append(
        text(WIDTH / 2, 100, "sudoku — partial",
             size=44, anchor="middle", style="italic")
    )

    elements.append(svg_close())
    return elements


if __name__ == "__main__":
    render(build(), main_path())
