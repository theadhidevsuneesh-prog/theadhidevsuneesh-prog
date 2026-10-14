# Appendix A: The one-stop formula sheet {.u9 data-eyebrow="Appendix A"}

::: {.recall t="How to use this"}
Print this section. Read it the night before the exam and again just before you walk in. Every formula here appears, with its reasoning, in a chapter of this book.
:::

## A.1 Unit I: matrices

::: {.formula t="Matrices and determinants"}
$(AB)^T=B^TA^T$ $\quad$ $(AB)^{-1}=B^{-1}A^{-1}$ $\quad$ $A^{-1}=\dfrac{\operatorname{adj}A}{\abs A}$ $\quad$ $\abs{AB}=\abs A\abs B$ $\quad$ $\abs{A^{-1}}=\dfrac1{\abs A}$ $\quad$ $\abs{kA}=k^n\abs A$ $\quad$ $\abs{\operatorname{adj}A}=\abs A^{n-1}$

$2\times2$ inverse: $\dfrac{1}{ad-bc}\begin{bmatrix}d&-b\\-c&a\end{bmatrix}$. Invertible $\iff\abs A\ne0\iff\operatorname{rank}A=n$.
:::

::: {.formula t="Rank, systems, eigenvalues"}
**Rouché–Capelli** ($r=\operatorname{rank}A,\ r'=\operatorname{rank}[A\mid B],\ n$ unknowns): $r\ne r'$: no solution; $r=r'=n$: unique; $r=r'<n$: infinitely many ($n-r$ parameters). Homogeneous: non-trivial solution $\iff r<n$ (square: $\abs A=0$).

**Eigenvalues:** $\abs{A-\lambda I}=0$. $\ 2\times2$: $\lambda^2-T\lambda+D=0$. $\ 3\times3$: $\lambda^3-S_1\lambda^2+S_2\lambda-\abs A=0$. Sum $=\operatorname{tr}A$, product $=\abs A$. $A^{-1}\to\frac1\lambda$, $A^m\to\lambda^m$, $kA\to k\lambda$, $A+kI\to\lambda+k$.

**Cayley–Hamilton:** $A$ satisfies its own characteristic equation; $2\times2$: $A^2-TA+DI=O$.
:::

## A.2 Unit II: differentiation

::: {.formula t="Rules and standard derivatives"}
$(uv)'=u'v+uv'$ $\quad$ $\left(\dfrac uv\right)'=\dfrac{u'v-uv'}{v^2}$ $\quad$ $\dfrac{d}{dx}f(g(x))=f'(g(x))g'(x)$ $\quad$ parametric: $\dfrac{dy}{dx}=\dfrac{dy/dt}{dx/dt}$

$(x^n)'=nx^{n-1}$ $\;(e^x)'=e^x$ $\;(a^x)'=a^x\ln a$ $\;(\ln x)'=\frac1x$ $\;(\sin x)'=\cos x$ $\;(\cos x)'=-\sin x$ $\;(\tan x)'=\sec^2x$ $\;(\cot x)'=-\operatorname{cosec}^2x$ $\;(\sec x)'=\sec x\tan x$ $\;(\operatorname{cosec}x)'=-\operatorname{cosec}x\cot x$

$(\sin^{-1}x)'=\dfrac1{\sqrt{1-x^2}}$ $\;(\cos^{-1}x)'=-\dfrac1{\sqrt{1-x^2}}$ $\;(\tan^{-1}x)'=\dfrac1{1+x^2}$ $\;(\cot^{-1}x)'=-\dfrac1{1+x^2}$ $\;(\sec^{-1}x)'=\dfrac1{\abs x\sqrt{x^2-1}}$

Log differentiation: $y=u^v\Rightarrow y'=y\Big[\dfrac{vu'}{u}+v'\ln u\Big]$.
:::

::: {.formula t="Theorems"}
**Rolle:** continuous on $[a,b]$, differentiable on $(a,b)$, $f(a)=f(b)\Rightarrow f'(c)=0$ for some $c\in(a,b)$.

