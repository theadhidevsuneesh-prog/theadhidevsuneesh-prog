# Limits: where is it heading? {.u2 data-eyebrow="Unit II · Chapter 9"}

::: {.idea t="Big idea"}
A **limit** describes what value a function is *heading towards* as its input gets close to some point. It does **not** care what happens *at* the point itself. This one idea is the foundation under both derivatives and integrals: a derivative is a limit of slopes, an integral is a limit of sums.
:::

## 9.1 The idea in a table

Let $f(x)=\dfrac{x^2-1}{x-1}$. At $x=1$ it is $\tfrac00$, undefined. But look at nearby values:

| $x$ | $0.9$ | $0.99$ | $0.999$ | $1$ | $1.001$ | $1.01$ | $1.1$ |
|---|---|---|---|---|---|---|---|
| $f(x)$ | $1.9$ | $1.99$ | $1.999$ | **?** | $2.001$ | $2.01$ | $2.1$ |

From both sides the outputs close in on $2$. We write
$$\lim_{x\to1}\frac{x^2-1}{x-1}=2.$$
Algebra confirms it: for $x\ne1$, $\frac{x^2-1}{x-1}=x+1\to2$.

::: {.def t="Limit (informal definition)"}
$\displaystyle\lim_{x\to c}f(x)=L$ means: $f(x)$ can be made as close to $L$ as we like by taking $x$ close enough to $c$ (but $x\neq c$).
:::

## 9.2 One-sided limits

Approach $c$ from the **left** ($x\to c^-$) or from the **right** ($x\to c^+$). These can differ.

::: {.thm t="Existence of a limit"}
$\displaystyle\lim_{x\to c}f(x)$ exists **if and only if** the left-hand limit and the right-hand limit both exist and are **equal**.
:::

![Left and right limits. In the left picture they disagree, so the limit does not exist. In the right picture both are 1 even though $f(0)=2$.](figs/fig_onesided.svg){width=92%}

## 9.3 Limit laws

If $\lim f=L$ and $\lim g=M$ (as $x\to c$), then:

::: {.formula t="Limit laws"}
$$\lim(f\pm g)=L\pm M,\quad \lim(fg)=LM,\quad \lim(kf)=kL,\quad \lim\frac fg=\frac LM\ (M\ne0),\quad \lim f^n=L^n$$
:::

**Squeeze (sandwich) theorem.** If $g(x)\le f(x)\le h(x)$ near $c$ and $g,h$ both tend to $L$, then $f\to L$ too. This is how we prove the most important limit in the course:

![$\dfrac{\sin x}{x}$ is not defined at $0$ but tends to $1$.](figs/fig_limit_sinx.svg){width=62%}

::: {.proof t="Why $\sin x/x\to1$"}
For small $x>0$ (radians!) geometry gives $\sin x<x<\tan x$. Dividing by $\sin x$: $1<\frac{x}{\sin x}<\frac1{\cos x}$, i.e. $\cos x<\frac{\sin x}x<1$. As $x\to0$, $\cos x\to1$, so $\frac{\sin x}{x}$ is squeezed to $1$.
:::

## 9.4 Techniques for finding limits

::: {.tip t="Always try these in order"}
1. **Substitute.** If the function is continuous at $c$ (polynomials, $\sin$, $e^x$, ...) the answer is $f(c)$. Done.
2. If you get $\tfrac00$: **factorise and cancel**, or **rationalise**.
3. For $x\to\pm\infty$: **divide numerator and denominator by the highest power of $x$**.
4. Recognise a **standard limit** (next table), possibly after a substitution.
5. As a last resort use **L'Hôpital's rule** (Chapter 16) or a **series** (Chapter 15).
:::

::: {.ex t="Example 9.1: factorise"}
$\displaystyle\lim_{x\to2}\frac{x^2-4}{x-2}=\lim_{x\to2}(x+2)=4.$
:::

::: {.ex t="Example 9.2: rationalise"}
$\displaystyle\lim_{x\to0}\frac{\sqrt{1+x}-1}{x}=\lim_{x\to0}\frac{(1+x)-1}{x(\sqrt{1+x}+1)}=\lim_{x\to0}\frac{1}{\sqrt{1+x}+1}=\frac12.$
:::

