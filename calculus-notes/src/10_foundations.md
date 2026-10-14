# The Toolkit: everything you need before calculus {.u0 data-eyebrow="Chapter 0 · Foundations"}

::: {.idea t="Why start here?"}
Calculus problems are rarely *hard calculus*. They are usually easy calculus buried inside algebra, trigonometry or logarithms. A student who can simplify fluently finds calculus gentle; a student who cannot finds it painful. This chapter is the cure.
:::

## 0.1 Numbers, intervals and absolute value

**Number families.** Each family sits inside the next: natural numbers $\mathbb{N}=\{1,2,3,\dots\}$, integers $\mathbb{Z}$, rationals $\mathbb{Q}$ (fractions), and the real numbers $\mathbb{R}$ (every point on the number line, including $\sqrt2$ and $\pi$). Calculus lives on $\mathbb{R}$.

**Intervals** are the standard way to describe "all numbers between".

| Notation | Meaning | Picture |
|---|---|---|
| $(a,b)$ | $a<x<b$ (ends **excluded**) | open circles at both ends |
| $[a,b]$ | $a\le x\le b$ (ends **included**) | filled circles |
| $[a,b)$ , $(a,b]$ | one end in, one end out | mixed |
| $(a,\infty)$ | $x>a$ | arrow to the right |
| $(-\infty,b]$ | $x\le b$ | arrow to the left |
| $\mathbb{R}=(-\infty,\infty)$ | every real number | the whole line |

Infinity is **never** included with a square bracket: $\infty$ is not a number, just a direction.

**Inequality rules.** You may add the same number to both sides, or multiply by a *positive* number. Multiplying or dividing by a **negative** number flips the sign: from $-2x<6$ we get $x>-3$.

::: {.def t="Absolute value (distance from zero)"}
$$\abs{x}=\begin{cases} x, & x\ge 0\\[2pt] -x, & x<0\end{cases}$$
So $\abs{5}=5$ and $\abs{-5}=5$. Geometrically, $\abs{x-a}$ is the distance between $x$ and $a$ on the number line.
:::

::: {.formula t="Working with absolute values"}
- $\abs{x}<a \iff -a<x<a$  (a "within $a$ of zero" statement, for $a>0$)
- $\abs{x}>a \iff x<-a$ or $x>a$
- $\abs{ab}=\abs{a}\abs{b}$ and $\sqrt{x^2}=\abs{x}$ (**not** $x$!)
- Triangle inequality: $\abs{a+b}\le\abs{a}+\abs{b}$
:::

::: {.ex t="Example 0.1"}
Solve $\abs{2x-3}\le 5$.

::: sol
$-5\le 2x-3\le 5 \Rightarrow -2\le 2x\le 8 \Rightarrow -1\le x\le 4$. Answer: $[-1,4]$.
:::
:::

**Why it matters later.** To integrate or differentiate $\abs{x-1}$ you will rewrite it as two separate formulas, one for $x\ge1$ and one for $x<1$ (Chapters 10, 12 and 25).

## 0.2 Functions: the central character

::: {.def t="Function"}
A **function** $f$ is a rule that assigns to each input $x$ in a set (the **domain**) exactly **one** output $f(x)$. The set of outputs actually produced is the **range**.
:::

![A function is a machine: one input in, exactly one output out.](figs/fig_function_machine.svg){width=62%}

**Finding the domain.** Ask "what could go wrong?" The only three things that can go wrong at this level:

| Danger | Rule | Example |
|---|---|---|
| Division by zero | denominator $\ne0$ | $\dfrac{1}{x-5}$: domain $x\ne5$ |
| Even root of a negative | radicand $\ge0$ | $\sqrt{x-1}$: domain $x\ge1$ |
| Log of a non-positive | argument $>0$ | $\ln(x+2)$: domain $x>-2$ |

Also $\sin^{-1}x$ and $\cos^{-1}x$ need $-1\le x\le1$, and $\tan x$ is undefined at odd multiples of $\pi/2$.

**Piecewise functions** use different formulas on different intervals, e.g. $\abs{x}$ above. Almost every continuity and differentiability question in Unit II uses one.

**Composition.** $(f\circ g)(x)=f(g(x))$: feed the output of $g$ into $f$. For example if $g(x)=x^2$ and $f(x)=\sin x$ then $f(g(x))=\sin(x^2)$, while $g(f(x))=\sin^2x$. Order matters! Composition is exactly what the **chain rule** (Chapter 12) differentiates.

**Even and odd functions.** These two labels are gold for definite integrals (Chapter 25).

::: {.def t="Even / odd"}
- **Even** if $f(-x)=f(x)$: the graph is a mirror image about the $y$-axis. Examples: $x^2,\ x^4,\ \cos x,\ \abs{x}$.
- **Odd** if $f(-x)=-f(x)$: the graph is symmetric about the origin. Examples: $x,\ x^3,\ \sin x,\ \tan x$.
- Most functions are neither (e.g. $x+1$, $e^x$).
:::

