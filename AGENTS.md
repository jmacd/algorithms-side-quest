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

* Do **not** import remote assets. Everything the deck renders must
  live in this repo so `slidev build` works offline in CI.
* Do **not** copy long prose verbatim from the essay onto a slide.
  Slides are the *talking points* the essay supports; the essay is the
  *justification* for the slides. The agent's job is to translate
  paragraphs into bullet lists, headings, and diagrams — not to paste.

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
3. Report to the user:
   * number of slides in `slides.md`,
   * number of SVGs in `diagram/out/`,
   * any sections of the essay that were under-specified and required
     a default choice (so the author can decide whether to pin those
     into the essay before the next regeneration).

Local preview is `npm run slides` (http://localhost:3030). The agent
should not start the dev server unless the user asks for it.

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
