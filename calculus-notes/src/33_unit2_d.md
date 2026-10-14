# Applications of derivatives (I) {.u2 data-eyebrow="Unit II · Chapter 17"}

::: {.idea t="Big idea"}
Now the derivative earns its keep. In this chapter it answers four practical questions: **How fast is it changing?** (rates), **Is it going up or down?** (monotonicity), **What does the curve look like at this point?** (tangents and normals), and **What is a quick estimate?** (approximations).
:::

## 17.1 Rate of change and related rates

$\dfrac{dy}{dx}$ is the **rate of change of $y$ with respect to $x$**. If $x$ and $y$ both depend on time $t$, the chain rule links their rates:
$$\frac{dy}{dx}=\frac{dy/dt}{dx/dt}\quad\left(\frac{dx}{dt}\ne0\right),\qquad\frac{dA}{dt}=\frac{dA}{dr}\cdot\frac{dr}{dt}.$$
**Sign:** $\dfrac{dy}{dx}>0$ if $y$ increases as $x$ increases; $<0$ if $y$ decreases.

::: {.idea t="The 5-step recipe for related-rates problems"}
1. **Draw** a picture and name every changing quantity ($x,y,r,V,\dots$). Treat each as a function of time $t$.
2. **Write one equation** linking them (a formula from geometry, Pythagoras, ...).
3. **Differentiate both sides with respect to $t$** (chain rule!).
4. **Only now substitute** the numbers for the instant asked about. (Substituting before differentiating freezes the variables and gives nonsense.)
5. Solve and state the answer **with units and sign** (negative $=$ decreasing).
:::

::: {.ex t="Example 17.1: a growing ripple"}
A stone makes circular ripples whose radius grows at $4$ cm/s. How fast is the area increasing when $r=10$ cm?

::: sol
$A=\pi r^2\Rightarrow\dfrac{dA}{dt}=2\pi r\dfrac{dr}{dt}=2\pi(10)(4)=\mathbf{80\pi\ cm^2/s}$.
:::
:::

::: {.ex t="Example 17.2: the cube"}
A cube's volume grows at $9$ cm$^3$/s. How fast is its surface area growing when the edge is $10$ cm?

::: sol
$V=x^3\Rightarrow9=3x^2\dfrac{dx}{dt}\Rightarrow\dfrac{dx}{dt}=\dfrac3{x^2}$. $S=6x^2\Rightarrow\dfrac{dS}{dt}=12x\dfrac{dx}{dt}=\dfrac{36}{x}=\mathbf{3.6\ cm^2/s}$ at $x=10$.
:::
:::

::: {.ex t="Example 17.3: the sliding ladder"}
A 5 m ladder leans on a wall. Its foot is pulled away at $2$ cm/s. How fast does its top slide down when the foot is $4$ m from the wall?

![The ladder: $x^2+y^2=25$.](figs/fig_ladder.svg){width=32%}

::: sol
$x^2+y^2=25\Rightarrow2x\dfrac{dx}{dt}+2y\dfrac{dy}{dt}=0\Rightarrow\dfrac{dy}{dt}=-\dfrac xy\dfrac{dx}{dt}$. When $x=4$, $y=3$: $\dfrac{dy}{dt}=-\dfrac43(2)=-\dfrac83$. The top **slides down at $\tfrac83$ cm/s**.
:::
:::

::: {.ex t="Example 17.4: two more classics"}
**Balloon.** A spherical balloon is inflated at $900$ cm$^3$/s. At $r=15$ cm: $V=\frac43\pi r^3\Rightarrow\frac{dV}{dt}=4\pi r^2\frac{dr}{dt}$, so $\dfrac{dr}{dt}=\dfrac{900}{4\pi\cdot225}=\dfrac1\pi$ cm/s.

**Sand cone.** Sand pours at $12$ cm$^3$/s into a cone whose height is always $\frac16$ of the base radius, so $r=6h$. $V=\frac13\pi r^2h=12\pi h^3$, $\frac{dV}{dt}=36\pi h^2\frac{dh}{dt}=12$. At $h=4$: $\dfrac{dh}{dt}=\dfrac{12}{36\pi\cdot16}=\dfrac1{48\pi}$ cm/s.
:::

::: {.ex t="Example 17.5: rectangle with two changing sides"}
Length $x$ decreases at $3$ cm/min, width $y$ increases at $2$ cm/min. At $x=10,\ y=6$: perimeter $P=2(x+y)$ gives $\dfrac{dP}{dt}=2(-3+2)=-2$ cm/min. Area $A=xy$ gives $\dfrac{dA}{dt}=y\dfrac{dx}{dt}+x\dfrac{dy}{dt}=6(-3)+10(2)=\mathbf2$ cm$^2$/min.
:::

