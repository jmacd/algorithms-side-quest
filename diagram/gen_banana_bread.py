"""Banana bread recipe card.

Per the essay (§ "A sequence of steps"): "the first few lines of recipe
for banana bread, ingredients & yield, cook time, list of steps; not
complete, just enough to recognize".

Original wording, no recipe lifted verbatim; the purpose is visual
recognition of "this is a recipe".
"""

from style import BLACK, FONT_MONO, GOLDEN, HEIGHT, WIDTH, YELLOW
from lib_svg import (
    line,
    main_path,
    rect,
    render,
    svg_close,
    svg_open,
    text,
)


HEADER = "Banana Bread"
META = [
    ("yield",  "1 loaf"),
    ("time",   "60 min"),
    ("oven",   "350 °F"),
]
INGREDIENTS = [
    "3 ripe bananas",
    "1/3 cup melted butter",
    "3/4 cup sugar",
    "1 egg, beaten",
    "1 tsp vanilla",
    "1 tsp baking soda",
    "pinch of salt",
    "1 1/2 cups flour",
]
STEPS = [
    "1.  Mash bananas in a bowl.",
    "2.  Stir in butter.",
    "3.  Mix in sugar, egg, vanilla.",
    "4.  Sprinkle baking soda, salt.",
    "5.  Fold in flour.",
    "6.  Pour into a buttered loaf pan.",
    "7.  Bake until a tester comes out clean.",
]


def build() -> list[str]:
    elements = svg_open(WIDTH, HEIGHT)

    # Card frame
    cx, cy, cw, ch = 120, 100, WIDTH - 240, HEIGHT - 200
    elements.append(rect(cx, cy, cw, ch, fill="#ffffff",
                         stroke=BLACK, sw=4))
    # Header strip
    elements.append(rect(cx, cy, cw, 110, fill=GOLDEN,
                         stroke=BLACK, sw=4))
    elements.append(
        text(cx + cw / 2, cy + 76, HEADER, size=72, anchor="middle",
             weight="bold")
    )

    # Meta line under header
    mx = cx + 60
    my = cy + 170
    for i, (k, v) in enumerate(META):
        ex = mx + i * 360
        elements.append(text(ex, my, k, size=28, anchor="start",
                             style="italic"))
        elements.append(text(ex + 110, my, v, size=32, font="mono",
                             anchor="start"))

    # Divider
    elements.append(line(cx + 40, cy + 210, cx + cw - 40, cy + 210,
                         stroke=BLACK, sw=1.5))

    # Two columns: ingredients (left), steps (right).
    col_y0 = cy + 270
    elements.append(text(cx + 60, col_y0, "ingredients", size=34,
                         weight="bold", style="italic"))
    for i, ing in enumerate(INGREDIENTS):
        elements.append(
            text(cx + 60, col_y0 + 52 + i * 44, ing, size=28, font="mono")
        )

    elements.append(text(cx + cw / 2 + 40, col_y0, "steps", size=34,
                         weight="bold", style="italic"))
    for i, step in enumerate(STEPS):
        elements.append(
            text(cx + cw / 2 + 40, col_y0 + 52 + i * 44, step,
                 size=28, font="mono")
        )

    elements.append(svg_close())
    return elements


if __name__ == "__main__":
    render(build(), main_path())
