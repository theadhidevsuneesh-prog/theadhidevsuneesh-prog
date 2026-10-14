# Meet the integral {.u3 data-eyebrow="Unit III · Chapter 20"}

::: {.idea t="Big idea"}
Integration answers two questions that turn out to be the **same question**:

1. *Undo differentiation:* if I know the **speed**, what was the **distance**? (an **antiderivative**)
2. *Add up infinitely many tiny pieces:* how much **area** lies under a curve? (a **definite integral**)

The **Fundamental Theorem of Calculus** is the bridge: to total up a rate, find an antiderivative and subtract its values at the ends.
:::

## 20.1 Antiderivatives and the "+C"

::: {.def t="Antiderivative and indefinite integral"}
$F$ is an **antiderivative** of $f$ if $F'(x)=f(x)$. All antiderivatives of $f$ are written
$$\int f(x)\,dx=F(x)+C,$$
where $C$ is an arbitrary constant, the **constant of integration**. ($\int$ is an elongated "S" for *sum*; $f(x)$ is the **integrand**; $dx$ says which variable we integrate with respect to.)
:::

**Why the $+C$?** Constants vanish when differentiated, so $x^2$, $x^2+5$ and $x^2-3$ all have derivative $2x$. Graphically, the antiderivatives of $2x$ are the **same parabola slid up and down**; at any given $x$ all of them have the same slope.

![Antiderivatives of $2x$ are the parabolas $y=x^2+C$: identical shape, different heights.](figs/fig_constants.svg){width=60%}

::: {.warn t="Never drop the $+C$"}
For an indefinite integral the $+C$ is part of the answer; leaving it out loses marks. (For **definite** integrals the constant cancels, so no $+C$ there.) Different methods can give answers that *look* different, e.g. $\frac{\tan^2x}{2}$ and $\frac{\sec^2x}{2}$, which differ by the constant $\frac12$.
:::

**Check any integral by differentiating your answer.** If the derivative gives back the integrand, you are right. This is the best self-check in the whole subject.

## 20.2 Area under a curve

How do we find the area under $y=x^2$ from $x=0$ to $x=2$? Slice it into thin vertical strips and treat each as a rectangle: height $f(x_i)$, width $\Delta x$. Add them up. More strips give a better answer:

![Approximating the area under $y=x^2$ on $[0,2]$ by 4 and by 12 rectangles, and the exact limit.](figs/fig_riemann.svg){width=100%}

::: {.def t="Definite integral (Riemann sum)"}
$$\int_a^bf(x)\,dx=\lim_{n\to\infty}\sum_{i=1}^{n}f(x_i^*)\,\Delta x,\qquad \Delta x=\frac{b-a}{n}.$$
It is the **signed area** between the curve and the $x$-axis from $x=a$ to $x=b$: area **above** the axis counts $+$, area **below** counts $-$.
:::

Computing that limit directly is painful. Luckily we never have to.

## 20.3 The Fundamental Theorem of Calculus

::: {.thm t="Fundamental Theorem of Calculus"}
**Part 1.** If $f$ is continuous on $[a,b]$ and $G(x)=\displaystyle\int_a^xf(t)\,dt$, then $G'(x)=f(x)$. *(Accumulated area grows at a rate equal to the height of the curve.)*

**Part 2.** If $F$ is **any** antiderivative of $f$, then
$$\boxed{\int_a^bf(x)\,dx=F(b)-F(a)=\Big[F(x)\Big]_a^b}$$
:::

::: {.ex t="Example 20.1"}
$\displaystyle\int_0^2x^2\,dx=\Big[\frac{x^3}{3}\Big]_0^2=\frac83-0=\frac83\approx2.67$, exactly what the rectangles were closing in on. Also $\displaystyle\int_0^2x^3\,dx=\Big[\frac{x^4}{4}\Big]_0^2=4$.
:::

::: {.story t="A very old problem solved in one stroke"}
Archimedes computed the area of a parabolic segment around 250 BC by an ingenious (and exhausting) limiting argument. Two thousand years later Newton and Leibniz realised, independently, that area and slope are inverse operations. The Fundamental Theorem turned Archimedes' months of work into one line.
:::

**Variable limits (Leibniz rule).** $\dfrac{d}{dx}\displaystyle\int_a^{g(x)}f(t)\,dt=f(g(x))\cdot g'(x)$. For instance $\dfrac{d}{dx}\displaystyle\int_0^{x^2}\sin t\,dt=2x\sin(x^2)$.