**Lagrange MVT:** $f'(c)=\dfrac{f(b)-f(a)}{b-a}$. **Cauchy MVT:** $\dfrac{f(b)-f(a)}{g(b)-g(a)}=\dfrac{f'(c)}{g'(c)}$.

**Taylor:** $f(x)=\displaystyle\sum_{k=0}^n\frac{f^{(k)}(a)}{k!}(x-a)^k+\frac{f^{(n+1)}(c)}{(n+1)!}(x-a)^{n+1}$. **Maclaurin:** $a=0$.

**L'Hôpital:** $\dfrac00$ or $\dfrac\infty\infty$: $\ \lim\dfrac fg=\lim\dfrac{f'}{g'}$. Other forms: convert; for $1^\infty,0^0,\infty^0$ take $\ln$.

**Leibniz:** $(uv)^{(n)}=\displaystyle\sum_{k=0}^n\binom nku^{(n-k)}v^{(k)}$.
:::

::: {.formula t="$n$-th derivatives"}
$D^ne^{ax}=a^ne^{ax}$ $\quad$ $D^n\sin(ax+b)=a^n\sin(ax+b+\frac{n\pi}2)$ $\quad$ $D^n\cos(ax+b)=a^n\cos(ax+b+\frac{n\pi}2)$ $\quad$ $D^n\dfrac1{ax+b}=\dfrac{(-1)^nn!a^n}{(ax+b)^{n+1}}$ $\quad$ $D^n\ln(ax+b)=\dfrac{(-1)^{n-1}(n-1)!a^n}{(ax+b)^n}$ $\quad$ $D^nx^n=n!$
:::

::: {.formula t="Standard limits and series"}
$\dfrac{\sin x}x,\ \dfrac{\tan x}x,\ \dfrac{\sin^{-1}x}x,\ \dfrac{\tan^{-1}x}x,\ \dfrac{e^x-1}x,\ \dfrac{\ln(1+x)}{x}\to1$ $\quad$ $\dfrac{1-\cos x}{x^2}\to\frac12$ $\quad$ $\dfrac{a^x-1}x\to\ln a$ $\quad$ $(1+\tfrac1x)^x\to e$

$e^x=\sum\frac{x^n}{n!}$ $\quad$ $\sin x=x-\frac{x^3}{3!}+\frac{x^5}{5!}-\cdots$ $\quad$ $\cos x=1-\frac{x^2}{2!}+\frac{x^4}{4!}-\cdots$ $\quad$ $\ln(1+x)=x-\frac{x^2}2+\frac{x^3}3-\cdots$ $\quad$ $\tan^{-1}x=x-\frac{x^3}3+\frac{x^5}5-\cdots$ $\quad$ $\frac1{1-x}=1+x+x^2+\cdots$ $\quad$ $(1+x)^n=1+nx+\frac{n(n-1)}{2!}x^2+\cdots$
:::

::: {.formula t="Applications"}
Tangent: $y-y_0=f'(x_0)(x-x_0)$. Normal: slope $-\dfrac1{f'(x_0)}$. Approximation: $f(x+\Delta x)\approx f(x)+f'(x)\Delta x$. $\ MC=\dfrac{dC}{dx}$.

**Extrema:** critical points $f'=0$ or undefined. First-derivative test ($+\to-$ max, $-\to+$ min). Second-derivative test ($f''<0$ max, $f''>0$ min, $=0$ inconclusive). On $[a,b]$: compare $f$ at critical points and end points.
:::

## A.3 Unit III: integration

::: {.formula t="Standard integrals (add $+C$)"}
$\int x^n=\frac{x^{n+1}}{n+1}$ $\;\int\frac1x=\ln\abs x$ $\;\int e^x=e^x$ $\;\int a^x=\frac{a^x}{\ln a}$ $\;\int\sin x=-\cos x$ $\;\int\cos x=\sin x$ $\;\int\sec^2x=\tan x$ $\;\int\operatorname{cosec}^2x=-\cot x$ $\;\int\sec x\tan x=\sec x$ $\;\int\operatorname{cosec}x\cot x=-\operatorname{cosec}x$

$\int\tan x=-\ln\abs{\cos x}$ $\;\int\cot x=\ln\abs{\sin x}$ $\;\int\sec x=\ln\abs{\sec x+\tan x}$ $\;\int\operatorname{cosec}x=\ln\abs{\operatorname{cosec}x-\cot x}$

$\int\frac{dx}{1+x^2}=\tan^{-1}x$ $\;\int\frac{dx}{\sqrt{1-x^2}}=\sin^{-1}x$ $\;\int\frac{dx}{x^2+a^2}=\frac1a\tan^{-1}\frac xa$ $\;\int\frac{dx}{x^2-a^2}=\frac1{2a}\ln\abs{\frac{x-a}{x+a}}$ $\;\int\frac{dx}{\sqrt{a^2-x^2}}=\sin^{-1}\frac xa$

$\int\frac{f'}{f}=\ln\abs f$ $\;\;\int f(ax+b)dx=\frac1aF(ax+b)$ $\;\;\int e^x[f+f']=e^xf$
:::

