# algorithms-side-quest

Slidev deck scaffold. Edit `slides.md`; pushes to `main` build and publish to GitHub Pages via `.github/workflows/deploy-slides.yml`.

## Live deck

https://jmacd.github.io/algorithms-side-quest/

## Run locally

Prerequisites: Node.js >= 20.19.

```bash
# 1. Install dependencies (only needed once, or after package.json changes)
npm install

# 2. Start the dev server
npm run slides
```

Then open http://localhost:3030 in your browser. The server hot-reloads on edits to `slides.md`.

Presenter mode: http://localhost:3030/presenter

Other commands:

```bash
npm run build    # static SPA into dist/
npm run export   # export to PDF (requires Playwright: npx playwright install chromium)
```

## Publishing

The `Deploy Slides to GitHub Pages` workflow runs on every push to `main` and
on manual dispatch. Enable **Settings → Pages → Source: GitHub Actions** once
in the repository for the first deploy to succeed.