**Integral of a rate is net change.** If $v(t)$ is velocity, $\int_a^bv\,dt$ is the **displacement**; if $f$ is a rate of production, $\int_a^b f$ is total production.

# Basic rules and standard integrals {.u3 data-eyebrow="Unit III · Chapter 21"}

::: {.idea t="Big idea"}
Every derivative formula you know, read backwards, is an integral formula. Mastering this table (and the three simple rules below) lets you do a huge fraction of exam questions by **direct integration**: no clever tricks, just recognition.
:::

## 21.1 Rules

::: {.formula t="Linearity and the linear-substitution rule"}
$$\int kf(x)\,dx=k\int f(x)\,dx,\qquad \int\big(f(x)\pm g(x)\big)dx=\int f\pm\int g$$
$$\boxed{\int f(ax+b)\,dx=\frac1a\,F(ax+b)+C}\qquad\text{where }F'=f$$
:::

The second rule is just the chain rule backwards: because $\frac{d}{dx}F(ax+b)=a\,f(ax+b)$, you must divide by $a$ to compensate. Examples: $\int\cos(3x+4)dx=\frac13\sin(3x+4)+C$, $\ \int e^{3x}dx=\frac{e^{3x}}3+C$, $\ \int(2x+3)^5dx=\frac{(2x+3)^6}{12}+C$.

::: {.warn t="Products and quotients do NOT split"}
$\int f\,g\,dx\ne\int f\,dx\int g\,dx$ and $\int\frac fg\,dx\neq\frac{\int f}{\int g}$. There is no "product rule" shortcut; use substitution or parts (Chapters 22–23).
:::

## 21.2 The standard table

::: {.formula t="Standard integrals (memorise all)"}

| $f(x)$ | $\displaystyle\int f(x)\,dx$ | $f(x)$ | $\displaystyle\int f(x)\,dx$ |
|---|---|---|---|
| $x^n\ (n\ne-1)$ | $\dfrac{x^{n+1}}{n+1}+C$ | $\sin x$ | $-\cos x+C$ |
| $\dfrac1x$ | $\ln\abs x+C$ | $\cos x$ | $\sin x+C$ |
| $e^x$ | $e^x+C$ | $\sec^2x$ | $\tan x+C$ |
| $a^x$ | $\dfrac{a^x}{\ln a}+C$ | $\operatorname{cosec}^2x$ | $-\cot x+C$ |
| $\dfrac{1}{1+x^2}$ | $\tan^{-1}x+C$ | $\sec x\tan x$ | $\sec x+C$ |
| $\dfrac1{\sqrt{1-x^2}}$ | $\sin^{-1}x+C$ | $\operatorname{cosec}x\cot x$ | $-\operatorname{cosec}x+C$ |
| $\dfrac{1}{x\sqrt{x^2-1}}$ | $\sec^{-1}\abs x+C$ | $\tan x$ | $-\ln\abs{\cos x}+C=\ln\abs{\sec x}+C$ |
| $\cot x$ | $\ln\abs{\sin x}+C$ | $\sec x$ | $\ln\abs{\sec x+\tan x}+C$ |
| $\operatorname{cosec}x$ | $\ln\abs{\operatorname{cosec}x-\cot x}+C$ | | |

:::

::: {.formula t="The 'a-forms' (the constant $a>0$ version of the inverse-trig and log integrals)"}
$$\int\frac{dx}{x^2+a^2}=\frac1a\tan^{-1}\frac xa+C,\qquad \int\frac{dx}{\sqrt{a^2-x^2}}=\sin^{-1}\frac xa+C$$
$$\int\frac{dx}{x^2-a^2}=\frac1{2a}\ln\left|\frac{x-a}{x+a}\right|+C,\qquad \int\frac{dx}{a^2-x^2}=\frac1{2a}\ln\left|\frac{a+x}{a-x}\right|+C$$
$$\int\frac{dx}{\sqrt{x^2\pm a^2}}=\ln\left|x+\sqrt{x^2\pm a^2}\right|+C,\qquad \int\sqrt{a^2-x^2}\,dx=\frac x2\sqrt{a^2-x^2}+\frac{a^2}2\sin^{-1}\frac xa+C$$
:::

