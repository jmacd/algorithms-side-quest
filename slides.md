---
theme: default
title: Algorithms Side Quest
info: |
  Algorithms Side Quest — Joshua MacDonald — May 28, 2026.
  Source of truth is README.md in this repo.
aspectRatio: 4/3
canvasWidth: 1024
fonts:
  sans: 'Roboto'
  mono: 'Roboto Mono'
  weights: '300,400,500,700'
drawings:
  persist: false
section: ''
---

<!-- markdownlint-disable MD022 MD025 MD033 MD040 MD060 -->

<div class="asq-title-block">
  <div class="asq-large">Algorithms Side Quest</div>
  <div class="asq-medium" style="margin-top: 0.8rem;">
    Joshua MacDonald · <span class="asq-mono">May 28, 2026</span>
  </div>
</div>

<div class="asq-title-spot">
  <img src="./diagram/out/01-spot-bees.svg" alt="three bees in flight over poppies" />
</div>

---
section: 'I ❤️ Algorithms'
---

<div class="asq-section-title">I ❤️ Algorithms</div>
<div class="asq-section-spot">
  <img src="./diagram/out/02-spot-euclid.svg" alt="Euclid GCD flow chart" />
</div>

---
section: 'I ❤️ Algorithms'
---

<div class="asq-stage">
  <div class="asq-large">How many ways to make</div>
  <div class="asq-large asq-mono asq-accent">$1.00</div>
  <div class="asq-medium">from <span class="asq-mono">5¢</span>, <span class="asq-mono">10¢</span>, <span class="asq-mono">25¢</span> coins?</div>
</div>

---
section: 'I ❤️ Algorithms'
---

<div class="asq-stage">
  <div class="asq-large">There's an <span class="asq-accent">algorithm</span>.</div>
  <img class="asq-figure-half" src="./diagram/static/algebra-of-mohammed-ben-musa.png" alt="A page from The Algebra of Mohammed ben Musa (1831 facsimile)" />
  <div class="asq-credit">A page from <em>The Algebra of Mohammed ben Musa</em>, Fredrick Rosen, 1831 — public domain, via Wikimedia Commons</div>
</div>

---
section: 'I ❤️ Algorithms'
---

<div class="asq-stage">
  <div class="asq-large">An algorithm is…</div>
  <img class="asq-figure-half" src="./diagram/static/gcd-through-successive-subtractions.svg" alt="GCD by successive subtraction — flow chart" />
  <div class="asq-credit">“GCD through successive subtractions” by Arthur Baelde — public domain, via Wikimedia Commons</div>
</div>

---
section: 'I ❤️ Algorithms'
---

<div class="asq-stage">
  <img class="asq-figure" src="./diagram/out/05-banana-bread.svg" alt="banana bread recipe card" />
</div>

---
section: 'I ❤️ Algorithms'
---

<div class="asq-stage">
  <pre class="asq-code">p = 3
for i in range(1, 100):
    term = 4 / (2*i * (2*i+1) * (2*i+2))
    p += term * (-1)**(i+1)
print(p)</pre>
  <div class="asq-caption">the Nilakantha series for computing π</div>
</div>

---
section: 'I ❤️ Algorithms'
---

<div class="asq-stage">
  <div class="asq-medium">equations define solutions</div>
  <div class="asq-medium">they don't say how to find them</div>
  <img class="asq-figure-half" src="./diagram/out/06-equation.svg" alt="100 = 5x + 10y + 25z with x,y,z ∈ W" style="margin-top: 1rem;" />
</div>

---
section: 'Every-day algorithms'
---

<div class="asq-section-title">Every-day algorithms</div>
<div class="asq-section-spot">
  <img src="./diagram/out/07-spot-maze.svg" alt="maze with left-hand-rule trace" />
</div>

---
section: 'Every-day algorithms'
---

<div class="asq-stage">
  <div class="asq-large">refrigerator search</div>
  <pre class="asq-code"><span class="asq-accent">problem</span>   find the ketchup
&#10;<span class="asq-accent">algorithm</span>
  1.  Pick any item.
  2.  Is it ketchup?  If yes, go to step 4.
  3.  Place it on the counter.  Go to step 1.
  4.  Return items to the refrigerator.</pre>
</div>

---
section: 'Every-day algorithms'
---

<div class="asq-stage">
  <div class="asq-large">mowing a lawn</div>
  <pre class="asq-code"><span class="asq-accent">problem</span>     cover the entire lawn
