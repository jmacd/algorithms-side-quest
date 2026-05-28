"""Odometer-style count-up from 0 to 100, in decimal (top) and binary (bottom).

Both panels stay strictly in sync: at any moment the decimal panel and
the binary panel show the same count `N` (0 ≤ N ≤ 100), N in base 10
above and N in base 2 below.  Each digit cell behaves like a single
wheel of a mechanical odometer: the ones digit rolls every tick, the
tens digit rolls only when the ones wraps 9 → 0, and the hundreds digit
rolls only when both lower wheels wrap.  For binary the same rule
applies per bit: bit 0 rolls every tick, bit k rolls only when bits
0..k-1 are all 1 and the next tick carries.

Timing
------
- 101 distinct counts (0..100) displayed for 0.25 s each.
- A final 0.25 s slot holds count 100 before the SVG loop snaps the
  wheels back to count 0 (the snap is instantaneous, like a fresh
  odometer being installed).
- Total cycle: 25.5 s, looping indefinitely.

Implementation
--------------
Each digit window is a `<clipPath>`-bounded rectangle, inside which a
vertical strip of digit `<text>` elements translates upward over time.
The strip carries only the *distinct consecutive* values that wheel
must show — so the hundreds wheel has just 2 cells ("0" and "1"), the
tens wheel has 11 cells (0..9 then back to 0 at count 100), and the
ones wheel has 101 cells.  Each wheel's animation `values` list
encodes per-count its own cell index (`positions[N]`), so the strip
*holds position* whenever the wheel's digit is unchanged from the
previous count, and translates by exactly one cell step on a carry
tick.  Wheels at different places therefore advance at completely
different rates, while staying in perfect sync at the keyframe grid.
"""

from style import (
    BLACK,
    FONT_MONO,
    FONT_SANS,
    INK_FAINT,
    INK_MID,
    SPOT_HEIGHT,
    SPOT_WIDTH,
    WHITE,
)
from lib_svg import (
    main_path,
    rect,
    render,
    svg_close,
    svg_open,
    text,
)


MAX_COUNT = 100
STEP_SECONDS = 0.25
N_STEPS = MAX_COUNT + 1                     # 101 distinct counts (0..100)
CYCLE_SECONDS = (N_STEPS + 1) * STEP_SECONDS  # forward steps + 1 rewind


def _strip_group(
    cx: float, cy: float, font_size: float,
    cells_content: list[int], positions: list[int],
    clip_id: str, step: float,
) -> str:
    """Wrap a vertical strip of digit cells in a clip + animation group.

    `cells_content` is the strip's digit faces, top to bottom (cell 0
    centered at (cx, cy), cell k at cy + k*step).  `positions[N]` is
    the cell index that should be centered in the window at count N.
    Whenever positions[N] == positions[N-1], the strip's animation
    value is unchanged between those two keyframes, so the wheel
    appears motionless across that interval — true odometer behavior.
    """
    baseline_offset = font_size * 0.35      # visual center → baseline shift
    cells: list[str] = []
    for i, d in enumerate(cells_content):
        cells.append(
            f'<text x="{cx:.2f}" y="{cy + i * step + baseline_offset:.2f}">{d}</text>'
        )

    # Per-count positions, plus one extra hold slot at count 100 before
    # the SVG loop snaps the wheel back to position 0 instantaneously.
    values = [-positions[n] * step for n in range(N_STEPS)]
    values.append(values[-1])
    n_keys = len(values)
    vals_str = ";".join(f"0,{v:.1f}" for v in values)
    keyTimes = ";".join(f"{i / (n_keys - 1):.5f}" for i in range(n_keys))
    anim = (
        f'<animateTransform attributeName="transform" type="translate" '
        f'values="{vals_str}" keyTimes="{keyTimes}" '
        f'dur="{CYCLE_SECONDS}s" repeatCount="indefinite" '
        f'calcMode="linear" additive="replace"/>'
    )

    return (
        f'<g clip-path="url(#{clip_id})">'
        f'<g transform="translate(0,0)" '
        f'font-family="{FONT_MONO}" font-size="{font_size}" '
        f'fill="{BLACK}" text-anchor="middle" font-weight="bold">'
        f'{"".join(cells)}{anim}</g></g>'
    )