::: {.ex t="Example 9.3: limits at infinity"}
$\displaystyle\lim_{x\to\infty}\frac{3x^2+2x}{5x^2-1}=\lim_{x\to\infty}\frac{3+2/x}{5-1/x^2}=\frac35.$

$\displaystyle\lim_{x\to\infty}\left(\sqrt{x^2+x}-x\right)=\lim\frac{x}{\sqrt{x^2+x}+x}=\lim\frac{1}{\sqrt{1+1/x}+1}=\frac12.$
:::

## 9.5 Standard limits (learn these cold)

::: {.formula t="The standard limit table"}

| Limit | Value |
|---|---|
| $\displaystyle\lim_{x\to0}\frac{\sin x}{x}$ , $\ \displaystyle\lim_{x\to0}\frac{\tan x}{x}$ , $\ \displaystyle\lim_{x\to0}\frac{\sin^{-1}x}{x}$ , $\ \displaystyle\lim_{x\to0}\frac{\tan^{-1}x}{x}$ | $1$ |
| $\displaystyle\lim_{x\to0}\frac{1-\cos x}{x^2}$ | $\dfrac12$ |
| $\displaystyle\lim_{x\to0}\frac{1-\cos x}{x}$ | $0$ |
| $\displaystyle\lim_{x\to0}\frac{e^x-1}{x}$ | $1$ |
| $\displaystyle\lim_{x\to0}\frac{a^x-1}{x}$ | $\ln a$ |
| $\displaystyle\lim_{x\to0}\frac{\ln(1+x)}{x}$ | $1$ |
| $\displaystyle\lim_{x\to0}(1+x)^{1/x}$ , $\ \displaystyle\lim_{x\to\infty}\left(1+\frac1x\right)^{x}$ | $e$ |
| $\displaystyle\lim_{x\to a}\frac{x^n-a^n}{x-a}$ | $na^{n-1}$ |

:::

::: {.warn t="Radians only"}
$\lim\frac{\sin x}{x}=1$ is true only when $x$ is in **radians**. In degrees the limit is $\pi/180$.
:::

## 9.6 Infinite limits

Look at $f(x)=\dfrac1x$ near $0$. As $x\to0^+$ the values $10,\,100,\,1000,\dots$ grow without bound; as $x\to0^-$ they fall to $-10,\,-100,\,-1000,\dots$ We write $\lim_{x\to0^+}\frac1x=+\infty$ and $\lim_{x\to0^-}\frac1x=-\infty$.

::: {.warn t="$\infty$ is not a number"}
"$=\infty$" describes **how** a limit fails to exist (it grows without bound). It never means the limit is a real number. You cannot do ordinary arithmetic like $\infty-\infty$ (that is an **indeterminate form**, Chapter 16).
:::

The line $x=0$ is a **vertical asymptote**; $y=L$ is a **horizontal asymptote** if $\lim_{x\to\pm\infty}f(x)=L$.

::: {.try t="Try it"}
Find: (a) $\displaystyle\lim_{x\to0}\frac{\sin5x}{x}$ (b) $\displaystyle\lim_{x\to0}\frac{1-\cos x}{x^2}$ (c) $\displaystyle\lim_{x\to\infty}\frac{2x+1}{x^2+3}$.
*Answers: (a) $5$ (write $5\cdot\frac{\sin5x}{5x}$). (b) $\frac12$. (c) $0$.*
:::

# Continuity {.u2 data-eyebrow="Unit II · Chapter 10"}

::: {.idea t="Big idea"}
**Pen test.** A function is continuous if you can draw its graph without lifting your pen. A discontinuity is a place where you *must* lift the pen: a hole, a jump, or a blow-up. Mathematically: *no surprises*, meaning the value of the function at a point equals the value it was heading towards.
:::

## 10.1 Definition

::: {.def t="Continuity at a point"}
A function $f$ is **continuous at $x=c$** if all three hold:

1. $f(c)$ is defined;
2. $\displaystyle\lim_{x\to c}f(x)$ exists (left limit $=$ right limit);
3. $\displaystyle\lim_{x\to c}f(x)=f(c)$.

In one line: $\ \text{LHL}=\text{RHL}=f(c)$. If this fails, $f$ is **discontinuous** at $c$.
:::

A function is **continuous on an interval** if it is continuous at every point of it. At an end point $a$ of $[a,b]$ we use the one-sided limit: $\lim_{x\to a^+}f(x)=f(a)$, and $\lim_{x\to b^-}f(x)=f(b)$.