::: {.formula t="The 'derivative on top' patterns (huge time-savers)"}
$$\int\frac{f'(x)}{f(x)}\,dx=\ln\abs{f(x)}+C,\qquad \int f'(x)\big[f(x)\big]^n dx=\frac{[f(x)]^{n+1}}{n+1}+C\ (n\ne-1),\qquad \int\frac{f'(x)}{\sqrt{f(x)}}dx=2\sqrt{f(x)}+C$$
:::

## 21.3 Tricks before the big methods

- **Split the fraction:** $\dfrac{x^2+1}{x}=x+\dfrac1x\Rightarrow\int=\dfrac{x^2}2+\ln\abs x+C$.
- **Use identities:** $\sin^2x+\cos^2x=1$ gives $\int(\sin^2x+\cos^2x)dx=x+C$. Power reduction gives $\int\cos^2x\,dx=\int\frac{1+\cos2x}{2}dx=\frac x2+\frac{\sin2x}4+C$.
- **Rewrite roots and reciprocals as powers:** $\sqrt x=x^{1/2}$, $\dfrac1{x^2}=x^{-2}$, so $\int\sqrt x\,dx=\frac23x^{3/2}+C$ and $\int\frac{dx}{x^2}=-\frac1x+C$.

::: {.ex t="Worked set (direct integration deck, Q16–Q30)"}
- $\int x^n dx=\dfrac{x^{n+1}}{n+1}+C$. $\quad\int\dfrac1x dx=\ln\abs x+C$. $\quad\int e^{3x}dx=\dfrac{e^{3x}}3+C$.
- $\int\sin x\,dx=-\cos x+C$. $\quad\int\sec^2x\,dx=\tan x+C$. $\quad\int\operatorname{cosec}^2x\,dx=-\cot x+C$.
- $\int(3x^2+2x+1)dx=x^3+x^2+x+C$.
- $\int\dfrac{dx}{1+x^2}=\tan^{-1}x+C$. $\quad\int\dfrac{dx}{\sqrt{1-x^2}}=\sin^{-1}x+C$.
- $\int\sqrt x\,dx=\frac23x^{3/2}+C$. $\quad\int\dfrac{dx}{x^2}=-\dfrac1x+C$. $\quad\int\cos2x\,dx=\dfrac{\sin2x}2+C$.
- $\int a^xdx=\dfrac{a^x}{\ln a}+C$. $\quad\int(\sin^2x+\cos^2x)dx=x+C$. $\quad\int\dfrac{x^2+1}xdx=\dfrac{x^2}2+\ln\abs x+C$.
:::

::: {.ex t="From the mixed practice set"}
$\int e^xdx=e^x+C$; $\ \int a^xdx=\frac{a^x}{\ln a}+C$; $\ \int\sec^2x\,dx=\tan x+C$; $\ \int(2x+3)dx=x^2+3x+C$; $\ \int\frac{f'}{f}dx=\ln\abs f+C$; $\ \int\tan x\,dx=-\ln\abs{\cos x}+C$; $\ \int\cos(3x+4)dx=\frac13\sin(3x+4)+C$.
:::

::: {.try t="Try it"}
(a) $\int(5x^4-\frac3{x}+2e^x)dx$ (b) $\int\left(\sqrt x+\frac1{\sqrt x}\right)dx$ (c) $\int\sin^2x\,dx$.
*Answers: (a) $x^5-3\ln\abs x+2e^x+C$. (b) $\frac23x^{3/2}+2\sqrt x+C$. (c) $\frac x2-\frac{\sin2x}4+C$.*
:::

# Integration by substitution {.u3 data-eyebrow="Unit III · Chapter 22"}

::: {.idea t="Big idea"}
Substitution is the **chain rule run backwards**. If the integrand contains a function **and its derivative** (up to a constant), rename the inner function $u$. The integral collapses to something simple in $u$.
:::

::: {.formula t="The method"}
$$\int f\big(g(x)\big)\,g'(x)\,dx=\int f(u)\,du,\qquad u=g(x),\quad du=g'(x)\,dx.$$
1. Choose $u$ = the **inside** of the nastiest piece (or a denominator, or an exponent).
2. Compute $du=u'\,dx$ and rewrite the **whole** integral (including $dx$) in terms of $u$. No $x$ may remain.
3. Integrate in $u$.
4. **Substitute back** $u=g(x)$. (For definite integrals: change the limits instead, see below.)
:::

::: {.ex t="Example 22.1: $\int2xe^{x^2}dx$"}
$u=x^2,\ du=2x\,dx$. So $\int e^u du=e^u+C=e^{x^2}+C$.
:::

::: {.ex t="Example 22.2: $\int x\sqrt{x^2+1}\,dx$"}
$u=x^2+1,\ du=2x\,dx\Rightarrow x\,dx=\frac12du$. So $\frac12\int u^{1/2}du=\frac12\cdot\frac23u^{3/2}+C=\dfrac13(x^2+1)^{3/2}+C$.
:::

::: {.ex t="Example 22.3: $\int\tan x\,dx$ and $\int\cot x\,dx$"}
$\int\frac{\sin x}{\cos x}dx$ with $u=\cos x,\ du=-\sin x\,dx$: $-\int\frac{du}u=-\ln\abs{\cos x}+C$. Similarly $\int\frac{\cos x}{\sin x}dx=\ln\abs{\sin x}+C$ (with $u=\sin x$).
:::

::: {.ex t="Example 22.4: more from the deck (Q31–Q45)"}
- $\int\sin^3x\cos x\,dx$: $u=\sin x$: $\int u^3du=\dfrac{\sin^4x}{4}+C$.
- $\int\dfrac{\ln x}x\,dx$: $u=\ln x$: $\int u\,du=\dfrac{(\ln x)^2}2+C$.
- $\int\dfrac{dx}{x\ln x}$: $u=\ln x$: $\int\dfrac{du}u=\ln\abs{\ln x}+C$.
- $\int\dfrac{e^x}{1+e^x}dx$: $u=1+e^x$: $\ln(1+e^x)+C$.
- $\int\cos(3x+2)dx$: $u=3x+2$: $\frac13\sin(3x+2)+C$.
- $\int(2x+3)^5dx$: $u=2x+3$: $\frac{(2x+3)^6}{12}+C$.
- $\int\dfrac x{x^2+1}dx$: $u=x^2+1$: $\frac12\ln(x^2+1)+C$.
- $\int\sec^2x\tan x\,dx$: $u=\tan x$: $\dfrac{\tan^2x}2+C$ (equivalently $\frac{\sec^2x}{2}+C'$).
- $\int\dfrac{dx}{\sqrt{1-4x^2}}$: $u=2x$: $\frac12\sin^{-1}(2x)+C$.
- $\int\dfrac{dx}{1+9x^2}$: $u=3x$: $\frac13\tan^{-1}(3x)+C$.
:::

::: {.tip t="Choosing $u$: a pattern guide"}

| You see... | Try |
|---|---|
| $f(ax+b)$ | $u=ax+b$ |
| a power or root of an expression whose derivative also appears | $u=$ that expression |
| $e^{g(x)}g'(x)$ | $u=g(x)$ |
| $\dfrac{\ln x}{x}$, $\dfrac{1}{x\ln x}$ | $u=\ln x$ |
| $\sin^m\!x\cos^n\!x$, $m$ **odd** | $u=\cos x$ (save one $\sin x$ for $du$) |
| $\sin^m\!x\cos^n\!x$, $n$ **odd** | $u=\sin x$ (save one $\cos x$) |
| $\sin^m\!x\cos^n\!x$, both **even** | power-reduction: $\frac{1\pm\cos2x}2$ |
| $\sqrt{a^2-x^2}$ | $x=a\sin\theta$ |
| $a^2+x^2$ | $x=a\tan\theta$ |
| $\sqrt{x^2-a^2}$ | $x=a\sec\theta$ |

:::

## 22.1 Trigonometric integrals

- **Odd power:** $\int\sin^3x\,dx=\int(1-\cos^2x)\sin x\,dx$, $u=\cos x$: $-\cos x+\dfrac{\cos^3x}3+C$. Likewise $\int\cos^3x\,dx=\sin x-\dfrac{\sin^3x}3+C$.
- **Even powers:** $\int\sin^2x\,dx=\frac x2-\frac{\sin2x}4+C$; $\ \int\sin^2x\cos^2x\,dx=\int\frac{\sin^22x}4dx=\frac18\int(1-\cos4x)dx=\frac x8-\frac{\sin4x}{32}+C$.
- **$\int\sec x\,dx$:** multiply and divide by $\sec x+\tan x$: $\int\frac{\sec^2x+\sec x\tan x}{\sec x+\tan x}dx=\ln\abs{\sec x+\tan x}+C$ (the numerator is exactly the derivative of the denominator).

## 22.2 Completing the square and trig substitutions

::: {.ex t="Example 22.5: completing the square"}
$\displaystyle\int\frac{dx}{x^2+2x+5}$: $x^2+2x+5=(x+1)^2+2^2$, so the integral is $\dfrac12\tan^{-1}\dfrac{x+1}2+C$.

$\displaystyle\int\frac{dx}{\sqrt{5-4x-x^2}}$: $5-4x-x^2=9-(x+2)^2$, so the integral is $\sin^{-1}\dfrac{x+2}3+C$.
:::

::: {.ex t="Example 22.6: $\int\sqrt{1-x^2}\,dx$"}
Let $x=\sin\theta$, $dx=\cos\theta\,d\theta$, $\sqrt{1-x^2}=\cos\theta$. So $\int\cos^2\theta\,d\theta=\frac\theta2+\frac{\sin2\theta}4+C=\frac12\big(\sin^{-1}x+x\sqrt{1-x^2}\big)+C$.
:::

## 22.3 Substitution in definite integrals

**Change the limits** along with the variable; then you never need to go back to $x$.

::: {.ex t="Example 22.7"}
$\displaystyle\int_0^1\frac{x}{1+x^2}dx$: $u=1+x^2$; $x=0\Rightarrow u=1$, $x=1\Rightarrow u=2$. $\ \displaystyle\frac12\int_1^2\frac{du}u=\frac12\ln2$.

$\displaystyle\int_0^1 2xe^{x^2}dx=\int_0^1e^udu=e-1$.
:::

::: {.warn t="Typical errors"}
- Leaving some $x$'s in an integral that is now in $u$.
- Forgetting the factor from $du$ (e.g. $du=2x\,dx$ means $x\,dx=\frac12du$).
- In a definite integral, converting the integrand but **not the limits**.
:::

# Integration by parts {.u3 data-eyebrow="Unit III · Chapter 23"}

::: {.idea t="Big idea"}
Integration by parts is the **product rule run backwards**. Use it when the integrand is a **product of two different kinds of function**, e.g. $x\,e^x$, $x\cos x$, $\ln x$, $\tan^{-1}x$, where substitution fails.
:::

::: {.formula t="The formula"}
From $(uv)'=u'v+uv'$ we get
$$\boxed{\int u\,dv=uv-\int v\,du}\qquad\Longleftrightarrow\qquad\int u(x)\,v'(x)\,dx=u(x)v(x)-\int u'(x)v(x)\,dx.$$
:::

**Choosing $u$: the ILATE rule.** Pick $u$ as the function that comes **first** in this list; the remaining factor is $dv$.

::: {.mem t="ILATE"}
**I**nverse trig ($\sin^{-1}x,\tan^{-1}x,\dots$) $\ \to\ $ **L**ogarithmic ($\ln x$) $\ \to\ $ **A**lgebraic ($x,\ x^2,\dots$) $\ \to\ $ **T**rigonometric ($\sin x,\cos x$) $\ \to\ $ **E**xponential ($e^x$).
*Reason:* the early ones become **simpler** when differentiated and the late ones are easy to integrate. (In ILATE, "I" stands for Inverse trigonometric functions, a practice-set question.)
:::

::: {.ex t="Example 23.1: $\int xe^x\,dx$"}
$u=x$ (algebraic), $dv=e^xdx$. $du=dx$, $v=e^x$. $\ \int xe^xdx=xe^x-\int e^xdx=xe^x-e^x+C=(x-1)e^x+C.$
:::

::: {.ex t="Example 23.2: $\int x\cos x\,dx$"}
$u=x,\ dv=\cos x\,dx\Rightarrow v=\sin x$. $\ =x\sin x-\int\sin x\,dx=x\sin x+\cos x+C.$ Similarly $\int x\sin x\,dx=-x\cos x+\sin x+C$.
:::

::: {.ex t="Example 23.3: $\int\ln x\,dx$ (the sneaky one)"}
There seems to be only one factor. Write $\ln x=\ln x\cdot1$: $u=\ln x,\ dv=dx\Rightarrow du=\frac{dx}{x},\ v=x$. $\ \int\ln x\,dx=x\ln x-\int1\,dx=x\ln x-x+C.$
:::

::: {.ex t="Example 23.4: $\int x\ln x\,dx$"}
ILATE: $u=\ln x$, $dv=x\,dx$. $\ =\dfrac{x^2}2\ln x-\int\dfrac{x^2}{2}\cdot\dfrac1x\,dx=\dfrac{x^2}{2}\ln x-\dfrac{x^2}4+C.$ In general $\int x^n\ln x\,dx=\dfrac{x^{n+1}}{n+1}\ln x-\dfrac{x^{n+1}}{(n+1)^2}+C$.
:::

::: {.ex t="Example 23.5: inverse trig functions"}
$\int\tan^{-1}x\,dx$: $u=\tan^{-1}x,\ dv=dx$. $\ =x\tan^{-1}x-\int\dfrac{x}{1+x^2}dx=x\tan^{-1}x-\dfrac12\ln(1+x^2)+C.$
Similarly $\int\sin^{-1}x\,dx=x\sin^{-1}x+\sqrt{1-x^2}+C$.
:::

::: {.ex t="Example 23.6: parts twice"}
$\int x^2e^xdx$: first $u=x^2$: $x^2e^x-2\int xe^xdx$; then use Example 23.1: $x^2e^x-2(x-1)e^x+C=e^x(x^2-2x+2)+C$.
:::

::: {.tip t="Tabular method (for polynomial $\times$ exponential/trig)"}
List derivatives of the polynomial down one column until $0$, and integrals of the other factor down another; multiply along the diagonals with alternating signs $+,-,+,\dots$ For $\int x^3e^xdx$:

| $D$ (derivatives of $x^3$) | $I$ (integrals of $e^x$) | sign |
|---|---|---|
| $x^3$ | $e^x$ | $+$ |
| $3x^2$ | $e^x$ | $-$ |
| $6x$ | $e^x$ | $+$ |
| $6$ | $e^x$ | $-$ |

Result: $e^x(x^3-3x^2+6x-6)+C$.
:::

## 23.1 The $e^x\big[f(x)+f'(x)\big]$ shortcut

::: {.thm t="Special integral"}
$$\int e^x\big[f(x)+f'(x)\big]dx=e^xf(x)+C$$
*Proof:* by parts, $\int e^xf(x)dx=e^xf(x)-\int e^xf'(x)dx$, so the two integrals cancel after moving terms across. (Or just differentiate $e^xf$ by the product rule.)
:::

::: {.ex t="Using the shortcut"}
- $\int e^x(\sin x+\cos x)dx=e^x\sin x+C$ (here $f=\sin x$, $f'=\cos x$).
- $\int e^x\left(\ln x+\dfrac1x\right)dx=e^x\ln x+C$.
- $\int e^x\dfrac{x}{(x+1)^2}dx$: split $\dfrac{x}{(x+1)^2}=\dfrac1{x+1}-\dfrac1{(x+1)^2}$, which is $f+f'$ with $f=\frac1{x+1}$. So the integral is $\dfrac{e^x}{x+1}+C$.
:::

## 23.2 The "boomerang" (cyclic) integrals

For $\int e^x\sin x\,dx$ apply parts twice and the original integral **reappears**; then solve for it algebraically.

::: {.ex t="Example 23.7"}
Let $I=\int e^x\sin x\,dx$. First: $I=e^x\sin x-\int e^x\cos x\,dx$. Second: $\int e^x\cos x\,dx=e^x\cos x+\int e^x\sin x\,dx=e^x\cos x+I$. So $I=e^x\sin x-e^x\cos x-I\Rightarrow I=\dfrac{e^x(\sin x-\cos x)}{2}+C.$

General result: $\displaystyle\int e^{ax}\sin bx\,dx=\frac{e^{ax}(a\sin bx-b\cos bx)}{a^2+b^2}+C$.
:::

::: {.warn t="Choose $u$ the wrong way and it gets worse"}
For $\int x\,e^x\,dx$, taking $u=e^x$, $dv=x\,dx$ gives $\frac{x^2}{2}e^x-\int\frac{x^2}2e^xdx$: **harder** than before. If the new integral is nastier, swap your choice of $u$.
:::
