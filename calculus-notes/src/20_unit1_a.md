# Matrices: organising numbers {.u1 data-eyebrow="Unit I · Chapter 1"}

::: {.idea t="Big idea"}
A **matrix** is just a rectangular table of numbers, like a spreadsheet. The magic is that we can *add*, *multiply* and *invert* whole tables as if they were single numbers. That lets us solve thousands of equations at once, describe rotations and stretches of space, model electrical networks, and run Google's page ranking.
:::

## 1.1 What is a matrix?

::: {.def t="Matrix, order, entry"}
A **matrix** of **order** $m\times n$ has $m$ rows and $n$ columns. The entry in row $i$, column $j$ is written $a_{ij}$.
$$A=\begin{bmatrix}a_{11}&a_{12}&a_{13}\\a_{21}&a_{22}&a_{23}\end{bmatrix}\quad\text{is a } 2\times3\text{ matrix.}$$
:::

Read "rows first, then columns": a $2\times3$ matrix has 2 rows and 3 columns.

**Types you must be able to name:**

| Name | Description | Example |
|---|---|---|
| Row / column matrix | one row / one column | $[1\ 2\ 3]$ , $\begin{bmatrix}1\\2\end{bmatrix}$ |
| Square matrix | $m=n$ | $\begin{bmatrix}1&2\\3&4\end{bmatrix}$ |
| Diagonal | square, all off-diagonal entries $0$ | $\begin{bmatrix}2&0\\0&5\end{bmatrix}$ |
| Scalar | diagonal with equal diagonal entries | $\begin{bmatrix}3&0\\0&3\end{bmatrix}$ |
| Identity $I_n$ | scalar with $1$'s: acts like the number 1 | $\begin{bmatrix}1&0\\0&1\end{bmatrix}$ |
| Null (zero) matrix $O$ | every entry $0$ | $\begin{bmatrix}0&0\\0&0\end{bmatrix}$ |
| Upper / lower triangular | all entries below / above the diagonal are $0$ | $\begin{bmatrix}1&2\\0&3\end{bmatrix}$ |
| Symmetric | $A^T=A$ (mirror image in the diagonal) | $\begin{bmatrix}1&5\\5&2\end{bmatrix}$ |
| Skew-symmetric | $A^T=-A$ (so the diagonal is all $0$) | $\begin{bmatrix}0&3\\-3&0\end{bmatrix}$ |

The **transpose** $A^T$ swaps rows and columns: $(A^T)_{ij}=A_{ji}$. The **trace** of a square matrix is the sum of its diagonal entries: $\operatorname{tr}A=a_{11}+a_{22}+\cdots+a_{nn}$. Trace will return in the eigenvalue chapter.

## 1.2 Adding and scaling

You may add matrices **only if they have the same order**, entry by entry. Scalar multiplication $kA$ multiplies every entry by $k$.
$$\begin{bmatrix}1&2\\3&4\end{bmatrix}+\begin{bmatrix}0&5\\-1&1\end{bmatrix}=\begin{bmatrix}1&7\\2&5\end{bmatrix},\qquad 3\begin{bmatrix}1&2\\3&4\end{bmatrix}=\begin{bmatrix}3&6\\9&12\end{bmatrix}$$

## 1.3 Multiplying matrices (the one that matters)

::: {.def t="Matrix product"}
$AB$ exists only when **(number of columns of $A$) = (number of rows of $B$)**. If $A$ is $m\times n$ and $B$ is $n\times p$ then $AB$ is $m\times p$, and
$$(AB)_{ij}=a_{i1}b_{1j}+a_{i2}b_{2j}+\cdots+a_{in}b_{nj}\quad\text{(row } i \text{ of } A\ \text{"times" column } j \text{ of } B).$$
:::

::: {.mem t="Dimension check"}
Write the orders side by side: $(m\times n)(n\times p)$. The two **inner** numbers must match; the two **outer** numbers give the answer's order.
:::