::: {.formula t="Methods"}
**Substitution:** $u=g(x)$. **By parts:** $\int u\,dv=uv-\int v\,du$, ILATE. **Partial fractions:** divide first if improper; forms $\frac A{x-a}$, $\frac A{x-a}+\frac B{(x-a)^2}$, $\frac{Ax+B}{x^2+px+q}$.

**Definite:** $\int_a^bf=F(b)-F(a)$. $P_2$ split; $P_3$ $f(a+b-x)$; $P_4$ $f(a-x)$; $P_6$ $\int_0^{2a}=2\int_0^a$ or $0$; $P_7$ even $\to2\int_0^a$, odd $\to0$. If $m\le f\le M$: $m(b-a)\le\int_a^bf\le M(b-a)$.
:::

## A.4 Trigonometry

::: {.formula t="Identities"}
$\sin^2+\cos^2=1$, $\;1+\tan^2=\sec^2$, $\;1+\cot^2=\operatorname{cosec}^2$. $\ \sin2\theta=2\sin\theta\cos\theta$, $\ \cos2\theta=\cos^2\theta-\sin^2\theta=2\cos^2\theta-1=1-2\sin^2\theta$. $\ \cos^2\theta=\frac{1+\cos2\theta}2$, $\ \sin^2\theta=\frac{1-\cos2\theta}2$. $\ \sin(A\pm B)=\sin A\cos B\pm\cos A\sin B$. $\ \tan(A\pm B)=\frac{\tan A\pm\tan B}{1\mp\tan A\tan B}$. $\ \sin2\theta=\frac{2\tan\theta}{1+\tan^2\theta}$, $\ \cos2\theta=\frac{1-\tan^2\theta}{1+\tan^2\theta}$. $\ \sin^{-1}x+\cos^{-1}x=\frac\pi2$.
:::

# Appendix B: The 30 most expensive mistakes {.u9 data-eyebrow="Appendix B"}

Every item below is a real, common way to lose marks. Skim the left column; if you recognise yourself, read the right.

::: {.longtable}

| # | The slip | The fix |
|---|---|---|
| 1 | $(a+b)^2=a^2+b^2$ | $(a+b)^2=a^2+2ab+b^2$ |
| 2 | $\sqrt{x^2}=x$ | $\sqrt{x^2}=\abs x$ |
| 3 | $\sin^{-1}x=\dfrac1{\sin x}$ | $\sin^{-1}x$ is the inverse function (an angle); $\frac1{\sin x}=\operatorname{cosec}x$ |
| 4 | $(fg)'=f'g'$ | product rule: $f'g+fg'$ |
| 5 | $\frac{d}{dx}x^x=x\cdot x^{x-1}$ | log differentiation: $x^x(1+\ln x)$ |
| 6 | $\frac{d}{dx}\sin(x^2)=\cos(x^2)$ | multiply by the inside: $2x\cos x^2$ |
| 7 | $\frac{d}{dx}e^{2x}=2xe^{2x-1}$ | $x^n$ and $a^x$ are different: $2e^{2x}$ |
| 8 | quotient rule with the subtraction reversed | low d-high minus high d-low |
| 9 | "$\frac00=0$" or "$\frac00=1$" | $\frac00$ is **indeterminate**; simplify or use L'Hôpital |
| 10 | treating $\infty$ as a number | it is a direction; $\infty-\infty$ is indeterminate |
| 11 | using the quotient rule on $f/g$ inside L'Hôpital | L'Hôpital differentiates numerator and denominator **separately** |
| 12 | L'Hôpital on a limit that is not $\frac00$ or $\frac\infty\infty$ | check the form first |
| 13 | $\lim_{x\to c}f(x)=f(c)$ always | only when $f$ is continuous at $c$ |
| 14 | continuous $\Rightarrow$ differentiable | false ($\abs x$ at $0$); the converse is true |
| 15 | $f'(c)=0\Rightarrow$ extremum | false ($x^3$ at $0$); check the sign change |
| 16 | Rolle/MVT without verifying conditions | check continuity, differentiability, $f(a)=f(b)$ |
| 17 | accepting a $c$ outside $(a,b)$ | $c$ must be in the **open** interval |
| 18 | second-derivative test "proves" something when $f''(c)=0$ | inconclusive; use the first-derivative test |
| 19 | absolute extrema on $[a,b]$ but forgetting the end points | always evaluate $f(a)$ and $f(b)$ |
| 20 | related rates: plugging numbers in **before** differentiating | differentiate first, substitute after |
| 21 | no domain check in optimisation | restrict to the physically allowed domain |
| 22 | forgetting $+C$ | every indefinite integral needs it |
| 23 | $\int fg=\int f\int g$ | there is no such rule; use substitution or parts |
| 24 | $\int\cos3x\,dx=\sin3x$ | divide by the inner derivative: $\frac13\sin3x$ |
| 25 | $\int\frac1x=\ln x$ for all $x$ | $\ln\abs x$ |
| 26 | substitution: leaving $x$'s behind, or forgetting $du$'s factor | rewrite **everything** in $u$ |
| 27 | definite substitution without changing limits | change them (or go back to $x$) |
| 28 | wrong choice of $u$ in parts | ILATE; switch if it gets harder |
| 29 | partial fractions on an improper fraction | long division first |
| 30 | matrices: $AB=BA$, $(AB)^{-1}=A^{-1}B^{-1}$, $\abs{kA}=k\abs A$ | $AB\ne BA$ in general; $(AB)^{-1}=B^{-1}A^{-1}$; $\abs{kA}=k^n\abs A$ |

