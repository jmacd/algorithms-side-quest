"""Animated DP-path diagram, coin order 1¢ → 2¢ → 5¢.

The companion to gen_paths_521.py — same 29 dynamic-programming
solutions but, because the smallest coin is processed first, the
paths grow geometrically in the opposite shape: lots of single
unit steps in the top row, big 5¢ strides at the bottom.

See lib_paths.py for the actual rendering and SMIL animation.
"""
from lib_paths import emit
from lib_svg import main_path

if __name__ == "__main__":
    emit((1, 2, 5), main_path())