::: {.ex t="Example 1.1: product depends on order"}
Let $A=\begin{bmatrix}1&2\\3&4\end{bmatrix}$ and $B=\begin{bmatrix}0&1\\1&0\end{bmatrix}$. Find $AB$ and $BA$.

::: sol
$AB=\begin{bmatrix}1\cdot0+2\cdot1&1\cdot1+2\cdot0\\3\cdot0+4\cdot1&3\cdot1+4\cdot0\end{bmatrix}=\begin{bmatrix}2&1\\4&3\end{bmatrix}$ (columns swapped).

$BA=\begin{bmatrix}0\cdot1+1\cdot3&0\cdot2+1\cdot4\\1\cdot1+0\cdot3&1\cdot2+0\cdot4\end{bmatrix}=\begin{bmatrix}3&4\\1&2\end{bmatrix}$ (rows swapped).

So $AB\neq BA$.
:::
:::

::: {.warn t="Matrices are not numbers"}
- In general $AB\ne BA$ (**not commutative**).
- $AB=O$ does **not** force $A=O$ or $B=O$. Example: $\begin{bmatrix}1&0\\0&0\end{bmatrix}\begin{bmatrix}0&0\\0&1\end{bmatrix}=O$.
- $AB=AC$ does **not** let you cancel $A$.
:::

::: {.formula t="Rules that do hold"}
$$A(BC)=(AB)C,\quad A(B+C)=AB+AC,\quad AI=IA=A$$
$$(A^T)^T=A,\quad (A+B)^T=A^T+B^T,\quad (kA)^T=kA^T,\quad \boxed{(AB)^T=B^TA^T}$$
:::

::: {.tip t="Every square matrix splits in two"}
$A=\underbrace{\tfrac12(A+A^T)}_{\text{symmetric}}+\underbrace{\tfrac12(A-A^T)}_{\text{skew-symmetric}}$. Exams love asking you to write this out.
:::

::: {.try t="Try it"}
If $A$ is $3\times2$ and $B$ is $2\times4$, what is the order of $AB$? Does $BA$ exist? &nbsp; *Answer: $AB$ is $3\times4$; $BA$ would need $4=3$, so it does not exist.*
:::

::: {.story t="Why do engineers care?"}
Rotating a point in the plane by angle $\theta$ is the matrix product $\begin{bmatrix}\cos\theta&-\sin\theta\\\sin\theta&\cos\theta\end{bmatrix}\begin{bmatrix}x\\y\end{bmatrix}$. Doing two rotations is multiplying two matrices. Computer graphics, robotics and signal processing are essentially fast matrix multiplication.
:::

# Determinants and the inverse {.u1 data-eyebrow="Unit I · Chapter 2"}

::: {.idea t="Big idea"}
A square matrix has a single number attached to it, its **determinant**. That number answers the biggest question you can ask: *can this matrix be undone?* If $\abs{A}\ne0$ the matrix is **invertible** and every system $AX=B$ has exactly one solution. If $\abs{A}=0$ the matrix collapses space (a plane squashed to a line) and information is lost for ever.
:::

## 2.1 Computing determinants

**$2\times2$:** $\begin{vmatrix}a&b\\c&d\end{vmatrix}=ad-bc$ (down-right product minus down-left product).

**$3\times3$ by expansion along the first row**, with alternating signs $+\ -\ +$:
$$\begin{vmatrix}a_1&a_2&a_3\\b_1&b_2&b_3\\c_1&c_2&c_3\end{vmatrix}=a_1\begin{vmatrix}b_2&b_3\\c_2&c_3\end{vmatrix}-a_2\begin{vmatrix}b_1&b_3\\c_1&c_3\end{vmatrix}+a_3\begin{vmatrix}b_1&b_2\\c_1&c_2\end{vmatrix}$$
You may expand along **any** row or column; use the one with the most zeros. The sign of position $(i,j)$ is $(-1)^{i+j}$:
$$\begin{bmatrix}+&-&+\\-&+&-\\+&-&+\end{bmatrix}$$

::: {.ex t="Example 2.1"}
Evaluate $\Delta=\begin{vmatrix}1&2&3\\0&4&5\\1&0&6\end{vmatrix}$.

