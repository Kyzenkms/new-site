**Units per standard NEP 2020 pattern — verify against class notes, since the official 2026-27 scheme is not published.**

# LAS — Linear Algebra & Statistics: CAE-1 Study Notes

**Subject:** Linear Algebra and Statistics (LAS) | **Sem-I, Cluster K** | **CAE-1 covers Units 1–3**

---

# UNIT 1: MATRICES

## Topics
1. Types of matrices
2. Rank of a matrix
3. Inverse of a matrix (adjoint method)
4. System of linear equations
5. Gauss elimination method
6. Consistency of linear equations
7. Linear dependence and independence of vectors

## 1.1 Types of Matrices

- **Zero (null) matrix:** all entries 0. Denoted O.
- **Row matrix:** single row, e.g. [1 2 3].
- **Column matrix:** single column.
- **Square matrix:** m = n (equal rows and columns).
- **Diagonal matrix:** square matrix with non-zero entries only on the main diagonal. E.g. diag(2, 5, 1).
- **Scalar matrix:** diagonal matrix with all diagonal entries equal: kI.
- **Identity (unit) matrix I:** diagonal entries all 1: **AI = IA = A**.
- **Upper triangular:** zeros below the diagonal. **Lower triangular:** zeros above the diagonal.
- **Symmetric:** Aᵀ = A. **Skew-symmetric:** Aᵀ = −A (diagonal entries are all 0).
- **Orthogonal:** AᵀA = AAᵀ = I, i.e. A⁻¹ = Aᵀ.
- **Idempotent:** A² = A. **Nilpotent:** Aⁿ = O for some n.
- **Singular:** |A| = 0 (non-invertible). **Non-singular:** |A| ≠ 0 (invertible).
- **Transpose Aᵀ:** rows ↔ columns. Rules: (Aᵀ)ᵀ = A, (AB)ᵀ = BᵀAᵀ.
- **Conjugate transpose (Hermitian conjugate):** A* = (Ā)ᵀ.

## 1.2 Rank of a Matrix

The **rank ρ(A)** = the order of the largest non-zero minor of A. Equivalently, the number of non-zero rows in the row-echelon form of A.

**Method (echelon form):** Apply row operations (R₁↔R₂, Rᵢ → kRᵢ, Rᵢ → Rᵢ + kRⱼ) to reduce A to row-echelon form (zeros below each leading entry). Count non-zero rows = rank.

**Example 1:** Find rank of A = [[1, 2, 3], [2, 4, 6], [1, 1, 1]].

R₂ → R₂ − 2R₁ gives [[1,2,3],[0,0,0],[1,1,1]]; then R₃ → R₃ − R₁ gives [[1,2,3],[0,0,0],[0,−1,−2]]. Swap R₂, R₃: [[1,2,3],[0,−1,−2],[0,0,0]]. Two non-zero rows ⇒ **ρ(A) = 2**.

**Example 2:** Find rank of B = [[2, 1, 3], [4, 2, 6], [1, 0, 1]].

R₂ → R₂ − 2R₁ gives [[2,1,3],[0,0,0],[1,0,1]]; R₃ → 2R₃ − R₁ gives [[2,1,3],[0,0,0],[0,−1,−1]]. Swap: [[2,1,3],[0,−1,−1],[0,0,0]] ⇒ **ρ(B) = 2**.

## 1.3 Inverse of a Matrix (Adjoint Method)

For a square matrix A with |A| ≠ 0:

**A⁻¹ = (1/|A|) · adj(A)**, where **adj(A) = (cofactor matrix)ᵀ**.

Steps: (1) compute |A|; (2) find cofactor matrix C (cofactor of each element, with sign (−1)^(i+j)); (3) transpose C to get adj(A); (4) divide by |A|.

**Example:** Find inverse of A = [[1, 2], [3, 4]].

|A| = 1(4) − 2(3) = −2. Cofactors: C₁₁ = 4, C₁₂ = −3, C₂₁ = −2, C₂₂ = 1. adj(A) = [[4, −2], [−3, 1]]. A⁻¹ = (1/−2)[[4,−2],[−3,1]] = [[−2, 1], [3/2, −1/2]]. Check: AA⁻¹ = I ✓.

(2×2 shortcut: for [[a,b],[c,d]], A⁻¹ = 1/(ad−bc) · [[d,−b],[−c,a]].)

