# Integration by partial fractions {.u3 data-eyebrow="Unit III · Chapter 24"}

::: {.idea t="Big idea"}
You already know how to **add** fractions: $\frac1{x-1}+\frac1{x+2}=\frac{2x+1}{(x-1)(x+2)}$. Partial fractions is doing that in **reverse**: break a complicated rational function into simple pieces, each of which integrates to a logarithm or an arctangent. It is the method for any integrand of the form $\dfrac{P(x)}{Q(x)}$ (polynomial over polynomial).
:::

## 24.1 The four-step method

::: {.idea t="Algorithm"}
1. **Improper?** If $\deg P\ge\deg Q$, divide first (long division). *This is the step students forget.* Then work with the proper remainder $\dfrac{R(x)}{Q(x)}$.
2. **Factorise** $Q(x)$ into linear factors and irreducible quadratics.
3. **Write the correct form** (table below) with unknown constants $A,B,C,\dots$
4. **Find the constants**, then **integrate** each simple term.
:::

::: {.formula t="Which form for which factor?"}

| Factor in the denominator | Terms to write |
|---|---|
| distinct linear $(x-a)$ | $\dfrac{A}{x-a}$ |
| repeated linear $(x-a)^2$ | $\dfrac{A}{x-a}+\dfrac{B}{(x-a)^2}$ (one term for each power up to the highest) |
| irreducible quadratic $(x^2+px+q)$ | $\dfrac{Ax+B}{x^2+px+q}$ |
| repeated quadratic $(x^2+px+q)^2$ | $\dfrac{Ax+B}{x^2+px+q}+\dfrac{Cx+D}{(x^2+px+q)^2}$ |

:::

**Examples of the correct form** (these are practice-set questions):

- $\dfrac1{(x-1)(x-2)}=\dfrac A{x-1}+\dfrac B{x-2}$
- $\dfrac{3x+1}{(x-1)^2}=\dfrac A{x-1}+\dfrac B{(x-1)^2}$
- $\dfrac1{(x^2+1)(x+2)}=\dfrac{Ax+B}{x^2+1}+\dfrac C{x+2}$

**What the integrals look like:**
$$\int\frac{A}{x-a}dx=A\ln\abs{x-a},\qquad\int\frac{B}{(x-a)^2}dx=-\frac{B}{x-a},\qquad\int\frac{Ax+B}{x^2+1}dx=\frac A2\ln(x^2+1)+B\tan^{-1}x.$$

## 24.2 Finding the constants

**Method 1: substitute convenient values (cover-up).** Multiply through by the denominator, then plug in the roots of the factors. For distinct linear factors this gives each constant instantly: *cover* the factor $(x-a)$ in the original fraction and evaluate what remains at $x=a$.

*Example:* $\dfrac{x+5}{(x-1)(x+2)}=\dfrac A{x-1}+\dfrac B{x+2}$. Cover $(x-1)$ and put $x=1$: $A=\dfrac{1+5}{1+2}=2$. Cover $(x+2)$, $x=-2$: $B=\dfrac{-2+5}{-2-1}=-1$. So the fraction is $\dfrac2{x-1}-\dfrac1{x+2}$.

**Method 2: compare coefficients.** Expand and match powers of $x$. Use it for quadratic factors or to find the leftover constants.

**Mix both:** use values for the easy constants, coefficient-comparison for the rest. Always **verify** by substituting one more value of $x$.

## 24.3 Your professor's two worked problems

::: {.ex t="Problem 1: $\displaystyle\int\frac{1-x^2}{x(1-2x)}\,dx$ (numerator and denominator have equal degree)"}
**Step 1: long division.** The denominator is $x-2x^2=-2x^2+x$, degree 2, same as the numerator $-x^2+1$. Dividing: $-x^2+1=\tfrac12(-2x^2+x)+\left(1-\tfrac x2\right)$. So
$$\frac{1-x^2}{x(1-2x)}=\frac12+\frac{1-\frac x2}{x(1-2x)}.$$
**Step 2: partial fractions** on the proper part: $\dfrac{1-\frac x2}{x(1-2x)}=\dfrac Ax+\dfrac B{1-2x}\Rightarrow1-\dfrac x2=A(1-2x)+Bx.$
Put $x=0$: $1=A$. Put $x=\frac12$: $1-\frac14=\frac B2\Rightarrow B=\frac32$.