**Marginal cost and revenue (economics).** If $C(x)$ is the total cost of producing $x$ items, the **marginal cost** $MC=\dfrac{dC}{dx}$ is the instantaneous rate of change of cost, approximately the cost of making **one more** item. Likewise the marginal revenue $MR=\dfrac{dR}{dx}$.

::: {.ex t="Example 17.6"}
$C(x)=0.005x^3-0.02x^2+30x+5000$. Then $MC=0.015x^2-0.04x+30$; at $x=3$ this is $0.135-0.12+30=\text{Rs }30.015\approx30.02$. For $R(x)=3x^2+36x+5$: $MR=6x+36$, so at $x=5$, $MR=\text{Rs }66$.
:::

## 17.2 Increasing and decreasing functions

::: {.def t="Monotonic functions"}
On an interval $I$, $f$ is **increasing** if $x_1<x_2\Rightarrow f(x_1)\le f(x_2)$; **strictly increasing** if $f(x_1)<f(x_2)$. Reversing the inequality gives **decreasing** and **strictly decreasing**. "Increasing" means *the graph rises as you move left to right*.
:::

::: {.thm t="First-derivative test for monotonicity"}
If $f$ is continuous on $[a,b]$ and differentiable on $(a,b)$, then
$$f'(x)>0\ \forall x\in(a,b)\Rightarrow f\text{ increasing},\qquad f'(x)<0\Rightarrow f\text{ decreasing},\qquad f'(x)=0\Rightarrow f\text{ constant}.$$
(This is MVT: $f(x_2)-f(x_1)=f'(c)(x_2-x_1)$ has the sign of $f'(c)$.)
:::

::: {.idea t="The sign-chart method"}
1. Compute $f'(x)$.
2. Solve $f'(x)=0$ (and note where $f'$ is undefined): these **critical points** cut the line into intervals.
3. Pick a test point in each interval and find the **sign of $f'$** (or factorise and multiply signs).
4. Conclude: $+$ means increasing, $-$ means decreasing.
5. Because $f$ is continuous, you may include the endpoint critical points in both neighbouring intervals.
:::