## 1.4–1.6 System of Linear Equations, Gauss Elimination, Consistency

A system AX = B, with A an n×n coefficient matrix, X unknowns, B constants.

**Augmented matrix** [A | B] = 
```
[a₁₁ a₁₂ … a₁ₙ | b₁]
[ ⋮              ⋮ ]
```

**Gauss elimination:** Apply row operations to [A|B] to get upper-triangular (echelon) form, then **back-substitute** from the last equation upward.

**Consistency theorem:** Let A be the coefficient matrix, C = [A|B] the augmented matrix.
- If **ρ(A) = ρ(C) = n** (number of unknowns) → **unique solution**.
- If **ρ(A) = ρ(C) = r < n** → **infinitely many solutions** (n − r free variables).
- If **ρ(A) ≠ ρ(C)** (ρ(C) > ρ(A)) → **no solution** (inconsistent).

**Example 1:** Solve x + 2y + z = 6; 2x + 3y + 3z = 14; x + 3y + 2z = 8 by Gauss elimination.

Augmented: [[1,2,1|6],[2,3,3|14],[1,3,2|8]].
R₂ → R₂ − 2R₁: [0,−1,1|2]. R₃ → R₃ − R₁: [0,1,1|2].
R₃ → R₃ + R₂: [0,0,2|4].
Back-substitution: 2z = 4 ⇒ z = 2; −y + z = 2 ⇒ y = 0; x + 2y + z = 6 ⇒ x = 4. **Solution: x = 4, y = 0, z = 2.**

**Example 2 (consistency):** Test consistency of x + y + z = 6; 2x + y + 2z = 10; 3x + 2y + 3z = 14.

[A|B] = [[1,1,1|6],[2,1,2|10],[3,2,3|14]]. R₂ → R₂ − 2R₁: [0,−1,0|−2]; R₃ → R₃ − 3R₁: [0,−1,0|−4]. R₃ → R₃ − R₂: [0,0,0|−2].
Row 3 reads 0 = −2, a contradiction ⇒ ρ(A) = 2, ρ(C) = 3 ⇒ **no solution (inconsistent)**.

## 1.7 Linear Dependence and Independence of Vectors

Vectors v₁, v₂, …, vₙ are **linearly independent** if c₁v₁ + c₂v₂ + … + cₙvₙ = 0 implies all cᵢ = 0. Otherwise **linearly dependent**.

**Matrix test:** Form a matrix with the vectors as columns (or rows). If ρ = number of vectors → independent; if ρ < number of vectors → dependent.

**Example:** Check if (1,2,3), (2,4,6), (1,1,1) are independent.

Matrix [[1,2,1],[2,4,1],[3,6,1]]. Column 2 = 2 × column 1, so rank ≤ 2 < 3 ⇒ **linearly dependent**. (Also: (2,4,6) = 2·(1,2,3), so one vector is a combination of another.)

**Quick facts:** Any set of more than n vectors in ℝⁿ is dependent. The zero vector alone or in any set makes the set dependent.

## Likely CAE-1 Questions — Unit 1

1. **Define rank of a matrix and find the rank of A = [[2,3,−1],[−1,−2,−3],[1,4,7]].**
   *Model answer:* Rank = order of largest non-zero minor / non-zero rows in echelon form. Reduce: R₂ → R₂ + (1/2)R₁ … working through gives echelon with 3 non-zero rows (verify: the determinant = 2(−14+12) − 3(−7+3) − 1(−4+2) = −4+12+2 = 10 ≠ 0), so **ρ = 3** (full rank).

2. **Find the inverse of [[2,1,1],[1,2,1],[1,1,2]] by the adjoint method.**
   *Outline:* |A| = 2(4−1) − 1(2−1) + 1(1−2) = 6 − 1 − 1 = 4. Compute the 9 cofactors, transpose, divide by 4. Answer: A⁻¹ = (1/4)[[3,−1,−1],[−1,3,−1],[−1,−1,3]].

3. **Solve by Gauss elimination: x + y + z = 6, x + 2y + 3z = 14, 2x + 3y + z = 11.**
   *Outline:* Augment, eliminate to upper triangular, back-substitute ⇒ x = 1, y = 2, z = 3.