**Step 3: integrate.**
$$\int\frac12dx+\int\frac1xdx+\frac32\int\frac{dx}{1-2x}=\frac x2+\ln\abs x+\frac32\cdot\frac{\ln\abs{1-2x}}{-2}+C=\boxed{\frac x2+\ln\abs x-\frac34\ln\abs{1-2x}+C}$$
(The $-2$ comes from the inner function $1-2x$: the linear-substitution rule.)
:::

::: {.ex t="Problem 2: $\displaystyle\int\frac{x}{(x-1)^2(x+2)}\,dx$ (a repeated factor)"}
**Form:** $\dfrac{x}{(x-1)^2(x+2)}=\dfrac A{x-1}+\dfrac B{(x-1)^2}+\dfrac C{x+2}$. Clear denominators:
$$x=A(x-1)(x+2)+B(x+2)+C(x-1)^2.$$
- $x=1$: $1=3B\Rightarrow B=\frac13$.
- $x=-2$: $-2=9C\Rightarrow C=-\frac29$.
- $x=0$: $0=-2A+2B+C=-2A+\frac23-\frac29\Rightarrow A=\frac29$.

*Cross-check with the $x^2$ coefficients:* the right side has $x^2(A+C)$ and the left side has none, so $A+C=0$ ✓.

**Integrate:** $\displaystyle\int\Big(\frac{2/9}{x-1}+\frac{1/3}{(x-1)^2}-\frac{2/9}{x+2}\Big)dx=\boxed{\frac29\ln\abs{x-1}-\frac1{3(x-1)}-\frac29\ln\abs{x+2}+C}$
:::

## 24.4 More examples (the deck's Q37–Q55)