## 10.2 The kinds of discontinuity

![Four behaviours at a point. The first is the only one that passes the pen test.](figs/fig_discontinuities.svg){width=100%}

| Type | What happens | Fixable? |
|---|---|---|
| **Removable** | limit exists but $\ne f(c)$, or $f(c)$ missing | Yes: redefine $f(c)$ to equal the limit |
| **Jump** | left limit $\ne$ right limit (both finite) | No |
| **Infinite** | a one-sided limit is $\pm\infty$ | No |

## 10.3 Examples from your textbook (worked)

::: {.ex t="Example 10.1: continuous at a point"}
$f(x)=2x+3$ at $x=1$: $f(1)=5$ and $\lim_{x\to1}(2x+3)=5$. Equal, so continuous. Similarly $x^2$ is continuous at $0$.
:::

::: {.ex t="Example 10.2: $\abs{x}$ at $0$"}
$\abs x=-x$ for $x<0$ and $x$ for $x\ge0$. LHL $=\lim_{x\to0^-}(-x)=0$, RHL $=\lim_{x\to0^+}x=0$, and $f(0)=0$. All three agree: **continuous**.
:::

::: {.ex t="Example 10.3: a removable discontinuity"}
$f(x)=x^3+3$ for $x\ne0$, and $f(0)=1$. Then $\lim_{x\to0}f(x)=3\ne f(0)=1$. **Discontinuous** at $0$ (and only there).
:::

::: {.ex t="Example 10.4: a jump"}
$f(x)=\begin{cases}x+2,&x\le1\\x-2,&x>1\end{cases}$.

