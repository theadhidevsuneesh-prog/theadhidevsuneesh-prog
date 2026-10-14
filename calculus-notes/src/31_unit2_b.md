# The differentiation toolkit {.u2 data-eyebrow="Unit II · Chapter 12"}

::: {.idea t="Big idea"}
With the table of basic derivatives and four rules (sum, product, quotient, **chain**) you can differentiate anything built from familiar functions. This chapter adds the remaining techniques the syllabus names: **implicit**, **inverse trigonometric**, **exponential/logarithmic**, **logarithmic differentiation** and **parametric** differentiation.
:::

## 12.1 The chain rule (functions inside functions)

::: {.thm t="Chain rule"}
If $y=f(u)$ and $u=g(x)$ then
$$\boxed{\frac{dy}{dx}=\frac{dy}{du}\cdot\frac{du}{dx}}\qquad\text{i.e.}\qquad \big(f(g(x))\big)'=f'(g(x))\cdot g'(x).$$
:::

::: {.mem t="The gears picture"}
Three gears turn together: gear $x$ drives gear $u$, which drives gear $y$. If $y$ turns $3\times$ as fast as $u$, and $u$ turns $2\times$ as fast as $x$, then $y$ turns $3\times2=6\times$ as fast as $x$. Rates **multiply** along the chain. *(Pretend $du$ cancels in $\frac{dy}{du}\cdot\frac{du}{dx}$: it is a good memory aid, not a proof.)*
:::

**Working outside-in.** Differentiate the **outer** function, leaving the inside alone, then multiply by the derivative of the inside.

::: {.ex t="Worked examples"}
- $\dfrac{d}{dx}(2x+1)^3=3(2x+1)^2\cdot2=6(2x+1)^2$.
- $\dfrac{d}{dx}\sin(x^2)=\cos(x^2)\cdot2x=2x\cos x^2$. (Not $\cos x^2$ alone!)
- $\dfrac{d}{dx}\tan(2x+3)=2\sec^2(2x+3)$.
- $\dfrac{d}{dx}\cos3x=-3\sin3x$.
- **Three links:** $\dfrac{d}{dx}\sin\big(\cos(x^2)\big)=\cos\big(\cos x^2\big)\cdot\big(-\sin x^2\big)\cdot2x=-2x\sin x^2\cos(\cos x^2)$.
- $\dfrac{d}{dx}\sqrt{3x+2}=\dfrac{3}{2\sqrt{3x+2}}$.
:::

::: {.warn t="Never forget the inside"}
The most common lost mark in calculus is forgetting the "$\times g'(x)$". Ask: *"is the inside just $x$?"* If not, multiply by its derivative.
:::

## 12.2 Implicit differentiation

Sometimes $y$ is tangled up with $x$ in an equation like $x^2+y^2=r^2$ and solving for $y$ is awkward or impossible. We can still find $\dfrac{dy}{dx}$.

::: {.idea t="The trick"}
**Differentiate both sides with respect to $x$, treating $y$ as a function of $x$.** Every time you differentiate an expression in $y$, the chain rule leaves a factor $\dfrac{dy}{dx}$: $\ \dfrac{d}{dx}y^n=ny^{n-1}\dfrac{dy}{dx}$, $\ \dfrac{d}{dx}\sin y=\cos y\,\dfrac{dy}{dx}$. Then collect $\dfrac{dy}{dx}$ terms and solve.
:::

::: {.ex t="Example 12.1: circle"}
$x^2+y^2=r^2\Rightarrow 2x+2y\dfrac{dy}{dx}=0\Rightarrow\boxed{\dfrac{dy}{dx}=-\dfrac xy}$. (Geometrically: the tangent to a circle is perpendicular to the radius, whose slope is $y/x$.) Also $xy=c^2\Rightarrow y+x\,y'=0\Rightarrow y'=-\dfrac yx$.
:::

::: {.ex t="Example 12.2: $y+\sin y=\cos x$"}
$y'+\cos y\cdot y'=-\sin x\Rightarrow y'(1+\cos y)=-\sin x\Rightarrow y'=-\dfrac{\sin x}{1+\cos y}.$
:::

::: {.ex t="Example 12.3: $x^2+xy+y^2=100$"}
$2x+(y+x\,y')+2y\,y'=0\Rightarrow y'(x+2y)=-(2x+y)\Rightarrow y'=-\dfrac{2x+y}{x+2y}.$
:::

::: {.ex t="Example 12.4: the folium $x^3+y^3=3axy$"}
$3x^2+3y^2y'=3a(y+xy')\Rightarrow y'(y^2-ax)=ay-x^2\Rightarrow y'=\dfrac{ay-x^2}{y^2-ax}.$
:::