::: {.ex t="Distinct linear factors"}
- $\dfrac1{x(x+1)}=\dfrac1x-\dfrac1{x+1}\Rightarrow\displaystyle\int=\ln\abs{\dfrac{x}{x+1}}+C$.
- $\dfrac1{(x-1)(x-2)}=\dfrac1{x-2}-\dfrac1{x-1}\Rightarrow\displaystyle\int=\ln\abs{\dfrac{x-2}{x-1}}+C$.
- $\dfrac1{x^2-1}=\dfrac12\Big[\dfrac1{x-1}-\dfrac1{x+1}\Big]\Rightarrow\displaystyle\int=\dfrac12\ln\abs{\dfrac{x-1}{x+1}}+C$.
- $\dfrac1{x^2+3x+2}=\dfrac1{(x+1)(x+2)}=\dfrac1{x+1}-\dfrac1{x+2}\Rightarrow\displaystyle\int=\ln\abs{\dfrac{x+1}{x+2}}+C$.
- $\dfrac{2x+3}{(x+1)(x+2)}=\dfrac1{x+1}+\dfrac1{x+2}\Rightarrow\displaystyle\int=\ln\abs{(x+1)(x+2)}+C$. *(Here the numerator is the derivative of the denominator $x^2+3x+2$, so $\int\frac{f'}{f}=\ln\abs f$ gives it at once.)*
- $\displaystyle\int\dfrac{2x}{x^2-1}dx=\ln\abs{x^2-1}+C$ (derivative on top again; partial fractions $\frac1{x-1}+\frac1{x+1}$ agree).
:::

::: {.ex t="With an irreducible quadratic"}
$\displaystyle\int\frac{dx}{(x^2+1)(x+2)}$: $\ 1=(Ax+B)(x+2)+C(x^2+1)$. $x=-2$: $C=\frac15$. Compare $x^2$: $A+C=0\Rightarrow A=-\frac15$. Compare constants: $2B+C=1\Rightarrow B=\frac25$. So
$$\int\Big[\frac{-\frac15x+\frac25}{x^2+1}+\frac{1/5}{x+2}\Big]dx=-\frac1{10}\ln(x^2+1)+\frac25\tan^{-1}x+\frac15\ln\abs{x+2}+C.$$
:::

::: {.ex t="An improper fraction"}
$\displaystyle\int\frac{x^2+1}{x^2-1}dx=\int\Big(1+\frac{2}{x^2-1}\Big)dx=\int\Big(1+\frac1{x-1}-\frac1{x+1}\Big)dx=x+\ln\abs{\frac{x-1}{x+1}}+C.$
:::

::: {.warn t="Slips to avoid"}
1. Skipping long division when $\deg P\ge\deg Q$.
2. For $(x-a)^2$ writing only $\frac{A}{(x-a)^2}$ and omitting $\frac{B}{x-a}$.
3. For an irreducible quadratic writing only a constant numerator $\frac{A}{x^2+1}$ instead of $\frac{Ax+B}{x^2+1}$.
4. Forgetting the factor $\frac1a$ when integrating $\frac{1}{ax+b}$, or forgetting the absolute value in the logarithm.
:::

# Definite integrals and their properties {.u3 data-eyebrow="Unit III · Chapter 25"}

::: {.idea t="Big idea"}
By the Fundamental Theorem, $\int_a^bf\,dx=F(b)-F(a)$. But many definite integrals that look impossible (e.g. $\int_0^{\pi/2}\ln\sin x\,dx$) have **no elementary antiderivative** at all. We solve them without ever finding one, using **symmetry tricks**: the properties of definite integrals. This chapter follows the handwritten sheets your professor shared.
:::

## 25.1 The basics

$$\int f(x)\,dx=F(x)+C\ \ (\text{indefinite: a family of functions}),\qquad\int_a^bf(x)\,dx=\Big[F(x)\Big]_a^b=F(b)-F(a)\ \ (\text{definite: a number}).$$
$b$ is the **upper limit**, $a$ the **lower limit**.

::: {.ex t="Warm-up from the sheet: $\displaystyle\int_0^\pi\cos^2x\,dx$"}
$=\displaystyle\int_0^\pi\frac{1+\cos2x}{2}dx=\frac12\Big[x+\frac{\sin2x}{2}\Big]_0^\pi=\frac12\big(\pi+0-0\big)=\frac\pi2.$
:::

## 25.2 The eight properties

::: {.formula t="Properties $P_0$ to $P_7$ (the numbering your professor uses)"}

| | Statement | In words |
|---|---|---|
| $P_0$ | $\displaystyle\int_a^bf(x)dx=\int_a^bf(t)dt$ | the variable name is a dummy |
| $P_1$ | $\displaystyle\int_a^bf\,dx=-\int_b^af\,dx$ , and $\displaystyle\int_a^af=0$ | swapping limits flips the sign |
| $P_2$ | $\displaystyle\int_a^bf\,dx=\int_a^cf\,dx+\int_c^bf\,dx$ | split at any point $c$ (use for $\abs{\ }$ and piecewise) |
| $P_3$ | $\displaystyle\int_a^bf(x)dx=\int_a^bf(a+b-x)dx$ | reflect the interval about its midpoint |
| $P_4$ | $\displaystyle\int_0^af(x)dx=\int_0^af(a-x)dx$ | special case of $P_3$ with lower limit $0$ |
| $P_5$ | $\displaystyle\int_0^{2a}f(x)dx=\int_0^af(x)dx+\int_0^af(2a-x)dx$ | split $[0,2a]$ at $a$ |
| $P_6$ | $\displaystyle\int_0^{2a}f(x)dx=\begin{cases}2\displaystyle\int_0^af(x)dx,&f(2a-x)=f(x)\\0,&f(2a-x)=-f(x)\end{cases}$ | halve the work, or get $0$ |
| $P_7$ | $\displaystyle\int_{-a}^af(x)dx=\begin{cases}2\displaystyle\int_0^af(x)dx,&f\text{ even}\\0,&f\text{ odd}\end{cases}$ | symmetric limits |

:::

![$P_4$: replacing $x$ by $a-x$ reflects the graph left-right and leaves the area unchanged.](figs/fig_king.svg){width=75%}

![$P_7$: even functions double; odd functions cancel.](figs/fig_even_odd.svg){width=78%}

**Even and odd test.** Compute $f(-x)$. If it equals $f(x)$, $f$ is **even** (e.g. $x^2,\ \cos x,\ \abs x$). If it equals $-f(x)$, it is **odd** (e.g. $x,\ x^3,\ \sin x,\ \tan x$).

::: {.idea t="Your professor's decision rule for $\displaystyle\int_0^af(x)\,dx$"}
Compute $f(a-x)$ and compare:

- **Same function back** ($f(a-x)=f(x)$): apply $P_6$: $\ I=2\displaystyle\int_0^{a/2}f(x)\,dx$.
- **Negative of it** ($f(a-x)=-f(x)$): $I=0$.
- **A *new* function** (e.g. $\sin\to\cos$): apply $P_4$ to get a second expression for $I$, **add the two**, and the integrand usually collapses: $2I=\int(\text{something simple})$.
:::

::: {.tip t="Order of attack for any definite integral"}

| Look at the limits and integrand | Use |
|---|---|
| limits $-a$ to $a$ | test even/odd first ($P_7$) |
| contains $\abs{\text{expression}}$ | find where the expression is $0$, split there ($P_2$), drop the bars piece by piece |
| limits $0$ to $a$, trig or $x\leftrightarrow a-x$ pairing | $P_4$ then add; or $P_6$ |
| limits $a$ to $b$ | $P_3$ ($x\to a+b-x$) |
| limits $0$ to $2a$ | $P_6$ |
| a messy antiderivative | change variable first and *change the limits* |

:::

## 25.3 Worked examples (the professor's sheets)

::: {.ex t="Example 25.1: $\displaystyle\int_0^1x(1-x)^{10}dx$"}
Here $f(1-x)=(1-x)x^{10}$, a *new* function, but expanding it is easy. By $P_4$:
$I=\displaystyle\int_0^1(1-x)x^{10}dx=\int_0^1(x^{10}-x^{11})dx=\frac1{11}-\frac1{12}=\boxed{\frac1{132}}.$
:::

::: {.ex t="Example 25.2: $\displaystyle\int_0^{\pi/2}\frac{\sin x}{\sin x+\cos x}dx$"}
$f(\frac\pi2-x)=\dfrac{\cos x}{\cos x+\sin x}$ (a new function). By $P_4$, $I=\displaystyle\int_0^{\pi/2}\frac{\cos x}{\cos x+\sin x}dx$. **Add:** $2I=\displaystyle\int_0^{\pi/2}\frac{\sin x+\cos x}{\sin x+\cos x}dx=\int_0^{\pi/2}1\,dx=\frac\pi2$. So $I=\boxed{\dfrac\pi4}$.
:::

::: {.ex t="Example 25.3: $\displaystyle\int_0^{\pi}\frac{2^{\abs{\sin x}}}{2^{\abs{\sin x}}+2^{\abs{\cos x}}}dx$"}
First, $f(\pi-x)=f(x)$, because $\abs{\sin(\pi-x)}=\abs{\sin x}$ and $\abs{\cos(\pi-x)}=\abs{\cos x}$. By $P_6$ (with $2a=\pi$): $I=2J$, where $J=\displaystyle\int_0^{\pi/2}\frac{2^{\sin x}}{2^{\sin x}+2^{\cos x}}dx$ (on $[0,\frac\pi2]$ the bars are unnecessary).

Now $f(\frac\pi2-x)$ swaps $\sin\leftrightarrow\cos$, a new function, so use $P_4$: $J=\displaystyle\int_0^{\pi/2}\frac{2^{\cos x}}{2^{\cos x}+2^{\sin x}}dx$. **Add** the two forms of $J$: $2J=\displaystyle\int_0^{\pi/2}1\,dx=\frac\pi2$, so $J=\frac\pi4$ and $I=2J=\boxed{\dfrac\pi2}$.
:::

::: {.ex t="Example 25.4: odd + even pieces, $\displaystyle\int_{-3}^{3}\big(4x^3-\tan x+x^2\sin x+1\big)dx$"}
$4x^3,\ \tan x$ and $x^2\sin x$ (even $\times$ odd) are **odd**; the constant $1$ is **even**. So the first three cancel over $[-3,3]$ and $I=0+2\displaystyle\int_0^31\,dx=\boxed6$.
:::

::: {.ex t="Example 25.5: absolute value, $\displaystyle\int_{-\pi}^{\pi}\abs{\cos x}\,dx$"}
$\abs{\cos(-x)}=\abs{\cos x}$: even. So $I=2\displaystyle\int_0^\pi\abs{\cos x}dx$. $\cos x\ge0$ on $[0,\frac\pi2]$ and $\le0$ on $[\frac\pi2,\pi]$ ($P_2$):
$I=2\Big[\displaystyle\int_0^{\pi/2}\cos x\,dx-\int_{\pi/2}^{\pi}\cos x\,dx\Big]=2\big[(1-0)-(0-1)\big]=\boxed4.$
:::

::: {.ex t="Example 25.6: $\displaystyle\int_0^{2\pi}\cos^5x\,dx$"}
$f(2\pi-x)=\cos^5x=f(x)$, so $I=2\displaystyle\int_0^\pi\cos^5x\,dx$. On $[0,\pi]$: $f(\pi-x)=\cos^5(\pi-x)=(-\cos x)^5=-\cos^5x=-f(x)$, so $\displaystyle\int_0^\pi\cos^5x\,dx=0$ by $P_6$ (with $2a=\pi$). Hence $I=\boxed0$.
:::

::: {.ex t="Example 25.7: $\displaystyle\int_{-2}^{2}\abs{x-1}\,dx$"}
$x-1$ changes sign at $x=1$. $I=\displaystyle\int_{-2}^1(1-x)dx+\int_1^2(x-1)dx=\Big[x-\frac{x^2}2\Big]_{-2}^1+\Big[\frac{x^2}{2}-x\Big]_1^2=\frac92+\frac12=\boxed5.$ (Two triangles: areas $\frac92$ and $\frac12$.)

![The two triangles under $\abs{x-1}$.](figs/fig_abs_integral.svg){width=48%}
:::

::: {.ex t="Example 25.8: the logarithm integral, $\displaystyle I=\int_0^{\pi/2}\ln\sin x\,dx$"}
By $P_4$: $I=\displaystyle\int_0^{\pi/2}\ln\cos x\,dx$. Add: $2I=\displaystyle\int_0^{\pi/2}\ln(\sin x\cos x)dx=\int_0^{\pi/2}\ln\frac{\sin2x}{2}dx=\int_0^{\pi/2}\ln\sin2x\,dx-\frac\pi2\ln2.$

For the first integral put $t=2x$: $\displaystyle\int_0^{\pi/2}\ln\sin2x\,dx=\frac12\int_0^\pi\ln\sin t\,dt$. Since $\sin(\pi-t)=\sin t$, $P_6$ gives $\int_0^\pi\ln\sin t\,dt=2I$, so that integral equals $\frac12\cdot2I=I$. Therefore $2I=I-\dfrac\pi2\ln2$, i.e.
$$\boxed{I=-\frac\pi2\ln2}.$$
:::

::: {.ex t="Example 25.9: your professor's challenge question"}
Evaluate $\displaystyle I=\int_{-\pi/16}^{3\pi/16}\ln(1+\tan2x)\,dx$.

::: sol
The limits sum to $a+b=-\frac\pi{16}+\frac{3\pi}{16}=\frac\pi8$, so use $P_3$: replace $x$ by $\frac\pi8-x$:
$$1+\tan\!\Big(\frac\pi4-2x\Big)=1+\frac{1-\tan2x}{1+\tan2x}=\frac{2}{1+\tan2x}.$$
So $I=\displaystyle\int\big[\ln2-\ln(1+\tan2x)\big]dx=\ln2\cdot\Big(\frac{3\pi}{16}+\frac\pi{16}\Big)-I$. Hence $2I=\dfrac\pi4\ln2$ and
$$\boxed{I=\frac\pi8\ln2}.$$
:::
:::

## 25.4 Further reminders

- $\displaystyle\int_0^1xe^xdx=\Big[(x-1)e^x\Big]_0^1=0-(-1)=1$ (parts, then limits).
- **Bounds:** if $m\le f(x)\le M$ on $[a,b]$ then $m(b-a)\le\displaystyle\int_a^bf\,dx\le M(b-a)$.
- $\displaystyle\int_a^b f\,dx\le\int_a^b\abs f\,dx$.
- $P_3$ **is the heart of every "add the two forms" trick:** the integrand and its reflection add up to something easy.

::: {.warn t="Frequent errors"}
- Using $P_7$ without checking that the **limits are symmetric** ($-a$ to $a$).
- Applying $P_4$ to limits that do not start at $0$ (use $P_3$ instead).
- Removing absolute value bars without splitting at the sign change.
- After a substitution, forgetting to **change the limits**.
:::

# Unit III: practice and answers {.u3 data-eyebrow="Unit III · Chapter 26"}

## 26.1 Your professor's MCQ deck (Q16–Q80) with results

::: {.longtable}

| Q | Ans | Result | Q | Ans | Result |
|---|---|---|---|---|---|
| 16 | D | $\int x^ndx=\frac{x^{n+1}}{n+1}$ | 49 | A | $\frac{Ax+B}{x^2+1}+\frac C{x+2}$ |
| 17 | A | $\ln\abs x$ | 50 | C | do long division |
| 18 | B | $\frac{e^{3x}}3$ | 51 | C | $\frac12\ln\abs{\frac{x-1}{x+1}}$ |
| 19 | C | $-\cos x$ | 52 | B | $\frac1x-\frac1{x+1}$ |
| 20 | D | $\tan x$ | 53 | D | $\ln\abs{(x+1)(x+2)}$ |
| 21 | B | $x^3+x^2+x$ | 54 | C | $A=2$ |
| 22 | C | $\tan^{-1}x$ | 55 | A | $\ln\abs{\frac{x+1}{x+2}}$ |
| 23 | A | $\sin^{-1}x$ | 56 | B | $uv-\int v\,du$ |
| 24 | B | $\frac23x^{3/2}$ | 57 | B | I = Inverse trig |
| 25 | D | $-\frac1x$ | 58 | D | $(x-1)e^x$ |
| 26 | C | $\frac{\sin2x}2$ | 59 | A | $x\sin x+\cos x$ |
| 27 | B | $\frac{a^x}{\ln a}$ | 60 | C | $x\ln x-x$ |
| 28 | A | $-\cot x$ | 61 | D | $\frac{x^2}2\ln x-\frac{x^2}4$ |
| 29 | D | $x$ | 62 | C | $x\tan^{-1}x-\frac12\ln(1+x^2)$ |
| 30 | C | $\frac{x^2}2+\ln\abs x$ | 63 | B | $e^xf(x)$ |
| 31 | B | $e^{x^2}$ | 64 | D | $e^x\sin x$ |
| 32 | C | $u=x^2+1$ | 65 | B | $e^x(x^2-2x+2)$ |
| 33 | B | $\frac13(x^2+1)^{3/2}$ | 66 | D | $-x\cos x+\sin x$ |
| 34 | D | $-\ln\abs{\cos x}$ | 67 | B | $u=\ln x$ |
| 35 | C | $\ln\abs{\sin x}$ | 68 | C | $-\int_b^a f$ |
| 36 | A | $\frac{\sin^4x}4$ | 69 | B | $\frac13$ |
| 37 | C | $\frac{(\ln x)^2}2$ | 70 | A | $5-2=3$ |
| 38 | D | $\ln\abs{\ln x}$ | 71 | D | $f(a+b-x)$ |
| 39 | B | $\ln(1+e^x)$ | 72 | B | $2\int_0^af$ |
| 40 | C | $\frac13\sin(3x+2)$ | 73 | D | $0$ |
| 41 | D | $\frac{(2x+3)^6}{12}$ | 74 | C | $0$ (odd) |
| 42 | C | $\frac12\ln(x^2+1)$ | 75 | A | $1$ |
| 43 | B | $\frac{\tan^2x}2$ | 76 | B | $\frac\pi4$ |
| 44 | A | $\frac12\sin^{-1}2x$ | 77 | C | $1$ |
| 45 | C | $\frac13\tan^{-1}3x$ | 78 | D | $e-1$ |
| 46 | B | $\frac A{x-1}+\frac B{x-2}$ | 79 | B | $m(b-a)$ to $M(b-a)$ |
| 47 | C | $\ln\abs{\frac{x-2}{x-1}}$ | 80 | D | $1$ |
| 48 | D | $\frac A{x-1}+\frac B{(x-1)^2}$ | | | |

:::

## 26.2 The Unit III questions from the mixed practice set

| Q | Question | Answer |
|---|---|---|
| 4 | $\int e^xdx$ | **(C)** $e^x+C$ |
| 5 | $\int a^xdx$ | **(B)** $\frac{a^x}{\ln a}+C$ |
| 7 | $\int\sec^2x\,dx$ | **(A)** $\tan x+C$ |
| 8 | $\int(2x+3)dx$ | **(B)** $x^2+3x+C$ |
| 12 | $\int\frac{f'}{f}dx$ | **(C)** $\ln\abs{f(x)}+C$ |
| 13 | $\int\tan x\,dx$ | **(C)** $-\ln\abs{\cos x}+C$ |
| 15 | $\int\cos(3x+4)dx$ | **(C)** $\frac13\sin(3x+4)+C$ |
| 16 | $\int\frac{e^x}{1+e^x}dx$ | **(A)** $\ln(1+e^x)+C$ |
| 24 | $\int xe^xdx$ | **(B)** $e^x(x-1)+C$ |
| 26 | $\int\ln x\,dx$ | **(A)** $x\ln x-x+C$ |
| 27 | $\int e^x[f+f']dx$ | **(C)** $e^xf(x)+C$ |
| 28 | $\int e^x(\sin x+\cos x)dx$ | **(B)** $e^x\sin x+C$ |
| 37 | $\int\frac1{x(x+1)}dx$ | **(B)** $\ln\abs{\frac x{x+1}}+C$ |
| 40 | $\int\frac{2x}{x^2-1}dx$ | $\ln\abs{x^2-1}+C$ |
| 41 | Fundamental Theorem | **(B)** $F(b)-F(a)$ |
| 42 | $\int_0^2x^3dx$ | **(B)** $4$ |
| 43 | $\int_0^{\pi/2}\cos x\,dx$ | **(B)** $1$ |
| 44 | $\int_1^e\frac1xdx$ | **(B)** $1$ |
| 45 | $\int_0^1e^xdx$ | **(B)** $e-1$ |

## 26.3 Extra practice

::: {.try t="Questions"}
1. $\int\sin^2x\,dx$ $\quad$ 2. $\int\dfrac{x}{\sqrt{1+x^2}}dx$ $\quad$ 3. $\int\cos^3x\,dx$
4. $\int\dfrac{2x+1}{x^2+x+5}dx$ $\quad$ 5. $\int x^2e^{-x}dx$ $\quad$ 6. $\int x\sec^2x\,dx$
7. $\int\dfrac{x+1}{(x-1)(x-2)}dx$ $\quad$ 8. $\int\dfrac{dx}{x^2+2x+5}$ $\quad$ 9. $\int x^3\ln x\,dx$
10. $\int\dfrac{dx}{x(x^2+1)}$ $\quad$ 11. $\displaystyle\int_0^{\pi/2}\frac{\cos x}{\sin x+\cos x}dx$ $\quad$ 12. $\displaystyle\int_{-1}^1(x^2+x)\,dx$
13. $\displaystyle\int_0^{\pi/4}\ln(1+\tan x)\,dx$ $\quad$ 14. $\displaystyle\int_0^3\abs{x-2}\,dx$ $\quad$ 15. $\displaystyle\int_0^1x(1-x)^5dx$
:::

::: {.sol}
**Answers.**
(1) $\frac x2-\frac{\sin2x}4+C$. (2) $\sqrt{1+x^2}+C$. (3) $\sin x-\frac{\sin^3x}3+C$.
(4) $\ln(x^2+x+5)+C$ (derivative on top). (5) $-e^{-x}(x^2+2x+2)+C$. (6) $x\tan x+\ln\abs{\cos x}+C$.
(7) $-2\ln\abs{x-1}+3\ln\abs{x-2}+C$. (8) $\frac12\tan^{-1}\frac{x+1}2+C$. (9) $\frac{x^4}4\ln x-\frac{x^4}{16}+C$.
(10) $\ln\abs x-\frac12\ln(x^2+1)+C$ (write $\frac1x-\frac{x}{x^2+1}$).
(11) $\frac\pi4$ (same as Example 25.2). (12) $\frac23$ ($x^2$ even gives $2\cdot\frac13$; $x$ is odd, so $0$).
(13) $\frac\pi8\ln2$ ($P_4$ with $a=\frac\pi4$: $1+\tan(\frac\pi4-x)=\frac2{1+\tan x}$).
(14) $\int_0^2(2-x)dx+\int_2^3(x-2)dx=2+\frac12=\frac52$. (15) $\int_0^1(1-x)x^5dx=\frac16-\frac17=\frac1{42}$.
:::
