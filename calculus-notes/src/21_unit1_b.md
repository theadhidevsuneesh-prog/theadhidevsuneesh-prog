# Solving systems of linear equations {.u1 data-eyebrow="Unit I · Chapter 5"}

::: {.idea t="Big idea"}
Every system of linear equations can be packaged as a single matrix equation $AX=B$. Each equation is a line (or plane); solving the system means finding where they all meet. Three things can happen, and **rank** tells us which.
:::

![Three possible pictures for two equations in two unknowns. The same trichotomy holds in every dimension.](figs/fig_linear_systems.svg){width=95%}

## 5.1 Matrix form

The system $\ a_{11}x_1+\cdots+a_{1n}x_n=b_1,\ \dots,\ a_{m1}x_1+\cdots+a_{mn}x_n=b_m\ $ becomes
$$\underbrace{\begin{bmatrix}a_{11}&\cdots&a_{1n}\\\vdots&&\vdots\\a_{m1}&\cdots&a_{mn}\end{bmatrix}}_{A}\underbrace{\begin{bmatrix}x_1\\\vdots\\x_n\end{bmatrix}}_{X}=\underbrace{\begin{bmatrix}b_1\\\vdots\\b_m\end{bmatrix}}_{B}$$
The **augmented matrix** is $[A\mid B]$: the coefficient matrix with the right-hand side glued on as an extra column.

## 5.2 The Rouché–Capelli theorem

::: {.thm t="Consistency theorem (Rouché–Capelli)"}
Let $r=\operatorname{rank}(A)$, $r'=\operatorname{rank}[A\mid B]$ and $n=$ number of unknowns.

| Condition | Conclusion |
|---|---|
| $r\neq r'$  (i.e. $r<r'$) | **No solution** (inconsistent) |
| $r=r'=n$ | **Unique solution** |
| $r=r'<n$ | **Infinitely many solutions**, with $n-r$ free parameters |

:::

::: {.mem t="Why?"}
If $r<r'$ the row-reduced augmented matrix contains a row $[0\ 0\ \cdots\ 0\mid c]$ with $c\ne0$, which says $0=c$: an impossibility. If $r=r'<n$, some variables are never pinned down and can be chosen freely.
:::

**Homogeneous systems ($AX=O$).** These are always consistent, because $X=O$ (the **trivial solution**) always works. So only two cases arise:

- $\operatorname{rank}A=n$: only the trivial solution.
- $\operatorname{rank}A<n$: **non-trivial solutions** exist (infinitely many).
- For a **square** homogeneous system: non-trivial solutions exist $\iff\abs{A}=0$.

## 5.3 Gauss elimination in practice

Row-reduce $[A\mid B]$ to echelon form, then back-substitute.

::: {.ex t="Example 5.1: unique solution"}
Solve $x+y+z=6,\quad x-y+z=2,\quad 2x+y-z=1$.

::: sol
$$\left[\begin{array}{ccc|c}1&1&1&6\\1&-1&1&2\\2&1&-1&1\end{array}\right]\xrightarrow[R_3\to R_3-2R_1]{R_2\to R_2-R_1}\left[\begin{array}{ccc|c}1&1&1&6\\0&-2&0&-4\\0&-1&-3&-11\end{array}\right]\xrightarrow{R_3\to R_3-\frac12R_2}\left[\begin{array}{ccc|c}1&1&1&6\\0&-2&0&-4\\0&0&-3&-9\end{array}\right]$$
Here $r=r'=3=n$. Back-substitute: $z=3$, $y=2$, $x=6-2-3=1$. **Solution $(1,2,3)$.**
:::
:::

::: {.ex t="Example 5.2: the classic 'find $\lambda,\mu$' question"}
Discuss the solutions of $\ x+y+z=6,\ \ x+2y+3z=10,\ \ x+2y+\lambda z=\mu.$

::: sol
$R_2\to R_2-R_1$ gives $y+2z=4$. $R_3\to R_3-R_1$ gives $y+(\lambda-1)z=\mu-6$. Now $R_3\to R_3-R_2$ gives $(\lambda-3)z=\mu-10$. So in echelon form the last row is $[0\ \ 0\ \ \lambda-3\mid\mu-10]$.