&#10;<span class="asq-accent">algorithm</span>   depends!</pre>
</div>

---
section: 'Every-day algorithms'
---

<div class="asq-stage">
  <div class="asq-large">count the houses in town</div>
  <img class="asq-figure-half" src="./diagram/out/08-fort-bragg.svg" alt="Fort Bragg street grid" />
</div>

---
section: 'Every-day algorithms'
---

<div class="asq-stage">
  <div class="asq-medium">searching   ·   sorting   ·   routing   ·   counting</div>
  <div class="asq-large" style="margin-top: 2.2rem;">how much <span class="asq-accent">time</span>?</div>
  <div class="asq-large">how much <span class="asq-accent">memory</span>?</div>
</div>

---
section: 'Counting exercises'
---

<div class="asq-section-title">Counting exercises</div>
<div class="asq-section-spot">
  <img src="./diagram/out/09-spot-chalkboard.svg" alt="person at chalkboard with n! = n·(n-1)!" />
</div>

---
section: 'Counting exercises'
---

<div class="asq-stage">
  <div class="asq-large">decimal</div>
  <div class="asq-medium">digits <span class="asq-mono asq-accent">0</span> … <span class="asq-mono asq-accent">9</span></div>
  <div class="asq-medium">place values are powers of <span class="asq-mono asq-accent">10</span></div>
  <div class="asq-code" style="margin-top: 1rem; font-size: 1.9rem;">5678₁₀ = 5·10³ + 6·10² + 7·10¹ + 8·10⁰</div>
</div>

---
section: 'Counting exercises'
---

<div class="asq-stage">
  <div class="asq-large">binary</div>
  <div class="asq-medium">digits <span class="asq-mono asq-accent">0</span> and <span class="asq-mono asq-accent">1</span></div>
  <div class="asq-medium">place values are powers of <span class="asq-mono asq-accent">2</span></div>
  <div class="asq-code" style="margin-top: 1rem; font-size: 1.9rem;">1111₂ = 1·2³ + 1·2² + 1·2¹ + 1·2⁰</div>
</div>

---
section: 'Counting exercises'
---

<div class="asq-stage">
  <div class="asq-large">a <span class="asq-accent">bit</span></div>
  <div class="asq-medium">one binary place value</div>
  <div class="asq-large asq-mono" style="margin-top: 1rem;"><span class="asq-accent">0</span>    or    <span class="asq-accent">1</span></div>
</div>

---
section: 'Counting exercises'
---

<div class="asq-stage">
  <div class="asq-large">8 bits = 1 <span class="asq-accent">byte</span></div>
  <img class="asq-figure-half" src="./diagram/out/10-byte-register.svg" alt="8-bit register equals 106" />
</div>

---
section: 'Counting exercises'
---

<div class="asq-stage">
  <div class="asq-large asq-mono">2⁸ = 256</div>
  <img class="asq-figure-half" src="./diagram/out/11-count-256.svg" alt="counting from 0 to 255" />
</div>

---
section: 'Counting exercises'
---

<div class="asq-stage">
  <img class="asq-figure-tall" src="./diagram/out/12-four-byte-register.svg" alt="32-bit register" />
</div>

---
section: 'Counting exercises'
---

<div class="asq-stage">
  <div class="asq-medium">10 bits ≈ 3 decimal digits</div>
  <div class="asq-large asq-mono">2¹⁰ = 1,024</div>
  <div class="asq-large asq-mono">10³ = 1,000</div>
  <div class="asq-medium asq-mono" style="margin-top: 1.4rem;">
    30 bits ≈ <span class="asq-accent">1 billion</span>
  </div>
  <div class="asq-medium asq-mono">
    60 bits ≈ <span class="asq-accent">1 quintillion</span>
  </div>
  <div class="asq-medium asq-mono">
    64 bits = 18,446,744,073,709,551,616
  </div>
</div>

---
section: 'Counting exercises'
---

<div class="asq-stage">
  <img class="asq-figure-tall" src="./diagram/out/29-odometer.svg" alt="decimal and binary odometer counting 0 to 100 in sync" />
</div>

---
section: 'Change the problem'
---

<div class="asq-section-title">Change the problem</div>
<div class="asq-section-spot">
  <img src="./diagram/out/13-spot-coins.svg" alt="pile of coins" />
</div>

---
section: 'Change the problem'
---

