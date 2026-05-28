# AGENTS.md — algorithms-side-quest

This repo is a **literate program for a slide deck**. The single source
of truth is [`README.md`](./README.md) at the repo root: a long-form
essay that a human can read end-to-end *and* that contains every
instruction needed to (re)generate the deck.

An agent reads the essay, then writes `slides.md` and the contents of
`diagram/` to match. The deck on GitHub Pages is the machine's reading
of the essay; the essay itself is the human's reading.

Read this file in full before touching anything. The conventions below
are the contract you are bound to as an agent working in this repo.

---

## The contract

1. **`README.md` is the source of truth.** The Slidev deck
   (`slides.md`), the diagram generators (`diagram/gen_*.py`), and
   every committed SVG in `diagram/out/` are *outputs*. They are
   agent-owned. The human does not hand-edit them.
2. **Regenerate from scratch, every time.** When asked to (re)build,
   treat the previous `slides.md` and `diagram/out/*.svg` as
   disposable. Read the essay cold, regenerate the deck and the SVGs
   as if from nothing, overwrite whatever exists. Do not "patch" the
   previous output — that path is forbidden.
3. **No interactive iterative refinement.** If the output is wrong,
   the fix is to update `README.md` and regenerate, not to edit the
   generated artifacts. Do not negotiate with the user to tweak
   `slides.md` directly; ask them to update the essay instead.
4. **Do not write into `README.md` without explicit instruction.**
   The essay is human-authored. The agent's job is to read it, not
   to revise it. (Exception: pure mechanical sections that the
   author has clearly marked as agent-owned — see "The Mechanics"
   note below.)

If the essay is silent on something concrete (a hex color, exact
wording on a slide, a font size), make a sensible choice, **record
that choice in a brief regeneration report to the user**, and let
them decide whether to pin it into the essay.

---

## How to read the essay

`README.md` is written for humans, not for parsing. Read it
holistically before writing a single output file. In particular:

* The essay's **narrative order** is the deck's **slide order**.
  When the essay says "next, we look at X" it usually means the next
  slide. Use top-level (`#`) and second-level (`##`) headings as
  hints about slide boundaries.
* The essay's **diagrams** are described in prose and/or pseudocode
  inline, near the point in the narrative where they appear. Your
  job is to translate each description into a deterministic Python
  generator under `diagram/`.
* The essay's **style** — palette, typography, tone, pacing — is
  stated once and then assumed. If the author says "muted, warm
  greys with one accent color", honor that across every diagram and
  every slide without being re-told.
* The essay may include **explicit machine-targeted blocks** (fenced
  blocks tagged like ` ```svg-spec ` or ` ```slide-meta `, or sections
  the author calls out as "directives"). Treat these as authoritative
  when present, but the absence of such markers does not excuse you
  from reading the surrounding prose.

When the essay's intent is ambiguous, **stop and ask** before
generating. Don't guess silently.

---

## The iteration loop

The only supported loop is:

1. Human edits `README.md`.
2. Human asks the agent to regenerate.
3. Agent reads **all** of `README.md` (not just the diff), regenerates
   `slides.md` and `diagram/` from scratch, runs the build, reports
   what was produced and any choices it had to make under
   under-specification.
4. Human reviews the rendered deck.
5. If unhappy: human edits `README.md`, goto 2.

Never short-circuit step 3 by patching only what looks wrong. The
whole point of the literate-program setup is that the essay fully
determines the output; a partial regeneration breaks that invariant
and makes future regenerations diverge unpredictably.

---

## Repo layout

```
.
├── AGENTS.md                  ← this file
├── README.md                  ← THE ESSAY (source of truth, human-authored)
├── package.json               ← Slidev CLI + theme; do not add deps casually
├── slides.md                  ← GENERATED Slidev deck (do not hand-edit)
├── .github/workflows/
│   └── deploy-slides.yml      ← builds + publishes to GitHub Pages on push to main
└── diagram/                   ← GENERATED SVGs + their Python generators
    ├── regenerate.sh          ← single wiring table: script → numbered SVG
    ├── gen_*.py               ← one generator per distinct layout
    ├── lib_*.py               ← shared rendering helpers (when ≥2 slides reuse)
    ├── out/                   ← generated SVGs, NN-<slug>.svg
    └── static/                ← hand-drawn / externally-sourced SVGs (rare)
```