- **$\lambda\neq3$:** $r=r'=3$. **Unique solution** (for any $\mu$).
- **$\lambda=3,\ \mu\ne10$:** last row $[0\,0\,0\mid\mu-10]$ with $\mu-10\neq0$. $r=2<r'=3$. **No solution.**
- **$\lambda=3,\ \mu=10$:** $r=r'=2<3$. **Infinitely many solutions.** Put $z=t$: $y=4-2t$, $x=6-y-z=2+t$. The solutions are $(2+t,\,4-2t,\,t)$.
:::
:::

::: {.ex t="Example 5.3: homogeneous system"}
For what $k$ does $\ x+2y+z=0,\ 2x+y+3z=0,\ 3x+3y+kz=0\ $ have a non-trivial solution?

::: sol
Need $\abs{A}=0$: $\begin{vmatrix}1&2&1\\2&1&3\\3&3&k\end{vmatrix}=1(k-9)-2(2k-9)+1(6-3)=12-3k=0\Rightarrow k=4.$
:::
:::

## 5.4 Two other methods (know they exist)

- **Inverse method:** if $\abs{A}\ne0$, then $X=A^{-1}B$.
- **Cramer's rule** (square, $\abs{A}\neq0$): $x_i=\dfrac{\abs{A_i}}{\abs{A}}$, where $A_i$ is $A$ with column $i$ replaced by $B$.

::: {.warn t="Common slip"}
Do **not** compare $\operatorname{rank}A$ with the *number of equations*. Compare it with the number of **unknowns** $n$ and with $\operatorname{rank}[A\mid B]$.
:::

# Eigenvalues and eigenvectors {.u1 data-eyebrow="Unit I · Chapter 6"}