<div class="asq-stage">
  <div class="asq-large">Travelling Salesman</div>
  <img class="asq-figure-half" src="./diagram/out/14-tsp.svg" alt="5-city TSP circuit" />
  <div class="asq-medium">no known fast algorithm</div>
</div>

---
section: 'Change the problem'
---

<div class="asq-stage">
  <div class="asq-medium">fast Travelling Salesman   ⇒   fast Sudoku</div>
  <img class="asq-figure-half" src="./diagram/out/15-sudoku.svg" alt="partial sudoku board" />
  <div class="asq-medium">thousands of problems in this class</div>
</div>

---
section: 'Change the problem'
---

<div class="asq-stage">
  <div class="asq-medium">Euclid, c. 300 BC   ·   greatest common divisor</div>
  <pre class="asq-code">// greatest common divisor of two numbers
func gcd2(a, b int) int {
    if b == 0 { return a }
    if a == 0 { return b }
    if a &gt; b { return gcd2(a-b, b) }
    return gcd2(a, b-a)
}</pre>
  <div class="asq-caption">a recursive algorithm</div>
</div>

---
section: 'Change the problem'
---

<div class="asq-stage">
  <div class="asq-mono" style="font-size: 3.6rem; font-weight: 700; white-space: nowrap;">
    <span class="asq-accent">gcd</span>(5, 10, 25, 100) = 5
  </div>
  <div class="asq-mono" style="font-size: 2.2rem; margin-top: 1.6rem; line-height: 1.5; text-align: center;">
    $1.00 made from {5¢, 10¢, 25¢}<br/>
    <span class="asq-accent" style="font-size: 2.6rem;">⇔</span><br/>
    $0.20 made from {1¢, 2¢, 5¢}
  </div>
  <pre class="asq-code" style="margin-top: 1.8rem;">// greatest common divisor of N numbers
func gcdN(a ...int) int {
    if len(a) &lt; 2 { return a[0] }
    return gcd2(a[0], gcdN(a[1:]...))
}</pre>
</div>

---
section: 'Counting from zero'
---

<div class="asq-section-title">Counting from zero</div>
<div class="asq-section-spot">
  <img src="./diagram/out/16-spot-dpgrid.svg" alt="dynamic programming grid zoom" />
</div>

---
section: 'Counting from zero'
---

<div class="asq-stage">
  <div class="asq-qa-grid asq-mono" style="font-size: 2.0rem; line-height: 1.25;">
    <div class="asq-q">ways to make $0.00 with <span class="asq-accent">0</span> different coins?</div>
    <div class="asq-a asq-accent">1</div>
    <div class="asq-q">ways to make $0.00 with <span class="asq-accent">1</span> different coins?</div>
    <div class="asq-a asq-accent">1</div>
    <div class="asq-q">ways to make $0.00 with <span class="asq-accent">2</span> different coins?</div>
    <div class="asq-a asq-accent">1</div>
  </div>
  <div class="asq-caption" style="margin-top: 1.6rem;">axiom — all empty sets are the same</div>
</div>

---
section: 'Counting from zero'
---

<div class="asq-stage">
  <div class="asq-medium asq-mono">ways to make $0.20 with all pennies?   <span class="asq-accent">1</span></div>
  <div class="asq-medium asq-mono">ways to make $0.19 with all pennies?   <span class="asq-accent">1</span></div>
  <div class="asq-medium asq-mono" style="opacity: 0.55;">…</div>
  <div class="asq-medium asq-mono">ways to make $0.01 with all pennies?   <span class="asq-accent">1</span></div>
  <div class="asq-medium asq-mono">ways to make $0.00 with all pennies?   <span class="asq-accent">1</span></div>
</div>

---
section: 'Counting from zero'
---

<div class="asq-stage">
  <div class="asq-medium asq-mono">ways to make $0.00 with all 5¢ coins?   <span class="asq-accent">1</span></div>
  <div class="asq-medium asq-mono">ways to make $0.01 with all 5¢ coins?   <span class="asq-accent">0</span></div>
  <div class="asq-medium asq-mono">ways to make $0.02 with all 5¢ coins?   <span class="asq-accent">0</span></div>
  <div class="asq-medium asq-mono">ways to make $0.03 with all 5¢ coins?   <span class="asq-accent">0</span></div>
  <div class="asq-medium asq-mono">ways to make $0.04 with all 5¢ coins?   <span class="asq-accent">0</span></div>
  <div class="asq-medium asq-mono">ways to make $0.05 with all 5¢ coins?   <span class="asq-accent">1</span></div>
</div>