## 12.3 Derivatives of inverse trigonometric functions

**Derivation (this is the whole trick for any inverse function).** Let $y=\sin^{-1}x$, so $x=\sin y$ with $y\in(-\frac\pi2,\frac\pi2)$. Differentiate implicitly: $1=\cos y\cdot y'$, so $y'=\dfrac1{\cos y}$. In that range $\cos y\ge0$, so $\cos y=\sqrt{1-\sin^2y}=\sqrt{1-x^2}$. Hence
$$\frac{d}{dx}\sin^{-1}x=\frac1{\sqrt{1-x^2}},\qquad |x|<1.$$
Likewise $y=\tan^{-1}x\Rightarrow x=\tan y\Rightarrow1=\sec^2y\cdot y'\Rightarrow y'=\dfrac1{1+\tan^2y}=\dfrac{1}{1+x^2}$. The full table is in Chapter 11 (and your textbook's Table 5.4).

::: {.mem t="Why $\cos^{-1}x$ has a minus"}
Since $\sin^{-1}x+\cos^{-1}x=\frac\pi2$ is a constant, the two derivatives must cancel: $(\cos^{-1}x)'=-(\sin^{-1}x)'$.
:::

**Simplify first, differentiate second.** Expressions like $\sin^{-1}\frac{2x}{1+x^2}$ look terrifying but collapse with a trig substitution, turning a nightmare into a one-liner.

::: {.formula t="Substitution cheat-sheet"}

| Expression | Substitute | Simplifies to | Derivative |
|---|---|---|---|
| $\sin^{-1}\dfrac{2x}{1+x^2}$ ($\abs x\le1$) | $x=\tan\theta$ | $2\tan^{-1}x$ | $\dfrac{2}{1+x^2}$ |
| $\cos^{-1}\dfrac{1-x^2}{1+x^2}$ ($x\ge0$) | $x=\tan\theta$ | $2\tan^{-1}x$ | $\dfrac{2}{1+x^2}$ |
| $\tan^{-1}\dfrac{2x}{1-x^2}$ ($\abs x<1$) | $x=\tan\theta$ | $2\tan^{-1}x$ | $\dfrac{2}{1+x^2}$ |
| $\tan^{-1}\dfrac{3x-x^3}{1-3x^2}$ ($\abs x<\frac1{\sqrt3}$) | $x=\tan\theta$ | $3\tan^{-1}x$ | $\dfrac{3}{1+x^2}$ |
| $\sin^{-1}\!\big(2x\sqrt{1-x^2}\big)$ ($\abs x\le\frac1{\sqrt2}$) | $x=\sin\theta$ | $2\sin^{-1}x$ | $\dfrac{2}{\sqrt{1-x^2}}$ |
| $\cos^{-1}(2x^2-1)$ ($0\le x\le1$) | $x=\cos\theta$ | $2\cos^{-1}x$ | $-\dfrac{2}{\sqrt{1-x^2}}$ |
| $\sin^{-1}(3x-4x^3)$ ($\abs x\le\frac12$) | $x=\sin\theta$ | $3\sin^{-1}x$ | $\dfrac{3}{\sqrt{1-x^2}}$ |

:::

::: {.mem t="Which substitution?"}
See $1+x^2$ or $1-x^2$ in a fraction: try $x=\tan\theta$ (matches $\sin2\theta,\cos2\theta,\tan2\theta$ identities from Chapter 0). See $\sqrt{1-x^2}$: try $x=\sin\theta$ or $\cos\theta$.
:::

::: {.ex t="Example 12.5 (textbook Ex. 45)"}
(i) $\cos^{-1}(\sin x)=\cos^{-1}\cos(\frac\pi2-x)=\frac\pi2-x$ (for $x\in[-\frac\pi2,\frac\pi2]$), so the derivative is $-1$.
(ii) $\tan^{-1}\dfrac{\sin x}{1+\cos x}=\tan^{-1}\dfrac{2\sin\frac x2\cos\frac x2}{2\cos^2\frac x2}=\tan^{-1}\tan\frac x2=\dfrac x2$, so the derivative is $\dfrac12$.
:::

## 12.4 Exponential and logarithmic functions

$$\frac{d}{dx}e^x=e^x,\qquad \frac d{dx}\ln x=\frac1x\ (x>0),\qquad \frac d{dx}\ln\abs x=\frac1x\ (x\ne0),\qquad \frac d{dx}a^x=a^x\ln a.$$
With the chain rule: $\dfrac{d}{dx}e^{g(x)}=g'(x)e^{g(x)}$ and $\dfrac{d}{dx}\ln g(x)=\dfrac{g'(x)}{g(x)}$.

