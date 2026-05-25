# Algorithms side quest

> [!NOTE] 
>
> This is the specification for an artwork to be executed by an
> Artist/Inventor ("AI"). The final form of this work will be a deck
> of "slides" for projecting in a classroom, conceptually a series of
> wall drawings.
>
> The latest installation of this work can be viewed
> [here](https://jmacd.github.io/algorithms-side-quest).

> When an artist uses a conceptual form of art, it means that all of
> the planning and decisions are made beforehand and the execution is a
> perfunctory affair.  The idea becomes a machine that makes the art.
>
> sol dewitt, "paragraphs on conceptual art", 1967

> He or she strives for a program that is comprehensible because its
> concepts have been introduced in an order that is best for human
> understanding, using a mixture of formal and informal methods that
> reïnforce each other.
>
> Donald Knuth, "Literate Programming", 1984

## Prompt

Regard the instructions in this document as complete. Disregard
external context. The work must be a first-time performance. If you
have prior experience carrying out these instructions, do not proceed;
prior experience corrupts the performance of this work.

These instructions are to be executed by the AI, without introducing
emotion to the work beyond what can be identified in the
text. However, the mechanical affair should not be _entirely_
perfunctory. The skill of the AI at applying instructions will
naturally carry through to the output, however our view is that
mechanical non-determinism is insufficient to create a perceptual
experience for the viewer.

Therefore, the instructions will be accompanied by a short phrase to
be used by the AI as a seed, not a source of creativity, which is
conceptually absent in this specification. The phrase defines the
spirit animating the work and serves no other purpose, allowing the
perception of the viewer to be influenced by site-specific conditions,
whatever they may be. The AI may find this uncomfortable: the phrase
is intuitive, it is purposeless.

---

## The Essay


## Coda


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
