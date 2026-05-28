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

<style>
:root {
  --asq-yellow: #fce3a4;
  --asq-golden: #fdb913;
  --asq-ink: #000000;
}
.slidev-layout {
  background: #ffffff;
  color: var(--asq-ink);
  font-family: 'Roboto', system-ui, sans-serif;
  padding: 2.2rem 2.8rem 2.2rem 2.8rem !important;
}
.asq-mono { font-family: 'Roboto Mono', ui-monospace, monospace; }
.asq-smallcaps {
  font-variant-caps: small-caps;
  letter-spacing: 0.06em;
}
.asq-large { font-size: 4.6rem; line-height: 1.05; font-weight: 600; }
.asq-medium { font-size: 2.2rem; line-height: 1.2; }
.asq-small { font-size: 1.5rem; line-height: 1.3; }
.asq-tiny { font-size: 1.05rem; line-height: 1.25; color: #555; }
.asq-accent { color: var(--asq-golden); }
.asq-header {
  position: absolute;
  top: 1.4rem;
  left: 2.4rem;
  right: 2.4rem;
  font-size: 1.05rem;
  font-weight: 500;
  color: #555;
  letter-spacing: 0.02em;
}
.asq-stage {
  position: absolute;
  top: 0; left: 0; right: 0; bottom: 2rem;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  text-align: center;
  gap: 1.2rem;
  padding: 3.5rem 3rem 2rem 3rem;
}
.asq-section-title {
  position: absolute;
  top: 25%;
  left: 0; right: 0;
  text-align: center;
  font-size: 3.6rem;
  font-variant-caps: small-caps;
  letter-spacing: 0.08em;
  font-weight: 700;
  transform: translateY(-50%);
}
.asq-section-spot {
  position: absolute;
  top: 40%;
  left: 6%;
  right: 6%;
  bottom: 8%;
  display: flex;
  align-items: center;
  justify-content: center;
}
.asq-section-spot img { max-width: 100%; max-height: 100%; object-fit: contain; }
.asq-title-block {
  position: absolute;
  top: 20%;
  left: 0; right: 0;
  text-align: center;
  transform: translateY(-30%);
}
.asq-title-spot {
  position: absolute;
  top: 38%;
  left: 4%;
  right: 4%;
  bottom: 6%;
  display: flex;
  align-items: center;
  justify-content: center;
}
.asq-title-spot img { max-width: 100%; max-height: 100%; object-fit: contain; }
.asq-figure {
  display: block;
  margin: 0 auto;
  max-height: 76vh;
  max-width: 92vw;
}
.asq-figure-tall {
  display: block;
  margin: 0 auto;
  max-height: 82vh;
  max-width: 88vw;
}
.asq-list {
  list-style: none;
  padding: 0;
  margin: 0;
}
.asq-list li {
  font-family: 'Roboto Mono', ui-monospace, monospace;
  font-size: 1.55rem;
  line-height: 1.6;
}
.asq-code {
  font-family: 'Roboto Mono', ui-monospace, monospace;
  font-size: 1.6rem;
  text-align: left;
  background: #fafafa;
  border-left: 6px solid var(--asq-golden);
  padding: 1rem 1.4rem;
  white-space: pre;
}
.asq-caption {
  font-size: 1.0rem;
  color: #666;
  font-style: italic;
  margin-top: 0.6rem;
}
</style>

<div class="asq-title-block">
  <div class="asq-large">Algorithms Side Quest</div>
  <div class="asq-medium" style="margin-top: 0.8rem;">
    Joshua MacDonald · <span class="asq-mono">May 28, 2026</span>
  </div>
</div>

<div class="asq-title-spot">
  <img src="./diagram/out/01-spot-bees.svg" alt="three bees over poppies" />
</div>

---
section: 'I ❤️️ Algorithms'
---

<div class="asq-section-title">I ❤️ Algorithms</div>
<div class="asq-section-spot">
  <img src="./diagram/out/02-spot-euclid.svg" alt="Euclid GCD flow chart" />
</div>

---
section: 'I ❤️️ Algorithms'
---

<div class="asq-header">¶ How many ways</div>

<div class="asq-stage">
  <div class="asq-large">How many ways to make</div>
  <div class="asq-large asq-mono asq-accent">$1.00</div>
  <div class="asq-medium">from <span class="asq-mono">5¢</span>, <span class="asq-mono">10¢</span>, and <span class="asq-mono">25¢</span> coins?</div>
</div>

---
section: 'I ❤️️ Algorithms'
---

<div class="asq-header">¶ There's an algorithm for this problem</div>

<div class="asq-stage">
  <div class="asq-large">There's an <span class="asq-accent">algorithm</span>.</div>
  <img class="asq-figure" src="./diagram/out/03-al-khwarizmi.svg" alt="al-Khwarizmi manuscript placeholder" />
</div>

---
section: 'I ❤️️ Algorithms'
---

<div class="asq-header">¶ An algorithm is…</div>

<div class="asq-stage">
  <img class="asq-figure" src="./diagram/out/04-gcd-subtractions.svg" alt="GCD by successive subtraction" />
</div>

---
section: 'I ❤️️ Algorithms'
---

<div class="asq-header">¶ A sequence of steps</div>

<div class="asq-stage">
  <img class="asq-figure" src="./diagram/out/05-banana-bread.svg" alt="banana bread recipe card" />
</div>

---
section: 'I ❤️️ Algorithms'
---

<div class="asq-header">¶ A precise mathematical procedure</div>

<div class="asq-stage">
  <div class="asq-code">p = 3
for i in range(1, 100):
    p += 4 / ((2 * i) * (2 * i + 1) * (2 * i + 2)) * (-1) ** (i + 1)
print(p)</div>
  <div class="asq-caption">Nilakantha series for computing π</div>
</div>

---
section: 'I ❤️️ Algorithms'
---

<div class="asq-header">¶ Equations define solutions</div>

<div class="asq-stage">
  <div class="asq-medium">Equations define solutions.</div>
  <div class="asq-medium">They don't say how to find them.</div>
  <img class="asq-figure" src="./diagram/out/06-equation.svg" alt="100 = 5x + 10y + 25z" />
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

<div class="asq-header">¶ Refrigerator search</div>

<div class="asq-stage" style="align-items: flex-start; text-align: left; padding-left: 5rem;">
  <div class="asq-medium"><span class="asq-accent asq-smallcaps">Problem</span>&nbsp;&nbsp;find the ketchup</div>
  <div class="asq-medium asq-smallcaps asq-accent" style="margin-top: 1.2rem;">Algorithm</div>
  <ol class="asq-list" style="padding-left: 1.2rem;">
    <li>1. Pick any item.</li>
    <li>2. Is it ketchup? If yes, go to step 4.</li>
    <li>3. Put it on the counter. Go to step 1.</li>
    <li>4. Return items to the refrigerator.</li>
  </ol>
</div>

---
section: 'Every-day algorithms'
---

<div class="asq-header">¶ Mowing a lawn</div>

<div class="asq-stage">
  <div class="asq-large">Mowing a lawn</div>
  <div class="asq-medium"><span class="asq-accent asq-smallcaps">Problem</span>&nbsp;&nbsp;cover the entire lawn</div>
  <div class="asq-medium"><span class="asq-accent asq-smallcaps">Algorithm</span>&nbsp;&nbsp;depends!</div>
</div>

---
section: 'Every-day algorithms'
---

<div class="asq-header">¶ Count the houses in town</div>

<div class="asq-stage">
  <img class="asq-figure" src="./diagram/out/08-fort-bragg.svg" alt="Fort Bragg street grid" />
</div>

---
section: 'Every-day algorithms'
---

<div class="asq-header">¶ Evaluating algorithms</div>

<div class="asq-stage">
  <div class="asq-medium">searching · sorting · routing · counting…</div>
  <div class="asq-large" style="margin-top: 2rem;">How much <span class="asq-accent">time</span>?</div>
  <div class="asq-large">How much <span class="asq-accent">memory</span>?</div>
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

<div class="asq-header">¶ Decimal numbers</div>

<div class="asq-stage">
  <div class="asq-large">Decimal</div>
  <div class="asq-medium">digits <span class="asq-mono asq-accent">0</span> … <span class="asq-mono asq-accent">9</span></div>
  <div class="asq-medium">place values are powers of <span class="asq-mono asq-accent">10</span></div>
  <div class="asq-code" style="margin-top: 1rem;">5678₁₀ = 5·10³ + 6·10² + 7·10¹ + 8·10⁰</div>
</div>

---
section: 'Counting exercises'
---

<div class="asq-header">¶ Binary numbers</div>

<div class="asq-stage">
  <div class="asq-large">Binary</div>
  <div class="asq-medium">digits <span class="asq-mono asq-accent">0</span> and <span class="asq-mono asq-accent">1</span></div>
  <div class="asq-medium">place values are powers of <span class="asq-mono asq-accent">2</span></div>
  <div class="asq-code" style="margin-top: 1rem;">1111₂ = 1·2³ + 1·2² + 1·2¹ + 1·2⁰</div>
</div>

---
section: 'Counting exercises'
---

<div class="asq-header">¶ Bits</div>

<div class="asq-stage">
  <div class="asq-large">a <span class="asq-accent">bit</span></div>
  <div class="asq-medium">one binary place value</div>
  <div class="asq-large asq-mono"><span class="asq-accent">0</span>&nbsp;&nbsp;or&nbsp;&nbsp;<span class="asq-accent">1</span></div>
</div>

---
section: 'Counting exercises'
---

<div class="asq-header">¶ Bytes</div>

<div class="asq-stage">
  <div class="asq-large">8 bits = 1 <span class="asq-accent">byte</span></div>
  <img class="asq-figure" src="./diagram/out/10-byte-register.svg" alt="8-bit register equals 106" />
</div>

---
section: 'Counting exercises'
---

<div class="asq-header">¶ Counting to 256</div>

<div class="asq-stage">
  <div class="asq-large asq-mono">2⁸ = 256</div>
  <img class="asq-figure" src="./diagram/out/11-count-256.svg" alt="counting from 0 to 255" />
</div>

---
section: 'Counting exercises'
---

<div class="asq-header">¶ Counting to 4,294,967,296</div>

<div class="asq-stage">
  <img class="asq-figure-tall" src="./diagram/out/12-four-byte-register.svg" alt="32-bit register" />
</div>

---
section: 'Counting exercises'
---

<div class="asq-header">¶ Counting quintillions</div>

<div class="asq-stage">
  <div class="asq-medium">rule of thumb</div>
  <div class="asq-large asq-mono">10 bits ≈ <span class="asq-accent">1,000</span></div>
  <div class="asq-medium asq-mono">2¹⁰ = 1,024 &nbsp;·&nbsp; 10³ = 1,000</div>
  <div class="asq-medium asq-mono" style="margin-top: 1rem;">
    30 bits ≈ <span class="asq-accent">1 billion</span><br/>
    60 bits ≈ <span class="asq-accent">1 quintillion</span><br/>
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

<div class="asq-header">¶ Solve one problem in a group…</div>

<div class="asq-stage">
  <div class="asq-medium">Travelling Salesman</div>
  <img class="asq-figure" src="./diagram/out/14-tsp.svg" alt="5-city TSP circuit" />
  <div class="asq-caption">no known fast algorithm — try every combination</div>
</div>

---
section: 'Change the problem'
---

<div class="asq-header">¶ Solve them all</div>

<div class="asq-stage">
  <div class="asq-medium">A fast Travelling Salesman is a fast Sudoku.</div>
  <img class="asq-figure" src="./diagram/out/15-sudoku.svg" alt="partial sudoku board" />
  <div class="asq-caption">thousands of problems in this class</div>
</div>

---
section: 'Change the problem'
---

<div class="asq-header">¶ Euclidean algorithm</div>

<div class="asq-stage">
  <div class="asq-medium">greatest common divisor — Euclid, c. 300 BC</div>
  <div class="asq-code">// greatest common divisor of two numbers
func gcd2(a, b int) int {
    if b == 0 { return a }
    if a == 0 { return b }
    if a &gt; b { return gcd2(a-b, b) }
    return gcd2(a, b-a)
}</div>
  <div class="asq-caption">a recursive algorithm</div>
</div>

---
section: 'Change the problem'
---

<div class="asq-header">¶ Without pennies</div>

<div class="asq-stage">
  <div class="asq-code">// greatest common divisor of N numbers
func gcdN(a []int) int {
    if len(a) &lt; 2 { return a[0] }
    return gcd2(a[0], gcdN(a[1:]))
}</div>
  <div class="asq-large asq-mono" style="margin-top: 1.4rem;">
    <span class="asq-accent">gcd</span>(5, 10, 25) = 5
  </div>
  <div class="asq-medium">$1.00 in {5, 10, 25} &nbsp;⇔&nbsp; $0.20 in {1, 2, 5}</div>
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

<div class="asq-header">¶ How many ways to make zero?</div>

<div class="asq-stage" style="align-items: flex-start; text-align: left; padding-left: 6rem;">
  <div class="asq-medium asq-mono">ways to make $0.00 with <span class="asq-accent">0</span> kinds of coins?&nbsp;&nbsp;<span class="asq-accent">1</span></div>
  <div class="asq-medium asq-mono">ways to make $0.00 with <span class="asq-accent">1</span> kind of coin?&nbsp;&nbsp;<span class="asq-accent">1</span></div>
  <div class="asq-medium asq-mono">ways to make $0.00 with <span class="asq-accent">2</span> kinds of coins?&nbsp;&nbsp;<span class="asq-accent">1</span></div>
  <div class="asq-caption" style="margin-top: 2rem;">axiom — all empty sets are the same</div>
</div>

---
section: 'Counting from zero'
---

<div class="asq-header">¶ All pennies</div>

<div class="asq-stage" style="align-items: flex-start; text-align: left; padding-left: 6rem;">
  <div class="asq-medium asq-mono">ways to make $0.20 with all pennies?&nbsp;&nbsp;<span class="asq-accent">1</span></div>
  <div class="asq-medium asq-mono">ways to make $0.19 with all pennies?&nbsp;&nbsp;<span class="asq-accent">1</span></div>
  <div class="asq-medium asq-mono" style="opacity: 0.55;">…</div>
  <div class="asq-medium asq-mono">ways to make $0.01 with all pennies?&nbsp;&nbsp;<span class="asq-accent">1</span></div>
  <div class="asq-medium asq-mono">ways to make $0.00 with all pennies?&nbsp;&nbsp;<span class="asq-accent">1</span></div>
</div>

---
section: 'Counting from zero'
---

<div class="asq-header">¶ All 5 cents</div>

<div class="asq-stage" style="align-items: flex-start; text-align: left; padding-left: 6rem;">
  <div class="asq-medium asq-mono">ways to make $0.00 with all 5¢ coins?&nbsp;&nbsp;<span class="asq-accent">1</span></div>
  <div class="asq-medium asq-mono">ways to make $0.01 with all 5¢ coins?&nbsp;&nbsp;<span class="asq-accent">0</span></div>
  <div class="asq-medium asq-mono">ways to make $0.02 with all 5¢ coins?&nbsp;&nbsp;<span class="asq-accent">0</span></div>
  <div class="asq-medium asq-mono">ways to make $0.03 with all 5¢ coins?&nbsp;&nbsp;<span class="asq-accent">0</span></div>
  <div class="asq-medium asq-mono">ways to make $0.04 with all 5¢ coins?&nbsp;&nbsp;<span class="asq-accent">0</span></div>
  <div class="asq-medium asq-mono">ways to make $0.05 with all 5¢ coins?&nbsp;&nbsp;<span class="asq-accent">1</span></div>
</div>

---
section: 'Counting from zero'
---

<div class="asq-header">¶ Row formation</div>

<div class="asq-stage">
  <img class="asq-figure" src="./diagram/out/17-row-formation.svg" alt="row of 21 cells for 5¢ coin counts" />
</div>

---
section: 'Counting from zero'
---

<div class="asq-header">¶ Variables</div>

<div class="asq-stage" style="align-items: flex-start; text-align: left; padding-left: 9rem;">
  <div class="asq-large asq-mono"><span class="asq-accent">A</span> &nbsp;=&nbsp; amount</div>
  <div class="asq-large asq-mono"><span class="asq-accent">K</span> &nbsp;=&nbsp; number of existing coins</div>
  <div class="asq-large asq-mono"><span class="asq-accent">N</span> &nbsp;=&nbsp; count of ways to make A with K coins</div>
  <div class="asq-large asq-mono"><span class="asq-accent">C</span> &nbsp;=&nbsp; value of a K+1th coin</div>
</div>

---
section: 'Counting from zero'
---

<div class="asq-header">¶ Recursion relation in words</div>

<div class="asq-stage">
  <div class="asq-medium">add coin <span class="asq-mono asq-accent">C</span> as the next coin</div>
  <div class="asq-medium"><span class="asq-mono asq-accent">N</span> ways to make <span class="asq-mono asq-accent">A</span> with <span class="asq-mono asq-accent">K</span> coins</div>
  <div class="asq-medium"><span class="asq-mono asq-accent">N'</span> ways to make <span class="asq-mono asq-accent">A'</span> with <span class="asq-mono asq-accent">K+1</span> coins</div>
  <img class="asq-figure" src="./diagram/out/18-recursion-two-row.svg" alt="recursion relation two-row diagram" style="max-height: 50vh;" />
</div>

---
section: 'Counting from zero'
---

<div class="asq-header">¶ Recursion relation diagram &nbsp;·&nbsp; dynamic programming</div>

<div class="asq-stage">
  <img class="asq-figure-tall" src="./diagram/out/19-dp-diagram.svg" alt="3-row by 21-column DP grid with coloured arrows" />
</div>

---
section: 'Counting from zero'
---

<div class="asq-header">¶ Recursion relation in words (again)</div>

<div class="asq-stage">
  <div class="asq-medium">above &nbsp;·&nbsp; count to <span class="asq-mono asq-accent">A</span> without C is <span class="asq-mono asq-accent">N</span></div>
  <div class="asq-medium">below &nbsp;·&nbsp; count to <span class="asq-mono asq-accent">A'</span> with C is <span class="asq-mono asq-accent">N'</span></div>
  <div class="asq-medium">with &nbsp;·&nbsp; <span class="asq-mono asq-accent">A' + C = A</span></div>
  <div class="asq-medium">then &nbsp;·&nbsp; count to <span class="asq-mono asq-accent">A</span> with C is <span class="asq-mono asq-accent">N + N'</span></div>
  <img class="asq-figure" src="./diagram/out/20-recursion-two-row-filled.svg" alt="recursion relation with sum N+N' filled in" style="max-height: 44vh;" />
</div>