4. **Test for consistency: x + 2y + 3z = 1, 2x + 4y + 6z = 2, x + y + z = 3.**
   *Model answer:* Rows 1 and 2 are proportional (R₂ = 2R₁) ⇒ ρ(A) = 2, ρ(C) = 3? Check: R₂ − 2R₁ = [0,0,0 | 0] (consistent there), then with R₃ present ρ(A) = ρ(C) = 2 < 3 unknowns ⇒ **consistent with infinitely many solutions** (one free variable).

5. **State and explain the conditions for consistency of AX = B using ranks.**
   *Model answer:* Unique solution iff ρ(A) = ρ([A|B]) = n; infinite solutions iff ρ(A) = ρ([A|B]) < n; no solution iff ρ(A) < ρ([A|B]).

6. **Check whether the vectors (1,0,0), (0,1,0), (0,0,1), (1,1,1) are linearly independent.**
   *Model answer:* 4 vectors in ℝ³ ⇒ **dependent** (more vectors than dimension). Alternatively matrix rank ≤ 3 < 4.

7. **If A is a 3×3 matrix with |A| = 5, find |adj(A)|.**
   *Model answer:* Use **|adj(A)| = |A|ⁿ⁻¹**. Here n = 3 ⇒ |adj A| = 5² = **25**.

8. **Show that the inverse of a symmetric non-singular matrix is symmetric.**
   *Outline:* Given Aᵀ = A, need (A⁻¹)ᵀ = A⁻¹. (A⁻¹)ᵀ = (Aᵀ)⁻¹ = A⁻¹ ✓ (using (A⁻¹)ᵀ = (Aᵀ)⁻¹).

---

# UNIT 2: EIGEN VALUES AND EIGEN VECTORS

## Topics
1. Characteristic equation
2. Eigen values and their properties
3. Eigen vectors
4. Cayley–Hamilton theorem (statement and verification)
5. Reduction to diagonal form

## 2.1 Characteristic Equation

For a square matrix A, the **characteristic equation** is

**|A − λI| = 0**

where λ is a scalar. Expanding gives a polynomial of degree n (the **characteristic polynomial**). Its roots λ₁, λ₂, …, λₙ are the **eigen values** of A.

**Example:** Characteristic equation of A = [[4, 1], [2, 3]].

|A − λI| = |4−λ, 1; 2, 3−λ| = (4−λ)(3−λ) − 2 = λ² − 7λ + 10 = 0 ⇒ λ = 5, 2.

## 2.2 Eigen Values and Their Properties

Key properties (memorize these — favourite short questions):
1. λ = 0 is an eigen value **iff A is singular** (|A| = 0).
2. **Sum of eigen values = trace(A)** (sum of diagonal entries).
3. **Product of eigen values = det(A)**.
4. If λ is an eigen value of A, then: A⁻¹ has eigen value **1/λ**; Aᵏ has **λᵏ**; Aᵀ has the **same** eigen values; kA has **kλ**.
5. Eigen values of a **triangular matrix** (upper or lower) are simply its **diagonal entries**.
6. Eigen values of a **real symmetric** matrix are **real**.
7. Eigen values of an **orthogonal** matrix have modulus 1 (|λ| = 1).

**Example:** Eigen values of [[2, 0, 0], [1, 3, 0], [4, 5, 1]] are 2, 3, 1 (diagonal, since lower triangular). Check: trace = 6 = 2+3+1 ✓; det = 2·3·1 = 6 ✓.

## 2.3 Eigen Vectors

For each eigen value λ, the **eigen vector** X (≠ 0) satisfies

**(A − λI)X = 0**

Solve this homogeneous system for x, y, z (one variable will be free — pick a convenient value, e.g. 1).

**Example:** Find eigen values and eigen vectors of A = [[4, 1], [2, 3]].

Eigen values: λ = 5, 2 (from above).
- λ = 5: (A − 5I)X = 0 ⇒ [[−1, 1], [2, −2]][x; y] = 0 ⇒ −x + y = 0 ⇒ y = x. Take x = 1: eigen vector **(1, 1)**.
- λ = 2: [[2, 1], [2, 1]][x; y] = 0 ⇒ 2x + y = 0 ⇒ y = −2x. Take x = 1: eigen vector **(1, −2)**.

**Example (3×3):** A = [[2, 0, 1], [0, 2, 0], [1, 0, 2]].