![The sign of $f'$ (bottom) controls the direction of $f$ (top).](figs/fig_incdec.svg){width=60%}

::: {.ex t="Example 17.7: a cubic"}
$f(x)=4x^3-6x^2-72x+30$. $f'(x)=12x^2-12x-72=12(x-3)(x+2)$, zero at $x=-2,3$.

| Interval | $(-\infty,-2)$ | $(-2,3)$ | $(3,\infty)$ |
|---|---|---|---|
| sign of $f'=12(x-3)(x+2)$ | $(-)(-)=+$ | $(-)(+)=-$ | $(+)(+)=+$ |
| behaviour of $f$ | increasing | decreasing | increasing |

So $f$ is increasing on $(-\infty,-2]$ and $[3,\infty)$, decreasing on $[-2,3]$.
:::

::: {.ex t="Example 17.8: more from the textbook"}
- $f(x)=x^2-4x+6$: $f'=2x-4$; decreasing on $(-\infty,2]$, increasing on $[2,\infty)$.
- $f(x)=x^3-3x^2+4x$: $f'=3(x-1)^2+1>0$ for all $x$, so **strictly increasing on $\mathbb{R}$**.
- $f(x)=\sin3x$ on $[0,\frac\pi2]$: $f'=3\cos3x$ vanishes at $x=\frac\pi6$; increasing on $[0,\frac\pi6]$, decreasing on $[\frac\pi6,\frac\pi2]$.
- $y=x^2e^{-x}$: $y'=x(2-x)e^{-x}>0$ exactly for $0<x<2$, so increasing on $(0,2)$ (a practice MCQ).
- $f(x)=\cos x$: strictly decreasing on $(0,\pi)$, strictly increasing on $(\pi,2\pi)$.
:::

::: {.tip t="Proving inequalities with monotonicity"}
To show $e^x>1+x$ for $x>0$: let $g(x)=e^x-1-x$. Then $g(0)=0$ and $g'(x)=e^x-1>0$ for $x>0$, so $g$ increases from $0$ and stays positive.
:::

## 17.3 Tangents and normals

The **tangent** at a point touches the curve with the same direction; the **normal** is the perpendicular to the tangent at that point.

::: {.formula t="Tangent and normal at $(x_0,y_0)$ on $y=f(x)$"}
$$\text{slope of tangent}=f'(x_0)=\frac{dy}{dx}\Big|_{(x_0,y_0)}$$
$$\text{Tangent:}\quad y-y_0=f'(x_0)\,(x-x_0)$$
$$\text{Normal:}\quad y-y_0=-\frac{1}{f'(x_0)}(x-x_0)\quad\Longleftrightarrow\quad (y-y_0)f'(x_0)+(x-x_0)=0$$
:::

**Special cases.** If $f'(x_0)=0$ the tangent is **horizontal**: $y=y_0$ (and the normal is $x=x_0$). If $f'(x_0)\to\infty$ the tangent is **vertical**: $x=x_0$ (and the normal is $y=y_0$). If the tangent makes angle $\theta$ with the positive $x$-axis, $f'(x_0)=\tan\theta$.

![Tangent (teal) and normal (coral) to $y=x^2$ at $(1,1)$ are perpendicular.](figs/fig_tangent_normal.svg){width=52%}

::: {.ex t="Example 17.9: the basics"}
- Slope of the tangent to $y=x^3-x$ at $x=2$: $y'=3x^2-1=11$.
- Tangent and normal to $y=x^2$ at $(1,1)$: slope $2$, so tangent $y-1=2(x-1)$, i.e. $y=2x-1$; normal $y-1=-\frac12(x-1)$.
- Point where the tangent to $y=\sqrt{4x-3}-1$ has slope $\frac23$: $y'=\dfrac{2}{\sqrt{4x-3}}=\dfrac23\Rightarrow4x-3=9\Rightarrow x=3$, $y=2$. Point $(3,2)$.
- Practice MCQ: slope of the normal to $y=2x^2+3\sin x$ at $x=0$: $y'=4x+3\cos x=3$, so the normal has slope $-\tfrac13$.
:::

::: {.ex t="Example 17.10: tangents with a given slope"}
Find all tangents of slope $2$ to $y=-\dfrac{2}{x-3}$.

::: sol
$y'=\dfrac2{(x-3)^2}=2\Rightarrow(x-3)^2=1\Rightarrow x=2$ or $4$, giving points $(2,2)$ and $(4,-2)$. Tangents: $y-2=2(x-2)$, i.e. $y=2x-2$, and $y+2=2(x-4)$, i.e. $y=2x-10$.
:::
:::

::: {.ex t="Example 17.11: implicit curves"}
(a) On $\dfrac{x^2}4+\dfrac{y^2}{25}=1$: $\ y'=-\dfrac{25x}{4y}$. Tangent **horizontal** when $x=0$: points $(0,\pm5)$. Tangent **vertical** when $y=0$: points $(\pm2,0)$.

(b) Astroid $x^{2/3}+y^{2/3}=2$ at $(1,1)$: $y'=-\big(\frac yx\big)^{1/3}=-1$. Tangent $x+y-2=0$; normal $y=x$.

(c) The line $y=x+1$ touches $y^2=4x$ at $(1,2)$: $y'=\frac2y=1$ there ✓ (practice MCQ).
:::

::: {.ex t="Example 17.12: parametric curve"}
$x=a\sin^3t,\ y=b\cos^3t$ at $t=\frac\pi2$: $\dfrac{dy}{dx}=\dfrac{-3b\cos^2t\sin t}{3a\sin^2t\cos t}=-\dfrac ba\cot t=0$ at $t=\frac\pi2$; the point is $(a,0)$. Tangent: $y=0$.
:::

## 17.4 Approximations using differentials

For a tiny change $\Delta x=dx$ the true change $\Delta y=f(x+\Delta x)-f(x)$ is well approximated by the **differential** $dy=f'(x)\,dx$ (the change *along the tangent line*).

![$dy$ (change along the tangent) and $\Delta y$ (true change) are nearly equal when $dx$ is small.](figs/fig_differential.svg){width=58%}

::: {.formula t="Linear approximation"}
$$\boxed{f(x+\Delta x)\approx f(x)+f'(x)\,\Delta x}$$
$$\text{absolute error}=\abs{dy},\qquad\text{relative error}=\frac{dy}{y},\qquad\text{percentage error}=\frac{dy}{y}\times100$$
:::

::: {.tip t="How to choose $x$ and $\Delta x$"}
Pick the nearest **easy** number as $x$ (a perfect square for $\sqrt{\ }$, a perfect cube for $\sqrt[3]{\ }$) and let $\Delta x$ be the small remainder, which may be negative.
:::

::: {.ex t="Example 17.13: estimating roots"}
**$\sqrt{36.6}$:** $y=\sqrt x$, $x=36$, $\Delta x=0.6$. $dy=\dfrac1{2\sqrt{36}}(0.6)=0.05$. So $\sqrt{36.6}\approx6.05$ (true: $6.0498$).

**$(25)^{1/3}$:** $y=x^{1/3}$, $x=27$, $\Delta x=-2$. $dy=\dfrac1{3\cdot27^{2/3}}(-2)=\dfrac{-2}{27}\approx-0.074$. So $25^{1/3}\approx2.926$ (true: $2.924$).

**$\sqrt{25.3}$:** $x=25,\ \Delta x=0.3$: $dy=\frac{0.3}{10}=0.03$, so $\approx5.03$.
:::

::: {.ex t="Example 17.14: evaluating a polynomial nearby"}
$f(x)=3x^2+5x+3$. Estimate $f(3.02)$: $f(3)=45$, $f'(3)=6(3)+5=23$, so $f(3.02)\approx45+23(0.02)=45.46$. (Exact: $45.4612$.) Likewise (practice MCQ) for $f(x)=3x^2+15x+5$: $f(3)=77$, $f'(3)=33$, so $f(3.02)\approx77+33(0.02)=77.66$.
:::

::: {.ex t="Example 17.15: measurement errors"}
- Cube side increased by $2\%$: $dV=3x^2\,dx=3x^2(0.02x)=0.06x^3$, i.e. a $6\%$ increase in volume (percentage errors multiply by the power).
- Sphere radius measured as $9$ cm with error $0.03$ cm: $dV=4\pi r^2dr=4\pi(81)(0.03)=9.72\pi$ cm$^3$.
- Diameter of a sphere has error $0.02$ cm, radius $10$ cm (Jain Ex. 1.2): $dr=0.01$, $dV=4\pi(100)(0.01)=4\pi$, and $\dfrac{dV}V\times100=\dfrac{4\pi}{\frac43\pi\cdot1000}\times100=0.3\%$.
:::

# Maxima and minima {.u2 data-eyebrow="Unit II · Chapter 18"}

::: {.idea t="Big idea"}
Engineers, economists and scientists constantly ask: *what is the biggest, smallest, cheapest, fastest?* On a graph, the answers sit at the **tops of hills and bottoms of valleys**, exactly the places where the tangent is flat, i.e. where $f'=0$. Calculus turns "find the best" into "solve $f'(x)=0$".
:::

## 18.1 Vocabulary

::: {.def t="Local and absolute extrema"}
- $f$ has a **local maximum** at $c$ if $f(c)\ge f(x)$ for all $x$ **near** $c$ (in some $(c-h,c+h)$); a **local minimum** if $f(c)\le f(x)$ near $c$.
- $f$ has an **absolute (global) maximum** on an interval $I$ if $f(c)\ge f(x)$ for **all** $x\in I$; similarly an absolute minimum.
- The common word is **extremum** (plural *extrema*).
- A **critical point** of $f$ is an interior point $c$ where $f'(c)=0$ **or** $f'(c)$ does not exist.
:::

![Local extrema (hills and valleys) versus absolute extrema on $[a,b]$ (left). Right: a flat tangent need not mean an extremum.](figs/fig_extrema.svg){width=96%}

::: {.thm t="Fermat's necessary condition"}
If $f$ has a local maximum or minimum at an **interior** point $c$, then either $f'(c)=0$ or $f'(c)$ does not exist. *The converse is false:* $f(x)=x^3$ has $f'(0)=0$ but $0$ is neither a max nor a min (it is a **point of inflection**).
:::

So: **extrema can only hide at critical points** (and at end points of the interval). The tests below decide which critical points are real hills or valleys.

## 18.2 The first-derivative test

::: {.thm t="First-derivative test"}
Let $f$ be continuous at a critical point $c$.

- If $f'$ changes from $+$ to $-$ as $x$ increases through $c$: **local maximum**.
- If $f'$ changes from $-$ to $+$: **local minimum**.
- If $f'$ does **not** change sign: neither (a point of inflection).
:::

::: {.mem t="Walking picture"}
Going **up then down** you have crossed a peak ($+\to-$: max). Going **down then up** you have crossed a valley ($-\to+$: min).
:::

::: {.ex t="Example 18.1"}
$f(x)=x^3-3x+3$: $f'=3(x-1)(x+1)$, critical points $\pm1$. Sign of $f'$: $+$ for $x<-1$, $-$ for $-1<x<1$, $+$ for $x>1$. So **local max at $x=-1$** with value $f(-1)=5$, and **local min at $x=1$** with value $f(1)=1$. (The Chapter 17 figure plots $x^3-3x$, which has the same shape, shifted down by 3.)
:::

::: {.ex t="Example 18.2: no extremum"}
$f(x)=2x^3-6x^2+6x+5$: $f'=6(x-1)^2\ge0$ never changes sign, so $x=1$ is a point of inflection and $f$ has **no extrema**.
:::

::: {.ex t="Example 18.3: a corner can be an extremum"}
$f(x)=3+\abs x$ is not differentiable at $0$, so the second-derivative test fails; but $f'=-1<0$ for $x<0$ and $+1>0$ for $x>0$ ($-\to+$), so $x=0$ is a **local (and absolute) minimum** with value $3$.
:::

## 18.3 The second-derivative test

::: {.thm t="Second-derivative test"}
Let $f'(c)=0$ and let $f''$ exist at $c$.

- $f''(c)<0\ \Rightarrow$ **local maximum** at $c$ (curve bends like a cap $\frown$).
- $f''(c)>0\ \Rightarrow$ **local minimum** at $c$ (curve bends like a cup $\smile$).
- $f''(c)=0\ \Rightarrow$ **test fails**: use the first-derivative test (or the higher-order test below).
:::

::: {.ex t="Example 18.4"}
$f(x)=3x^4+4x^3-12x^2+12$. $f'=12x^3+12x^2-24x=12x(x-1)(x+2)$, critical points $0,1,-2$. $f''=36x^2+24x-24$:

| $c$ | $f''(c)$ | verdict | value |
|---|---|---|---|
| $0$ | $-24<0$ | local **max** | $f(0)=12$ |
| $1$ | $36>0$ | local **min** | $f(1)=7$ |
| $-2$ | $72>0$ | local **min** | $f(-2)=-20$ |

:::

::: {.thm t="Higher-order test (Jain, Theorem 1.6)"}
If $f'(c)=f''(c)=\cdots=f^{(n-1)}(c)=0$ but $f^{(n)}(c)\ne0$, then: **$n$ even** $\Rightarrow$ extremum (maximum if $f^{(n)}(c)<0$, minimum if $>0$); **$n$ odd** $\Rightarrow$ **no** extremum (inflection).
:::

*Example:* $f(x)=x^4$ has $f'(0)=f''(0)=f'''(0)=0$ and $f^{(4)}(0)=24>0$ ($n=4$ even): a minimum.

## 18.4 Absolute maximum and minimum on a closed interval

::: {.thm t="Extreme Value Theorem"}
A function **continuous on $[a,b]$** attains an absolute maximum and an absolute minimum there. (On an open interval it may attain neither: $f(x)=x$ on $(0,1)$ has no max or min.)
:::

::: {.idea t="Working rule for $[a,b]$"}
1. Find all critical points of $f$ **inside** $(a,b)$ ($f'=0$ or $f'$ undefined).
2. Add the **end points** $a$ and $b$.
3. Compute $f$ at every one of these points.
4. The **largest** value is the absolute maximum; the **smallest** is the absolute minimum.
:::

::: {.ex t="Example 18.5"}
$f(x)=2x^3-15x^2+36x+1$ on $[1,5]$. $f'=6(x-2)(x-3)$: critical points $2,3$. Values: $f(1)=24,\ f(2)=29,\ f(3)=28,\ f(5)=56$. **Absolute max $56$ at $x=5$; absolute min $24$ at $x=1$.**
:::

::: {.ex t="Example 18.6: a non-differentiable critical point"}
$f(x)=12x^{4/3}-6x^{1/3}$ on $[-1,1]$. $f'(x)=16x^{1/3}-2x^{-2/3}=\dfrac{2(8x-1)}{x^{2/3}}$: zero at $x=\frac18$, undefined at $x=0$. Both are critical points. Values: $f(-1)=18,\ f(0)=0,\ f(\tfrac18)=-\tfrac94,\ f(1)=6$. **Absolute max $18$ at $x=-1$; absolute min $-\frac94$ at $x=\frac18$.**
:::

::: {.ex t="Example 18.7: trigonometric"}
$f(x)=\sin x+\cos x$ on $[0,\pi]$: $f'=\cos x-\sin x=0\Rightarrow x=\frac\pi4$. $f(0)=1,\ f(\frac\pi4)=\sqrt2,\ f(\pi)=-1$. Max $\sqrt2$, min $-1$.
:::

## 18.5 Optimisation: the word-problem method

::: {.idea t="The six-step recipe"}
1. **Draw** a diagram; name the variables.
2. **Write the quantity $Q$** to be maximised/minimised.
3. **Write the constraint** that links the variables.
4. **Eliminate** to get $Q$ as a function of **one** variable; state its domain.
5. **Differentiate**, set $Q'=0$, and test the critical points (second derivative, sign change, or end points).
6. **Answer the question asked**, with units.
:::

::: {.ex t="Example 18.8: minimum sum of squares"}
Two positive numbers sum to $15$; minimise the sum of their squares. Let them be $x$ and $15-x$: $S=x^2+(15-x)^2$, $S'=4x-30=0\Rightarrow x=\frac{15}2$, $S''=4>0$ (min). Both numbers are $7.5$. *(In general, for a fixed sum the sum of squares is smallest when the numbers are equal.)*
:::

::: {.ex t="Example 18.9: the open box"}
A square tin sheet of side $18$ cm has a square of side $x$ cut from each corner and the flaps are folded up to make an open box. Maximise the volume.

![Cut-and-fold box and its volume curve.](figs/fig_box.svg){width=92%}

::: sol
Base side $18-2x$, height $x$: $V=x(18-2x)^2$, $0<x<9$. $V'=(18-2x)^2-4x(18-2x)=(18-2x)(18-6x)=0\Rightarrow x=3$ (not $9$). $V''=24x-144$ gives $V''(3)=-72<0$: a maximum. $V_{\max}=3\cdot12^2=\mathbf{432\ cm^3}$.

For the textbook's $45\times24$ sheet: $V=x(45-2x)(24-2x)$, $V'=12(x-5)(x-18)$; only $x=5$ is allowed ($x<12$).
:::
:::

::: {.ex t="Example 18.10: rectangle in a circle"}
Of all rectangles inscribed in a circle of radius $R$, the **square** has the greatest area. Let one side be $x$; the diagonal is $2R$, so the other side is $\sqrt{4R^2-x^2}$ and $A=x\sqrt{4R^2-x^2}$. Maximise $A^2=x^2(4R^2-x^2)$: $\frac{d}{dx}=8R^2x-4x^3=0\Rightarrow x^2=2R^2$, so both sides equal $R\sqrt2$: a square of area $2R^2$.
:::

::: {.ex t="Example 18.11: cylinder in a cone"}
A right circular cylinder is inscribed in a cone of base radius $r$ and height $h$. Show the cylinder of greatest curved surface has radius $\frac r2$.

![Cross-section of the cone with the cylinder of radius $x$.](figs/fig_cone_cyl.svg){width=36%}

::: sol
By similar triangles the cylinder's height is $\dfrac{h(r-x)}{r}$. Curved surface $S=2\pi x\cdot\dfrac{h(r-x)}r=\dfrac{2\pi h}{r}(rx-x^2)$. $S'=\dfrac{2\pi h}{r}(r-2x)=0\Rightarrow x=\frac r2$, and $S''=-\frac{4\pi h}r<0$: a maximum. ✓
:::
:::

::: {.ex t="Example 18.12: the cheapest can"}
A closed cylindrical can must hold $100$ cm$^3$. Minimise the surface area.

::: sol
$V=\pi r^2h=100\Rightarrow h=\dfrac{100}{\pi r^2}$. $S=2\pi r^2+2\pi rh=2\pi r^2+\dfrac{200}{r}$. $S'=4\pi r-\dfrac{200}{r^2}=0\Rightarrow r^3=\dfrac{50}{\pi}$, $r\approx2.52$ cm, and then $h=2r\approx5.03$ cm. **The best can has height equal to its diameter.** $S''=4\pi+\frac{400}{r^3}>0$ confirms a minimum.
:::
:::

::: {.ex t="Example 18.13: a wire cut in two"}
A $28$ m wire is cut; one piece forms a square, the other a circle. Minimise the total area.

::: sol
Square piece $x$ (side $\frac x4$), circle piece $28-x$ (radius $\frac{28-x}{2\pi}$): $A=\dfrac{x^2}{16}+\dfrac{(28-x)^2}{4\pi}$. $A'=\dfrac x8-\dfrac{28-x}{2\pi}=0\Rightarrow x=\dfrac{112}{\pi+4}$. The pieces are $\dfrac{112}{\pi+4}$ m (square) and $\dfrac{28\pi}{\pi+4}$ m (circle).
:::
:::

::: {.ex t="Example 18.14: nearest approach"}
A helicopter flies along $y=x^2+7$; a soldier is at $(3,7)$. The squared distance is $D^2=(x-3)^2+x^4$, with derivative $2(x-3)+4x^3=2(x-1)(2x^2+2x+3)$. The quadratic factor has no real roots, so the only critical point is $x=1$, where $D^2=4+1=5$. Check: at $x=0$, $D^2=9>5$. **Nearest distance $\sqrt5$.** *(Minimise $D^2$, not $D$: same location, no square root.)*
:::

::: {.ex t="Example 18.15: business and projectiles"}
- **Profit** $p(x)=41-24x-18x^2$: $p'=-24-36x=0\Rightarrow x=-\frac23$, $p=49$.
- **Ball** thrown from a 60 m building follows $h(x)=60+x-\dfrac{x^2}{60}$: $h'=1-\frac{x}{30}=0\Rightarrow x=30$, so the maximum height is $60+30-15=\mathbf{75\ m}$.
- **Orange grove** profit $P(x)=ax+bx^2$ ($b<0$): maximised at $x=-\dfrac a{2b}$ trees per acre.
- **Right triangle with hypotenuse $h$:** area $\frac12x\sqrt{h^2-x^2}$ is maximal when $x=\frac h{\sqrt2}$ (an isosceles right triangle), with area $\frac{h^2}4$ (Jain Ex. 1.14).
:::

::: {.tip t="Common optimisation checks"}
- Always find the **domain** (lengths positive, $x<9$ in the box problem).
- Reject critical points outside the domain.
- If the end points make physical sense, **compare** the critical-point value with the end values.
- Minimising $D$ and $D^2$ gives the same point; use $D^2$ to avoid square roots.
:::

## 18.6 Concavity and inflection (a short note)

$f''>0$ on an interval: the curve is **concave up** (holds water, like a cup). $f''<0$: **concave down**. A **point of inflection** is where concavity changes (e.g. $x=0$ for $x^3$, where $f''=6x$ changes sign). That is why the second-derivative test works: a critical point with $f''>0$ sits at the bottom of a cup.

# Unit II: practice and answers {.u2 data-eyebrow="Unit II · Chapter 19"}

## 19.1 Your professor's differentiation MCQs (Q1–Q15 of the deck)

| Q | Question | Ans | Working |
|---|---|---|---|
| 1 | $\frac{d}{dx}x^5$ | **B** | $5x^4$ |
| 2 | $\frac{d}{dx}\sin x$ | **A** | $\cos x$ |
| 3 | $\frac{d}{dx}e^{2x}$ | **C** | $2e^{2x}$ (chain rule) |
| 4 | $\frac{d}{dx}\ln x$ | **D** | $1/x$ |
| 5 | $\frac{d}{dx}(x\sin x)$ | **A** | $\sin x+x\cos x$ |
| 6 | $\frac{d}{dx}\frac{x}{x+1}$ | **B** | $\frac{(x+1)-x}{(x+1)^2}=\frac1{(x+1)^2}$ |
| 7 | $\frac{d}{dx}\sin(x^2)$ | **C** | $2x\cos(x^2)$ |
| 8 | $\frac{d}{dx}\tan x$ | **D** | $\sec^2x$ |
| 9 | $\frac{d}{dx}a^x$ | **B** | $a^x\ln a$ |
| 10 | $\frac{d}{dx}\tan^{-1}x$ | **A** | $\frac1{1+x^2}$ |
| 11 | $\frac{d}{dx}x^x$ | **C** | $x^x(1+\ln x)$ |
| 12 | $\frac{d}{dx}\sqrt x$ | **D** | $\frac1{2\sqrt x}$ |
| 13 | $y=\ln\sin x$ | **B** | $\cot x$ |
| 14 | $f=x^4$, $f''$ | **C** | $12x^2$ |
| 15 | $\frac{d}{dx}\cos3x$ | **B** | $-3\sin3x$ |

## 19.2 The Unit II questions from the mixed practice set

| Q | Topic | Ans | Why |
|---|---|---|---|
| 1 | $(\tan x)'$ | B $\sec^2x$ | quotient rule |
| 2 | product rule | C $uv'+vu'$ | definition |
| 5 | $x^2+y^2=r^2$, $y'$ | B $-\frac xy$ | implicit |
| 6 | $xy=c^2$, $y'$ | B $-\frac yx$ | implicit |
| 7 | $x=at^2,y=2at$ | B $\frac1t$ | parametric |
| 8 | $x=a\cos\theta,y=a\sin\theta$ | D $-\cot\theta$ | parametric |
| 10 | $y=\ln x^3$ | C $\frac3x$ | $3\ln x$ |
| 12 | $y=x^x$ | C $x^x(1+\ln x)$ | log differentiation |
| 13 | $(e^{3x})''$ | C $9e^{3x}$ | chain twice |
| 16 | $(\ln x)''$ | B $-\frac1{x^2}$ | $(1/x)'$ |
| 19 | $(a^x)''$ | B $a^x(\ln a)^2$ | repeat |
| 21 | not needed for Rolle | D "$f'$ strictly increasing" | only 3 conditions |
| 22 | conclusion of Rolle | B $f'(c)=0$ | theorem |
| 24 | Rolle fails for $\abs x$ on $[-1,1]$ | C not differentiable at 0 | corner |
| 25 | Lagrange MVT | A $\frac{f(b)-f(a)}{b-a}$ | theorem |
| 27 | Rolle for $x^2-4x+3$ on $[1,3]$ | B $c=2$ | $2c-4=0$ |
| 28 | MVT for $x^2$ on $[0,2]$ | C $c=1$ | $2c=2$ |
| 32 | Taylor coefficient of $(x-a)^n$ | B $\frac{f^{(n)}(a)}{n!}$ | derivation |
| 33 | Maclaurin of $e^x$ | C $1+x+\frac{x^2}{2!}+\cdots$ | all derivatives $=1$ |
| 34 | Maclaurin of $\sin x$ | B only odd powers | odd function |
| 35 | Maclaurin of $\cos x$ | A only even powers | even function |
| 36 | $(1-x)^{-1}$, first 3 terms | B $1+x+x^2$ | geometric series |
| 43 | $\lim\frac{\sin x}x$ | B $1$ | standard |
| 44 | $\lim\frac{1-\cos x}x$ | B $0$ | $\frac{\sin x}1\to0$ |
| 46 | $\lim_{x\to\infty}\frac{e^x}x$ | D $\infty$ | growth ladder |
| 47 | $\lim_{x\to1}\frac{\ln x}{x-1}$ | B $1$ | L'Hôpital |
| 49 | $\lim\frac{\tan x}x$ | B $1$ | standard |
| 50 | $\lim_{x\to\infty}xe^{-x}$ | C $0$ | $\frac x{e^x}\to0$ |
| 55 | critical points of $x^3-3x$ | B $x=\pm1$ | $3x^2-3=0$ |
| 56 | max of $4x-x^2$ | C $4$ | at $x=2$ |

## 19.3 Extra practice

::: {.try t="Questions"}
1. Is $f(x)=\abs{x-2}+\abs{x+1}$ continuous and differentiable everywhere? Where does it fail?
2. Differentiate $y=x^{\sin x}+(\sin x)^x$.
3. Show $\dfrac{d}{dx}\tan^{-1}\dfrac{1+x}{1-x}=\dfrac1{1+x^2}$.
4. For $x=a(\cos t+t\sin t)$, $y=a(\sin t-t\cos t)$ find $\dfrac{dy}{dx}$ and $\dfrac{d^2y}{dx^2}$.
5. Verify Rolle's theorem for $\sin x$ on $[0,\pi]$ and MVT for $\ln x$ on $[1,e]$; find $c$.
6. Write the Maclaurin series of $e^x\cos x$ up to $x^4$.
7. Evaluate $\displaystyle\lim_{x\to0}\frac{\tan x-x}{x^3}$.
8. Find the local extrema of $f(x)=x^3-6x^2+9x+15$.
9. Find the absolute extrema of $f(x)=x^3$ on $[-2,2]$.
10. A circle's radius grows at $3$ cm/s. How fast is its area growing when $r=10$?
11. Equation of the tangent to $y=x^3-3x$ at $x=2$.
12. Intervals of increase and decrease of $f(x)=2x^3-9x^2+12x$.
13. Of all rectangles with perimeter $40$ m, which has the greatest area?
14. Differentiate $\ln\!\big(x+\sqrt{x^2+1}\big)$.
:::

::: {.sol}
**Answers.**
(1) Continuous everywhere (sum of continuous functions). **Not differentiable at $x=-1$ and $x=2$** (corners).
(2) $x^{\sin x}\left(\dfrac{\sin x}{x}+\cos x\ln x\right)+(\sin x)^x\left(\ln\sin x+x\cot x\right)$.
(3) The expression equals $\frac\pi4+\tan^{-1}x$ (for $x<1$), whose derivative is $\frac1{1+x^2}$.
(4) $\dfrac{dx}{dt}=at\cos t$, $\dfrac{dy}{dt}=at\sin t$, so $\dfrac{dy}{dx}=\tan t$ and $\dfrac{d^2y}{dx^2}=\dfrac{\sec^2t}{at\cos t}=\dfrac{\sec^3t}{at}$.
(5) $c=\frac\pi2$ for Rolle (since $\cos c=0$); $c=e-1\approx1.718$ for MVT.
(6) $1+x-\dfrac{x^3}{3}-\dfrac{x^4}{6}$ (the $x^2$ term cancels).
(7) $\dfrac13$ (use $\tan x=x+\frac{x^3}3+\cdots$ or L'Hôpital three times).
(8) $f'=3(x-1)(x-3)$: local max $f(1)=19$ at $x=1$; local min $f(3)=15$ at $x=3$.
(9) Max $8$ at $x=2$; min $-8$ at $x=-2$ (no interior extremum since $f'=3x^2\ge0$).
(10) $\dfrac{dA}{dt}=2\pi r\dfrac{dr}{dt}=60\pi\ \text{cm}^2/\text{s}$.
(11) $y'=3x^2-3=9$ at $x=2$; point $(2,2)$; tangent $y=9x-16$.
(12) $f'=6(x-1)(x-2)$: increasing on $(-\infty,1]$ and $[2,\infty)$; decreasing on $[1,2]$.
(13) A square of side $10$ m (area $100$ m$^2$).
(14) $\dfrac1{\sqrt{x^2+1}}$.
:::