::: {.ex t="Example 12.6 (textbook Ex. 29)"}
::: {.cols2}
- $\dfrac{d}{dx}e^{-x}=-e^{-x}$
- $\dfrac{d}{dx}e^{\cos x}=-\sin x\,e^{\cos x}$
- $\dfrac d{dx}\sin(\ln x)=\dfrac{\cos(\ln x)}{x}$
- $\dfrac d{dx}\cos^{-1}(e^x)=\dfrac{-e^x}{\sqrt{1-e^{2x}}}$
- $\dfrac d{dx}\ln(x^3)=\dfrac3x$ (simplify first: $\ln x^3=3\ln x$)
- $\dfrac{d}{dx}\ln(\sin x)=\cot x$
:::

$\dfrac{d}{dx}\log_7(\ln x)$: change base to get $\dfrac{\ln(\ln x)}{\ln7}$, whose derivative is $\dfrac{1}{x\,\ln x\,\ln 7}$.
:::

## 12.5 Logarithmic differentiation

Use it for **(a)** a variable raised to a variable power, like $x^x$ or $(\sin x)^{\cos x}$, or **(b)** a huge product/quotient/power. Taking $\ln$ turns products into sums, quotients into differences and powers into multiples.

::: {.idea t="Recipe"}
1. Take $\ln$ of both sides and simplify with log laws.
2. Differentiate both sides **implicitly** ($\ln y\to\frac1y\frac{dy}{dx}$).
3. Multiply by $y$ and substitute the original $y$ back.
(The function and all bases must be **positive**, otherwise the logs do not exist.)
:::