::: sol
Expand along row 1: $\Delta=1(4\cdot6-5\cdot0)-2(0\cdot6-5\cdot1)+3(0\cdot0-4\cdot1)=24+10-12=22.$
:::
:::

::: {.formula t="Properties of determinants (use them to simplify!)"}
1. $\abs{A^T}=\abs{A}$.
2. **Swapping** two rows (or columns) changes the sign of the determinant.
3. If two rows (or columns) are **identical** or proportional, $\abs{A}=0$. A row or column of zeros also gives $0$.
4. Multiplying **one** row by $k$ multiplies $\abs{A}$ by $k$. Hence for an $n\times n$ matrix $\abs{kA}=k^n\abs{A}$.
5. Adding a multiple of one row to another row **does not change** $\abs{A}$ (this is the row-reduction workhorse).
6. $\abs{AB}=\abs{A}\,\abs{B}$.
7. For triangular and diagonal matrices, $\abs{A}$ is the **product of the diagonal entries**.
:::

## 2.2 The inverse matrix

::: {.def t="Inverse"}
$B$ is the **inverse** of $A$ (written $A^{-1}$) if $AB=BA=I$. It exists **iff $\abs{A}\ne0$**; such a matrix is called **non-singular** (invertible). If $\abs{A}=0$ the matrix is **singular**.
:::

**Formula using the adjoint.** The **minor** $M_{ij}$ is the determinant left after deleting row $i$ and column $j$. The **cofactor** is $C_{ij}=(-1)^{i+j}M_{ij}$. The **adjoint** $\operatorname{adj}A$ is the *transpose* of the cofactor matrix. Then
$$A\,(\operatorname{adj}A)=\abs{A}\,I\qquad\Longrightarrow\qquad \boxed{A^{-1}=\frac{1}{\abs{A}}\operatorname{adj}A}$$

For a $2\times2$ matrix this is the pleasant shortcut: swap the diagonal, negate the off-diagonal, divide by the determinant.
$$\begin{bmatrix}a&b\\c&d\end{bmatrix}^{-1}=\frac{1}{ad-bc}\begin{bmatrix}d&-b\\-c&a\end{bmatrix}$$

::: {.ex t="Example 2.2: $2\times2$"}
$A=\begin{bmatrix}2&1\\5&3\end{bmatrix}$, $\abs{A}=6-5=1$, so $A^{-1}=\begin{bmatrix}3&-1\\-5&2\end{bmatrix}$. *Check:* $\begin{bmatrix}2&1\\5&3\end{bmatrix}\begin{bmatrix}3&-1\\-5&2\end{bmatrix}=\begin{bmatrix}6-5&-2+2\\15-15&-5+6\end{bmatrix}=I$ ✓.
:::

::: {.ex t="Example 2.3: $3\times3$ by the adjoint"}
Find $A^{-1}$ for $A=\begin{bmatrix}1&2&3\\0&1&4\\5&6&0\end{bmatrix}$.

::: sol
$\abs{A}=1(0-24)-2(0-20)+3(0-5)=-24+40-15=1$.

Cofactors: $C_{11}=-24,\ C_{12}=20,\ C_{13}=-5;\quad C_{21}=18,\ C_{22}=-15,\ C_{23}=4;\quad C_{31}=5,\ C_{32}=-4,\ C_{33}=1.$

Cofactor matrix $\begin{bmatrix}-24&20&-5\\18&-15&4\\5&-4&1\end{bmatrix}$; transpose it to get the adjoint:
$$A^{-1}=\frac11\begin{bmatrix}-24&18&5\\20&-15&-4\\-5&4&1\end{bmatrix}.$$
:::
:::

::: {.formula t="Inverse rules (these are tested directly in MCQs)"}
$$\boxed{(AB)^{-1}=B^{-1}A^{-1}},\qquad (A^T)^{-1}=(A^{-1})^T,\qquad (A^{-1})^{-1}=A,\qquad \boxed{\abs{A^{-1}}=\frac1{\abs{A}}}$$
$$\abs{\operatorname{adj}A}=\abs{A}^{\,n-1}\ (n\times n),\qquad (kA)^{-1}=\tfrac1kA^{-1}$$
:::