:::

# Appendix C: Map of your professor's resources {.u9 data-eyebrow="Appendix C"}

Use this to practise on exactly the material you were given.

::: {.longtable}

| Resource | Covers | Where in this book |
|---|---|---|
| **Syllabus** (Units I – III) | the three units | the whole book; see the table of contents |
| **Practice problems from Units 1, 2, 3** (mixed MCQs) | matrices, derivatives, Rolle/MVT, Taylor, limits, critical points, integrals | Chapters 8, 19, 26 |
| **Practice problems Units 2 & 3** (80-question deck) | differentiation, integration (direct, substitution, partial fractions, parts), definite integrals | Chapters 19, 26 and Appendix D |
| **Chapter 5: Continuity and Differentiability** (textbook) | continuity, chain rule, implicit, inverse trig, exp/log, log differentiation, parametric, second order, Rolle, MVT | Chapters 10 – 14 |
| **Chapter 6: Applications of Derivatives** (textbook) | rate of change, increasing/decreasing, tangents/normals, approximations, maxima/minima | Chapters 17 – 18 |
| **Unit 2 (R. K. Jain, Engineering Mathematics)** | differentials, Rolle, Lagrange and Cauchy MVT, L'Hôpital, monotonicity, extrema, Leibniz, Taylor | Chapters 13 – 18 |
| **Taylor and Maclaurin sheet** | the two theorems with remainder, the 10 standard series | Chapter 15 |
| **Partial fractions and properties (handwritten)** | integrals of rational functions; $P_4,P_6$; log and trig integrals | Chapters 24 – 25 |
| **Properties of definite integrals (handwritten)** | $P_0$–$P_7$, even/odd, worked examples Q1–Q6 | Chapter 25 |

:::

## Exercise map for the textbook chapters

| Exercise | Topic | Chapter |
|---|---|---|
| 5.1 (Q1–34) | continuity, finding constants | 10 |
| 5.2 (Q1–10) | chain rule; $\abs{x-1}$ and $[x]$ not differentiable | 11, 12.1 |
| 5.3 (Q1–15) | implicit differentiation (and inverse trig, Examples 40–45) | 12.2, 12.3 |
| 5.4 | exponential and log derivatives | 12.4 |
| 5.5 | logarithmic differentiation | 12.5 |
| 5.6 | parametric derivatives | 12.6 |
| 5.7 | second-order derivatives | 13 |
| 5.8 | Rolle's theorem and MVT | 14 |
| 6.1 | rates of change, marginal cost/revenue | 17.1 |
| 6.2 | increasing and decreasing | 17.2 |
| 6.3 | tangents and normals | 17.3 |
| 6.4 | approximations | 17.4 |
| 6.5 | maxima, minima, optimisation | 18 |
| Jain Ex. 1.1 | Q1–5 approximations, Q6–14 MVT/Rolle, Q15–28 limits, Q29–37 monotonicity, Q38–45 extrema, Q46–50 higher derivatives, Q51–75 Taylor | 17, 14, 16, 17, 18, 13, 15 |

# Appendix D: Complete MCQ answer key {.u9 data-eyebrow="Appendix D"}

The 80-question deck on differentiation and integration (Units II & III). Check your attempts here, then use the chapter tables to see *why*.