---
section: 'Counting from zero'
---

<div class="asq-stage">
  <img class="asq-figure" src="./diagram/out/17-row-formation.svg" alt="row of 21 cells for 5¢ coin counts" />
</div>

---
section: 'Counting from zero'
---

<div class="asq-stage">
  <div class="asq-medium asq-mono"><span class="asq-accent">A</span>   =   amount</div>
  <div class="asq-medium asq-mono"><span class="asq-accent">K</span>   =   number of coins so far</div>
  <div class="asq-medium asq-mono"><span class="asq-accent">N</span>   =   count of ways to make A with K</div>
  <div class="asq-medium asq-mono"><span class="asq-accent">C</span>   =   value of a K+1th coin</div>
</div>

---
section: 'Counting from zero'
---

<div class="asq-stage">
  <div class="asq-medium">add coin <span class="asq-mono asq-accent">C</span> as the next coin</div>
  <div class="asq-medium"><span class="asq-mono asq-accent">N</span> ways to make <span class="asq-mono asq-accent">A</span> with <span class="asq-mono asq-accent">K</span> coins</div>
  <div class="asq-medium"><span class="asq-mono asq-accent">N'</span> ways to make <span class="asq-mono asq-accent">A'</span> with <span class="asq-mono asq-accent">K+1</span> coins</div>
  <img class="asq-figure-half" src="./diagram/out/18-recursion-two-row.svg" alt="recursion relation two-row diagram" style="margin-top: 0.4rem;" />
</div>

---
section: 'Counting from zero'
---

<div class="asq-stage">
  <img class="asq-figure-tall" src="./diagram/out/19-dp-diagram.svg" alt="3-row × 21-column DP grid with coloured arrows" />
</div>

---
section: 'Counting from zero'
---

<div class="asq-stage" style="gap: 0.7rem;">
  <div>
    <div class="asq-small asq-accent asq-smallcaps">in the row above</div>
    <div class="asq-medium">count to <span class="asq-mono">A</span> without the new coin <span class="asq-mono">C</span> is <span class="asq-mono">N</span></div>
  </div>
  <div>
    <div class="asq-small asq-accent asq-smallcaps">in the row below</div>
    <div class="asq-medium">count to <span class="asq-mono">A'</span> with the new coin <span class="asq-mono">C</span> is <span class="asq-mono">N'</span></div>
  </div>
  <div>
    <div class="asq-small asq-accent asq-smallcaps">with</div>
    <div class="asq-medium asq-mono">A' + C = A</div>
  </div>
  <div>
    <div class="asq-small asq-accent asq-smallcaps">then</div>
    <div class="asq-medium">count to <span class="asq-mono">A</span> with the new coin is <span class="asq-mono">N + N'</span></div>
  </div>
  <img class="asq-figure-half" src="./diagram/out/20-recursion-two-row-filled.svg" alt="recursion relation with sum N+N' filled in" style="margin-top: 0.3rem; max-height: 28vh;" />
</div>

---
section: 'Counting from zero'
---

<div class="asq-stage">
  <img class="asq-figure-tall" src="./diagram/out/20-recursion-two-row-filled.svg" alt="recursion relation with sum N+N' filled in (full frame)" />
</div>

---
section: 'Counting from zero'
---

<div class="asq-stage">
  <img class="asq-figure-tall" src="./diagram/out/19-dp-diagram.svg" alt="3-row × 21-column DP grid with coloured arrows (reprise)" />
</div>

---
section: 'Counting from zero'
---

<div class="asq-stage">
  <div class="asq-medium">Path iteration</div>
  <div class="asq-small asq-accent asq-smallcaps">coin order &nbsp;·&nbsp; 5¢ → 2¢ → 1¢</div>
  <img class="asq-figure-half" src="./diagram/out/21-paths-521.svg" alt="29 dynamic-programming paths through a 3×21 grid, biggest coin first" style="max-height: 64vh;" />
</div>

---
section: 'Counting from zero'
---

<div class="asq-stage">
  <div class="asq-medium">Path iteration</div>
  <div class="asq-small asq-accent asq-smallcaps">coin order &nbsp;·&nbsp; 1¢ → 2¢ → 5¢</div>
  <img class="asq-figure-half" src="./diagram/out/22-paths-125.svg" alt="29 dynamic-programming paths through a 3×21 grid, smallest coin first" style="max-height: 64vh;" />
</div>

---
section: 'Counting from zero'
---

