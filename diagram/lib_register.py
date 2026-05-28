"""Shared layout for binary register diagrams.

Used by the byte (8-bit) slide and the 4-byte (32-bit) slide.  A
register is a horizontal row of square cells, each holding a single
bit.  Cells set to 1 are filled with the golden accent.
"""

from __future__ import annotations

from style import BLACK, FONT_MONO, GOLDEN, WHITE
from lib_svg import rect, text


def draw_register(
    bits: list[int],
    x: float,
    y: float,
    cell: float = 70,
    gap: float = 6,
    byte_gap: float = 22,
    label: str | None = None,
    decimal: int | None = None,
    decimal_size: float = 56,
) -> list[str]:
    """Render a register of ``bits`` (MSB first).

    Bytes are visually separated when more than one is present.  Returns
    a flat list of SVG element strings.
    """
    elements: list[str] = []
    n = len(bits)

    # Compute horizontal advance, inserting an extra gap between bytes.
    total_w = 0
    advances = []
    for i in range(n):
        advances.append(total_w)
        total_w += cell
        if i < n - 1:
            extra = byte_gap if (i + 1) % 8 == 0 else gap
            total_w += extra

    for i, bit in enumerate(bits):
        cx = x + advances[i]
        fill = GOLDEN if bit else WHITE
        elements.append(rect(cx, y, cell, cell, fill=fill, stroke=BLACK, sw=2.5))
        elements.append(
            text(
                cx + cell / 2,
                y + cell / 2 + 14,
                str(bit),
                size=38,
                font="mono",
                anchor="middle",
                weight="bold",
            )
        )

    if label:
        elements.append(
            text(x - 22, y + cell / 2 + 14, label, size=36, anchor="end")
        )

    if decimal is not None:
        elements.append(
            text(
                x + total_w + 32,
                y + cell / 2 + decimal_size / 3,
                f"= {decimal:,}",
                size=decimal_size,
                font="mono",
                anchor="start",
            )
        )

    return elements


def bits_from_int(value: int, width: int) -> list[int]:
    return [(value >> (width - 1 - i)) & 1 for i in range(width)]