|A − λI| = (2−λ)[(2−λ)² − 1] = (2−λ)(λ² − 4λ + 3) = (2−λ)(λ−1)(λ−3). Eigen values: **λ = 1, 2, 3**.
- λ = 1: [[1,0,1],[0,1,0],[1,0,1]] ⇒ x + z = 0, y = 0 ⇒ take z = 1: **(1, 0, −1)**… wait, x = −z ⇒ take x = 1, z = −1: eigen vector **(1, 0, −1)**.
- λ = 2: [[0,0,1],[0,0,0],[1,0,0]] ⇒ z = 0, x = 0, y free ⇒ **(0, 1, 0)**.
- λ = 3: [[−1,0,1],[0,−1,0],[1,0,−1]] ⇒ x = z, y = 0 ⇒ take x = 1: **(1, 0, 1)**.

## 2.4 Cayley–Hamilton Theorem

**Statement:** Every square matrix satisfies its own characteristic equation.

If the characteristic equation is λⁿ + a₁λⁿ⁻¹ + … + aₙ = 0, then Aⁿ + a₁Aⁿ⁻¹ + … + aₙI = O.

**Use:** Express Aⁿ (or higher powers) in terms of lower powers, and find A⁻¹ = −(1/aₙ)(Aⁿ⁻¹ + a₁Aⁿ⁻² + … + aₙ₋₁I).

**Example (verification):** Verify Cayley–Hamilton for A = [[1, 2], [3, 4]].

Characteristic: |A − λI| = (1−λ)(4−λ) − 6 = λ² − 5λ − 2 = 0.
Compute A² = [[1,2],[3,4]]·[[1,2],[3,4]] = [[7,10],[15,22]].
A² − 5A − 2I = [[7,10],[15,22]] − [[5,10],[15,20]] − [[2,0],[0,2]] = [[0,0],[0,0]] = O ✓ **Verified.**

Bonus: A⁻¹ from C–H: A² − 5A − 2I = O ⇒ A(A − 5I) = 2I ⇒ A⁻¹ = (1/2)(A − 5I) = (1/2)[[−4,2],[3,−1]] = [[−2,1],[3/2,−1/2]] ✓ (matches Unit 1 example).

## 2.5 Reduction to Diagonal Form (Diagonalization)

A matrix A is **diagonalizable** if there exists non-singular P such that **P⁻¹AP = D**, a diagonal matrix whose diagonal entries are the eigen values of A. P is the **modal matrix**: its columns are the eigen vectors of A (in the same order as the eigen values in D).

Sufficient condition: if A has **n distinct eigen values** (n×n), it is diagonalizable. Symmetric matrices are always diagonalizable.

**Example:** Diagonalize A = [[4, 1], [2, 3]].

Eigen values 5, 2 with eigen vectors (1,1), (1,−2) (from §2.3). P = [[1, 1], [1, −2]], D = diag(5, 2). Then P⁻¹AP = D. (Exam usually asks only for P and D.)

**Application:** Aⁿ = PDⁿP⁻¹ — diagonal matrices are trivial to raise to powers.

## Likely CAE-1 Questions — Unit 2

1. **Find the eigen values and eigen vectors of [[5, 4], [1, 2]].**
   *Model answer:* |A − λI| = λ² − 7λ + 6 = 0 ⇒ λ = 6, 1. λ = 6: −x + 4y = 0 ⇒ **(4, 1)**. λ = 1: 4x + 4y = 0 ⇒ **(1, −1)**.

2. **State the Cayley–Hamilton theorem and verify it for A = [[2, 1], [1, 2]].**
   *Outline:* Char. eq: λ² − 4λ + 3 = 0. A² = [[5,4],[4,5]]; A² − 4A + 3I = [[5,4],[4,5]] − [[8,4],[4,8]] + [[3,0],[0,3]] = O ✓.

3. **If 2 and 3 are eigen values of a 2×2 matrix A, find |A| and trace(A).**
   *Model answer:* trace = sum = **5**; det = product = **6**.

4. **Show that λ = 0 is an eigen value of A iff A is singular.**
   *Outline:* λ = 0 is an eigen value ⇔ |A − 0·I| = 0 ⇔ |A| = 0 ⇔ A singular ✓.