Combining: even $\times$ even = even; odd $\times$ odd = even; even $\times$ odd = odd. Sum of an odd and an even function is generally neither.

**Inverse functions.** If $f$ takes $a$ to $b$, the inverse $f^{-1}$ takes $b$ back to $a$. The graph of $f^{-1}$ is the graph of $f$ reflected in the line $y=x$. Only one-to-one functions have inverses; $\sin x$ gets one *after* restricting its domain, which is why inverse trig functions have fussy ranges (see 0.4).

**The greatest integer (floor) function** $[x]$ is the largest integer $\le x$: $[2.7]=2$, $[-1.2]=-2$, $[3]=3$. Its graph is a staircase, famously discontinuous at every integer (Chapter 10).

**A gallery of the functions you must recognise on sight:**

![Eight graphs to know by heart](figs/fig_gallery.svg){width=100%}

## 0.3 Algebra you must not forget

::: {.formula t="Exponent laws (for $a,b>0$)"}
$$a^m a^n=a^{m+n},\quad \frac{a^m}{a^n}=a^{m-n},\quad (a^m)^n=a^{mn},\quad (ab)^n=a^nb^n,\quad a^{-n}=\frac1{a^n},\quad a^{1/n}=\sqrt[n]{a},\quad a^0=1$$
:::

::: {.formula t="Factorisation identities"}
$$a^2-b^2=(a-b)(a+b),\qquad (a\pm b)^2=a^2\pm2ab+b^2$$
$$a^3-b^3=(a-b)(a^2+ab+b^2),\qquad a^3+b^3=(a+b)(a^2-ab+b^2)$$
$$(a+b)^3=a^3+3a^2b+3ab^2+b^3$$
:::

**Quadratics.** The roots of $ax^2+bx+c=0$ are $x=\dfrac{-b\pm\sqrt{b^2-4ac}}{2a}$. **Completing the square** rewrites $x^2+bx+c=(x+\tfrac b2)^2+c-\tfrac{b^2}4$, a trick used constantly in integration (Chapter 22).

**Polynomial long division.** Dividing like long division of numbers. This is *the* tool for improper fractions in partial fractions (Chapter 24).

::: {.ex t="Example 0.2"}
Divide $x^2+3x+5$ by $x+1$.

::: sol
$x^2+3x+5=(x+1)(x+2)+3$. So $\dfrac{x^2+3x+5}{x+1}=x+2+\dfrac{3}{x+1}$.
:::
:::

**Binomial theorem.** $(1+x)^n=1+nx+\dfrac{n(n-1)}{2!}x^2+\dfrac{n(n-1)(n-2)}{3!}x^3+\cdots$, a fact you will meet again as a Maclaurin series.

**Sigma notation and factorials.** $n!=n(n-1)\cdots2\cdot1$, with $0!=1$. $\displaystyle\sum_{k=1}^{n}a_k=a_1+a_2+\cdots+a_n$ is just shorthand for "add them up".

## 0.4 Trigonometry in one place

**Radians.** $\pi$ radians $=180^\circ$. Calculus **always** uses radians. In radians the limit $\lim\frac{\sin x}{x}=1$ holds; in degrees it does not.

![The unit circle: the point at angle $\theta$ has coordinates $(\cos\theta,\sin\theta)$.](figs/fig_unit_circle.svg){width=62%}

::: {.formula t="The value table (memorise it)"}

| $\theta$ | $0$ | $30^\circ=\frac\pi6$ | $45^\circ=\frac\pi4$ | $60^\circ=\frac\pi3$ | $90^\circ=\frac\pi2$ | $180^\circ=\pi$ |
|---|---|---|---|---|---|---|
| $\sin\theta$ | $0$ | $\frac12$ | $\frac{\sqrt2}{2}$ | $\frac{\sqrt3}{2}$ | $1$ | $0$ |
| $\cos\theta$ | $1$ | $\frac{\sqrt3}{2}$ | $\frac{\sqrt2}{2}$ | $\frac12$ | $0$ | $-1$ |
| $\tan\theta$ | $0$ | $\frac1{\sqrt3}$ | $1$ | $\sqrt3$ | undefined | $0$ |

:::

::: {.mem t="Trick for the table"}
For $\sin$ write $\frac{\sqrt0}{2},\frac{\sqrt1}{2},\frac{\sqrt2}{2},\frac{\sqrt3}{2},\frac{\sqrt4}{2}$ for $0^\circ,30^\circ,45^\circ,60^\circ,90^\circ$. For $\cos$ read the same list backwards.
:::

