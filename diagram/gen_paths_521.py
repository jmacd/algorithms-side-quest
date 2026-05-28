"""Animated DP-path diagram, coin order 5¢ → 2¢ → 1¢.

One of the two permutations the essay calls out for the
"We're path-counting" slide.  Same 29 paths as the 1-2-5 ordering,
but with the biggest coin processed first the geometric paths look
visibly different: long 5¢ strides at the top, fine 1¢ steps at the
bottom.

See lib_paths.py for the actual rendering and SMIL animation.
"""
from lib_paths import emit
from lib_svg import main_path

if __name__ == "__main__":
    emit((5, 2, 1), main_path())