5. **Diagonalize the matrix [[1, 2], [2, 1]].**
   *Outline:* Eigen values: λ² − 2λ − 3 = 0 ⇒ λ = 3, −1. Eigen vectors: λ = 3 ⇒ (1, 1); λ = −1 ⇒ (1, −1). P = [[1,1],[1,−1]], D = diag(3, −1), and P⁻¹AP = D.

6. **Find the eigen values of A³ if the eigen values of A are 1, 2, 3.**
   *Model answer:* If λ is an eigen value of A, λ³ is an eigen value of A³ ⇒ **1, 8, 27**.

7. **Write the characteristic equation of [[3, 1, 0], [0, 3, 2], [0, 0, 5]].**
   *Model answer:* Upper triangular ⇒ eigen values 3, 3, 5; characteristic equation: **(λ − 3)²(λ − 5) = 0**, i.e. λ³ − 11λ² + 39λ − 45 = 0.

---

# UNIT 3: STATISTICS

## Topics
1. Measures of central tendency: mean, median, mode
2. Measures of dispersion: range, variance, standard deviation
3. Correlation (Karl Pearson coefficient)
4. Regression lines
5. Introduction to probability: addition and multiplication theorems, conditional probability, Bayes' theorem

## 3.1 Measures of Central Tendency

For data x₁, x₂, …, xₙ:

- **Mean (arithmetic mean):** **x̄ = (Σxᵢ)/n**. For grouped data: x̄ = Σfᵢxᵢ / Σfᵢ.
- **Median:** middle value of **sorted** data. If n odd: value at position (n+1)/2. If n even: average of values at positions n/2 and n/2 + 1.
- **Mode:** the most frequently occurring value.

**Empirical relation (moderately skewed distribution):** **Mode = 3·Median − 2·Mean**.

**Example:** Data: 4, 8, 6, 5, 8, 3, 8.
Mean = (4+8+6+5+8+3+8)/7 = 42/7 = 6. Sorted: 3, 4, 5, 6, 8, 8, 8 ⇒ median = 5th… 4th value = **6**. Mode = **8** (occurs 3 times). Check relation: 3(6) − 2(6) = 6 ≈ mode 8 (rough — relation is approximate).

## 3.2 Measures of Dispersion

- **Range** = maximum − minimum.
- **Variance:** **σ² = Σ(xᵢ − x̄)²/n = (Σxᵢ²)/n − x̄²** (population). Sample variance uses n−1.
- **Standard deviation:** **σ = √variance**.
- **Mean deviation** about mean = Σ|xᵢ − x̄|/n (less common in exams).

**Example:** Find SD of 2, 4, 6, 8, 10.
x̄ = 30/5 = 6. Σ(xᵢ − x̄)² = 16 + 4 + 0 + 4 + 16 = 40. σ² = 40/5 = 8 ⇒ **σ = √8 = 2√2 ≈ 2.83**. Range = 10 − 2 = 8.

**Example (grouped):** Marks: x: 10, 20, 30, 40 with f: 2, 3, 4, 1. Σf = 10, Σfx = 20+60+120+40 = 240 ⇒ x̄ = 24. Σfx² = 200+1200+3600+1600 = 6600. σ² = 6600/10 − 24² = 660 − 576 = 84 ⇒ σ ≈ 9.17.

## 3.3 Correlation — Karl Pearson Coefficient

Measures **linear** relationship between two variables x and y:

**r = Σ(xᵢ − x̄)(yᵢ − ȳ) / √[Σ(xᵢ − x̄)² · Σ(yᵢ − ȳ)²]**

Computational form: **r = [nΣxy − ΣxΣy] / √[(nΣx² − (Σx)²)(nΣy² − (Σy)²)]**

- **−1 ≤ r ≤ 1**. r = +1: perfect positive linear; r = −1: perfect negative linear; r = 0: no linear correlation.
- r > 0: y tends to increase with x; r < 0: y decreases as x increases.

**Example:** x: 1, 2, 3, 4, 5; y: 2, 4, 5, 4, 6. n = 5.
Σx = 15, Σy = 21, Σxy = 2+8+15+16+30 = 71, Σx² = 55, Σy² = 4+16+25+16+36 = 97.
Numerator: 5(71) − 15(21) = 355 − 315 = 40. Denominator: √[(5·55 − 225)(5·97 − 441)] = √[(275−225)(485−441)] = √[50·44] = √2200 ≈ 46.9. **r ≈ 0.85** → strong positive correlation.

