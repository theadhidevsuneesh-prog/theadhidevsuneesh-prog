# Rolle's theorem and the Mean Value theorems {.u2 data-eyebrow="Unit II · Chapter 14"}

::: {.idea t="Big idea"}
Two of the most useful sentences in calculus, each with a one-line everyday meaning:

- **Rolle:** if you leave home and later return to the same spot, then at some moment your velocity was exactly **zero** (when you turned around).
- **Mean Value:** if your *average* speed over a trip was 80 km/h, then at some moment your *speedometer* read exactly 80 km/h.
:::

![Left: Rolle's theorem. Right: the Mean Value Theorem. In both, a tangent line is parallel to a chord (flat in the Rolle case).](figs/fig_rolle_mvt.svg){width=95%}

::: {.story t="The speed-camera theorem"}
Two cameras 10 km apart on a motorway clock a car at 12:00 and 12:05. That is 10 km in 5 minutes: an average of 120 km/h. The driver cannot argue "I was never *at* 120": by the Mean Value Theorem there was an instant when the speedometer read exactly 120. (Real speed cameras use exactly this logic.)
:::

## 14.1 Rolle's theorem

::: {.thm t="Rolle's theorem"}
Let $f:[a,b]\to\mathbb{R}$ satisfy

1. $f$ is **continuous** on the closed interval $[a,b]$,
2. $f$ is **differentiable** on the open interval $(a,b)$,
3. $f(a)=f(b)$.

Then there is **at least one** $c\in(a,b)$ with $f'(c)=0$.
:::

**Why is it true?** A continuous function on $[a,b]$ has a highest and a lowest point (Extreme Value Theorem). If both occur at the end points, the function is constant ($f'=0$ everywhere). Otherwise one occurs *inside*, at some $c$, where the graph has a hilltop or valley, so the tangent is flat: $f'(c)=0$.

::: {.warn t="Each condition matters"}
- **Not continuous:** $f(x)=x$ for $0\le x<1$ and $f(1)=0$ has $f(0)=f(1)$ and is differentiable on $(0,1)$, but $f'(x)=1$ never vanishes. The jump at $x=1$ breaks Rolle.
- **Not differentiable:** $f(x)=\abs x$ on $[-1,1]$ has $f(-1)=f(1)$ but a corner at $0$ and $f'(x)=\pm1$ never $0$. Rolle **fails** (practice MCQ: the reason is that $f$ is *not differentiable at $x=0$*).
- **$f(a)\ne f(b)$:** $f(x)=x^2-1$ on $[1,2]$ has $f'(x)=2x\ne0$ in $(1,2)$.

Also, Rolle gives a **sufficient** condition. Its converse is false: $f'(c)=0$ can happen when the hypotheses fail.
:::

::: {.ex t="Example 14.1: verifying Rolle"}
$f(x)=x^2-4x+3$ on $[1,3]$: polynomial, so continuous and differentiable; $f(1)=0=f(3)$. $f'(x)=2x-4=0\Rightarrow c=2\in(1,3)$ ✓. Similarly $f(x)=x^2+2x-8$ on $[-4,2]$ ($f(-4)=f(2)=0$): $f'(c)=2c+2=0\Rightarrow c=-1$ ✓.
:::

::: {.ex t="Example 14.2: using Rolle to locate roots"}
If $p(x)=(x-1)(x-2)(x-3)$ then $p(1)=p(2)=p(3)=0$, so Rolle on $[1,2]$ and $[2,3]$ shows that $p'(x)=0$ has a root in $(1,2)$ **and** one in $(2,3)$. Since $p'$ is a quadratic, these are *all* its roots.

*Contrapositive form:* if $f$ is differentiable and $f'$ **never vanishes** on $[-5,5]$, then $f(-5)\ne f(5)$ (textbook Ex. 5.8 Q3).
:::

## 14.2 Lagrange's Mean Value Theorem

::: {.thm t="Mean Value Theorem (MVT)"}
If $f$ is continuous on $[a,b]$ and differentiable on $(a,b)$, there exists $c\in(a,b)$ with
$$\boxed{f'(c)=\frac{f(b)-f(a)}{b-a}}.$$
Geometrically: some tangent is **parallel to the chord** joining $(a,f(a))$ and $(b,f(b))$. When $f(a)=f(b)$ the chord is horizontal and we recover Rolle's theorem.
:::

::: {.proof t="Proof (by reducing to Rolle)"}
Define $F(x)=f(x)-\dfrac{f(b)-f(a)}{b-a}\,x$. Then $F$ is continuous on $[a,b]$, differentiable on $(a,b)$, and one checks $F(a)=F(b)$. By Rolle there is $c$ with $F'(c)=0$, i.e. $f'(c)=\dfrac{f(b)-f(a)}{b-a}$. $\blacksquare$
:::

::: {.ex t="Example 14.3: finding $c$"}
- $f(x)=x^2$ on $[0,2]$: slope of chord $=\frac{4-0}2=2=2c\Rightarrow c=1$. On $[2,4]$: $\frac{16-4}{2}=6=2c\Rightarrow c=3$.
- $f(x)=x^2-4x-3$ on $[1,4]$: chord slope $=\frac{-3-(-6)}{3}=1$; $f'(c)=2c-4=1\Rightarrow c=\frac52$.
- $f(x)=x^3-5x^2-3x$ on $[1,3]$: chord slope $=\frac{-27-(-7)}{2}=-10$; $3c^2-10c-3=-10\Rightarrow3c^2-10c+7=0\Rightarrow c=1$ or $\frac73$. Only $c=\frac73$ lies in the **open** interval $(1,3)$.
- $f(x)=\ln x$ on $[1,e]$: $\frac{1-0}{e-1}=\frac1c\Rightarrow c=e-1\approx1.72$.
:::

**What MVT is used for.** MVT is the engine behind many results:

- If $f'(x)=0$ on an interval then $f$ is **constant** there (every chord has slope $0$).
- If $f'>0$ then $f$ is **increasing**; if $f'<0$, decreasing (the basis of Chapter 17).
- **Inequalities and error bounds.**

::: {.ex t="Example 14.4: proving inequalities with MVT"}
(i) $\abs{\cos b-\cos a}\le\abs{b-a}$: $\ \dfrac{\cos b-\cos a}{b-a}=-\sin c$ and $\abs{\sin c}\le1$.

(ii) $e^x>1+x$ for $x>0$: $\ \dfrac{e^x-1}{x}=e^c>1$ for some $c\in(0,x)$.

(iii) $\ln(1+x)<x$ for $x>0$: $\ \dfrac{\ln(1+x)-0}{x}=\dfrac1{1+c}<1$.

(iv) *Bounds on a value* (Jain Ex. 1.5): if $f'(x)=\dfrac1{3-x^2}$ and $f(0)=1$, then $f(1)-1=f'(c)\in\big[\frac13,\frac12\big]$ because $\frac1{3-x^2}$ ranges over $[\frac13,\frac12]$ on $[0,1]$. Hence $\frac43\le f(1)\le\frac32$.
:::

## 14.3 Cauchy's Mean Value Theorem

::: {.thm t="Cauchy MVT"}
If $f,g$ are continuous on $[a,b]$, differentiable on $(a,b)$, and $g'(x)\ne0$ on $(a,b)$, then for some $c\in(a,b)$
$$\frac{f(b)-f(a)}{g(b)-g(a)}=\frac{f'(c)}{g'(c)}.$$
:::

This is the MVT for a curve given *parametrically* $(x,y)=(g(t),f(t))$: some tangent is parallel to the chord. With $g(x)=x$ it becomes Lagrange's MVT. **Do not** try to prove it by applying Lagrange separately to numerator and denominator: that gives two *different* points $c_1\ne c_2$.

::: {.ex t="Example 14.5"}
$f(x)=x^2$, $g(x)=x^3$ on $[1,2]$: $\dfrac{4-1}{8-1}=\dfrac37=\dfrac{2c}{3c^2}=\dfrac2{3c}\Rightarrow c=\dfrac{14}9\in(1,2)$ ✓.
:::

::: {.tip t="Exam checklist for any Rolle/MVT question"}
1. State and **verify the three conditions** (continuity on $[a,b]$, differentiability on $(a,b)$, plus $f(a)=f(b)$ for Rolle).
2. Compute $f'$ and solve for $c$ (Rolle: $f'(c)=0$; MVT: $f'(c)=\frac{f(b)-f(a)}{b-a}$).
3. **Reject** any $c$ outside the *open* interval $(a,b)$.
:::

# Taylor's and Maclaurin's theorems {.u2 data-eyebrow="Unit II · Chapter 15"}

::: {.idea t="Big idea"}
Polynomials are the easiest functions in the world: you can evaluate them with just $+,-,\times$. Taylor's theorem says that **any smooth function behaves like a polynomial near a point**, and tells you exactly which polynomial and how big the error is. That is how calculators compute $\sin$, $\cos$, $e^x$ and $\ln$.
:::

## 15.1 Building the polynomial

Near $x=a$ the tangent line approximates $f$: $f(x)\approx f(a)+f'(a)(x-a)$. It matches the **value** and the **slope** at $a$. To hug the curve better, also match the **curvature** ($f''$), then $f'''$, and so on. Demand that a degree-$n$ polynomial
$$P_n(x)=c_0+c_1(x-a)+c_2(x-a)^2+\cdots+c_n(x-a)^n$$
has the same value and the first $n$ derivatives as $f$ at $x=a$. Differentiating $k$ times and putting $x=a$ gives $P_n^{(k)}(a)=k!\,c_k$. Setting this equal to $f^{(k)}(a)$:
$$\boxed{c_k=\frac{f^{(k)}(a)}{k!}}$$

![Taylor polynomials of $\sin x$ about $0$. Each extra term adds a wiggle and the copy stays accurate for longer.](figs/fig_taylor_sin.svg){width=78%}

## 15.2 Taylor's theorem

::: {.thm t="Taylor's theorem with Lagrange's remainder (your professor's sheet)"}
Let $f$ and its first $(n-1)$ derivatives be continuous on $[a,a+h]$, and let $f^{(n)}$ exist on $(a,a+h)$. Then there is a number $\theta$ with $0<\theta<1$ such that
$$f(a+h)=f(a)+hf'(a)+\frac{h^2}{2!}f''(a)+\cdots+\frac{h^{n-1}}{(n-1)!}f^{(n-1)}(a)+\underbrace{\frac{h^n}{n!}f^{(n)}(a+\theta h)}_{\text{Lagrange remainder }R_n}$$
Writing $a+h=x$, this reads
$$f(x)=f(a)+(x-a)f'(a)+\frac{(x-a)^2}{2!}f''(a)+\cdots+\frac{(x-a)^n}{n!}f^{(n)}(a+\theta h).$$
:::

::: {.formula t="The same theorem in Jain's notation (remainder after the degree-$n$ term)"}
$$f(x)=\sum_{k=0}^{n}\frac{f^{(k)}(a)}{k!}(x-a)^k+R_n(x),\qquad R_n(x)=\frac{(x-a)^{n+1}}{(n+1)!}f^{(n+1)}(c),\ \ c\text{ between }a\text{ and }x.$$
The two statements are identical; they only differ in whether $n$ counts the terms or the degree. Know both so that you are never confused by a textbook.
:::

**Special cases worth knowing.**

- $n=1$ gives $f(a+h)=f(a)+hf'(a+\theta h)$: **the Mean Value Theorem**. Taylor's theorem is MVT for higher derivatives.
- **Maclaurin's theorem** is Taylor with $a=0$, $h=x$:
$$f(x)=f(0)+xf'(0)+\frac{x^2}{2!}f''(0)+\cdots+\frac{x^{n}}{n!}f^{(n)}(\theta x).$$
- If the remainder $R_n\to0$ as $n\to\infty$, we get the infinite **Taylor series** $\displaystyle f(x)=\sum_{n=0}^\infty\frac{f^{(n)}(a)}{n!}(x-a)^n$ and, for $a=0$, the **Maclaurin series** $\displaystyle f(x)=\sum_{n=0}^\infty\frac{f^{(n)}(0)}{n!}x^n$.

::: {.mem t="The recipe"}
**Taylor coefficient of $(x-a)^n$ is $\dfrac{f^{(n)}(a)}{n!}$** (practice MCQ answer B). Not $f^{(n)}(a)$ alone: the $n!$ cancels the factors that appear when you differentiate $(x-a)^n$ repeatedly.
:::

**Error bound.** Since $c$ is unknown, we *bound* the remainder:
$$\abs{R_n(x)}\le\frac{M\,\abs{x-a}^{n+1}}{(n+1)!},\qquad M=\max\abs{f^{(n+1)}}\text{ on the interval.}$$

## 15.3 The standard Maclaurin series

::: {.formula t="Memorise (these are on your professor's sheet)"}

| Function | Series | Valid for |
|---|---|---|
| $e^x$ | $1+x+\dfrac{x^2}{2!}+\dfrac{x^3}{3!}+\cdots=\displaystyle\sum_{n\ge0}\frac{x^n}{n!}$ | all $x$ |
| $e^{-x}$ | $1-x+\dfrac{x^2}{2!}-\dfrac{x^3}{3!}+\cdots$ | all $x$ |
| $\sin x$ | $x-\dfrac{x^3}{3!}+\dfrac{x^5}{5!}-\cdots=\displaystyle\sum_{n\ge0}(-1)^n\frac{x^{2n+1}}{(2n+1)!}$ | all $x$ |
| $\cos x$ | $1-\dfrac{x^2}{2!}+\dfrac{x^4}{4!}-\cdots=\displaystyle\sum_{n\ge0}(-1)^n\frac{x^{2n}}{(2n)!}$ | all $x$ |
| $\sinh x$ | $x+\dfrac{x^3}{3!}+\dfrac{x^5}{5!}+\cdots$ | all $x$ |
| $\cosh x$ | $1+\dfrac{x^2}{2!}+\dfrac{x^4}{4!}+\cdots$ | all $x$ |
| $\tan^{-1}x$ | $x-\dfrac{x^3}{3}+\dfrac{x^5}{5}-\cdots$ | $\abs x\le1$ |
| $\ln(1+x)$ | $x-\dfrac{x^2}{2}+\dfrac{x^3}{3}-\dfrac{x^4}{4}+\cdots$ | $-1<x\le1$ |
| $\ln(1-x)$ | $-x-\dfrac{x^2}{2}-\dfrac{x^3}{3}-\cdots$ | $-1\le x<1$ |
| $(1+x)^n$ | $1+nx+\dfrac{n(n-1)}{2!}x^2+\dfrac{n(n-1)(n-2)}{3!}x^3+\cdots$ | $\abs x<1$ (any $n$) |
| $\dfrac1{1-x}$ | $1+x+x^2+x^3+\cdots$ | $\abs x<1$ |
| $\tan x$ | $x+\dfrac{x^3}{3}+\dfrac{2x^5}{15}+\cdots$ | $\abs x<\frac\pi2$ |

:::

::: {.mem t="Patterns that answer MCQs instantly"}
- $\sin x$ contains only **odd** powers (it is an odd function); $\cos x$ only **even** powers (an even function).
- Signs **alternate** for $\sin,\cos,\ln(1+x),\tan^{-1}x$; they do **not** for $e^x,\ \sinh,\ \cosh,\ \frac1{1-x}$.
- $\dfrac1{1-x}$: first three terms $1+x+x^2$ (practice MCQ answer B). Replace $x$ by $-x$ for $\dfrac1{1+x}=1-x+x^2-\cdots$.
:::

**Derivation of $\sin x$.** The derivatives of $\sin x$ at $0$ cycle: $0,\ 1,\ 0,\ -1,\ 0,\ 1,\dots$ Divide by $n!$ and you get $x-\frac{x^3}{3!}+\frac{x^5}{5!}-\cdots$. For $e^x$ every derivative is $e^x$, which is $1$ at $0$, so $c_n=\frac1{n!}$.

![Left: $e^x$ is captured perfectly by its polynomials for every $x$. Right: $\ln(1+x)$ is only reproduced for $-1<x\le1$; outside that range the polynomials fly away.](figs/fig_taylor_ln.svg){width=95%}

::: {.story t="Euler's masterpiece"}
Put $x=i\theta$ (with $i^2=-1$) into the series for $e^x$ and separate real and imaginary parts: the real part is exactly the series for $\cos\theta$, the imaginary part is the series for $\sin\theta$. So $e^{i\theta}=\cos\theta+i\sin\theta$, and at $\theta=\pi$ we get the famous $e^{i\pi}+1=0$, which ties together $e,\ i,\ \pi,\ 1,\ 0$.
:::

## 15.4 Worked examples

::: {.ex t="Example 15.1: Taylor polynomial about $a\neq0$"}
Find the Taylor polynomial of degree 3 for $f(x)=\sqrt x$ about $a=1$.

::: sol
$f=x^{1/2},\ f'=\tfrac12x^{-1/2},\ f''=-\tfrac14x^{-3/2},\ f'''=\tfrac38x^{-5/2}$. At $x=1$: $1,\ \tfrac12,\ -\tfrac14,\ \tfrac38$. Divide by $k!$:
$$P_3(x)=1+\tfrac12(x-1)-\tfrac18(x-1)^2+\tfrac1{16}(x-1)^3.$$
Test: $P_3(1.2)=1+0.1-0.005+0.0005=1.0955$, and $\sqrt{1.2}=1.09545$ ✓.
:::
:::

::: {.ex t="Example 15.2: compute $\sin29^\circ$"}
Convert: $29^\circ=\dfrac{29\pi}{180}\approx0.506145$ rad. Then
$\sin x\approx x-\dfrac{x^3}{6}+\dfrac{x^5}{120}=0.506145-0.021611+0.000277\approx0.48481.$
The true value is $0.48481$. The first omitted term is about $x^7/5040\approx1.7\times10^{-6}$, so the answer is right to 5 decimal places.
:::

::: {.ex t="Example 15.3: how many terms for $e$?"}
Use $e^x$ at $x=1$: $R_n=\dfrac{e^c}{(n+1)!}<\dfrac3{(n+1)!}$ since $e^c<e<3$. For error $<0.001$ we need $(n+1)!>3000$, i.e. $n+1=7$, so $n=6$ (since $7!=5040$). Indeed $1+1+\frac12+\frac16+\frac1{24}+\frac1{120}+\frac1{720}=2.71806$, and $e=2.71828$.
:::

::: {.ex t="Example 15.4: build new series from old ones"}
- Replace $x$ by $-x^2$ in $e^x$: $\ e^{-x^2}=1-x^2+\dfrac{x^4}{2}-\dfrac{x^6}{6}+\cdots$
- **Multiply** series: $e^x\sin x=(1+x+\frac{x^2}2+\frac{x^3}6)(x-\frac{x^3}6)=x+x^2+\frac{x^3}{3}+\cdots$ (the $x^3$ terms: $\frac12-\frac16=\frac13$).
- Likewise $e^x\cos x=1+x-\dfrac{x^3}3-\dfrac{x^4}6+\cdots$
:::

::: {.ex t="Example 15.5: series make limits easy"}
$\displaystyle\lim_{x\to0}\frac{\sin x-x}{x^3}=\lim\frac{-\frac{x^3}{6}+\frac{x^5}{120}-\cdots}{x^3}=-\frac16.$

$\displaystyle\lim_{x\to0}\frac{e^x-1-x}{x^2}=\frac12,\qquad \lim_{x\to0}\frac{x-\ln(1+x)}{x^2}=\frac12,\qquad\lim_{x\to0}\frac{\tan x-x}{x^3}=\frac13.$
:::

## 15.5 Summary

::: {.recall t="Taylor in a nutshell"}
- **Idea:** match $f$ and its first $n$ derivatives at $a$.
- **Coefficient:** $\dfrac{f^{(k)}(a)}{k!}(x-a)^k$.
- **Error:** $R_n=\dfrac{f^{(n+1)}(c)}{(n+1)!}(x-a)^{n+1}$; bound it with the largest $\abs{f^{(n+1)}}$.
- **Maclaurin** $=$ Taylor at $a=0$. **Taylor** with $n=1$ $=$ **MVT**.
- **Validity:** the infinite series converges only inside its interval (e.g. $\abs x<1$ for $\ln(1+x)$).
:::

# Indeterminate forms and L'Hôpital's rule {.u2 data-eyebrow="Unit II · Chapter 16"}

::: {.idea t="Big idea"}
Some limits look like a tug-of-war with no winner: $\frac00$ ("zero over zero") or $\frac\infty\infty$. Each could be anything: $\frac{x}{x}\to1$, $\frac{x^2}{x}\to0$, $\frac{x}{x^2}\to\infty$. They are called **indeterminate forms**. L'Hôpital's rule resolves them by comparing **how fast** numerator and denominator are changing, i.e. by comparing their derivatives.
:::

## 16.1 The seven indeterminate forms

$$\frac00,\quad\frac\infty\infty,\quad0\cdot\infty,\quad\infty-\infty,\quad1^\infty,\quad0^0,\quad\infty^0.$$

::: {.warn t="Forms that are NOT indeterminate"}
$\infty+\infty=\infty$, $\ \infty\cdot\infty=\infty$, $\ \infty^\infty=\infty$, $\ 0^\infty=0$, $\ \infty^{-\infty}=0$, and $\dfrac{c}{0}$ ($c\ne0$) is infinite. L'Hôpital's rule must **not** be used on these (Jain, Remark 4).
:::

## 16.2 L'Hôpital's rule

::: {.thm t="L'Hôpital's rule"}
Let $f,g$ be differentiable near $a$ (except possibly at $a$), with $g'(x)\ne0$ nearby. If $\displaystyle\lim_{x\to a}\frac{f(x)}{g(x)}$ is of the form $\dfrac00$ **or** $\dfrac{\pm\infty}{\pm\infty}$, then
$$\boxed{\lim_{x\to a}\frac{f(x)}{g(x)}=\lim_{x\to a}\frac{f'(x)}{g'(x)}}$$
provided the right-hand limit exists (or is $\pm\infty$). If $\frac{f'}{g'}$ is again indeterminate, apply the rule again. It also works as $x\to\pm\infty$ and for one-sided limits.
:::

**Why it works ($\frac00$ case).** If $f(a)=g(a)=0$ then $\dfrac{f(x)}{g(x)}=\dfrac{[f(x)-f(a)]/(x-a)}{[g(x)-g(a)]/(x-a)}\to\dfrac{f'(a)}{g'(a)}$.

::: {.warn t="Three big warnings"}
1. **Check the form first.** Apply the rule only to $\frac00$ or $\frac\infty\infty$. (Applying it to a limit like $\frac{1-\cos x}{x}$ is fine, since it is $\frac00$.)
2. **Differentiate top and bottom separately.** Do **not** use the quotient rule!
3. If $\lim\frac{f'}{g'}$ does not exist, L'Hôpital says **nothing**. Example: $\lim_{x\to\infty}\frac{x+\sin x}{x}$ is $\frac\infty\infty$, and $\frac{1+\cos x}{1}$ has no limit, yet the original limit equals $1$ (divide by $x$).
:::

## 16.3 Worked examples (including your practice questions)

::: {.ex t="Example 16.1: the practice-set limits"}
- $\displaystyle\lim_{x\to0}\frac{\sin x}{x}=\lim\frac{\cos x}{1}=1$. $\qquad$ $\displaystyle\lim_{x\to0}\frac{\tan x}{x}=\lim\frac{\sec^2x}{1}=1$.
- $\displaystyle\lim_{x\to0}\frac{1-\cos x}{x}=\lim\frac{\sin x}{1}=0$.
- $\displaystyle\lim_{x\to1}\frac{\ln x}{x-1}=\lim\frac{1/x}{1}=1$.
- $\displaystyle\lim_{x\to\infty}\frac{e^x}{x}=\lim\frac{e^x}{1}=\infty$.
- $\displaystyle\lim_{x\to\infty}xe^{-x}=\lim\frac{x}{e^x}=\lim\frac{1}{e^x}=0$ (a $0\cdot\infty$ form rewritten as $\frac\infty\infty$).
:::

::: {.ex t="Example 16.2: repeated application"}
$\displaystyle\lim_{x\to0}\frac{e^x-e^{-x}-2x}{x-\sin x}$ is $\frac00$. Differentiate: $\frac{e^x+e^{-x}-2}{1-\cos x}$, still $\frac00$. Again: $\frac{e^x-e^{-x}}{\sin x}$, still $\frac00$. Again: $\frac{e^x+e^{-x}}{\cos x}\to\frac21=\mathbf2$.
:::

## 16.4 Reducing the other forms

::: {.formula t="Conversion table"}

| Form | What to do |
|---|---|
| $0\cdot\infty$ | write $f\cdot g=\dfrac{f}{1/g}$ to get $\frac00$ or $\frac\infty\infty$ |
| $\infty-\infty$ | combine into one fraction (common denominator) or rationalise |
| $1^\infty,\ 0^0,\ \infty^0$ | let $y=f^g$, take $\ln y=g\ln f$ (a $0\cdot\infty$ form), find its limit $L$, then the answer is $e^{L}$ |

:::

::: {.ex t="Example 16.3: $0^0$"}
$\displaystyle\lim_{x\to0^+}x^x$: $\ln y=x\ln x=\dfrac{\ln x}{1/x}\to\dfrac{1/x}{-1/x^2}=-x\to0$. So $y\to e^0=\mathbf1$.
:::

::: {.ex t="Example 16.4: $\infty-\infty$"}
$\displaystyle\lim_{x\to0}\Big(\frac1x-\frac1{\sin x}\Big)=\lim\frac{\sin x-x}{x\sin x}=\lim\frac{\cos x-1}{\sin x+x\cos x}=\lim\frac{-\sin x}{2\cos x-x\sin x}=\frac02=\mathbf0.$
:::

::: {.ex t="Example 16.5: $1^\infty$"}
$\displaystyle\lim_{x\to\infty}\Big(1+\frac1x\Big)^x=e$. More generally, $\displaystyle\lim_{x\to\infty}\Big(\frac{x+4}{x+2}\Big)^{x+3}$: write $\frac{x+4}{x+2}=1+\frac2{x+2}$, so $\ln y=(x+3)\ln\!\big(1+\tfrac2{x+2}\big)\approx(x+3)\cdot\tfrac2{x+2}\to2$ and the limit is $\mathbf{e^2}$.
:::

::: {.ex t="Example 16.6: more $\infty^0$ and $1^\infty$ type limits"}
- $\displaystyle\lim_{x\to\pi/2}(\sin x)^{\tan x}$: $\ln y=\dfrac{\ln\sin x}{\cot x}\to\dfrac{\cot x}{-\operatorname{cosec}^2x}=-\sin x\cos x\to0$, so the limit is $e^0=\mathbf1$.
- $\displaystyle\lim_{x\to0}(\cos x)^{1/x^2}=e^{-1/2}$ because $\dfrac{\ln\cos x}{x^2}\to\dfrac{-\tan x}{2x}\to-\dfrac12$.
- $\displaystyle\lim_{x\to\infty}x\tan\frac1x=\lim\frac{\tan(1/x)}{1/x}=1$.
:::

## 16.5 The growth ladder

::: {.formula t="Who wins at infinity?"}
$$\ln x\ \ll\ x^p\ (p>0)\ \ll\ a^x\ (a>1)\ \ll\ x!\ \ll\ x^x$$
Meaning: $\dfrac{\ln x}{x^p}\to0$ and $\dfrac{x^p}{a^x}\to0$ as $x\to\infty$. So any exponential beats any power, and any power beats any logarithm. This is why $\lim\frac{e^x}{x}=\infty$ and $\lim xe^{-x}=0$. Near $0$: $x^n\ln x\to0$ for every $n>0$.
:::

::: {.tip t="L'Hôpital or Taylor?"}
For limits with $\sin,\cos,e^x,\ln(1+x)$ at $0$, expanding each in its series often finishes in one line and avoids repeated differentiation. For limits at infinity or with messy quotients, L'Hôpital is the cleaner tool.
:::
