"""Shared style constants for every diagram.

The essay (`../README.md` § "Design system") pins the palette, fonts,
and aspect ratio.  All generators import from here so a single change
propagates across the deck.
"""

# Canvas --------------------------------------------------------------------
# 4:3 aspect ratio.  Generators emit SVG with a viewBox of this size so the
# rendered diagrams scale cleanly to any screen.
WIDTH = 1600
HEIGHT = 1200

# Spot illustrations fill the area below the section title at y25.  They
# render inside a square-ish region centred on the slide.
SPOT_WIDTH = 1400
SPOT_HEIGHT = 800

# Palette -------------------------------------------------------------------
WHITE = "#ffffff"
BLACK = "#000000"
YELLOW = "#fce3a4"   # accent (lighter)
GOLDEN = "#fdb913"   # accent (saturated)

# Derived greys used only for axis/grid lines that must read as "subdued"
# rather than as a third accent colour.  Used sparingly.
INK_FAINT = "#9a9a9a"
INK_MID = "#555555"

# Fonts ---------------------------------------------------------------------
# Roboto for general text, Roboto Mono for numerals and source code.
# Generic fallbacks ensure rendering on systems without Roboto installed.
FONT_SANS = "Roboto, 'Helvetica Neue', Arial, sans-serif"
FONT_MONO = "'Roboto Mono', 'Menlo', 'Consolas', monospace"

# Type scale in svg user units.  The essay's slide-level "large/medium/small"
# scale (8/16/24 rows per slide) is enforced in slides.md by CSS; diagram
# text uses these scaled sizes so labels stay legible at deck resolution.
TEXT_LARGE = 64
TEXT_MEDIUM = 40
TEXT_SMALL = 28
TEXT_TINY = 20

# Stroke widths -------------------------------------------------------------
STROKE_HAIR = 1.5
STROKE_LIGHT = 2.5
STROKE_MED = 4
STROKE_HEAVY = 6
