"""Minimal stdlib-only SVG emitter.

Generators build a list of element strings and hand them to ``render``.
No third-party deps; output is byte-deterministic for a given input so
the committed SVGs produce meaningful ``git diff``s.
"""

from __future__ import annotations

import os
import sys
from html import escape

from style import (
    BLACK,
    FONT_MONO,
    FONT_SANS,
    HEIGHT,
    WHITE,
    WIDTH,
)


def svg_open(width: int = WIDTH, height: int = HEIGHT, bg: str = WHITE) -> list[str]:
    return [
        f'<svg xmlns="http://www.w3.org/2000/svg" '
        f'viewBox="0 0 {width} {height}" '
        f'preserveAspectRatio="xMidYMid meet">',
        f'<rect x="0" y="0" width="{width}" height="{height}" fill="{bg}"/>',
        # Reusable arrow marker for line termini.
        '<defs>',
        '  <marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" '
        'markerWidth="7" markerHeight="7" orient="auto-start-reverse">',
        '    <path d="M0,0 L10,5 L0,10 Z" fill="context-stroke"/>',
        '  </marker>',
        '  <marker id="arrow-gold" viewBox="0 0 10 10" refX="9" refY="5" '
        'markerWidth="7" markerHeight="7" orient="auto-start-reverse">',
        '    <path d="M0,0 L10,5 L0,10 Z" fill="#fdb913"/>',
        '  </marker>',
        '</defs>',
    ]


def svg_close() -> str:
    return '</svg>'


def text(
    x: float,
    y: float,
    content: str,
    size: float = 32,
    font: str = "sans",
    fill: str = BLACK,
    anchor: str = "start",
    weight: str = "normal",
    style: str = "normal",
) -> str:
    family = FONT_MONO if font == "mono" else FONT_SANS
    return (
        f'<text x="{x}" y="{y}" font-family="{family}" font-size="{size}" '
        f'fill="{fill}" text-anchor="{anchor}" font-weight="{weight}" '
        f'font-style="{style}">{escape(content)}</text>'
    )


def tspan_text(
    x: float,
    y: float,
    spans: list[tuple[str, str]],
    size: float = 32,
    font: str = "sans",
    anchor: str = "start",
) -> str:
    """Render text with multiple fills (each (string, color))."""
    family = FONT_MONO if font == "mono" else FONT_SANS
    inner = "".join(
        f'<tspan fill="{c}">{escape(s)}</tspan>' for s, c in spans
    )
    return (
        f'<text x="{x}" y="{y}" font-family="{family}" font-size="{size}" '
        f'text-anchor="{anchor}">{inner}</text>'
    )


def rect(
    x: float, y: float, w: float, h: float,
    fill: str = "none", stroke: str = BLACK, sw: float = 2,
    rx: float = 0,
) -> str:
    return (
        f'<rect x="{x}" y="{y}" width="{w}" height="{h}" '
        f'fill="{fill}" stroke="{stroke}" stroke-width="{sw}" rx="{rx}"/>'
    )


def line(
    x1: float, y1: float, x2: float, y2: float,
    stroke: str = BLACK, sw: float = 2, dash: str | None = None,
    marker_end: bool = False,
    marker_start: bool = False,
) -> str:
    extra = ''
    if dash:
        extra += f' stroke-dasharray="{dash}"'
    if marker_end:
        extra += ' marker-end="url(#arrow)"'
    if marker_start:
        extra += ' marker-start="url(#arrow)"'
    return (
        f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" '
        f'stroke="{stroke}" stroke-width="{sw}"{extra}/>'
    )


def path(
    d: str, stroke: str = BLACK, fill: str = "none", sw: float = 2,
    dash: str | None = None, marker_end: bool = False,
    linecap: str = "round", linejoin: str = "round",
) -> str:
    extra = ''
    if dash:
        extra += f' stroke-dasharray="{dash}"'
    if marker_end:
        extra += ' marker-end="url(#arrow)"'
    return (
        f'<path d="{d}" stroke="{stroke}" fill="{fill}" stroke-width="{sw}" '
        f'stroke-linecap="{linecap}" stroke-linejoin="{linejoin}"{extra}/>'
    )


def circle(
    cx: float, cy: float, r: float,
    fill: str = "none", stroke: str = BLACK, sw: float = 2,
) -> str:
    return (
        f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{fill}" '
        f'stroke="{stroke}" stroke-width="{sw}"/>'
    )


def ellipse(
    cx: float, cy: float, rx: float, ry: float,
    fill: str = "none", stroke: str = BLACK, sw: float = 2,
) -> str:
    return (
        f'<ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" fill="{fill}" '
        f'stroke="{stroke}" stroke-width="{sw}"/>'
    )


def polygon(
    points: list[tuple[float, float]],
    fill: str = "none", stroke: str = BLACK, sw: float = 2,
) -> str:
    pts = " ".join(f"{x},{y}" for x, y in points)
    return (
        f'<polygon points="{pts}" fill="{fill}" stroke="{stroke}" '
        f'stroke-width="{sw}"/>'
    )


def group(elements: list[str], transform: str = "") -> str:
    attr = f' transform="{transform}"' if transform else ''
    return f'<g{attr}>' + "".join(elements) + '</g>'


def render(elements: list[str], output_path: str) -> None:
    body = "\n".join(elements) + "\n"
    os.makedirs(os.path.dirname(output_path) or ".", exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(body)
    size = os.path.getsize(output_path)
    print(f"wrote {output_path} ({size} bytes)")


def main_path() -> str:
    """Resolve argv[1] for ``python3 gen_xxx.py <output>``; exit on misuse."""
    if len(sys.argv) < 2:
        print(f"usage: {sys.argv[0]} <output.svg>", file=sys.stderr)
        sys.exit(2)
    return sys.argv[1]