::: {.idea t="Big idea"}
A matrix $A$ transforms vectors: it rotates, stretches and shears them. Most vectors get turned to point in a *new* direction. But some special directions are only **stretched or shrunk**, never turned. Those directions are the **eigenvectors**, and the stretch factors are the **eigenvalues**. (*Eigen* is German for "own": these are the matrix's own special directions.)
:::

![The matrix $A$ stretches the diagonal direction by 3 and leaves the anti-diagonal direction unchanged; the whole circle becomes an ellipse whose axes are the eigen-directions.](figs/fig_eigen.svg){width=95%}

::: {.def t="Eigenvalue and eigenvector"}
For a square matrix $A$, a number $\lambda$ is an **eigenvalue** and a **non-zero** vector $x$ is a corresponding **eigenvector** if
$$Ax=\lambda x.$$
:::

## 6.1 How to find them

Rewrite $Ax=\lambda x$ as $(A-\lambda I)x=0$. A non-zero solution $x$ exists only if $A-\lambda I$ is singular:
$$\boxed{\abs{A-\lambda I}=0}\qquad\text{(the characteristic equation)}$$
Expanding the determinant gives a polynomial in $\lambda$ of degree $n$ (the characteristic polynomial); its roots are the eigenvalues. For each eigenvalue, solve $(A-\lambda I)x=0$ to get the eigenvectors.

::: {.formula t="Shortcuts for the characteristic equation"}
**$2\times2$:** $\ \lambda^2-T\lambda+D=0$, where $T=\operatorname{tr}A$ and $D=\abs{A}$.

**$3\times3$:** $\ \lambda^3-S_1\lambda^2+S_2\lambda-\abs{A}=0$, where $S_1=\operatorname{tr}A$ and $S_2=$ sum of the three principal $2\times2$ minors (the minors of the diagonal entries).
:::

::: {.ex t="Example 6.1: a $2\times2$ from start to finish"}
Find the eigenvalues and eigenvectors of $A=\begin{bmatrix}2&1\\1&2\end{bmatrix}$.

::: sol
$T=4$, $D=3$, so $\lambda^2-4\lambda+3=0\Rightarrow(\lambda-1)(\lambda-3)=0$: **$\lambda=1,\,3$**.

$\lambda=3$: $(A-3I)x=\begin{bmatrix}-1&1\\1&-1\end{bmatrix}x=0\Rightarrow x_1=x_2$. Eigenvector $(1,1)$ (any non-zero multiple).

$\lambda=1$: $\begin{bmatrix}1&1\\1&1\end{bmatrix}x=0\Rightarrow x_1=-x_2$. Eigenvector $(1,-1)$.

Matches the picture above: the diagonal $(1,1)$ is stretched by 3, the anti-diagonal $(1,-1)$ is unchanged.
:::
:::

::: {.ex t="Example 6.2: a $3\times3$ symmetric matrix"}
Find the eigenvalues of $A=\begin{bmatrix}8&-6&2\\-6&7&-4\\2&-4&3\end{bmatrix}$ and one eigenvector.

::: sol
$S_1=8+7+3=18$. $S_2=(56-36)+(24-4)+(21-16)=20+20+5=45$. $\abs{A}=8(21-16)+6(-18+8)+2(24-14)=40-60+20=0$.

Characteristic equation: $\lambda^3-18\lambda^2+45\lambda=0\Rightarrow\lambda(\lambda-3)(\lambda-15)=0$.

**Eigenvalues: $0,\ 3,\ 15$.** (Check: sum $=18=$ trace ✓, product $=0=\abs{A}$ ✓.)

For $\lambda=3$: $(A-3I)x=0$ gives $x=2y,\ z=-2y$, so an eigenvector is $(2,1,-2)$. Similarly $(1,2,2)$ for $\lambda=0$ and $(2,-2,1)$ for $\lambda=15$. These three eigenvectors are mutually perpendicular, as the theory of symmetric matrices predicts.
:::
:::

## 6.2 Properties of eigenvalues

::: {.formula t="The big list (examiners adore these)"}
Let $\lambda_1,\dots,\lambda_n$ be the eigenvalues of an $n\times n$ matrix $A$.

1. **Sum $=$ trace:** $\lambda_1+\cdots+\lambda_n=\operatorname{tr}A$.
2. **Product $=$ determinant:** $\lambda_1\lambda_2\cdots\lambda_n=\abs{A}$.
3. $A$ is **singular** ($\abs A=0$) $\iff$ $0$ is an eigenvalue.
4. $A$ and $A^T$ have the **same** eigenvalues.
5. $kA$ has eigenvalues $k\lambda_i$.
6. $A^m$ has eigenvalues $\lambda_i^{\,m}$.
7. If $A$ is invertible, $A^{-1}$ has eigenvalues $\dfrac1{\lambda_i}$ (same eigenvectors).
8. $A+kI$ has eigenvalues $\lambda_i+k$.
9. For any polynomial $p$, $p(A)$ has eigenvalues $p(\lambda_i)$.
10. For a **triangular or diagonal** matrix the eigenvalues are the **diagonal entries**.
11. Eigenvectors for **distinct** eigenvalues are linearly independent.
12. For a **real symmetric** matrix: all eigenvalues are real, and eigenvectors of different eigenvalues are orthogonal.
:::

::: {.proof t="Why is (7) true?"}
$Ax=\lambda x$. Multiply both sides by $A^{-1}$: $x=\lambda A^{-1}x$, so $A^{-1}x=\frac1\lambda x$. (We need $\lambda\ne0$, guaranteed since $A$ is invertible.)
:::

::: {.ex t="Example 6.3: using the properties"}
A $3\times3$ matrix has eigenvalues $1,2,3$. Find $\abs A$, $\operatorname{tr}A$, and the eigenvalues of $A^{-1}$, $A^2+I$ and $2A$.

::: sol
$\abs A=1\cdot2\cdot3=6$; $\operatorname{tr}A=6$. $A^{-1}$: $1,\tfrac12,\tfrac13$. $A^2+I$: $2,5,10$. $2A$: $2,4,6$.
:::
:::

::: {.try t="Try it"}
If the trace of a $2\times2$ matrix is $5$ and its determinant is $6$, what are its eigenvalues? *Answer: $\lambda^2-5\lambda+6=0$, so $2$ and $3$.*
:::

# The Cayley–Hamilton theorem {.u1 data-eyebrow="Unit I · Chapter 7"}

::: {.idea t="Big idea"}
We know every matrix has a characteristic polynomial $p(\lambda)$. The astonishing theorem says: if you plug the **matrix itself** into its own characteristic polynomial, you get the zero matrix. This lets you compute inverses and high powers of a matrix with nothing but addition and multiplication.
:::

::: {.thm t="Cayley–Hamilton"}
Every square matrix satisfies its own characteristic equation. If $\ \lambda^n+c_{1}\lambda^{n-1}+\cdots+c_n=0\ $ is the characteristic equation of $A$, then
$$A^n+c_1A^{n-1}+\cdots+c_nI=O.$$
(The constant term $c_n$ is multiplied by the **identity matrix** $I$.)
:::

For a $2\times2$ matrix this reads $\boxed{A^2-TA+DI=O}$, with $T=\operatorname{tr}A$ and $D=\abs A$.

::: {.ex t="Example 7.1: verify and find $A^{-1}$"}
For $A=\begin{bmatrix}1&2\\3&4\end{bmatrix}$ ($T=5$, $D=-2$) the characteristic equation is $\lambda^2-5\lambda-2=0$.

::: sol
*Verify:* $A^2=\begin{bmatrix}7&10\\15&22\end{bmatrix}$, $5A=\begin{bmatrix}5&10\\15&20\end{bmatrix}$, so $A^2-5A=\begin{bmatrix}2&0\\0&2\end{bmatrix}=2I$, i.e. $A^2-5A-2I=O$ ✓.

*Inverse:* multiply $A^2-5A-2I=O$ by $A^{-1}$: $A-5I-2A^{-1}=O$, so
$$A^{-1}=\tfrac12(A-5I)=\tfrac12\begin{bmatrix}-4&2\\3&-1\end{bmatrix}=\begin{bmatrix}-2&1\\\frac32&-\frac12\end{bmatrix}.$$
:::
:::

::: {.tip t="The standard exam recipe"}
1. Write $\abs{A-\lambda I}=0$ (use the $S_1,S_2$ shortcut).
2. Replace $\lambda$ by $A$ and the constant by $\times I$.
3. To find $A^{-1}$: multiply by $A^{-1}$ and solve for it. (The constant term must be non-zero, i.e. $\abs A\ne0$.)
4. To find a high power, e.g. $A^4$: reduce it with $A^3=\cdots$ repeatedly.
:::

::: {.ex t="Example 7.2: a $3\times3$ inverse"}
Use Cayley–Hamilton to find $A^{-1}$ for $A=\begin{bmatrix}1&0&2\\0&2&1\\2&0&3\end{bmatrix}$.

::: sol
$S_1=6$; principal minors: $6,\,-1,\,2$ so $S_2=7$; $\abs A=1(6-0)+2(0-4)=-2$. Characteristic equation: $\lambda^3-6\lambda^2+7\lambda+2=0$.

By Cayley–Hamilton $A^3-6A^2+7A+2I=O$. Multiply by $A^{-1}$: $A^2-6A+7I+2A^{-1}=O$, so $A^{-1}=-\tfrac12(A^2-6A+7I)$.

With $A^2=\begin{bmatrix}5&0&8\\2&4&5\\8&0&13\end{bmatrix}$: $\ A^2-6A+7I=\begin{bmatrix}6&0&-4\\2&-1&-1\\-4&0&2\end{bmatrix}$, hence
$$A^{-1}=\begin{bmatrix}-3&0&2\\-1&\frac12&\frac12\\2&0&-1\end{bmatrix}.$$
:::
:::

::: {.ex t="Example 7.3: the MCQ pattern"}
If $A^2-3A+2I=O$, express $A^{-1}$.

::: sol
Multiply by $A^{-1}$: $A-3I+2A^{-1}=O\Rightarrow A^{-1}=\tfrac12(3I-A)$. (This exact question is in your practice set.) Also, the eigenvalues must satisfy $\lambda^2-3\lambda+2=0$, so they can only be $1$ or $2$.
:::
:::

::: {.story t="A theorem with a surprising history"}
Arthur Cayley stated it for small matrices in 1858 and William Rowan Hamilton had met a special case in his work on quaternions a few years earlier. The general proof came later, from Frobenius in 1878.
:::

# Unit I: practice and answers {.u1 data-eyebrow="Unit I · Chapter 8"}

## 8.1 Your professor's practice questions (with reasons)

These are the Unit I questions from the mixed practice set. Cover the answer column and try each first.

| Q | Question (short) | Answer | Why |
|---|---|---|---|
| 2 | Rank of the null matrix $m\times n$ | **(A) 0** | no non-zero row |
| 3 | Two non-zero vectors dependent iff | **(B) one is a scalar multiple of the other** | parallel vectors |
| 5 | Characteristic equation | **(B) $\abs{A-\lambda I}=0$** | from $(A-\lambda I)x=0$ |
| 6 | Cayley–Hamilton: satisfies its own | **(B) characteristic equation** | the theorem |
| 7 | Invertible iff | **(B) non-singular, $\abs A\neq0$** | $A^{-1}=\operatorname{adj}A/\abs A$ |
| 8 | Rank of $I_n$ | **(D) $n$** | $n$ pivots |
| 9 | Set containing the zero vector | **(A) linearly dependent** | $1\cdot0=0$ |
| 10 | Unique solution of $AX=B$ | **(C) rank $A=$ rank$[A\mid B]=n$** | Rouché–Capelli |
| 11 | Sum of eigenvalues | **(B) the trace of $A$** | property 1 |
| 13 | $(AB)^{-1}$ | **(B) $B^{-1}A^{-1}$** | socks and shoes |
| 16 | Infinitely many solutions | **(C) rank $A=$ rank$[A\mid B]<n$** | free parameters |
| 17 | Product of eigenvalues | **(B) the determinant** | property 2 |
| 18 | $2\times2$ with trace $T$, det $D$ | **(B) $\lambda^2-T\lambda+D=0$** | shortcut |
| 19 | $\abs{A^{-1}}$ | **(B) $1/\abs A$** | $\abs{A}\abs{A^{-1}}=1$ |
| 21 | Independent if $\sum c_iv_i=0$ implies | **(C) all $c_i=0$** | definition |
| 22 | No solution if | **(B) rank $A<$ rank$[A\mid B]$** | inconsistent |
| 23 | Eigenvalue of $A^{-1}$ | **(C) $1/\lambda$** | property 7 |
| 24 | $A^2-3A+2I=O$, $A^{-1}=$ | **(A) $\frac12(3I-A)$** | Example 7.3 |

## 8.2 Extra practice

::: {.try t="Questions"}
1. Find the rank of $\begin{bmatrix}1&2&3\\2&4&7\\3&6&10\end{bmatrix}$.
2. Find $A^{-1}$ for $A=\begin{bmatrix}1&2\\3&7\end{bmatrix}$.
3. Solve $x+y+z=3,\ 2x-y+z=2,\ x+2y-z=2$.
4. For what $k$ is $\ x+y+z=1,\ x+2y+4z=k,\ x+4y+10z=k^2\ $ consistent?
5. Eigenvalues and eigenvectors of $\begin{bmatrix}4&1\\2&3\end{bmatrix}$.
6. $A=\begin{bmatrix}1&2\\0&3\end{bmatrix}$. Find the eigenvalues of $A^{-1}$, $A^2+I$ and $2A$.
7. Use Cayley–Hamilton to find $A^{-1}$ for $A=\begin{bmatrix}2&1\\1&1\end{bmatrix}$.
8. Are $(1,2,3),(2,3,4),(3,4,5)$ independent?
9. A $3\times3$ matrix has eigenvalues $1,2,3$. Find the eigenvalues of $A^3$ and $\abs{\operatorname{adj}A}$.
:::

::: {.sol}
**Answers.**
(1) Rank $2$ ($R_2-2R_1=[0,0,1]$, $R_3-3R_1=[0,0,1]$).
(2) $\begin{bmatrix}7&-2\\-3&1\end{bmatrix}$.
(3) $\abs A=7\ne0$; unique solution $(1,1,1)$.
(4) Row reduce: the last row becomes $[0\,0\,0\mid k^2-3k+2]$, so consistent for $k=1$ or $k=2$ (then infinitely many solutions).
(5) $\lambda^2-7\lambda+10=0$: $\lambda=2$ (eigenvector $(1,-2)$), $\lambda=5$ (eigenvector $(1,1)$).
(6) Triangular, so eigenvalues $1,3$. $A^{-1}$: $1,\frac13$. $A^2+I$: $2,10$. $2A$: $2,6$.
(7) $A^2-3A+I=O$, so $A^{-1}=3I-A=\begin{bmatrix}1&-1\\-1&2\end{bmatrix}$.
(8) Dependent: $(3,4,5)=2(2,3,4)-(1,2,3)$.
(9) $A^3$: $1,8,27$. $\abs A=6$, so $\abs{\operatorname{adj}A}=6^{2}=36$.
:::
