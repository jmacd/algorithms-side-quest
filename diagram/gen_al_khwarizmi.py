"""Placeholder card for the al-Khwarizmi manuscript image referenced in
the essay (§ "I ❤️ Algorithms", "There's an **algorithm** for this
problem").

The essay cites:
  https://en.wikipedia.org/wiki/Al-Khwarizmi#/media/File:The_Algebra_of_Mohammed_ben_Musa_(Arabic).png

Per ``AGENTS.md`` we do not import remote assets and we do not
fabricate stand-ins for cited historical images.  This card displays
a stylised manuscript-page silhouette plus a visible citation block so
the slide is honest about what is missing.
"""

from style import BLACK, FONT_SANS, GOLDEN, HEIGHT, WIDTH, YELLOW
from lib_svg import (
    line,
    main_path,
    path,
    rect,
    render,
    svg_close,
    svg_open,
    text,
)


def build() -> list[str]:
    elements = svg_open(WIDTH, HEIGHT)

    # Page silhouette: an old-manuscript leaf, aged-paper colour.
    px, py = 460, 180
    pw, ph = 680, 740
    elements.append(rect(px, py, pw, ph, fill=YELLOW, stroke=BLACK, sw=4))
    # Inner frame
    elements.append(rect(px + 24, py + 24, pw - 48, ph - 48,
                         fill="none", stroke=BLACK, sw=1.5))

    # Faux Arabic-style script: a sequence of horizontal flowing lines
    # with intermittent loops, evoking the cited manuscript without
    # transcribing actual text.  Drawn right-to-left to honour script
    # direction; purely abstract.
    line_y = py + 90
    for i in range(11):
        y = line_y + i * 56
        elements.append(
            path(
                f"M{px + pw - 60},{y} "
                f"q-40,16 -80,0 q-40,-16 -80,0 q-40,16 -80,0 "
                f"q-40,-16 -80,0 q-40,16 -80,0 q-40,-16 -80,0",
                stroke=BLACK, sw=2.2, fill="none",
            )
        )
        if i % 3 == 1:
            # Accent dot row
            for j in range(6):
                cx = px + pw - 90 - j * 90
                elements.append(rect(cx, y - 18, 4, 4, fill=BLACK,
                                     stroke=BLACK, sw=0.5))

    # Marginal illumination flourish in golden.
    elements.append(rect(px + 30, py + 30, 24, ph - 60, fill=GOLDEN,
                         stroke=BLACK, sw=1.5))
    for i in range(8):
        cy = py + 60 + i * 90
        elements.append(rect(px + 36, cy, 12, 12, fill=BLACK,
                             stroke=BLACK, sw=0))

    # Visible citation block under the image.
    cy = py + ph + 50
    elements.append(
        text(WIDTH / 2, cy, "[image placeholder — al-Khwarizmi, The Algebra]",
             size=30, anchor="middle", style="italic")
    )
    elements.append(
        text(
            WIDTH / 2, cy + 44,
            "credit: Wikipedia (File:The_Algebra_of_Mohammed_ben_Musa_(Arabic).png)",
            size=24, anchor="middle",
        )
    )

    elements.append(svg_close())
    return elements


if __name__ == "__main__":
    render(build(), main_path())