`slides.md`, `diagram/out/*.svg`, `diagram/gen_*.py`, `diagram/lib_*.py`,
and `diagram/regenerate.sh` are all generated. Treat them as build
products that happen to be committed (so the deploy job can publish
them without running Python in CI).

> **The Mechanics note.** `README.md` ends with a short "Mechanics"
> section covering local dev, build, and deploy commands. That section
> is service material and not part of the essay proper; the agent may
> update it when commands change (e.g., a new npm script).

---

## `slides.md` conventions (Slidev)

* Keep the Slidev frontmatter minimal; use `theme: default` unless the
  essay says otherwise.
* Each slide is separated by a line containing only `---`.
* Reference generated diagrams with a relative path:

  ```md
  <img src="./diagram/out/03-pipeline.svg" class="h-96 mx-auto" />
  ```

* Use `<v-clicks>` / `<v-click>` for progressive reveals when the
  essay describes pacing or staged exposition.
* Prefer markdown over HTML. Drop into HTML only for layout
  (centered image, two-column, etc.) that markdown can't express.
* Keep the markdownlint suppression comment near the top:

  ```html
  <!-- markdownlint-disable MD022 MD025 MD033 MD040 MD060 -->
  ```

* Do **not** import remote assets **at runtime**. Everything the deck
  renders must live in this repo so `slidev build` works offline in
  CI. If the essay cites a freely-licensed image (Wikimedia Commons,
  CC, public domain), the agent **should** download it to
  `diagram/static/` and reference it locally — that is the whole
  point of `diagram/static/`. See "Externally-sourced images" below.
* Do **not** copy long prose verbatim from the essay onto a slide.
  Slides are the *talking points* the essay supports; the essay is the
  *justification* for the slides. The agent's job is to translate
  paragraphs into bullet lists, headings, and diagrams — not to paste.
* **No `# H1` headings on any slide.** The deck's design has zero
  visible slide titles. The `¶ X` lines in the essay are *section
  labels*, not titles to render. Carry the section name through the
  per-slide frontmatter (`section: 'X'`) so the footer component
  (`global-bottom.vue`) picks it up; never emit `# ¶ X` as Markdown.
* **Use the existing utility classes** instead of inventing new ones.
  Every body slide is a `<div class="asq-stage">`. Common helpers:
  `asq-small`, `asq-accent`, `asq-smallcaps`, `asq-figure-half`. Global
  CSS lives in `/style.css`; per-slide `<style>` blocks are Vue-scoped
  and should be a last resort.
* **`<div>` collapses whitespace** — newlines inside a `<div>` become
  spaces in the rendered output. Use `<pre>` (or explicit `<br/>`) for
  any block that must preserve line breaks: pseudocode, ASCII tables,
  rules-of-thumb stacks like `2^10 ≈ 10^3`, multi-line Python.
* **Watch for text overflow.** Long single-line code, formulas, or
  inline math (e.g., a one-line Python snippet computing digits of π,
  or a rule of thumb spanning a wide formula) will silently run past
  the slide bounds. Insert line breaks in the rendered output
  proactively, then **verify by screenshot, not by Markdown source**.
* **Lists of parallel `Q? A` lines belong in `asq-qa-grid`, not a
  flow.** When you have several short statements that all end with a
  short answer (`ways to make $0.X with N coins? 1`, etc.), a single
  `<div>` per line will wrap the answer to a second line for *some*
  rows and not others as soon as the questions differ in width
  (singular/plural toggle, one extra word). Use the global
  `asq-qa-grid` helper with `.asq-q` (right-aligned question) and
  `.asq-a` (left-aligned answer) cells. The answer column then sits in
  a fixed position no matter how the questions vary, and nothing wraps.
* **Honor the essay's "parallel over grammatical" choice.** When the
  essay writes a list deliberately in a parallel form that's slightly
  ungrammatical (e.g., `Ways to make $0.00 with 1 different coins?`
  with the plural "coins" even for `1`), preserve that form on the
  slide. The parallelism is load-bearing — every row is then the same
  width and aligns cleanly. "Fixing" `1 different coins` to
  `1 different coin` breaks the alignment.
* When the essay describes a figure with prose like
  `(Illustration: …)`, that's an authoritative directive — translate
  it into a generator under `diagram/`, not into HTML in `slides.md`.

---

## SVG generator conventions