::: sol
Away from $x=1$ both pieces are polynomials, hence continuous. At $x=1$: LHL $=1+2=3$, RHL $=1-2=-1$. They differ, so $f$ has a **jump discontinuity at $x=1$** (the only one). Changing the value of $f(1)$ to $0$ (as in your textbook's next example) does not repair it.
:::
:::

::: {.ex t="Example 10.5: stitched nicely"}
$f(x)=\begin{cases}x,&x\ge0\\x^2,&x<0\end{cases}$. At $0$: RHL $=0$, LHL $=0^2=0$, $f(0)=0$. **Continuous everywhere.**
:::

::: {.warn t="Is $f(x)=1/x$ a continuous function?"}
Yes! At every point of its **domain** ($x\ne0$) it is continuous. $x=0$ is not in the domain, so there is nothing to be continuous *at*. The graph has a break, but not a *point of discontinuity* in the technical sense. (Your textbook, Example 9, makes exactly this point.) By contrast, the **greatest integer function** below is defined at every real number and *is* discontinuous at every integer.
:::

![The greatest-integer (floor) function $[x]$ is discontinuous at every integer. Filled dot: included; open dot: excluded.](figs/fig_floor.svg){width=50%}

## 10.4 Which functions are continuous?

::: {.thm t="Algebra of continuous functions"}
If $f$ and $g$ are continuous at $c$, so are $f+g$, $f-g$, $f\cdot g$, $kf$, and $f/g$ (provided $g(c)\neq0$). If $g$ is continuous at $c$ and $f$ is continuous at $g(c)$, then the **composition** $f\circ g$ is continuous at $c$.
:::

Using this, the following are continuous **wherever they are defined**: polynomials, rational functions, $\sin x,\cos x$, $\tan x$ (except odd multiples of $\pi/2$), $e^x$, $\ln x$ ($x>0$), $\abs x$, $x^{1/n}$, inverse trigonometric functions, and any sum, product, quotient or composition of these. So $\sin(x^2)$ and $\abs{1-x+\abs x}$ are continuous everywhere with no further work.

## 10.5 Finding unknown constants

The standard exam question: *"find $k$ so that $f$ is continuous at $c$."* The method never changes:

::: {.tip t="Three-line method"}
1. Compute the LHL and RHL at the break point (they will contain $k$).
2. Compute $f(c)$.
3. Set LHL $=$ RHL $=f(c)$ and solve.
:::

::: {.ex t="Worked set (textbook Exercise 5.1)"}
**(a)** $f(x)=\begin{cases}ax+1,&x\le3\\bx+3,&x>3\end{cases}$ continuous at $3$: $\ 3a+1=3b+3\Rightarrow\boxed{3a-3b=2}$.

**(b)** $f(x)=\begin{cases}\dfrac{k\cos x}{\pi-2x},&x\neq\frac\pi2\\3,&x=\frac\pi2\end{cases}$. Put $t=\frac\pi2-x\to0$: $\cos x=\sin t$, $\pi-2x=2t$, so the limit is $\frac k2\cdot\frac{\sin t}{t}\to\frac k2$. Set $\frac k2=3\Rightarrow\boxed{k=6}$.

**(c)** $f(x)=\begin{cases}kx^2,&x\le2\\3,&x>2\end{cases}$: $\ 4k=3\Rightarrow\boxed{k=\tfrac34}$.

**(d)** $f(x)=\begin{cases}kx+1,&x\le\pi\\\cos x,&x>\pi\end{cases}$: $\ k\pi+1=-1\Rightarrow\boxed{k=-\tfrac2\pi}$.

**(e)** $f(x)=\begin{cases}kx+1,&x\le5\\3x-5,&x>5\end{cases}$: $\ 5k+1=10\Rightarrow\boxed{k=\tfrac95}$.

**(f)** $f=\begin{cases}5,&x\le2\\ax+b,&2<x<10\\21,&x\ge10\end{cases}$ continuous: $\ 2a+b=5$ and $10a+b=21\Rightarrow\boxed{a=2,\ b=1}$.

**(g)** $f(x)=\begin{cases}\lambda(x^2-2x),&x\le0\\4x+1,&x>0\end{cases}$. At $0$: LHL $=0$, RHL $=1$: **never** equal, so no $\lambda$ makes $f$ continuous at $0$. At $x=1$: $f$ is just $4x+1$ near $1$, so it is continuous there for every $\lambda$.
:::

::: {.ex t="A famous one: $x^2\sin(1/x)$"}
$f(x)=\begin{cases}x^2\sin\frac1x,&x\ne0\\0,&x=0\end{cases}$. Since $-x^2\le x^2\sin\frac1x\le x^2$ and both bounds $\to0$, the **squeeze theorem** gives $\lim_{x\to0}f(x)=0=f(0)$. So $f$ is continuous at $0$.
:::

## 10.6 Two big theorems about continuous functions

::: {.thm t="Intermediate Value Theorem"}
If $f$ is continuous on $[a,b]$ and $N$ lies between $f(a)$ and $f(b)$, then $f(c)=N$ for some $c\in(a,b)$. *(A continuous path from below sea level to above sea level must cross sea level.)* Use: $f(x)=x^3-x-1$ has a root in $(1,2)$ because $f(1)=-1<0<5=f(2)$.
:::

::: {.thm t="Extreme Value Theorem"}
A function continuous on a **closed interval** $[a,b]$ attains an absolute maximum and an absolute minimum on it. This guarantee is what makes the max/min method of Chapter 18 work.
:::

::: {.try t="Try it"}
Is $f(x)=\begin{cases}\dfrac{x^2-9}{x-3},&x\neq3\\5,&x=3\end{cases}$ continuous at $3$? If not, what value of $f(3)$ would fix it? *Answer: the limit is $6\ne5$, so no. Define $f(3)=6$.*
:::

# The derivative from scratch {.u2 data-eyebrow="Unit II · Chapter 11"}

::: {.idea t="Big idea"}
The derivative measures **how fast something is changing at an instant**. A speedometer shows your derivative of distance with respect to time. On a graph, the derivative is the **slope of the tangent line**. To get it we do something clever: compute the average rate over a short interval, then shrink the interval to nothing.
:::

## 11.1 From average speed to instant speed

A ball falls so that its distance after $t$ seconds is $s(t)=t^2$ metres. Its *average* speed between $t=1$ and $t=1+h$ is
$$\frac{s(1+h)-s(1)}{h}=\frac{(1+h)^2-1}{h}=\frac{2h+h^2}{h}=2+h.$$
Make the time gap $h$ tinier and tinier: $h=0.1$ gives $2.1$; $h=0.001$ gives $2.001$. The speed *at the instant* $t=1$ is the limit: **2 m/s**.

Geometrically, the average speed is the slope of a **secant** line through two points on the graph, and the instant speed is the slope of the **tangent**.

![As $h$ shrinks, the secant lines (amber/orange) rotate into the tangent line (teal).](figs/fig_secant.svg){width=70%}

## 11.2 The definition

::: {.def t="Derivative"}
The derivative of $f$ at $x=c$ is
$$f'(c)=\lim_{h\to0}\frac{f(c+h)-f(c)}{h}\qquad\Big(=\lim_{x\to c}\frac{f(x)-f(c)}{x-c}\Big)$$
provided the limit exists (is finite). As a function: $\displaystyle f'(x)=\lim_{h\to0}\frac{f(x+h)-f(x)}{h}$.
:::

**Notation.** $f'(x)$, $\dfrac{dy}{dx}$, $\dfrac{d}{dx}f(x)$, $y'$, $D f$ all mean the same thing. $\dfrac{dy}{dx}\Big|_{x=c}$ means "evaluate at $x=c$". **Meaning:** slope of the tangent, rate of change of $y$ with respect to $x$, instantaneous velocity.

## 11.3 Computing derivatives from first principles

::: {.ex t="Example 11.1: $f(x)=x^2$"}
$\dfrac{(x+h)^2-x^2}{h}=\dfrac{2xh+h^2}h=2x+h\ \to\ 2x.$
:::

::: {.ex t="Example 11.2: $f(x)=1/x$"}
$\dfrac{\frac1{x+h}-\frac1x}{h}=\dfrac{x-(x+h)}{hx(x+h)}=\dfrac{-1}{x(x+h)}\to-\dfrac1{x^2}.$
:::

::: {.ex t="Example 11.3: $f(x)=\sqrt x$"}
Multiply by the conjugate: $\dfrac{\sqrt{x+h}-\sqrt x}{h}=\dfrac{1}{\sqrt{x+h}+\sqrt x}\to\dfrac{1}{2\sqrt x}.$
:::

::: {.ex t="Example 11.4: $f(x)=\sin x$"}
$\dfrac{\sin(x+h)-\sin x}{h}=\sin x\cdot\dfrac{\cos h-1}{h}+\cos x\cdot\dfrac{\sin h}{h}\to\sin x\cdot0+\cos x\cdot1=\cos x.$
:::

## 11.4 The rules of differentiation

::: {.formula t="General rules"}
For differentiable $u(x)$, $v(x)$ and constant $k$:
$$(k)'=0,\quad (ku)'=ku',\quad (u\pm v)'=u'\pm v'$$
$$\boxed{(uv)'=u'v+uv'}\quad\text{(product rule)},\qquad \boxed{\left(\frac uv\right)'=\frac{u'v-uv'}{v^2}}\quad(v\ne0)\ \text{(quotient rule)}$$
:::

::: {.mem t="Quotient rule chant"}
"**Low d-high minus high d-low, over the square of what's below.**" (Low = $v$, high = $u$.) In symbols: $\dfrac{vu'-uv'}{v^2}$. The order of subtraction matters.
:::

::: {.proof t="Why the product rule is true"}
$\dfrac{u(x+h)v(x+h)-u(x)v(x)}{h}=\dfrac{u(x+h)-u(x)}{h}v(x+h)+u(x)\dfrac{v(x+h)-v(x)}{h}$ (add and subtract $u(x)v(x+h)$ in the numerator). Let $h\to0$: $u'v+uv'$.
:::

::: {.formula t="Table of standard derivatives (memorise all of it)"}

| $f(x)$ | $f'(x)$ | $f(x)$ | $f'(x)$ |
|---|---|---|---|
| $x^n$ | $nx^{n-1}$ | $\sin x$ | $\cos x$ |
| $e^x$ | $e^x$ | $\cos x$ | $-\sin x$ |
| $a^x$ | $a^x\ln a$ | $\tan x$ | $\sec^2x$ |
| $\ln x$ | $\dfrac1x$ | $\cot x$ | $-\operatorname{cosec}^2x$ |
| $\log_ax$ | $\dfrac1{x\ln a}$ | $\sec x$ | $\sec x\tan x$ |
| $\sqrt x$ | $\dfrac1{2\sqrt x}$ | $\operatorname{cosec}x$ | $-\operatorname{cosec}x\cot x$ |
| $\sin^{-1}x$ | $\dfrac{1}{\sqrt{1-x^2}}$ | $\cos^{-1}x$ | $-\dfrac{1}{\sqrt{1-x^2}}$ |
| $\tan^{-1}x$ | $\dfrac{1}{1+x^2}$ | $\cot^{-1}x$ | $-\dfrac{1}{1+x^2}$ |
| $\sec^{-1}x$ | $\dfrac{1}{\abs x\sqrt{x^2-1}}$ | $\operatorname{cosec}^{-1}x$ | $-\dfrac{1}{\abs x\sqrt{x^2-1}}$ |

:::

::: {.mem t="The co- pattern"}
Every "co-" function ($\cos,\cot,\operatorname{cosec},\cos^{-1},\cot^{-1},\operatorname{cosec}^{-1}$) has a **minus sign** in its derivative. (Your textbook writes $x$ instead of $\abs x$ in the $\sec^{-1}$ and $\operatorname{cosec}^{-1}$ formulas; they agree for $x>1$.)
:::

::: {.ex t="Example 11.5: derive $\tan x$ with the quotient rule"}
$(\tan x)'=\left(\dfrac{\sin x}{\cos x}\right)'=\dfrac{\cos x\cos x-\sin x(-\sin x)}{\cos^2x}=\dfrac{1}{\cos^2x}=\sec^2x.$ (Practice MCQ Q1.)
:::

## 11.5 Differentiability

::: {.def t="Differentiable"}
$f$ is **differentiable at $c$** if $f'(c)$ exists, i.e. the **left-hand derivative** $\displaystyle\lim_{h\to0^-}\frac{f(c+h)-f(c)}h$ and the **right-hand derivative** $\displaystyle\lim_{h\to0^+}\frac{f(c+h)-f(c)}h$ both exist, are finite, and are **equal**.
:::

::: {.thm t="Differentiable $\Rightarrow$ continuous"}
If $f$ is differentiable at $c$, then $f$ is continuous at $c$.
:::

::: {.proof t="Proof"}
For $x\ne c$: $f(x)-f(c)=\dfrac{f(x)-f(c)}{x-c}\cdot(x-c)$. Let $x\to c$: the first factor tends to $f'(c)$ and the second to $0$, so $f(x)-f(c)\to f'(c)\cdot0=0$. Hence $\lim f(x)=f(c)$. $\blacksquare$
:::

::: {.warn t="The converse is FALSE"}
Continuous does **not** imply differentiable. $f(x)=\abs x$ is continuous at $0$, but
$$\text{left derivative}=\lim_{h\to0^-}\frac{\abs h}{h}=\frac{-h}{h}=-1,\qquad \text{right derivative}=\lim_{h\to0^+}\frac{h}{h}=+1.$$
They differ, so $\abs x$ has a **corner** at $0$ and no derivative there. *Differentiable* is the stronger property; continuity is a necessary but not sufficient condition.
:::

![Four ways a function can fail to be differentiable at a point.](figs/fig_nondiff.svg){width=100%}

::: {.ex t="Example 11.6: gluing two pieces"}
For $f(x)=\begin{cases}x^2,&x\le1\\ax+b,&x>1\end{cases}$ to be differentiable at $1$, find $a,b$.

::: sol
*Continuity:* $1=a+b$. *Equal slopes:* left derivative $2x|_{x=1}=2$, right derivative $a$, so $a=2$ and then $b=-1$. A function is **smooth** (differentiable) at a join only if the values *and* the slopes match.
:::
:::

::: {.ex t="Example 11.7: smooth despite $\abs{\ }$"}
$f(x)=x\abs x$ at $0$: $\dfrac{f(h)-f(0)}{h}=\dfrac{h\abs h}{h}=\abs h\to0$. So $f'(0)=0$: differentiable even though it contains an absolute value. (Absolute value does not automatically kill differentiability; the function must have a corner.)
:::

::: {.ex t="Example 11.8 (textbook Ex. 5.2 Q9, Q10)"}
$f(x)=\abs{x-1}$ is not differentiable at $x=1$ (a corner, same argument as $\abs x$). The greatest integer function $[x]$ is not even continuous at $x=1,2$, so it cannot be differentiable there.
:::

::: {.try t="Try it"}
Is $f(x)=\abs{x}^3$ differentiable at $0$?
*Answer: yes. $\dfrac{f(h)-f(0)}{h}=\dfrac{\abs h^3}{h}=h\abs h\to0$, so $f'(0)=0$. In fact $f'(x)=3x\abs x$ and $f''(x)=6\abs x$ exist everywhere, but the third derivative at $0$ does not (textbook Misc. Ex. 18).*
:::
