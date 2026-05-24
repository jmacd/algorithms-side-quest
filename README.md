# algorithms-side-quest

> This `README.md` is the deck.
>
> What follows is a long-form essay describing what the deck shows,
> why, and how. It is written to be read end-to-end by a human; it is
> also the **single source of truth** from which an agent generates
> the Slidev deck (`slides.md`) and every diagram under `diagram/`.
> See [`AGENTS.md`](./AGENTS.md) for the contract the agent works
> under.
>
> Live deck: https://jmacd.github.io/algorithms-side-quest/

---

## Prelude

<!--
TODO: replace this section with the opening of the essay — what the
deck is about, who it is for, what the reader will walk away with.
Everything below should read as continuous prose. The agent will use
the narrative order, section headings, and any diagram descriptions
embedded here to (re)generate the deck.
-->

*(placeholder)*

---

## The Essay

<!--
TODO: the body of the essay. Use ## headings to mark logical sections;
the agent will treat the narrative order as the slide order. Describe
each diagram inline, near the point in the narrative where it appears.
State style choices (palette, typography, tone) once; they will be
honored throughout regeneration.
-->

*(placeholder)*

---

## Coda

<!--
TODO: closing thoughts, references, acknowledgements.
-->

*(placeholder)*

---

## Mechanics

This section is service material, not part of the essay. The agent
may update it when build commands change.

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