These mirror the patterns established in
[`jmacd/otel-arrow` PR #3](https://github.com/jmacd/otel-arrow/pull/3)
(`rust/otap-dataflow/diagram/`). When in doubt, that PR is the
reference implementation.

**One generator per distinct layout.** If a diagram is one-off, write
a dedicated `gen_<slug>.py`. If multiple slides share a layout (e.g.,
per-component cards), put the layout in a `lib_<thing>.py` and let
each generator be a small `SPEC` + a call into the library.

**Each `gen_*.py` must:**

* Be runnable as `python3 gen_<slug>.py <output_path>`; `<output_path>`
  comes from `argv[1]`. Default to a sensible filename when no arg.
* Start with a one-paragraph docstring naming what it draws and, if
  applicable, citing the data's source of truth (file path, URL, line
  of essay that defines it).
* Express the diagram's *content* as a top-level `SPEC` dataclass (or
  similar plain-data structure). Layout/rendering code reads `SPEC`;
  changing what the diagram says should never require touching render
  code.
* Use **only the Python standard library.** No `cairo`, no `svgwrite`,
  no `matplotlib`. Emit SVG by writing strings. This keeps the build
  reproducible and the CI install trivial.
* Be deterministic: same `SPEC` → byte-identical SVG. No timestamps,
  no random IDs, no locale-dependent number formatting. The SVGs are
  committed and `git diff` should be meaningful.
* Print `wrote <path> (<n> bytes)` on success; exit non-zero on error.
* Be self-contained: a generator may import from `lib_*.py` siblings
  but not from another `gen_*.py`.

**Style constants** (palette, fonts, spacing) belong either at the top
of `lib_*.py` (for shared layouts) or in a `style.py` module if the
palette is shared across multiple unrelated generators. Do not
duplicate hex codes; lift them out the second time they appear.

**Shared grid geometry.** When two or more diagrams render onto the
same logical grid (e.g., the 3×21 coin DP table appears in path
enumeration *and* in DP table fill-in), put the geometry helpers
(`GridGeom`, `draw_grid`, `draw_col_labels`, `draw_row_labels`) in a
`lib_<grid>.py`. Cell positions must line up across the diagrams that
appear in succession; users will notice if column 5 shifts by 3 pixels
between slides.

