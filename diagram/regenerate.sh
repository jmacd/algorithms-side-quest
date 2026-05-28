#!/usr/bin/env bash
# Single wiring table: maps each generator to its numbered output SVG.
# Adding a slide diagram = adding one line.  Order matters because it
# defines the slide order in the deck (numeric prefix == slide order).
#
# Usage:
#   ./regenerate.sh             # clean diagram/out and rebuild everything
#   ./regenerate.sh --no-clean  # incremental rebuild
set -euo pipefail

cd "$(dirname "$0")"

CLEAN=1
if [[ "${1:-}" == "--no-clean" ]]; then
  CLEAN=0
fi

OUT_DIR=out
mkdir -p "$OUT_DIR"
if [[ $CLEAN -eq 1 ]]; then
  rm -f "$OUT_DIR"/*.svg
fi

# Numbering convention: NN-<slug>.svg, two-digit prefix sets order.
GENERATORS=(
  "01:spot-bees:gen_spot_bees.py"

  # Section: I ❤️ Algorithms
  "02:spot-euclid:gen_spot_euclid.py"
  # 03 al-khwarizmi → diagram/static/algebra-of-mohammed-ben-musa.png (Wikimedia Commons, PD)
  # 04 gcd-subtractions → diagram/static/gcd-through-successive-subtractions.svg (Wikimedia Commons, PD)
  "05:banana-bread:gen_banana_bread.py"
  "06:equation:gen_equation.py"

  # Section: Every-day algorithms
  "07:spot-maze:gen_spot_maze.py"
  # 08 fort-bragg → real OSM data cached in diagram/static/fort-bragg-streets.json
  #                (Overpass API snapshot; © OpenStreetMap contributors, ODbL)
  "08:fort-bragg:gen_fort_bragg.py"

  # Section: Counting exercises
  "09:spot-chalkboard:gen_spot_chalkboard.py"
  "10:byte-register:gen_byte_register.py"
  "11:count-256:gen_count_256.py"
  "12:four-byte-register:gen_four_byte_register.py"

  # Section: Change the problem
  "13:spot-coins:gen_spot_coins.py"
  "14:tsp:gen_tsp.py"
  "15:sudoku:gen_sudoku.py"

  # Section: Counting from zero
  "16:spot-dpgrid:gen_spot_dpgrid.py"
  "17:row-formation:gen_row_formation.py"
  "18:recursion-two-row:gen_recursion_two_row.py"
  "19:dp-diagram:gen_dp_diagram.py"
  "20:recursion-two-row-filled:gen_recursion_two_row.py"
  "21:paths-521:gen_paths_521.py"
  "22:paths-125:gen_paths_125.py"
  "23:dpanim-521:gen_dpanim_521.py"
  "24:dpanim-125:gen_dpanim_125.py"
)

fail=0
for entry in "${GENERATORS[@]}"; do
  IFS=':' read -r num slug script <<<"$entry"
  out="$OUT_DIR/${num}-${slug}.svg"
  if ! python3 "$script" "$out"; then
    echo "FAILED: $script" >&2
    fail=1
  fi
done

if [[ $fail -ne 0 ]]; then
  echo "one or more generators failed" >&2
  exit 1
fi

echo "all $(ls $OUT_DIR/*.svg | wc -l | tr -d ' ') SVGs regenerated"