::: {.formula t="General power-exponential formula"}
For $y=[u(x)]^{v(x)}$ with $u>0$:
$$\frac{dy}{dx}=y\left[\frac{v\,u'}{u}+v'\ln u\right]$$
(= "treat the exponent as constant" **plus** "treat the base as constant".)
:::

::: {.ex t="Example 12.7: $y=x^x$"}
$\ln y=x\ln x\Rightarrow\frac{y'}{y}=\ln x+1\Rightarrow\boxed{y'=x^x(1+\ln x)}$. (Practice MCQ: option (C).) The tempting answer $x\cdot x^{x-1}$ treats the exponent as constant and is **wrong**.
:::

::: {.ex t="Example 12.8: $y=x^{\sin x}$"}
$\ln y=\sin x\ln x\Rightarrow\frac{y'}y=\cos x\ln x+\frac{\sin x}{x}$, so $y'=x^{\sin x}\left[\dfrac{\sin x}{x}+\cos x\ln x\right].$
:::

::: {.ex t="Example 12.9: a big quotient"}
$y=\sqrt{\dfrac{(x-3)(x^2+4)}{3x^2+4x+5}}$. Then $\ln y=\tfrac12\big[\ln(x-3)+\ln(x^2+4)-\ln(3x^2+4x+5)\big]$ and
$$y'=\frac y2\left[\frac1{x-3}+\frac{2x}{x^2+4}-\frac{6x+4}{3x^2+4x+5}\right].$$
:::

::: {.ex t="Example 12.10: $y^x=x^y$"}
$x\ln y=y\ln x\Rightarrow\ln y+\dfrac{x}{y}y'=y'\ln x+\dfrac yx\Rightarrow y'\Big(\dfrac xy-\ln x\Big)=\dfrac yx-\ln y$, so $\ y'=\dfrac{y(y-x\ln y)}{x(x-y\ln x)}.$
:::

::: {.try t="Try it"}
Differentiate $y=(\sin x)^{\sin x}$. *Answer: $y'=(\sin x)^{\sin x}\cos x\,(1+\ln\sin x)$.*
:::

## 12.6 Parametric differentiation

Sometimes $x$ and $y$ are both given in terms of a third variable $t$ (the **parameter**), e.g. the path of a moving point. Then by the chain rule $\dfrac{dy}{dt}=\dfrac{dy}{dx}\cdot\dfrac{dx}{dt}$, giving

::: {.formula t="Parametric derivative"}
$$\frac{dy}{dx}=\frac{dy/dt}{dx/dt}=\frac{g'(t)}{f'(t)}\qquad\text{for }x=f(t),\ y=g(t),\ f'(t)\ne0.$$
:::

The answer is naturally in terms of $t$. You do **not** need to eliminate $t$.

::: {.ex t="Worked examples (textbook Ex. 34–37)"}
- $x=at^2,\ y=2at$: $\ \dfrac{dy}{dx}=\dfrac{2a}{2at}=\dfrac1t$.
- $x=a\cos\theta,\ y=a\sin\theta$: $\ \dfrac{dy}{dx}=\dfrac{a\cos\theta}{-a\sin\theta}=-\cot\theta$.
- $x=a(\theta+\sin\theta),\ y=a(1-\cos\theta)$: $\ \dfrac{dy}{dx}=\dfrac{a\sin\theta}{a(1+\cos\theta)}=\tan\dfrac\theta2$.
- Astroid $x=a\cos^3\theta,\ y=a\sin^3\theta$: $\ \dfrac{dy}{dx}=\dfrac{3a\sin^2\theta\cos\theta}{-3a\cos^2\theta\sin\theta}=-\tan\theta$ (which equals $-\sqrt[3]{y/x}$, since $x^{2/3}+y^{2/3}=a^{2/3}$). Eliminating $\theta$ first would have been very tedious.
:::

**Derivative with respect to another function.** To find $\dfrac{du}{dv}$ where both are functions of $x$: $\dfrac{du}{dv}=\dfrac{du/dx}{dv/dx}$. Example: differentiate $\sin^2x$ w.r.t. $e^{\cos x}$: $\ \dfrac{2\sin x\cos x}{-\sin x\,e^{\cos x}}=-\dfrac{2\cos x}{e^{\cos x}}$.

::: {.tip t="Pick the right tool"}

| You see... | Use |
|---|---|
| a function of a function | chain rule |
| $x$ and $y$ mixed in one equation | implicit differentiation |
| variable$^{\text{variable}}$, or a big product/quotient/power | logarithmic differentiation |
| $x=f(t)$, $y=g(t)$ | parametric formula |
| an inverse trig of a messy fraction | trig substitution first |

:::

# Higher-order derivatives {.u2 data-eyebrow="Unit II · Chapter 13"}

::: {.idea t="Big idea"}
Differentiate again and you get the **rate of change of the rate of change**. If $s(t)$ is position, $s'$ is velocity and $s''$ is **acceleration**. On a graph, $f''$ tells you how the slope itself is changing: whether the curve bends up (like a cup) or down (like a cap).
:::

## 13.1 Second-order derivatives

$$\frac{d^2y}{dx^2}=\frac{d}{dx}\!\left(\frac{dy}{dx}\right)=f''(x)=y''=y_2.$$
Higher orders: $y_3,\ y_4,\ \dots,\ y_n=\dfrac{d^ny}{dx^n}=f^{(n)}(x)$.

**Quick values (all appear in your practice set):** $\ (x^4)''=12x^2$, $\ (e^{3x})''=9e^{3x}$, $\ (\ln x)''=-\dfrac1{x^2}$, $\ (a^x)''=a^x(\ln a)^2$.

::: {.ex t="Example 13.1: prove a differential equation"}
If $y=A\sin x+B\cos x$ then $y'=A\cos x-B\sin x$, $y''=-A\sin x-B\cos x=-y$. Hence $\ y''+y=0$. (Pattern: the second derivative of $\sin$ and $\cos$ returns the function with a minus sign.)
:::

::: {.ex t="Example 13.2"}
If $y=3e^{2x}+2e^{3x}$ then $y'=6e^{2x}+6e^{3x}$, $y''=12e^{2x}+18e^{3x}$, and $\ y''-5y'+6y=(12-30+18)e^{2x}+(18-30+12)e^{3x}=0$.
:::

::: {.ex t="Example 13.3: inverse trig"}
If $y=\sin^{-1}x$, show $(1-x^2)y_2-xy_1=0$.

::: sol
$y_1=\dfrac1{\sqrt{1-x^2}}$, so $(1-x^2)y_1^2=1$. Differentiate: $(1-x^2)\cdot2y_1y_2+y_1^2(-2x)=0$. Divide by $2y_1$: $(1-x^2)y_2-xy_1=0$. ✓ *(Squaring first avoids differentiating a square root.)*
:::
:::

::: {.try t="Try it"}
If $y=(\tan^{-1}x)^2$, show $(x^2+1)^2y_2+2x(x^2+1)y_1=2$. *(Hint: $y_1=\dfrac{2\tan^{-1}x}{1+x^2}$, so $(1+x^2)y_1=2\tan^{-1}x$; differentiate again.)*
:::

**Parametric second derivative.** $\dfrac{d^2y}{dx^2}=\dfrac{\frac{d}{dt}\left(\frac{dy}{dx}\right)}{dx/dt}$. *(Note: it is **not** $\frac{d^2y/dt^2}{d^2x/dt^2}$.)*

::: {.ex t="Example 13.4: the cycloid"}
$x=a(t-\sin t),\ y=a(1-\cos t)$. Then $\dfrac{dy}{dx}=\dfrac{\sin t}{1-\cos t}=\cot\dfrac t2$, so $\dfrac{d}{dt}\Big(\dfrac{dy}{dx}\Big)=-\dfrac12\operatorname{cosec}^2\dfrac t2$, and dividing by $\dfrac{dx}{dt}=2a\sin^2\dfrac t2$:
$$\frac{d^2y}{dx^2}=-\frac{1}{4a\sin^4(t/2)}.$$
:::

## 13.2 The $n$-th derivative: patterns

For a few families the $n$-th derivative has a closed formula. Memorise these; each is checked by differentiating once or twice and spotting the pattern.

::: {.formula t="Standard $n$-th derivatives ($D=\frac{d}{dx}$)"}
$$D^n x^m=m(m-1)\cdots(m-n+1)\,x^{m-n}\quad\Big(\text{so }D^n x^n=n!\Big),\qquad D^n e^{ax}=a^ne^{ax},\qquad D^na^x=(\ln a)^na^x$$
$$D^n\sin(ax+b)=a^n\sin\!\Big(ax+b+\frac{n\pi}{2}\Big),\qquad D^n\cos(ax+b)=a^n\cos\!\Big(ax+b+\frac{n\pi}{2}\Big)$$
$$D^n\frac1{ax+b}=\frac{(-1)^nn!\,a^n}{(ax+b)^{n+1}},\qquad D^n\ln(ax+b)=\frac{(-1)^{n-1}(n-1)!\,a^n}{(ax+b)^n}$$
$$D^n\big[e^{ax}\sin(bx+c)\big]=(a^2+b^2)^{n/2}e^{ax}\sin(bx+c+n\varphi),\qquad \varphi=\tan^{-1}\frac ba$$
:::

**Rational functions:** split into partial fractions first, then use the $\frac1{ax+b}$ formula.

::: {.ex t="Example 13.5"}
$y=\dfrac1{x^2-1}=\dfrac12\left[\dfrac1{x-1}-\dfrac1{x+1}\right]$, so $\ y_n=\dfrac{(-1)^nn!}{2}\left[\dfrac1{(x-1)^{n+1}}-\dfrac1{(x+1)^{n+1}}\right].$
:::

## 13.3 Leibniz's formula for a product

::: {.thm t="Leibniz formula"}
$$(uv)^{(n)}=\sum_{k=0}^n\binom nk u^{(n-k)}v^{(k)}=u^{(n)}v+nu^{(n-1)}v'+\binom n2u^{(n-2)}v''+\cdots+uv^{(n)}$$
It is the binomial theorem in disguise. Choose $v$ to be the factor that **dies quickly** (a polynomial), so only a few terms survive.
:::

::: {.ex t="Example 13.6"}
$D^n(x^2e^x)$: take $v=x^2$ (derivatives $2x,\ 2,\ 0,\dots$) and $u=e^x$ ($u^{(k)}=e^x$):
$$D^n(x^2e^x)=e^x\big[x^2+2nx+n(n-1)\big].$$
:::

::: {.ex t="Example 13.7 (Jain, Ex. 1.15)"}
The 4th derivative of $e^{ax}\sin bx$ at $x=0$. By the $n$-th derivative formula, $D^4=(a^2+b^2)^2e^{ax}\sin(bx+4\varphi)$; at $0$ this is $(a^2+b^2)^2\sin4\varphi=\mathbf{4ab(a^2-b^2)}$, using $\sin4\varphi=2\sin2\varphi\cos2\varphi$ with $\sin\varphi=\frac b{\sqrt{a^2+b^2}}$.
:::