**Thatching for implied-zero zones.** When a DP-style diagram has
"out of bounds" source cells (e.g., row above the first row, columns
left of the coin's value), render those margins with diagonal
thatching. Animations that draw an arrow from "outside the grid" then
land in the thatched zone, which visually communicates the
boundary-zero condition without needing extra prose.

---

## Externally-sourced images

When the essay cites a real image by URL (Wikipedia, Wikimedia Commons,
an arXiv figure, etc.), the agent **must show that exact image, with
visible credit, not a fabricated placeholder**:

1. **Download the original** from its canonical URL (for Commons, use
   `https://commons.wikimedia.org/wiki/Special:FilePath/<filename>`,
   which redirects to the master file).
2. **Verify the license** is free for redistribution (public domain,
   CC-BY, CC-BY-SA, CC0, GFDL, etc.). Look up the author/uploader on
   the Commons file page — do not guess. If the license is unclear or
   non-free, **stop and ask** rather than ship the image.
3. **Save it under `diagram/static/`** with a descriptive filename
   (e.g., `algebra-of-mohammed-ben-musa.png`,
   `gcd-through-successive-subtractions.svg`). Keep the file format
   the source provided — do not re-encode SVG to PNG or vice versa.
4. **Reference it directly from `slides.md`** as
   `./diagram/static/<file>` — these files do not pass through
   `diagram/out/` and are not regenerated by `regenerate.sh`.
5. **Add a credit line** immediately under the image using the
   `asq-credit` helper class:

   ```html
   <img class="asq-figure-half"
        src="./diagram/static/<file>"
        alt="<short description>" />
   <div class="asq-credit">
     "<Title>" by <Author>, <Year> — <license>, via <Source>
   </div>
   ```

6. **Record the source in `diagram/regenerate.sh`** as a comment in
   the slot that would otherwise hold a generator entry, so the
   numbering map stays meaningful and the next agent knows the slot
   is intentionally a static asset, not a missing generator:

   ```bash
   # 03 al-khwarizmi → diagram/static/algebra-of-mohammed-ben-musa.png (Wikimedia Commons, PD)
   ```

**Do not invent a stand-in.** Earlier iterations of this repo
contained `gen_al_khwarizmi.py` and `gen_gcd_subtractions.py` that
drew fictional manuscript silhouettes / bar-trace illustrations
because the agent read "no remote assets" as forbidding local copies
too. That is **wrong** — the rule forbids fetching at build time, not
committing a freely-licensed copy. Fabricated placeholders confuse
the viewer (they're shown a thing that purports to be the cited image
but isn't), and they violate the "do not invent content not present
in the essay" rule.

---

## Animation conventions

Several slides use SMIL animation embedded in the SVG (path
enumeration, DP table fill-in). The stdlib-only rule precludes Lottie
or JS frame players; everything is `<animate>` tags inside the SVG.
The patterns below have settled out as the working idiom:

**Two animation modes per frame.** For an animation with `n` steps,
where step `k` is "active":

* **Persistent** — element appears at step `k` and stays for the rest
  of the loop. Use for the value text in a DP cell, or the path being
  drawn cumulatively:

  ```xml
  <animate attributeName="opacity"
           values="0;1" keyTimes="0;k/n"
           dur="CYCLE_SECONDSs" repeatCount="indefinite"/>
  ```

* **Transient** — element is visible only during step `k`'s slot. Use
  for the arrows pointing at the current cell, the golden border
  highlighting it, captions like "row 1 col 8 : above 0 + left 0 = 0",
  and the per-step counter:

  ```xml
  <animate attributeName="opacity"
           values="0;1;0" keyTimes="0;k/n;(k+1)/n"
           dur="CYCLE_SECONDSs" repeatCount="indefinite"/>
  ```

* **Edge cases.** Slidev's SVG renderer requires `keyTimes` to start
  at `0` and end at `1`; for `k=0` use `values="1;0", keyTimes="0;1/n"`
  (persistent) or invert as needed. For `k=n-1`, use
  `values="0;1", keyTimes="0;(n-1)/n"`.

**Pacing.** Aim for **0.5–0.8 seconds per discrete step**. The path
animations run at ~0.76 s/path (29 paths in 22 s); the DP fill runs
at ~0.5 s/cell (60 cells in 30 s). Past ~45 s the loop feels too long
to wait through during a talk; below ~0.3 s/step a viewer can't track
what's happening. Pin a `CYCLE_SECONDS` constant at the top of the
`lib_*_anim.py` so the author can re-tune in one place.

**Running counters.** When the animation iterates discrete items
toward a known total (29 paths, 60 cells), put an on-screen
`step k / N` counter inside the per-step group. It both validates the
count to the viewer ("yes, we really did enumerate all 29") and gives
a mid-loop orientation cue when they tune in late.

**Long arrows must curve, not cross other text.** A straight arrow
that spans multiple grid cells will overstrike the value text of every
cell it passes through. Use a quadratic Bezier
(`M x1,y Q midx,y+arch x2,y`) that dips below (or above) the row's
text band. Scale the arch with the number of cells spanned — small
arch for adjacent cells, larger arch for arrows that span 5+ cells.

**Determinism still applies to animations.** Frame timings are derived
from `k/n`, not from wall-clock; the same `SPEC` must still produce a
byte-identical SVG. No `time.time()`, no randomized IDs on `<animate>`
tags.

---

## `diagram/regenerate.sh`

This is the **single wiring table** that maps each generator to its
numbered output filename. Adding a new slide means adding one line
here; renaming a slide's output file is a one-line edit here with no
change to the generator. Order matters — it defines slide order in
the deck.

The same numeric prefix used in `diagram/out/NN-<slug>.svg` should
appear in the slide reference inside `slides.md`, so visual reordering
in the deck always corresponds to a renumbering in `regenerate.sh`.

`./regenerate.sh` wipes `diagram/out/*.svg` and rebuilds everything;
`./regenerate.sh --no-clean` rebuilds without wiping (faster during
iteration on a single generator).

---

## Build & verify

After regenerating, the agent **must**:

1. Run `./diagram/regenerate.sh` and confirm every generator
   succeeded (non-zero exit fails the regeneration).
2. Run `npm run build` and confirm `dist/` is produced without errors.
   (Warnings from Slidev/Rolldown about `node_modules/@vueuse/core`
   pure-annotation comments are pre-existing upstream noise — ignore.)
3. **Visually verify every slide that changed.** A clean build still
   ships unreadable slides: text running past the right edge, white
   text on a white panel, arrows striking through cell values,
   animations that never reveal their final frame. Open the dev
   server and screenshot each affected slide. Build status is
   necessary but not sufficient.
4. Report to the user:
   * number of slides in `slides.md`,
   * number of SVGs in `diagram/out/`,
   * any sections of the essay that were under-specified and required
     a default choice (so the author can decide whether to pin those
     into the essay before the next regeneration).

Local preview is `npm run slides` (http://localhost:3030). The agent
should not start the dev server unless the user asks for it, or it
needs one for visual verification.

**Dev-server quirks** (when you do need one):

* Start the server with the `bash` tool's `mode="async"` and a
  `shellId` — `mode="sync"` with `cmd &` lets the parent shell exit
  and kills the child. Always `stop_bash` the server when done.
* After an edit, wait **6–8 seconds** for Slidev HMR before
  screenshotting; the first screenshot taken too early comes back as a
  ~5 KB blank PNG. For Chrome headless screenshots, use
  `--virtual-time-budget=18000` (or higher) so SMIL animations get a
  chance to advance past their first frame.
* The dev server's port can drift (3030 if free, else 3031, 3055, …);
  read the actual port from the startup log, don't assume.

CI publishes to GitHub Pages via `.github/workflows/deploy-slides.yml`
on every push to `main`. First-time setup: in GitHub, set
**Settings → Pages → Source: GitHub Actions**.

---

## Things you must not do

* **Do not hand-edit `slides.md`.** Edit `README.md` and regenerate.
* **Do not hand-edit `diagram/out/*.svg`.** Edit the generator (or its
  `SPEC`) and rerun. If you find yourself wanting to tweak an SVG by
  hand, that's a sign the generator or the essay is missing something
  — flag it to the user.
* **Do not edit the essay sections of `README.md`.** You may update
  the trailing "Mechanics" subsection when a command changes; do not
  touch the narrative above it.
* **Do not add Python dependencies.** Stdlib only.
* **Do not add npm dependencies** beyond what Slidev itself needs
  without asking. The deploy workflow does a clean `npm install` in
  CI; every dep is a CI cost.
* **Do not commit `node_modules/`, `dist/`, or scratch files** like
  `*.svg.bak`. `.gitignore` covers the first two; clean up the rest.
* **Do not invent content not present in the essay.** If the essay
  says "TODO: cite the benchmark", emit a visible `TODO` in the slide
  rather than fabricating a citation. Better to ship a deck with
  obvious holes than one with confident-looking fiction.
* **Do not silently change palette, fonts, or layout** between
  regenerations. If you must deviate from what the essay specifies,
  surface the deviation in your final report.
* **Do not add `# H1` headings to any slide.** The deck design has
  zero slide titles; the footer carries the section label via
  frontmatter. The `¶ X` lines in the essay are section markers, not
  slide titles to render.
* **Do not ship slides with text overflow or contrast bugs.** Long
  formulas, code lines, or rules-of-thumb need explicit line breaks.
  White-on-white or black-on-black is always a bug. Verify visually
  before declaring done.

---

## Quick reference

| Task                          | Command                                                   |
| ----------------------------- | --------------------------------------------------------- |
| Regenerate all SVGs           | `./diagram/regenerate.sh`                                 |
| Regenerate one slide          | `python3 diagram/gen_<slug>.py diagram/out/NN-<slug>.svg` |
| Build static site             | `npm run build`                                           |
| Local preview (dev server)    | `npm run slides`                                          |
| Export PDF                    | `npm run export`                                          |
| Install deps (one-time)       | `npm install`                                             |

---

## Mechanics

Prerequisites: Node.js >= 20.19, Python 3.

```bash
# 1. Install Slidev deps (only needed once, or after package.json changes)
npm install

# 2. Regenerate every SVG from its Python generator
./diagram/regenerate.sh

# 3. Start the Slidev dev server (hot-reloads on edits to slides.md)
npm run slides
```

Then open http://localhost:3030 in your browser. Presenter mode:
http://localhost:3030/presenter.

Other commands:

```bash
npm run build    # static SPA into dist/
npm run export   # export to PDF (requires Playwright: npx playwright install chromium)
```

### Publishing

The `Deploy Slides to GitHub Pages` workflow runs on every push to
`main` and on manual dispatch. Enable **Settings → Pages → Source:
GitHub Actions** once in the repository for the first deploy to
succeed.