<div class="mcqgrid">
<div><b>1.</b> B</div><div><b>2.</b> A</div><div><b>3.</b> C</div><div><b>4.</b> D</div><div><b>5.</b> A</div><div><b>6.</b> B</div><div><b>7.</b> C</div><div><b>8.</b> D</div><div><b>9.</b> B</div><div><b>10.</b> A</div>
<div><b>11.</b> C</div><div><b>12.</b> D</div><div><b>13.</b> B</div><div><b>14.</b> C</div><div><b>15.</b> B</div><div><b>16.</b> D</div><div><b>17.</b> A</div><div><b>18.</b> B</div><div><b>19.</b> C</div><div><b>20.</b> D</div>
<div><b>21.</b> B</div><div><b>22.</b> C</div><div><b>23.</b> A</div><div><b>24.</b> B</div><div><b>25.</b> D</div><div><b>26.</b> C</div><div><b>27.</b> B</div><div><b>28.</b> A</div><div><b>29.</b> D</div><div><b>30.</b> C</div>
<div><b>31.</b> B</div><div><b>32.</b> C</div><div><b>33.</b> B</div><div><b>34.</b> D</div><div><b>35.</b> C</div><div><b>36.</b> A</div><div><b>37.</b> C</div><div><b>38.</b> D</div><div><b>39.</b> B</div><div><b>40.</b> C</div>
<div><b>41.</b> D</div><div><b>42.</b> C</div><div><b>43.</b> B</div><div><b>44.</b> A</div><div><b>45.</b> C</div><div><b>46.</b> B</div><div><b>47.</b> C</div><div><b>48.</b> D</div><div><b>49.</b> A</div><div><b>50.</b> C</div>
<div><b>51.</b> C</div><div><b>52.</b> B</div><div><b>53.</b> D</div><div><b>54.</b> C</div><div><b>55.</b> A</div><div><b>56.</b> B</div><div><b>57.</b> B</div><div><b>58.</b> D</div><div><b>59.</b> A</div><div><b>60.</b> C</div>
<div><b>61.</b> D</div><div><b>62.</b> C</div><div><b>63.</b> B</div><div><b>64.</b> D</div><div><b>65.</b> B</div><div><b>66.</b> D</div><div><b>67.</b> B</div><div><b>68.</b> C</div><div><b>69.</b> B</div><div><b>70.</b> A</div>
<div><b>71.</b> D</div><div><b>72.</b> B</div><div><b>73.</b> D</div><div><b>74.</b> C</div><div><b>75.</b> A</div><div><b>76.</b> B</div><div><b>77.</b> C</div><div><b>78.</b> D</div><div><b>79.</b> B</div><div><b>80.</b> D</div>
</div>

# Appendix E: Plain-English glossary {.u9 data-eyebrow="Appendix E"}

::: {.longtable}

| Term | In plain English |
|---|---|
| **Function** | a rule giving exactly one output for each input |
| **Domain / range** | the allowed inputs / the outputs actually produced |
| **Limit** | the value a function is heading towards as $x$ nears a point |
| **Continuous** | no breaks; can draw it without lifting the pen |
| **Derivative** | instantaneous rate of change; slope of the tangent |
| **Tangent / normal** | the line that just touches the curve / the line perpendicular to it |
| **Chain rule** | derivative of a function of a function: multiply the rates |
| **Implicit** | $y$ is defined by an equation mixing $x$ and $y$ |
| **Critical point** | where $f'=0$ or $f'$ does not exist; candidates for max/min |
| **Local vs absolute extremum** | highest/lowest nearby vs highest/lowest on the whole interval |
| **Point of inflection** | where the curve changes from cup-shaped to cap-shaped (or vice versa) |
| **Indeterminate form** | an expression like $\frac00$ whose value is not decided by the form alone |
| **Taylor/Maclaurin series** | rewriting a function as an infinite polynomial around a point (around $0$) |
| **Antiderivative** | a function whose derivative is the given function |
| **Indefinite / definite integral** | a family of antiderivatives / a number (signed area) |
| **Integrand** | the function being integrated |
| **Substitution** | renaming an inner function $u$ to simplify an integral |
| **Integration by parts** | the product rule in reverse |
| **Partial fractions** | splitting a rational function into simple fractions |
| **Matrix / order** | a rectangular table of numbers / its number of rows $\times$ columns |
| **Determinant** | a number measuring whether a square matrix can be undone |
| **Singular / non-singular** | determinant zero (no inverse) / non-zero (invertible) |
| **Rank** | the number of independent rows (non-zero rows in echelon form) |
| **Linearly independent** | none of the vectors can be built from the others |
| **Consistent system** | a system of equations that has at least one solution |
| **Eigenvalue / eigenvector** | a stretch factor / a direction that is only stretched by the matrix |
| **Characteristic equation** | $\abs{A-\lambda I}=0$, whose roots are the eigenvalues |

:::