## 3.4 Regression Lines

Two lines of regression:
- **y on x:** **y − ȳ = b_yx (x − x̄)**, where **b_yx = r·(σ_y/σ_x)** (regression coefficient of y on x).
- **x on y:** **x − x̄ = b_xy (y − ȳ)**, where **b_xy = r·(σ_x/σ_y)**.

Key results: **r² = b_yx · b_xy** ⇒ **r = ±√(b_yx·b_xy)** (sign = sign of the coefficients). Both regression lines pass through **(x̄, ȳ)**.

**Example:** Given x̄ = 20, ȳ = 30, σ_x = 4, σ_y = 5, r = 0.8. Find both regression lines.
b_yx = 0.8·(5/4) = 1.0 ⇒ y − 30 = 1.0(x − 20) ⇒ **y = x + 10**.
b_xy = 0.8·(4/5) = 0.64 ⇒ x − 20 = 0.64(y − 30) ⇒ **x = 0.64y + 0.8**.

**Example:** If b_yx = 1.2 and b_xy = 0.3, find r. r = √(1.2·0.3) = √0.36 = 0.6; both coefficients positive ⇒ **r = +0.6**.

## 3.5 Introduction to Probability

- **Sample space S:** set of all possible outcomes. **Event:** subset of S.
- **Classical probability:** **P(A) = (favourable outcomes)/(total outcomes)**.
- Axioms: 0 ≤ P(A) ≤ 1; P(S) = 1.

**Addition theorem:** **P(A ∪ B) = P(A) + P(B) − P(A ∩ B)**. If A, B mutually exclusive: **P(A ∪ B) = P(A) + P(B)**.

**Multiplication theorem:** **P(A ∩ B) = P(A)·P(B|A)**. If A, B independent: **P(A ∩ B) = P(A)·P(B)**.

**Conditional probability:** **P(A|B) = P(A ∩ B)/P(B)**, P(B) ≠ 0.

**Bayes' theorem:** If E₁, E₂, …, Eₙ form a partition of S and A is any event with P(A) > 0:

**P(Eᵢ|A) = P(Eᵢ)·P(A|Eᵢ) / Σⱼ P(Eⱼ)·P(A|Eⱼ)**

(Total probability: P(A) = Σ P(Eⱼ)·P(A|Eⱼ) — the denominator.)

**Example 1 (addition):** A card is drawn from a deck. P(king or queen) = 4/52 + 4/52 = **8/52 = 2/13** (mutually exclusive).

**Example 2 (Bayes):** Two bags: Bag I has 3 red, 2 black balls; Bag II has 2 red, 3 black. A bag is chosen at random and a red ball is drawn. What is the probability it came from Bag I?

P(B₁) = P(B₂) = 1/2. P(R|B₁) = 3/5, P(R|B₂) = 2/5.
P(B₁|R) = (1/2)(3/5) / [(1/2)(3/5) + (1/2)(2/5)] = (3/10)/(5/10) = **3/5**.

**Example 3 (conditional):** Two dice thrown. Given the sum is 8, find P(first die shows 3).
Outcomes with sum 8: (2,6),(3,5),(4,4),(5,3),(6,2) → 5 outcomes. Favourable: (3,5) → 1. **P = 1/5**.

## Likely CAE-1 Questions — Unit 3

1. **Define mean, median and mode. Find them for: 7, 3, 9, 7, 5, 7, 2.**
   *Model answer:* Mean = 40/7 ≈ 5.71; sorted 2,3,5,7,7,7,9 ⇒ median = 7; mode = 7 (most frequent).

2. **Calculate the standard deviation of: 5, 10, 15, 20, 25.**
   *Model answer:* x̄ = 15; Σ(xᵢ−x̄)² = 100+25+0+25+100 = 250; σ² = 250/5 = 50 ⇒ **σ = 5√2 ≈ 7.07**.

3. **Compute Karl Pearson's coefficient of correlation for x: 2,4,6,8,10 and y: 3,5,7,9,11.**
   *Model answer:* y = x + 1 exactly ⇒ **r = +1** (perfect positive linear correlation). Show via formula: numerator = denominator.