::: {.formula t="Identities that appear in calculus every day"}
$$\sin^2\theta+\cos^2\theta=1,\qquad 1+\tan^2\theta=\sec^2\theta,\qquad 1+\cot^2\theta=\operatorname{cosec}^2\theta$$
$$\sin2\theta=2\sin\theta\cos\theta,\qquad \cos2\theta=\cos^2\theta-\sin^2\theta=2\cos^2\theta-1=1-2\sin^2\theta$$
$$\boxed{\cos^2\theta=\frac{1+\cos2\theta}{2}},\qquad \boxed{\sin^2\theta=\frac{1-\cos2\theta}{2}}\quad\text{(power reduction: essential for integration)}$$
$$\sin(A\pm B)=\sin A\cos B\pm\cos A\sin B,\qquad \cos(A\pm B)=\cos A\cos B\mp\sin A\sin B$$
$$\tan(A\pm B)=\frac{\tan A\pm\tan B}{1\mp\tan A\tan B}$$
$$\sin2\theta=\frac{2\tan\theta}{1+\tan^2\theta},\quad \cos2\theta=\frac{1-\tan^2\theta}{1+\tan^2\theta},\quad \tan2\theta=\frac{2\tan\theta}{1-\tan^2\theta}$$
$$\tan3\theta=\frac{3\tan\theta-\tan^3\theta}{1-3\tan^2\theta}$$
:::

**Inverse trigonometric functions.** "$\sin^{-1}x$" means "the angle whose sine is $x$" (it is **not** $1/\sin x$). To make it a proper function, mathematicians agree on a **principal range**:

![Domains and principal ranges of the inverse trig functions](figs/fig_inverse_trig.svg){width=100%}

::: {.formula t="Identities for inverse trig"}
$$\sin^{-1}x+\cos^{-1}x=\frac\pi2,\qquad \tan^{-1}x+\cot^{-1}x=\frac\pi2$$
$$\sin^{-1}(\sin x)=x\ \text{only for}\ x\in[-\tfrac\pi2,\tfrac\pi2],\qquad \tan^{-1}x+\tan^{-1}y=\tan^{-1}\!\frac{x+y}{1-xy}\ \ (xy<1)$$
:::

## 0.5 Exponentials and logarithms

The number $e\approx2.71828$ is defined by $e=1+\frac1{1!}+\frac1{2!}+\frac1{3!}+\cdots$. The function $e^x$ is the unique function that equals its own derivative. The **natural logarithm** $\ln x$ (written $\log x$ in your NCERT chapter) is its inverse: $\ln x=y\iff e^y=x$.

![$e^x$ and $\ln x$ are mirror images in the line $y=x$](figs/fig_exp_log.svg){width=50%}

::: {.formula t="Log laws (all logs of positive numbers)"}
$$\ln(pq)=\ln p+\ln q,\quad \ln\frac pq=\ln p-\ln q,\quad \ln p^n=n\ln p,\quad \ln1=0,\quad \ln e=1$$
$$e^{\ln x}=x\ (x>0),\qquad \ln e^{x}=x,\qquad \log_a p=\frac{\ln p}{\ln a}\ \text{(change of base)}$$
$$a^x=e^{x\ln a}\quad(a>0)$$
:::

::: {.warn t="A subtle trap"}
$x=e^{\ln x}$ is true **only for $x>0$**, because $\ln x$ does not exist otherwise (your textbook's Example 28). Domain first, algebra second.
:::

::: {.story t="Where does $e$ come from?"}
In 1683 Jacob Bernoulli asked what happens if a bank pays 100% interest per year but compounds it more and more often. Compounding $n$ times a year multiplies your money by $(1+\frac1n)^n$. As $n$ grows this settles on $2.71828\ldots$, the number $e$.
:::

![Exponentials eventually overtake every power of $x$](figs/fig_growth.svg){width=62%}

## 0.6 Quick self-check

::: {.try t="Ten questions, ten minutes"}
1. Write $\abs{x+2}<3$ without absolute values.
2. Domain of $\dfrac{\sqrt{x-1}}{x-4}$?
3. Is $f(x)=x^3\cos x$ even, odd or neither?
4. Simplify $\dfrac{x^2-9}{x^2+x-12}$.
5. $\sin^2\theta=$ ? in terms of $\cos2\theta$.
6. $\sin\frac\pi6+\cos\frac\pi3=$ ?
7. Simplify $\ln\dfrac{e^3}{x}$.
8. $\sin^{-1}(1)=$ ? and $\tan^{-1}(1)=$ ?
9. Convert $\dfrac{5\pi}{6}$ to degrees.
10. Divide $x^3-1$ by $x-1$.
:::

::: {.sol}
**Answers.** (1) $-5<x<1$. (2) $x\ge1$ and $x\ne4$. (3) odd (odd $\times$ even). (4) $\frac{(x-3)(x+3)}{(x+4)(x-3)}=\frac{x+3}{x+4}$, $x\ne3$. (5) $\frac{1-\cos2\theta}{2}$. (6) $\frac12+\frac12=1$. (7) $3-\ln x$. (8) $\frac\pi2$ and $\frac\pi4$. (9) $150^\circ$. (10) $x^2+x+1$.
:::
