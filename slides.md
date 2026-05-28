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
  <img class="asq-figure-half" src="./diagram/out/03-al-khwarizmi.svg" alt="al-Khwarizmi manuscript card" />
</div>

---
section: 'I ❤️ Algorithms'
---

<div class="asq-stage">
  <div class="asq-large">An algorithm is…</div>
  <img class="asq-figure-half" src="./diagram/out/04-gcd-subtractions.svg" alt="GCD by successive subtraction" />
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
  <pre class="asq-code">// greatest common divisor of N numbers
func gcdN(a []int) int {
    if len(a) &lt; 2 { return a[0] }
    return gcd2(a[0], gcdN(a[1:]))
}</pre>
  <div class="asq-large asq-mono" style="margin-top: 1.6rem;">
    <span class="asq-accent">gcd</span>(5, 10, 25) = 5
  </div>
  <div class="asq-medium">$1.00 in { 5, 10, 25 }    ⇔    $0.20 in { 1, 2, 5 }</div>
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
  <div class="asq-medium asq-mono">ways to make $0.00 with <span class="asq-accent">0</span> kinds of coins?   <span class="asq-accent">1</span></div>
  <div class="asq-medium asq-mono">ways to make $0.00 with <span class="asq-accent">1</span> kind of coin?   <span class="asq-accent">1</span></div>
  <div class="asq-medium asq-mono">ways to make $0.00 with <span class="asq-accent">2</span> kinds of coins?   <span class="asq-accent">1</span></div>
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

<div class="asq-stage">
  <div class="asq-medium">above   ·   count to <span class="asq-mono asq-accent">A</span> without <span class="asq-mono asq-accent">C</span> is <span class="asq-mono asq-accent">N</span></div>
  <div class="asq-medium">below   ·   count to <span class="asq-mono asq-accent">A'</span> with <span class="asq-mono asq-accent">C</span> is <span class="asq-mono asq-accent">N'</span></div>
  <div class="asq-medium">with   ·   <span class="asq-mono asq-accent">A' + C = A</span></div>
  <div class="asq-medium">then   ·   count to <span class="asq-mono asq-accent">A</span> with <span class="asq-mono asq-accent">C</span> is <span class="asq-mono asq-accent">N + N'</span></div>
  <img class="asq-figure-half" src="./diagram/out/20-recursion-two-row-filled.svg" alt="recursion relation with sum N+N' filled in" style="margin-top: 0.4rem;" />
</div>