4. **Given b_yx = 0.8, b_xy = 0.45, x̄ = 10, ȳ = 25, write both regression lines.**
   *Model answer:* r = √(0.8·0.45) = 0.6. y on x: y − 25 = 0.8(x − 10) ⇒ **y = 0.8x + 17**. x on y: x − 10 = 0.45(y − 25) ⇒ **x = 0.45y − 1.25**.

5. **State and prove the addition theorem of probability. / A die is thrown; find P(even or multiple of 3).**
   *Model answer:* P(A ∪ B) = P(A) + P(B) − P(A ∩ B). P(even) = 3/6, P(multiple of 3) = 2/6, P(both) = P(6) = 1/6 ⇒ P = 3/6 + 2/6 − 1/6 = **4/6 = 2/3**.

6. **Define conditional probability. Two coins are tossed; given at least one head, find P(both heads).**
   *Model answer:* P(A|B) = P(A ∩ B)/P(B). Sample space given ≥1 head: {HH, HT, TH} → 3 outcomes; favourable HH → 1 ⇒ **P = 1/3**.

7. **State Bayes' theorem and solve: A factory has machines A and B producing 60% and 40% of items, with defect rates 2% and 3%. An item is defective — find P(it came from machine A).**
   *Model answer:* P(A|D) = (0.6·0.02)/[(0.6·0.02)+(0.4·0.03)] = 0.012/0.024 = **0.5**.

8. **Distinguish between correlation and regression.**
   *Model answer:* Correlation (r, −1 ≤ r ≤ 1) measures strength/direction of linear association, symmetric in x,y. Regression gives the actual predictive line (y on x or x on y), asymmetric, with slope b = r·σ_y/σ_x; r² = b_yx·b_xy.

---

# QUICK-REVISION CHECKLIST — FORMULAS TO MEMORIZE

## Unit 1 — Matrices
- **(AB)ᵀ = BᵀAᵀ**; (Aᵀ)ᵀ = A
- **A⁻¹ = (1/|A|) · adj(A)**; 2×2: 1/(ad−bc)·[[d,−b],[−c,a]]
- **|adj(A)| = |A|ⁿ⁻¹** (n×n); |AB| = |A||B|; |Aᵀ| = |A|
- Rank ρ = non-zero rows in echelon form
- Consistency of AX = B: ρ(A) = ρ([A|B]) = n → unique; ρ(A) = ρ([A|B]) < n → infinite; ρ(A) < ρ([A|B]) → no solution
- Gauss elimination: row-reduce [A|B] → upper triangular → back-substitute
- Vectors independent iff ρ = number of vectors

## Unit 2 — Eigen values/vectors
- Characteristic equation: **|A − λI| = 0**
- Eigen vector: **(A − λI)X = 0**, X ≠ 0
- **Σλᵢ = trace(A)**; **Πλᵢ = |A|**
- λ = 0 eigen value ⇔ A singular
- Eigen values of: A⁻¹ → 1/λ; Aᵏ → λᵏ; kA → kλ; Aᵀ → same λ; triangular matrix → diagonal entries
- **Cayley–Hamilton:** A satisfies its own characteristic equation (use for Aⁿ, A⁻¹)
- Diagonalization: **P⁻¹AP = D**, columns of P = eigen vectors, D = diag(eigen values)

## Unit 3 — Statistics
- **x̄ = Σx/n**; median = middle of sorted data; mode = most frequent; **Mode = 3·Median − 2·Mean**
- **σ² = Σ(x− x̄)²/n = Σx²/n − x̄²**; σ = √σ²; range = max − min
- **r = [nΣxy − ΣxΣy] / √[(nΣx² − (Σx)²)(nΣy² − (Σy)²)]**, −1 ≤ r ≤ 1
- Regression y on x: **y − ȳ = b_yx(x − x̄), b_yx = rσ_y/σ_x**; x on y: **x − x̄ = b_xy(y − ȳ), b_xy = rσ_x/σ_y**
- **r² = b_yx·b_xy**; both lines pass through (x̄, ȳ)
- **P(A ∪ B) = P(A) + P(B) − P(A ∩ B)**; independent: P(A ∩ B) = P(A)P(B)
- **P(A|B) = P(A ∩ B)/P(B)**
- **Bayes: P(Eᵢ|A) = P(Eᵢ)P(A|Eᵢ) / ΣⱼP(Eⱼ)P(A|Eⱼ)**