def _digit_window(
    cx: float, cy: float, cell_w: float, cell_h: float,
    cells_content: list[int], positions: list[int],
    clip_id: str, font_size: float, step: float,
    place_label: str | None = None,
) -> tuple[list[str], tuple[float, float, float, float]]:
    """Build the static frame for one window and the strip+anim group.

    Returns (frame_elements, clip_rect_xywh) so the caller can
    register the clipPath in a single shared <defs>.
    """
    x = cx - cell_w / 2
    y = cy - cell_h / 2
    frame: list[str] = []
    # Window background and rounded border.
    frame.append(rect(x, y, cell_w, cell_h, fill="#fdf8ec",
                      stroke=INK_MID, sw=2.4, rx=10))
    if place_label:
        frame.append(text(cx, y - 18, place_label, size=20,
                          font="sans", anchor="middle", fill=INK_MID))

    # Strip is rendered first, then the top/bottom shading bands sit
    # on top to mask any sliver of the neighboring cell that creeps
    # into the window when the wheel is at a held position.
    strip = _strip_group(cx, cy, font_size, cells_content, positions,
                         clip_id, step=step)
    frame.append(strip)

    band_h = cell_h * 0.18
    frame.append(rect(x + 1, y + 1, cell_w - 2, band_h,
                      fill="#e9e2cd", stroke="none", sw=0, rx=10))
    frame.append(rect(x + 1, y + cell_h - band_h - 1, cell_w - 2,
                      band_h, fill="#e9e2cd", stroke="none", sw=0,
                      rx=10))
    return frame, (x, y, cell_w, cell_h)


def build() -> list[str]:
    W, H = SPOT_WIDTH, SPOT_HEIGHT
    elements = svg_open(W, H)

    cx = W / 2

    # --- Plan layout & accumulate window specs --------------------------
    # Decimal panel: hundreds, tens, ones.
    dec_cell_w, dec_cell_h = 140, 190
    dec_gap = 22
    dec_y = 280
    dec_places = [(100, "hundreds"), (10, "tens"), (1, "ones")]
    dec_total_w = (len(dec_places) * dec_cell_w
                   + (len(dec_places) - 1) * dec_gap)
    dec_x0 = cx - dec_total_w / 2

    # Binary panel: bits 6..0 (MSB on the left, matching place-value).
    bin_bits = 7
    bin_cell_w, bin_cell_h = 78, 118
    bin_gap = 14
    bin_y = 640
    bin_total_w = bin_bits * bin_cell_w + (bin_bits - 1) * bin_gap
    bin_x0 = cx - bin_total_w / 2

    # --- Build clip defs + window strips -------------------------------
    clip_defs: list[str] = []
    windows: list[str] = []

    # Decimal place P: wheel ticks once every P counts.
    #   positions[N]      = N // P      (wheel face visible at count N)
    #   cells_content[k]  = k % 10      (cyclic 0..9)
    #   number of faces   = (MAX_COUNT // P) + 1
    for col, (place, label) in enumerate(dec_places):
        win_cx = dec_x0 + col * (dec_cell_w + dec_gap) + dec_cell_w / 2
        positions = [n // place for n in range(N_STEPS)]
        n_cells = positions[-1] + 1
        cells_content = [k % 10 for k in range(n_cells)]
        clip_id = f"clip-dec-{place}"
        frame, (rx, ry, rw, rh) = _digit_window(
            win_cx, dec_y, dec_cell_w, dec_cell_h,
            cells_content, positions, clip_id,
            font_size=130, step=130, place_label=label,
        )
        clip_defs.append(
            f'<clipPath id="{clip_id}">'
            f'<rect x="{rx}" y="{ry}" width="{rw}" height="{rh}"/>'
            f'</clipPath>'
        )
        windows.extend(frame)

    # Binary bit k: wheel ticks once every 2^k counts.
    #   positions[N]      = N >> k
    #   cells_content[i]  = i & 1       (alternating 0/1)
    #   number of faces   = (MAX_COUNT >> k) + 1
    for col in range(bin_bits):
        bit = bin_bits - 1 - col            # MSB first
        win_cx = bin_x0 + col * (bin_cell_w + bin_gap) + bin_cell_w / 2
        positions = [n >> bit for n in range(N_STEPS)]
        n_cells = positions[-1] + 1
        cells_content = [i & 1 for i in range(n_cells)]
        clip_id = f"clip-bin-{bit}"
        label = f"2^{bit}" if bit > 0 else "1"
        frame, (rx, ry, rw, rh) = _digit_window(
            win_cx, bin_y, bin_cell_w, bin_cell_h,
            cells_content, positions, clip_id,
            font_size=72, step=78, place_label=label,
        )
        clip_defs.append(
            f'<clipPath id="{clip_id}">'
            f'<rect x="{rx}" y="{ry}" width="{rw}" height="{rh}"/>'
            f'</clipPath>'
        )
        windows.extend(frame)

    # --- Emit ----------------------------------------------------------
    # Augment the <defs> block (svg_open already opened one) with our clips.
    elements.append("<defs>" + "".join(clip_defs) + "</defs>")

    # Panel labels.
    elements.append(
        text(cx, 100, "decimal", size=44, font="sans",
             anchor="middle", fill=INK_MID, weight="bold")
    )
    elements.append(
        text(cx, 500, "binary", size=44, font="sans",
             anchor="middle", fill=INK_MID, weight="bold")
    )

    elements.extend(windows)
    elements.append(svg_close())
    return elements


if __name__ == "__main__":
    render(build(), main_path())