::: {.mem t="Socks and shoes"}
You put on socks, then shoes. To undo it you take off the **shoes first**, then socks. That is why $(AB)^{-1}=B^{-1}A^{-1}$ reverses the order.
:::

# Rank and elementary operations {.u1 data-eyebrow="Unit I · Chapter 3"}

::: {.idea t="Big idea"}
The **rank** of a matrix counts how many rows carry *genuinely new information*. If one row is just a combination of others it is redundant and the rank drops. Rank is the master key to linear systems: it decides whether solutions exist, and how many.
:::

## 3.1 Elementary row operations

There are exactly three, and none of them changes the rank or the solutions of a system:

| Operation | Symbol | Meaning |
|---|---|---|
| Swap | $R_i\leftrightarrow R_j$ | exchange two rows |
| Scale | $R_i\to kR_i\ (k\neq0)$ | multiply a row by a non-zero number |
| Replace | $R_i\to R_i+kR_j$ | add a multiple of one row to another |

::: {.def t="Echelon form"}
A matrix is in **row echelon form** if (i) all zero rows are at the bottom, and (ii) the first non-zero entry (the *pivot*) of each row is strictly to the right of the pivot above it, so the matrix looks like a staircase.
$$\begin{bmatrix}\boxed{2}&1&3&0\\0&\boxed{5}&1&4\\0&0&0&\boxed{7}\\0&0&0&0\end{bmatrix}$$
:::

## 3.2 Rank

::: {.def t="Rank"}
The **rank** $\rho(A)$ is the **number of non-zero rows in an echelon form of $A$**. Equivalently, it is the largest order of a square sub-matrix (minor) with non-zero determinant.
:::

::: {.formula t="Facts to memorise"}
- $\operatorname{rank}(O)=0$ for the **null matrix** of any order $m\times n$.
- $\operatorname{rank}(I_n)=n$.
- $\operatorname{rank}(A)\le\min(m,n)$ for an $m\times n$ matrix.
- $\operatorname{rank}(A)=\operatorname{rank}(A^T)$.
- For a square $n\times n$ matrix: $\operatorname{rank}=n\iff\abs{A}\ne0\iff A$ invertible.
- A non-zero matrix has rank $\ge1$.
:::

::: {.ex t="Example 3.1: reduce to echelon form"}
Find the rank of $A=\begin{bmatrix}1&2&3&4\\2&3&4&5\\3&4&5&6\end{bmatrix}$.

::: sol
$R_2\to R_2-2R_1,\ R_3\to R_3-3R_1$:
$$\begin{bmatrix}1&2&3&4\\0&-1&-2&-3\\0&-2&-4&-6\end{bmatrix}\xrightarrow{R_3\to R_3-2R_2}\begin{bmatrix}1&2&3&4\\0&-1&-2&-3\\0&0&0&0\end{bmatrix}$$
Two non-zero rows, so $\operatorname{rank}A=2$.
:::
:::

::: {.ex t="Example 3.2: rank depending on a parameter"}
Find the rank of $A=\begin{bmatrix}1&1&1\\1&2&3\\1&3&k\end{bmatrix}$ for every $k$.

::: sol
$\abs{A}=1(2k-9)-1(k-3)+1(3-2)=k-5$. So for $k\neq5$, $\abs{A}\ne0$ and **rank $=3$**. For $k=5$, $\abs{A}=0$ but the first two rows are not proportional, so **rank $=2$**.
:::
:::

## 3.3 Finding an inverse by row operations (Gauss–Jordan)

Write $[A\mid I]$ and apply row operations until the left block becomes $I$; the right block is then $A^{-1}$.

::: {.ex t="Example 3.3"}
Invert $A=\begin{bmatrix}2&1\\5&3\end{bmatrix}$ this way.

