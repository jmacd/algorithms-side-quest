"""Animated DP table fill-in, coin order 5¢ → 2¢ → 1¢.

Companion to gen_paths_521.py: same grid, same coin order, but here
the table fills in cell-by-cell instead of enumerating completed
solutions.  Bottom-right cell ends at 29 — the same total.

See lib_dp_anim.py for the actual rendering and SMIL animation.
"""
from lib_dp_anim import emit
from lib_svg import main_path

if __name__ == "__main__":
    emit((5, 2, 1), main_path())