<div class="asq-stage">
  <div class="asq-medium">Counting paths</div>
  <div class="asq-small asq-accent asq-smallcaps">coin order &nbsp;·&nbsp; 5¢ → 2¢ → 1¢</div>
  <img class="asq-figure-half" src="./diagram/out/23-dpanim-521.svg" alt="60-frame DP table fill-in animation, biggest coin first" style="max-height: 64vh;" />
</div>

---
section: 'Counting from zero'
---

<div class="asq-stage">
  <div class="asq-medium">Counting paths</div>
  <div class="asq-small asq-accent asq-smallcaps">coin order &nbsp;·&nbsp; 1¢ → 2¢ → 5¢</div>
  <img class="asq-figure-half" src="./diagram/out/24-dpanim-125.svg" alt="60-frame DP table fill-in animation, smallest coin first" style="max-height: 64vh;" />
</div>

---
section: 'Counting from zero'
---

<div class="asq-stage">
  <div class="asq-large">Counting-change family</div>
  <div class="asq-medium" style="margin-top: 2rem;">same algorithm, different problem</div>
  <div class="asq-medium" style="margin-top: 1.4rem;">compute <span class="asq-accent">similarity</span></div>
  <div class="asq-small asq-accent asq-smallcaps">autocomplete &nbsp;·&nbsp; DNA analysis</div>
  <div class="asq-medium" style="margin-top: 1.4rem;">solve the <span class="asq-accent">shortest-edit</span> problem</div>
</div>

---
section: 'Art and Science'
---

<div class="asq-section-title">Art and Science</div>
<div class="asq-section-spot">
  <img src="./diagram/out/25-spot-painter.svg" alt="painter on a ladder sketching lines on a wall" />
</div>

---
section: 'Art and Science'
---

<div class="asq-stage">
  <div class="asq-large">Sol LeWitt</div>
  <div class="asq-small asq-accent asq-smallcaps">1928 – 2007 &nbsp;·&nbsp; conceptual art</div>
  <img class="asq-figure-half" src="./diagram/out/26-lewitt-wall.svg" alt="LeWitt-style wall drawing in four panels, each one direction of lines" style="max-height: 52vh;" />
  <div class="asq-medium">wall-drawing <span class="asq-accent">specifications</span>, installed by others &mdash; "as if by machine"</div>
</div>

---
section: 'Art and Science'
---

<div class="asq-stage">
  <div class="asq-large">Donald Knuth</div>
  <div class="asq-small asq-accent asq-smallcaps">b. 1938 &nbsp;·&nbsp; <em>The Art of Computer Programming</em></div>
  <img src="./diagram/static/knuth-quadratic.svg" alt="rendered math: 'The quadratic formula is' followed by (-b ± √(b² − 4ac)) / 2a" style="display: block; margin: 1.8rem auto; max-height: 36vh; max-width: 80%;" />
  <div class="asq-medium"><span class="asq-accent">literate programming</span> &mdash; formal and informal text, machine-executable and human-readable</div>
  <div class="asq-credit" style="margin-top: 0.6rem;">"Algorithm" illustration, Wikipedia &mdash; public-domain math rendering</div>
</div>

---
section: 'Art and Science'
---

<div class="asq-stage">
  <div class="asq-large">Made with AI</div>
  <div class="asq-medium" style="margin-top: 1.8rem;">LeWitt's idea was to <span class="asq-accent">specify art</span> so the artifact could be made without skill.</div>
  <div class="asq-medium" style="margin-top: 1.2rem;">Knuth's idea was that computer programs made with <span class="asq-accent">only skill</span> are not art.</div>
  <div class="asq-medium" style="margin-top: 2.0rem;">I wrote a specification for these slides &mdash;</div>
  <div class="asq-medium">a very-skilled, lifeless artist made them</div>
  <div class="asq-small asq-mono" style="margin-top: 1.6rem;">
    <a href="https://github.com/jmacd/algorithms-side-quest/blob/main/README.md">github.com/jmacd/algorithms-side-quest</a>
  </div>
</div>

---
section: 'Art and Science'
---

<div class="asq-stage">
  <div class="asq-large">About the title</div>
  <div class="asq-medium" style="margin-top: 0.8rem;">video games &nbsp;&middot;&nbsp; so many algorithms</div>
  <img class="asq-figure-half" src="./diagram/out/28-about-title.svg" alt="3D rendering setup: camera, view frustum, teapot in scene, bee in flight" style="max-height: 56vh;" />
</div>