::: sol
$$\left[\begin{array}{cc|cc}2&1&1&0\\5&3&0&1\end{array}\right]\xrightarrow{R_1\to\frac12R_1}\left[\begin{array}{cc|cc}1&\frac12&\frac12&0\\5&3&0&1\end{array}\right]\xrightarrow{R_2\to R_2-5R_1}\left[\begin{array}{cc|cc}1&\frac12&\frac12&0\\0&\frac12&-\frac52&1\end{array}\right]$$
$$\xrightarrow{R_2\to2R_2}\left[\begin{array}{cc|cc}1&\frac12&\frac12&0\\0&1&-5&2\end{array}\right]\xrightarrow{R_1\to R_1-\frac12R_2}\left[\begin{array}{cc|cc}1&0&3&-1\\0&1&-5&2\end{array}\right]$$
So $A^{-1}=\begin{bmatrix}3&-1\\-5&2\end{bmatrix}$, agreeing with Example 2.2.
:::
:::

::: {.tip t="Which method?"}
For a $2\times2$ use the shortcut. For $3\times3$ the adjoint formula is fine but error-prone; Gauss–Jordan is more reliable and generalises to any size.
:::

# Linear dependence and independence {.u1 data-eyebrow="Unit I · Chapter 4"}

::: {.idea t="Big idea"}
A set of vectors is **linearly dependent** if at least one of them is *redundant*, i.e. can be built from the others. It is **independent** if every vector adds a new direction. In the plane, two vectors pointing along the same line are dependent; two vectors pointing in different directions are independent. Three vectors in the plane are *always* dependent, since there are only two directions to go.
:::

::: {.def t="Linear independence"}
Vectors $v_1,\dots,v_k$ are **linearly independent** if
$$c_1v_1+c_2v_2+\cdots+c_kv_k=0\quad\Longrightarrow\quad c_1=c_2=\cdots=c_k=0.$$
They are **linearly dependent** if the equation has a solution with **at least one $c_i\neq0$**.
:::

::: {.formula t="Quick facts"}
- Any set **containing the zero vector** is dependent (give the zero vector coefficient $1$ and all others $0$).
- **Two non-zero vectors** are dependent iff one is a scalar multiple of the other.
- More than $n$ vectors in $\mathbb{R}^n$ are always dependent.
- A single non-zero vector is independent.
- Any subset of an independent set is independent; any superset of a dependent set is dependent.
:::

**The practical test.** Put the vectors as the rows of a matrix and find its rank.

$$\text{rank}=\text{number of vectors}\ \Rightarrow\ \text{independent};\qquad \text{rank}<\text{number of vectors}\ \Rightarrow\ \text{dependent.}$$

For $n$ vectors in $\mathbb{R}^n$ this simplifies to: **independent $\iff\det\ne0$**.

::: {.ex t="Example 4.1"}
Are $v_1=(1,0,1),\ v_2=(0,1,1),\ v_3=(1,1,2)$ independent?

::: sol
Notice $v_3=v_1+v_2$, i.e. $1\cdot v_1+1\cdot v_2-1\cdot v_3=0$ with non-zero coefficients. **Dependent.** Check: $\begin{vmatrix}1&0&1\\0&1&1\\1&1&2\end{vmatrix}=1(2-1)-0+1(0-1)=0$ ✓.
:::
:::

::: {.ex t="Example 4.2: find the parameter"}
For which $\lambda$ are $(1,2,3),\ (3,-1,2),\ (5,3,\lambda)$ linearly dependent?

::: sol
Dependent $\iff$ determinant $=0$:
$$\begin{vmatrix}1&2&3\\3&-1&2\\5&3&\lambda\end{vmatrix}=1(-\lambda-6)-2(3\lambda-10)+3(9+5)=-7\lambda+56=0\ \Rightarrow\ \lambda=8.$$
:::
:::

::: {.try t="Try it"}
Are $(1,2,-1),(2,-1,3),(0,1,1)$ independent? *Answer: the determinant is $-10\ne0$, so yes.*
:::
