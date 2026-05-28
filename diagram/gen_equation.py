"""The diophantine equation 100 = 5x + 10y + 25z with x, y, z ∈ W.

Big centred display.  Could be rendered as KaTeX on the slide, but
keeping it as an SVG ensures consistent type with surrounding diagrams.
"""

from style import BLACK, GOLDEN, HEIGHT, WIDTH, YELLOW
from lib_svg import main_path, render, svg_close, svg_open, text, tspan_text


def build() -> list[str]:
    elements = svg_open(WIDTH, HEIGHT)

    # Equation, centred, large
    elements.append(
        tspan_text(
            WIDTH / 2, HEIGHT / 2 - 40,
            [("100 = 5", BLACK), ("x", GOLDEN), (" + 10", BLACK),
             ("y", GOLDEN), (" + 25", BLACK), ("z", GOLDEN)],
            size=120, font="mono", anchor="middle",
        )
    )

    # Set-membership line below.
    elements.append(
        tspan_text(
            WIDTH / 2, HEIGHT / 2 + 140,
            [("x", GOLDEN), (", ", BLACK), ("y", GOLDEN),
             (", ", BLACK), ("z", GOLDEN), ("  ∈  ", BLACK),
             ("W", BLACK)],
            size=80, font="mono", anchor="middle",
        )
    )
    # "W = whole numbers" gloss
    elements.append(
        text(WIDTH / 2, HEIGHT / 2 + 220,
             "W  =  { 0, 1, 2, 3, … }",
             size=44, font="mono", anchor="middle")
    )

    elements.append(svg_close())
    return elements


if __name__ == "__main__":
    render(build(), main_path())
