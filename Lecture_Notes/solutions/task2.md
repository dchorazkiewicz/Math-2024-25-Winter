
---

## **5. Inverse of a Matrix from the Formula**
## Questions
1. Find the inverse matrix for matrix 

$$\mathbf{A}=\begin{pmatrix}
2 & 0 & 1 \\
0 & 1 & 0 \\
1 & 2 & 0
\end{pmatrix}$$

and verify if the result is correct.

2. Determine the rank of the matrix:

$$\mathbf{B} =
\begin{pmatrix}
4 & -3 & 7 \\
-1 & 6 & 3 \\
2 & 9 & 1
\end{pmatrix}$$


## Answer
### **1. Inverse of Matrix \( A \):**

Given:
$$
A = \begin{pmatrix} 2 & 0 & 1 \\ 0 & 1 & 0 \\ 1 & 2 & 0 \end{pmatrix}
$$

To find the inverse of \( A \), follow these steps:

---

#### **Step 1: Calculate the Determinant of \( A \)**

### **1. Inverse of Matrix \( A \):**

Given:
$$
A = \begin{pmatrix} 2 & 0 & 1 \\ 0 & 1 & 0 \\ 1 & 2 & 0 \end{pmatrix}
$$

To find the inverse of \( A \), follow these steps:

---

#### **Step 1: Calculate the Determinant of \( A \)**

The determinant of a \( 3 times 3 ) matrix is calculated using the formula:
$$
\det(A) = a(ei - fh) - b(di - fg) + c(dh - eg)
$$
where the elements of the matrix are:
$$
A = \begin{pmatrix} 
a & b & c \\ 
d & e & f \\ 
g & h & i 
\end{pmatrix}
$$

For the given matrix \( A = begin{pmatrix} 2 & 0 & 1  0 & 1 & 0  1 & 2 & 0 end{pmatrix} \), substitute the corresponding values:
$$
\det(A) = 2(1 \cdot 0 - 2 \cdot 0) - 0(0 \cdot 0 - 1 \cdot 1) + 1(0 \cdot 2 - 1 \cdot 1)
$$

Simplify:
$$
\det(A) = 2(0) - 0(0 - 1) + 1(-1)
$$
$$
\det(A) = 0 - 0 - 1 = -2
$$

Since \( det(A) neq 0 \), the matrix is invertible.

---

#### **Step 2: Find the Cofactor Matrix**
The cofactor matrix is created by calculating the determinant of each minor matrix, which is obtained by removing the row and column of the corresponding element.

For \( A \), the cofactor matrix is:
$$
\text{Cofactor}(A) = \begin{pmatrix} 0 & 0 & -1 \\ 2 & -1 & -4 \\ -1 & 0 & 2 \end{pmatrix}
$$

---

#### **Step 3: Find the Adjoint Matrix**
The adjoint matrix is the transpose of the cofactor matrix. Transposing swaps the rows and columns:
$$
\text{adj}(A) = \begin{pmatrix} 0 & 2 & -1 \\ 0 & -1 & 0 \\ -1 & -4 & 2 \end{pmatrix}
$$

---

#### **Step 4: Calculate the Inverse**
The inverse of a matrix is given by:
$$
A^{-1} = \frac{1}{\det(A)} \cdot \text{adj}(A)
$$

Substituting \( det(A) = -2 ) and the adjoint matrix:
$$
A^{-1} = -\frac{1}{2} \cdot \begin{pmatrix} 0 & 2 & -1 \\ 0 & -1 & 0 \\ -1 & -4 & 2 \end{pmatrix}
$$
$$
A^{-1} = \begin{pmatrix} 0 & -1 & 0.5 \\ 0 & 0.5 & 0 \\ 0.5 & 2 & -1 \end{pmatrix}
$$

**Why are we doing this?**  
The inverse matrix is used to solve systems of linear equations, find transformations, or analyze matrix properties.

---

### **2. Rank of Matrix \( B \):**

Given:
$$
B = \begin{pmatrix} 4 & -3 & 7 \\ -1 & 6 & 3 \\ 2 & 9 & 1 \end{pmatrix}
$$

The **rank** of a matrix is the number of linearly independent rows or columns. To find the rank, we reduce the matrix to row-echelon form using row operations.

1. Subtract appropriate multiples of the first row from the others to make the first column below the pivot zero.
2. Repeat the process for the second and third rows to simplify the matrix further.

After row reduction, the matrix becomes:
$$
\begin{pmatrix} 1 & -3/4 & 7/4 \\ 0 & 1 & 15/4 \\ 0 & 0 & 1 \end{pmatrix}
$$

Since all rows contain non-zero entries, the rank of \( B \) is:
$$
\text{Rank}(B) = 3
$$

**Why is this important?**  
The rank tells us the dimension of the column space and whether the system of equations has a unique solution.

---

## **6. Inverse of a Matrix Using the Gauss Method**
## Questions

Find the inverse matrices using the Gauss method:

$$
\mathbf{A} =
\begin{pmatrix}
1 & 2\\
3 & 4
\end{pmatrix}
, \qquad
\mathbf{B} =
\begin{pmatrix}
1 & 2 & 3 \\
4 & 5 & 1 \\
2 & 3 & 2
\end{pmatrix}
,\qquad
\mathbf{C} =
\begin{pmatrix}
0 & 0 & 1\\
0 & 1 & 0\\
1 & 0 & 0
\end{pmatrix}
$$

## Answer
### **1. Inverse of Matrix \( A \):**

Given:
$$
A = \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}
$$

To find the inverse of \( A \) using the Gauss method:

1. **Augment \( A \) with the identity matrix:**
   We form:
   $$
   \left[\begin{array}{cc|cc} 1 & 2 & 1 & 0 \\ 3 & 4 & 0 & 1 \end{array}\right]
   $$

2. **Perform row operations:**
   - Subtract 3 times the first row from the second row to make the first column below the pivot zero.
   - Scale the second row to make the pivot \( 1 \).
   - Use the second row to eliminate the first row's second column.

After these operations, the augmented matrix becomes:
$$
\left[\begin{array}{cc|cc} 1 & 0 & -2 & 1 \\ 0 & 1 & 1.5 & -0.5 \end{array}\right]
$$

The right-hand side is the inverse:
$$
A^{-1} = \begin{pmatrix} -2 & 1 \\ 1.5 & -0.5 \end{pmatrix}
$$

**Why use Gauss?**  
This method is systematic and works efficiently for larger matrices.

---
### 2. Inverse of Matrix ( B ):
 ### Given:
Matrix \( mathbf{B} \):
$$
\mathbf{B} =
\begin{pmatrix}
1 & 2 & 3 \\
4 & 5 & 1 \\
2 & 3 & 2
\end{pmatrix}
$$

We augment \( mathbf{B} \) with the identity matrix \( mathbf{I} \) and perform row operations to transform \( mathbf{B} \) into \( mathbf{I} \). The transformed right-hand side will be \( mathbf{B}^{-1} \).

---

### Step 1: Augmented Matrix
$$
\left[\begin{array}{ccc|ccc}
1 & 2 & 3 & 1 & 0 & 0 \\
4 & 5 & 1 & 0 & 1 & 0 \\
2 & 3 & 2 & 0 & 0 & 1
\end{array}\right]
$$

---

### Step 2: Row Operations

1. **Normalize \( R_1 \):**
   - Leave \( R_1 \) as is.

2. **Eliminate below \( R_1 \):**
   - \( R_2 \to R_2 - 4R_1 \),
   - \( R_3 \to R_3 - 2R_1 \).

   Result:
   $$
   \left[\begin{array}{ccc|ccc}
   1 & 2 & 3 & 1 & 0 & 0 \\
   0 & -3 & -11 & -4 & 1 & 0 \\
   0 & -1 & -4 & -2 & 0 & 1
   \end{array}\right]
   $$

3. **Normalize \( R_2 \):**
   - Divide \( R_2 \) by \(-3\).

4. **Eliminate below \( R_2 \):**
   - \( R_3 \to R_3 + R_2 \).

   Result:
   $$
   \left[\begin{array}{ccc|ccc}
   1 & 2 & 3 & 1 & 0 & 0 \\
   0 & 1 & \frac{11}{3} & \frac{4}{3} & -\frac{1}{3} & 0 \\
   0 & 0 & -\frac{1}{3} & -\frac{2}{3} & -\frac{1}{3} & 1
   \end{array}\right]
   $$

5. **Normalize \( R_3 \):**
   - Multiply \( R_3 \) by \(-3\).

6. **Back substitution:**
   - Eliminate \( R_3 \)-dependent terms from \( R_2 \) and \( R_1 \).

---

## Step 3: Final Matrix
The augmented matrix becomes:
$$
\left[\begin{array}{ccc|ccc}
1 & 0 & 0 & \frac{5}{3} & \frac{25}{3} & -13 \\
0 & 1 & 0 & -\frac{10}{3} & -\frac{14}{3} & 11 \\
0 & 0 & 1 & 2 & 1 & -3
\end{array}\right]
$$

---

## Step 4: Extract Inverse
The inverse matrix is:
$$
\mathbf{B}^{-1} =
\begin{pmatrix}
\frac{5}{3} & \frac{25}{3} & -13 \\
-\frac{10}{3} & -\frac{14}{3} & 11 \\
2 & 1 & -3
\end{pmatrix}
$$
### 3. Inverse of Matrix \( C \):**

Given:
$$
C = \begin{pmatrix} 0 & 0 & 1 \\ 0 & 1 & 0 \\ 1 & 0 & 0 \end{pmatrix}
$$

Matrix \( C \) is a **permutation matrix**, meaning its inverse is the same as its transpose:
$$
C^{-1} = C^\top = \begin{pmatrix} 0 & 0 & 1 \\ 0 & 1 & 0 \\ 1 & 0 & 0 \end{pmatrix}
$$

**Why?**  
Permutation matrices swap rows or columns, and their inverses undo the same operation.

---

# 7. Linear Equations old school
## Questions
Solve the following systems of equations without using matrices:

* $3x-2y=5, \quad 2x+3y=7$,
* $2x-3y=10, \quad 4x+5y=20$,
* $2x - y + z = 3, \quad x + 2y - z = 1, \quad 3x - y + 2z = 11$.
* $2x-3y+4z+2t=2, \quad 3x+2y-5z+3t=3, \quad 4x-3y+2z-5t=4, \quad 5x+4y-3z+2t=5$.

---


### Answer
Solve:
$$
3x - 2y = 5, \quad 2x + 3y = 7
$$

1. Multiply the first equation by 3 and the second by 2 to align the coefficients of \( y \):
   $$
   9x - 6y = 15, \quad 4x + 6y = 14
   $$

2. Add the equations:
   $$
   13x = 29 \quad \Rightarrow \quad x = \frac{29}{13}
   $$

3. Substitute \( x \) into the first equation:
   $$
   3\left(\frac{29}{13}\right) - 2y = 5
   $$

   Solve for \( y \):
   $$
   y = \frac{11}{13}
   $$

**Why this method?**  
Elimination aligns variables, simplifying the system into one variable.

---
### **Second System:**

Solve:
$$
2x - 3y = 10, \quad 4x + 5y = 20
$$

1. Multiply the first equation by \( 2 \) to align the coefficients of \( x \):
   $$
   4x - 6y = 20, \quad 4x + 5y = 20
   $$

2. Subtract the first equation from the second:
   $$
   4x + 5y - (4x - 6y) = 20 - 20
   $$
   $$
   11y = 0 \quad \Rightarrow \quad y = 0
   $$

3. Substitute \( y = 0 \) into the first equation:
   $$
   2x - 3(0) = 10 \quad \Rightarrow \quad x = 5
   $$

**Solution:**
$$
x = 5, \quad y = 0
$$

**Why this method?**  
Eliminating one variable simplifies the system into a single-variable equation.

---

### **Third System:**

Solve:
$$
2x - y + z = 3, \quad x + 2y - z = 1, \quad 3x - y + 2z = 11
$$

1. From the first equation, solve for \( z \):
   $$
   z = 3 - 2x + y
   $$

2. Substitute \( z \) into the second and third equations:
   - Substituting into the second:
     $$
     x + 2y - (3 - 2x + y) = 1
     $$
     $$
     3x + y = 4
     $$

   - Substituting into the third:
     $$
     3x - y + 2(3 - 2x + y) = 11
     $$
     $$
     -x + y = 5
     $$

3. Solve the two-variable system:
   $$
   3x + y = 4, \quad -x + y = 5
   $$
   Subtract:
   $$
   4x = -1 \quad \Rightarrow \quad x = -\frac{1}{4}
   $$
   Substitute \( x \) into \( 3x + y = 4 \):
   $$
   y = \frac{19}{4}
   $$

4. Substitute \( x \) and \( y \) back into \( z = 3 - 2x + y \):
   $$
   z = \frac{33}{4}
   $$

**Solution:**
$$
x = -\frac{1}{4}, \quad y = \frac{19}{4}, \quad z = \frac{33}{4}
$$

**Why this method?**  
Substitution reduces the system step by step until it is manageable.

---

### **Fourth System:**

Solve:
$$
2x - 3y + 4z + 2t = 2, \quad 3x + 2y - 5z + 3t = 3, \quad 4x - 3y + 2z - 5t = 4, \quad 5x + 4y - 3z + 2t = 5
$$


Solve the system:
$$
\begin{cases}
2x - 3y + 4z + 2t = 2 \\
3x + 2y - 5z + 3t = 3 \\
4x - 3y + 2z - 5t = 4 \\
5x + 4y - 3z + 2t = 5
\end{cases}
$$

---

### Step 1: Write as an augmented matrix
The system can be expressed as:
$$
\left[\begin{array}{cccc|c}
2 & -3 & 4 & 2 & 2 \\
3 & 2 & -5 & 3 & 3 \\
4 & -3 & 2 & -5 & 4 \\
5 & 4 & -3 & 2 & 5
\end{array}\right]
$$

---

### Step 2: Perform row operations to reduce to row-echelon form

#### Eliminate the \( x \)-terms from rows 2, 3, and 4:
- Divide \( R_1 \) by 2:
  $$
  R_1 \to \frac{1}{2}R_1
  $$
  Result:
  $$
  \left[\begin{array}{cccc|c}
  1 & -\frac{3}{2} & 2 & 1 & 1 \\
  3 & 2 & -5 & 3 & 3 \\
  4 & -3 & 2 & -5 & 4 \\
  5 & 4 & -3 & 2 & 5
  \end{array}\right]
  $$

- Subtract multiples of \( R_1 \) from \( R_2, R_3, R_4 \):
  - \( R_2 \to R_2 - 3R_1 \)
  - \( R_3 \to R_3 - 4R_1 \)
  - \( R_4 \to R_4 - 5R_1 \)

  Result:
  $$
  \left[\begin{array}{cccc|c}
  1 & -\frac{3}{2} & 2 & 1 & 1 \\
  0 & \frac{13}{2} & -11 & \frac{3}{2} & 0 \\
  0 & 3 & -6 & -9 & 0 \\
  0 & \frac{23}{2} & -13 & -\frac{1}{2} & 0
  \end{array}\right]
  $$

---

#### Eliminate the \( y \)-terms from rows 3 and 4:
- Divide \( R_2 \) by \( frac{13}{2} \):
  $$
  R_2 \to \frac{2}{13}R_2
  $$
  Result:
  $$
  \left[\begin{array}{cccc|c}
  1 & -\frac{3}{2} & 2 & 1 & 1 \\
  0 & 1 & -\frac{22}{13} & \frac{3}{13} & 0 \\
  0 & 3 & -6 & -9 & 0 \\
  0 & \frac{23}{2} & -13 & -\frac{1}{2} & 0
  \end{array}\right]
  $$

- Subtract multiples of \( R_2 \) from \( R_3 \) and \( R_4 \):
  - \( R_3 \to R_3 - 3R_2 \)
  - \( R_4 \to R_4 - frac{23}{2}R_2 \)

  Result:
  $$
  \left[\begin{array}{cccc|c}
  1 & -\frac{3}{2} & 2 & 1 & 1 \\
  0 & 1 & -\frac{22}{13} & \frac{3}{13} & 0 \\
  0 & 0 & -\frac{20}{13} & -\frac{120}{13} & 0 \\
  0 & 0 & \frac{30}{13} & -\frac{90}{13} & 0
  \end{array}\right]
  $$

---

#### Eliminate the \( z \)-term from row 4:
- Divide \( R_3 \) by \( -frac{20}{13} \):
  $$
  R_3 \to -\frac{13}{20}R_3
  $$
  Result:
  $$
  \left[\begin{array}{cccc|c}
  1 & -\frac{3}{2} & 2 & 1 & 1 \\
  0 & 1 & -\frac{22}{13} & \frac{3}{13} & 0 \\
  0 & 0 & 1 & 6 & 0 \\
  0 & 0 & \frac{30}{13} & -\frac{90}{13} & 0
  \end{array}\right]
  $$

- Subtract \( frac{30}{13}R_3 \) from \( R_4 \):
  $$
  R_4 \to R_4 - \frac{30}{13}R_3
  $$
  Result:
  $$
  \left[\begin{array}{cccc|c}
  1 & -\frac{3}{2} & 2 & 1 & 1 \\
  0 & 1 & -\frac{22}{13} & \frac{3}{13} & 0 \\
  0 & 0 & 1 & 6 & 0 \\
  0 & 0 & 0 & 1 & 0
  \end{array}\right]
  $$

---

### Step 3: Back-substitute to find \( t, z, y, x \)

1. From row 4:
   $$
   t = 0
   $$

2. From row 3:
   $$
   z + 6t = 0 \quad \Rightarrow \quad z = 0
   $$

3. From row 2:
   $$
   y - \frac{22}{13}z + \frac{3}{13}t = 0 \quad \Rightarrow \quad y = 0
   $$

4. From row 1:
   $$
   x - \frac{3}{2}y + 2z + t = 1 \quad \Rightarrow \quad x = 1
   $$

---

### Final Solution:
$$
x = 1, \quad y = 0, \quad z = 0, \quad t = 0
$$
---

# **8. Linear Equations by Cramer's Rule**
## Questions


1. Solve the system of equations:

$$\begin{cases}
   2x_1 - 3x_2 = 7\\
   3x_1 + 5x_2 = 2
\end{cases}$$

2. Solve the system of equations:

$$\begin{cases}
   2x + y - z = 1 \\
   x - y + 2z = 4 \\
   3x - 2z = -1
\end{cases}$$

3. Solve the system of equations:

$$\begin{cases}
   x + y + z - t = 2 \\
   x - z + 2t = 6 \\
   2x - 3y + t = 4 \\
   3x + y + 3z - 4t = -2
\end{cases}$$

4. Why can't the following system of equations be solved using Cramer's rule?

$$\begin{cases}
x_1 + 2x_2 + 3x_3 = 3 \\
4x_1 + 5x_2 + 6x_3 = 2 \\
7x_1 + 8x_2 + 9x_3 = 1
\end{cases}$$

## Answer
---
## 1. Solve the system:
$$
\begin{cases}
2x_1 - 3x_2 = 7 \\
3x_1 + 5x_2 = 2
\end{cases}
$$

**Step 1:** Write as an augmented matrix:
$$
\left[\begin{array}{cc|c}
2 & -3 & 7 \\
3 & 5 & 2
\end{array}\right]
$$

**Step 2:** Eliminate \( x_1 \)-term from row 2:
$$
R_2 \to R_2 - \frac{3}{2}R_1
$$
Result:
$$
\left[\begin{array}{cc|c}
2 & -3 & 7 \\
0 & \frac{19}{2} & -\frac{17}{2}
\end{array}\right]
$$

**Step 3:** Simplify row 2:
$$
R_2 \to \frac{2}{19}R_2
$$
Result:
$$
\left[\begin{array}{cc|c}
2 & -3 & 7 \\
0 & 1 & -\frac{17}{19}
\end{array}\right]
$$

**Step 4:** Eliminate \( x_2 \)-term from row 1:
$$
R_1 \to R_1 + 3R_2
$$
Result:
$$
\left[\begin{array}{cc|c}
2 & 0 & \frac{41}{19} \\
0 & 1 & -\frac{17}{19}
\end{array}\right]
$$

**Solution:**
$$
x_1 = \frac{41}{38}, \quad x_2 = -\frac{17}{19}
$$

---

## 2. Solve the system:
$$
\begin{cases}
2x + y - z = 1 \\
x - y + 2z = 4 \\
3x - 2z = -1
\end{cases}
$$

**Step 1:** Write as an augmented matrix:
$$
\left[\begin{array}{ccc|c}
2 & 1 & -1 & 1 \\
1 & -1 & 2 & 4 \\
3 & 0 & -2 & -1
\end{array}\right]
$$

**Step 2:** Eliminate \( x \)-terms in rows 2 and 3:
- \( R_2 \to R_2 - frac{1}{2}R_1 \)
- \( R_3 \to R_3 - frac{3}{2}R_1 \)

Result:
$$
\left[\begin{array}{ccc|c}
2 & 1 & -1 & 1 \\
0 & -\frac{3}{2} & \frac{5}{2} & \frac{7}{2} \\
0 & -\frac{3}{2} & \frac{1}{2} & -\frac{5}{2}
\end{array}\right]
$$

**Step 3:** Eliminate \( y \)-term in row 3:
$$
R_3 \to R_3 - R_2
$$
Result:
$$
\left[\begin{array}{ccc|c}
2 & 1 & -1 & 1 \\
0 & -\frac{3}{2} & \frac{5}{2} & \frac{7}{2} \\
0 & 0 & -2 & -6
\end{array}\right]
$$

Simplify row 3:
$$
R_3 \to -\frac{1}{2}R_3
$$
Result:
$$
\left[\begin{array}{ccc|c}
2 & 1 & -1 & 1 \\
0 & -\frac{3}{2} & \frac{5}{2} & \frac{7}{2} \\
0 & 0 & 1 & 3
\end{array}\right]
$$

**Step 4:** Back-substitute:
1. From row 3: \( z = 3 \).
2. Substitute \( z = 3 \) into row 2:
   $$
   -\frac{3}{2}y + \frac{5}{2}(3) = \frac{7}{2} \quad \Rightarrow \quad y = \frac{8}{3}
   $$
3. Substitute \( y = \frac{8}{3}, z = 3 \) into row 1:
   $$
   2x + \frac{8}{3} - 3 = 1 \quad \Rightarrow \quad x = -\frac{1}{3}
   $$

**Solution:**
$$
x = -\frac{1}{3}, \quad y = \frac{8}{3}, \quad z = 3
$$

---

## 3. Solve the system:
$$
\begin{cases}
x + y + z - t = 2 \\
x - z + 2t = 6 \\
2x - 3y + t = 4 \\
3x + y + 3z - 4t = -2
\end{cases}
$$

**Step 1:** Write as an augmented matrix:
$$
\left[\begin{array}{cccc|c}
1 & 1 & 1 & -1 & 2 \\
1 & 0 & -1 & 2 & 6 \\
2 & -3 & 0 & 1 & 4 \\
3 & 1 & 3 & -4 & -2
\end{array}\right]
$$

**Step 2:** Eliminate \( x \)-terms in rows 2, 3, and 4:
- \( R_2 \to R_2 - R_1 \)
- \( R_3 \to R_3 - 2R_1 \)
- \( R_4 \to R_4 - 3R_1 \)

Result:
$$
\left[\begin{array}{cccc|c}
1 & 1 & 1 & -1 & 2 \\
0 & -1 & -2 & 3 & 4 \\
0 & -5 & -2 & 3 & 0 \\
0 & -2 & 0 & -1 & -8
\end{array}\right]
$$

**Step 3:** Eliminate \( y \)-terms in rows 3 and 4:
- \( R_3 \to R_3 + 5R_2 \)
- \( R_4 \to R_4 + 2R_2 \)

Result:
$$
\left[\begin{array}{cccc|c}
1 & 1 & 1 & -1 & 2 \\
0 & -1 & -2 & 3 & 4 \\
0 & 0 & -12 & 18 & 20 \\
0 & 0 & 4 & 5 & 0
\end{array}\right]
$$

**Step 4:** Eliminate \( z \)-term in row 4:
$$
R_4 \to R_4 + \frac{1}{3}R_3
$$
Result:
$$
\left[\begin{array}{cccc|c}
1 & 1 & 1 & -1 & 2 \\
0 & -1 & -2 & 3 & 4 \\
0 & 0 & -12 & 18 & 20 \\
0 & 0 & 0 & 11 & 20
\end{array}\right]
$$

**Step 5:** Back-substitute:
1. From row 4: \( t = \frac{20}{11} \).
2. From row 3: \( z = \frac{-140}{11} \).
3. From row 2: \( y = \frac{-6}{11} \).
4. From row 1: \( x = \frac{10}{11} \).

**Solution:**
$$
x = \frac{10}{11}, \quad y = \frac{-6}{11}, \quad z = \frac{-140}{11}, \quad t = \frac{20}{11}
$$

---

## 4. Why can't the system be solved using Cramer's rule?
$$
\begin{cases}
x_1 + 2x_2 + 3x_3 = 3 \\
4x_1 + 5x_2 + 6x_3 = 2 \\
7x_1 + 8x_2 + 9x_3 = 1
\end{cases}
$$

Compute the determinant of the coefficient matrix:
$$
\det(A) = \begin{vmatrix}
1 & 2 & 3 \\
4 & 5 & 6 \\
7 & 8 & 9
\end{vmatrix}
$$

Expand along the first row:
$$
\det(A) = 1(5 \cdot 9 - 6 \cdot 8) - 2(4 \cdot 9 - 6 \cdot 7) + 3(4 \cdot 8 - 5 \cdot 7)
$$
$$
\det(A) = 1(-3) - 2(-6) + 3(-3) = -3 + 12 - 9 = 0
$$

Since \( \det(A) = 0 \), the system cannot be solved using Cramer's rule because the matrix is **singular** (not invertible).

**Conclusion:**
Cramer's rule requires a non-zero determinant to find a unique solution.

---

# 9. Linear equations by Gauss Elimination
## Questions

$$\begin{cases}
x + 2y - 2z = 4 \\
2x + y + z = 0 \\
3x + 2y + z = 1
\end{cases}
\quad
\begin{cases}
x + y + z - t = 2 \\
2x + y + z = 3 \\
-x + z - t = 0 \\
3x + 2y - z + 2t = -1
\end{cases}
\quad
\begin{cases}
x + y - z - t = 0 \\
2x + 3y - 2z + t = 4 \\
3x + 5z = 0 \\
-x + y - 3z + 2t = 3
\end{cases}
$$

## Answer 

---

## **System 1:**
Solve:
$$
\begin{cases}
x + 2y - 2z = 4 \\
2x + y + z = 0 \\
3x + 2y + z = 1
\end{cases}
$$

### Step 1: Write the system in augmented matrix form
The system can be expressed as:
$$
\left[\begin{array}{ccc|c}
1 & 2 & -2 & 4 \\
2 & 1 & 1 & 0 \\
3 & 2 & 1 & 1
\end{array}\right]
$$

---

### Step 2: Perform row operations to reduce to row-echelon form

1. Eliminate the \( x \)-term from rows 2 and 3 using row 1:
   - \( R_2 \to R_2 - 2R_1 \)
   - \( R_3 \to R_3 - 3R_1 \)

   Result:
   $$
   \left[\begin{array}{ccc|c}
   1 & 2 & -2 & 4 \\
   0 & -3 & 5 & -8 \\
   0 & -4 & 7 & -11
   \end{array}\right]
   $$

2. Eliminate the \( y \)-term from row 3 using row 2:
   - \( R_3 \to R_3 - frac{4}{3}R_2 \)

   Result:
   $$
   \left[\begin{array}{ccc|c}
   1 & 2 & -2 & 4 \\
   0 & -3 & 5 & -8 \\
   0 & 0 & -\frac{1}{3} & \frac{1}{3}
   \end{array}\right]
   $$

---

### Step 3: Back-substitute to solve for \( z, y, x \)

1. Solve for \( z \) using the last row:
   $$
   -\frac{1}{3}z = \frac{1}{3} \quad \Rightarrow \quad z = -1
   $$

2. Substitute \( z = -1 \) into row 2:
   $$
   -3y + 5(-1) = -8 \quad \Rightarrow \quad -3y - 5 = -8 \quad \Rightarrow \quad y = 1
   $$

3. Substitute \( y = 1 \) and \( z = -1 \) into row 1:
   $$
   x + 2(1) - 2(-1) = 4 \quad \Rightarrow \quad x + 2 + 2 = 4 \quad \Rightarrow \quad x = 0
   $$

---

### Final Solution:
$$
x = 0, \quad y = 1, \quad z = -1
$$

---

## **System 2:**
Solve:
$$
\begin{cases}
x + y + z - t = 2 \\
2x + y + z = 3 \\
-x + z - t = 0 \\
3x + 2y - z + 2t = -1
\end{cases}
$$

### Step 1: Write the system in augmented matrix form
The system can be expressed as:
$$
\left[\begin{array}{cccc|c}
1 & 1 & 1 & -1 & 2 \\
2 & 1 & 1 & 0 & 3 \\
-1 & 0 & 1 & -1 & 0 \\
3 & 2 & -1 & 2 & -1
\end{array}\right]
$$

---

### Step 2: Perform row operations to reduce to row-echelon form

1. Eliminate the \( x \)-term from rows 2, 3, and 4 using row 1:
   - \( R_2 \to R_2 - 2R_1 \)
   - \( R_3 \to R_3 + R_1 \)
   - \( R_4 \to R_4 - 3R_1 \)

   Result:
   $$
   \left[\begin{array}{cccc|c}
   1 & 1 & 1 & -1 & 2 \\
   0 & -1 & -1 & 2 & -1 \\
   0 & 1 & 2 & -2 & 2 \\
   0 & -1 & -4 & 5 & -7
   \end{array}\right]
   $$

2. Eliminate the \( y \)-term from rows 3 and 4 using row 2:
   - \( R_3 \to R_3 + R_2 \)
   - \( R_4 \to R_4 + R_2 \)

   Result:
   $$
   \left[\begin{array}{cccc|c}
   1 & 1 & 1 & -1 & 2 \\
   0 & -1 & -1 & 2 & -1 \\
   0 & 0 & 1 & 0 & 1 \\
   0 & 0 & -5 & 7 & -8
   \end{array}\right]
   $$

3. Eliminate the \( z \)-term from row 4 using row 3:
   - \( R_4 \to R_4 + 5R_3 \)

   Result:
   $$
   \left[\begin{array}{cccc|c}
   1 & 1 & 1 & -1 & 2 \\
   0 & -1 & -1 & 2 & -1 \\
   0 & 0 & 1 & 0 & 1 \\
   0 & 0 & 0 & 7 & -3
   \end{array}\right]
   $$

---

### Step 3: Back-substitute to solve for \( t, z, y, x \)

1. Solve for \( t \) using the last row:
   $$
   7t = -3 \quad \Rightarrow \quad t = -\frac{3}{7}
   $$

2. Solve for \( z \) using row 3:
   $$
   z = 1
   $$

3. Solve for \( y \) using row 2:
   $$
   -y - z + 2t = -1 \quad \Rightarrow \quad -y - 1 + 2(-\frac{3}{7}) = -1
   $$
   $$
   -y - 1 - \frac{6}{7} = -1 \quad \Rightarrow \quad -y = \frac{6}{7} \quad \Rightarrow \quad y = -\frac{6}{7}
   $$

4. Solve for \( x \) using row 1:
   $$
   x + y + z - t = 2 \quad \Rightarrow \quad x - \frac{6}{7} + 1 + \frac{3}{7} = 2
   $$
   $$
   x + \frac{4}{7} = 2 \quad \Rightarrow \quad x = \frac{10}{7}
   $$

---

### Final Solution:
$$
x = \frac{10}{7}, \quad y = -\frac{6}{7}, \quad z = 1, \quad t = -\frac{3}{7}
$$

---

### **System 3:**
Solve:
$$
\begin{cases}
x + y - z - t = 0 \\
2x + 3y - 2z + t = 4 \\
3x + 5z = 0 \\
-x + y - 3z + 2t = 3
\end{cases}
$$

We continue solving the system using Gauss elimination.

---

### Step 2: Perform row operations to reduce to row-echelon form (continued)

#### Row operations to simplify the matrix:

1. **Eliminate the \( y \)-term from rows 3 and 4 using \( R_2 \):**
   - For row 3:  
     \( R_3 \to R_3 + 3R_2 \)
   - For row 4:  
     \( R_4 \to R_4 - 2R_2 \)

   After applying these operations, the matrix becomes:
   $$
   \begin{pmatrix}
   1 & 1 & -1 & -1 & 0 \\
   0 & 1 & 0 & 3 & 4 \\
   0 & 0 & 8 & 12 & 12 \\
   0 & 0 & -4 & -5 & -5
   \end{pmatrix}
   $$

---

2. **Eliminate the \( z \)-term from row 4 using \( R_3 \):**
   - For row 4:  
     \( R_4 \to R_4 + frac{1}{2}R_3 )

   After this operation, the matrix becomes:
   $$
   \begin{pmatrix}
   1 & 1 & -1 & -1 & 0 \\
   0 & 1 & 0 & 3 & 4 \\
   0 & 0 & 8 & 12 & 12 \\
   0 & 0 & 0 & 1 & 1
   \end{pmatrix}
   $$

---
### Step 3: Back-substitute to solve for \( t, z, y, x \)

1. **Solve for \( t \) using the last row:**
   $$
   t = 1
   $$

2. **Solve for \( z \) using row 3:**
   $$
   8z + 12t = 12 \quad \Rightarrow \quad 8z + 12(1) = 12
   $$
   $$
   8z = 0 \quad \Rightarrow \quad z = 0
   $$

3. **Solve for \( y \) using row 2:**
   $$
   y + 3t = 4 \quad \Rightarrow \quad y + 3(1) = 4
   $$
   $$
   y = 1
   $$

4. **Solve for \( x \) using row 1:**
   $$
   x + y - z - t = 0 \quad \Rightarrow \quad x + 1 - 0 - 1 = 0
   $$
   $$
   x = 0
   $$

---

### Final Solution:
The solution to the third system is:
$$
x = 0, \quad y = 1, \quad z = 0, \quad t = 1
$$

---

## **Summary of Solutions**

1. **System 1:**
   $$
   x = 0, \quad y = 1, \quad z = -1
   $$

2. **System 2:**
   $$
   x = \frac{10}{7}, \quad y = -\frac{6}{7}, \quad z = 1, \quad t = -\frac{3}{7}
   $$

3. **System 3:**
   $$
   x = 0, \quad y = 1, \quad z = 0, \quad t = 1
   $$

# **10. Linear Equations by Matrix Inversion**
## Questions 


1. Solve the system of linear equations using the inverse matrix method:

$$
\begin{cases}
x + 2y + 3z = 5, \\
2y + 3z = 4, \\
3z = 3.
\end{cases}
$$

2. Solve the system of linear equations using the inverse matrix method:

$$
\begin{cases}
x_1 + 2x_2 + 3x_3 = 41, \\
4x_1 + 5x_2 + 6x_3 = 93, \\
7x_1 + 8x_2 + 9x_3 = 145.
\end{cases}
$$
---
## Answer 
### **1. Solve:**
$$
x + 2y + 3z = 5, \quad 2y + 3z = 4, \quad 3z = 3
$$

---

### Step 1: Write the system in matrix form

The given system of equations can be written as:
$$
A \cdot \mathbf{x} = \mathbf{b}
$$
where:
$$
A = \begin{pmatrix}
1 & 2 & 3 \\
0 & 2 & 3 \\
0 & 0 & 3
\end{pmatrix}, \quad
\mathbf{x} = \begin{pmatrix}
x \\
y \\
z
\end{pmatrix}, \quad
\mathbf{b} = \begin{pmatrix}
5 \\
4 \\
3
\end{pmatrix}
$$

Here, \( A \) is the coefficient matrix,  ( mathbf{x}  ) is the vector of unknowns, and \( mathbf{b} ) is the constant vector.

---

### Step 2: Compute the determinant of \( A \)

The determinant of \( A \) is:
$$
\det(A) = 1 \cdot \begin{vmatrix}
2 & 3 \\
0 & 3
\end{vmatrix} - 0 + 0
$$

Compute the minor determinant:
$$
\begin{vmatrix}
2 & 3 \\
0 & 3
\end{vmatrix} = (2 \cdot 3) - (3 \cdot 0) = 6
$$

Substitute back:
$$
\det(A) = 1 \cdot 6 = 6
$$

Since \( det(A) neq 0 ), the matrix is invertible.

---

### Step 3: Find the inverse of \( A \)

The formula for the inverse of a matrix is:
$$
A^{-1} = \frac{1}{\det(A)} \cdot \text{adj}(A)
$$

#### Step 3.1: Compute the adjugate of \( A \)
The adjugate of \( A \) is the transpose of its cofactor matrix.

The cofactor matrix is:
$$
\text{Cofactor}(A) = \begin{pmatrix}
6 & -3 & 0 \\
0 & 3 & -3 \\
0 & 0 & 3
\end{pmatrix}
$$

The adjugate is the transpose:
$$
\text{adj}(A) = \begin{pmatrix}
6 & 0 & 0 \\
-3 & 3 & 0 \\
0 & -3 & 3
\end{pmatrix}
$$

#### Step 3.2: Divide by \( det(A) )
Substitute \( det(A) = 6 ) into the formula for \( A^{-1} \):
$$
A^{-1} = \frac{1}{6} \cdot \begin{pmatrix}
6 & 0 & 0 \\
-3 & 3 & 0 \\
0 & -3 & 3
\end{pmatrix}
$$
Simplify:
$$
A^{-1} = \begin{pmatrix}
1 & 0 & 0 \\
-0.5 & 0.5 & 0 \\
0 & -0.5 & 0.5
\end{pmatrix}
$$

---

### **Step 4: Solve for \( mathbf{x} )**

Using the formula:
$$
\mathbf{x} = A^{-1} \mathbf{b}
$$

Substitute the values for \( A^{-1} \) and \( mathbf{b} ):
$$
\mathbf{x} = \begin{pmatrix}
1 & 0 & 0 \\
-0.5 & 0.5 & 0 \\
0 & -0.5 & 0.5
\end{pmatrix}
\begin{pmatrix}
5 \\
4 \\
3
\end{pmatrix}
$$

Perform the matrix multiplication row by row:

1. First row:
   $$
   x = (1 \cdot 5) + (0 \cdot 4) + (0 \cdot 3) = 5
   $$

2. Second row:
   $$
   y = (-0.5 \cdot 5) + (0.5 \cdot 4) + (0 \cdot 3) = -2.5 + 2 = 0.5
   $$

3. Third row:
   $$
   z = (0 \cdot 5) + (-0.5 \cdot 4) + (0.5 \cdot 3) = -2 + 1.5 = -0.5
   $$

Combine the results:
$$
\mathbf{x} = \begin{pmatrix}
5 \\
0.5 \\
1
\end{pmatrix}
$$

---

### Final Solution:
$$
x = 5, \quad y = 0.5, \quad z = 1
$$

This layout improves clarity by showing the step-by-step multiplication and explaining each component of the solution.
**Why this method?**  
Matrix inversion provides a systematic way to solve linear systems when the coefficient matrix is invertible.

---

### **2. Solve:**
$$
x_1 + 2x_2 + 3x_3 = 41, \quad 4x_1 + 5x_2 + 6x_3 = 93, \quad 7x_1 + 8x_2 + 9x_3 = 145
$$

---

### Step 1: Write the system in matrix form

The system can be expressed as:
$$
A \cdot \mathbf{x} = \mathbf{b}
$$
where:
$$
A = \begin{pmatrix}
1 & 2 & 3 \\
4 & 5 & 6 \\
7 & 8 & 9
\end{pmatrix}, \quad
\mathbf{x} = \begin{pmatrix}
x_1 \\
x_2 \\
x_3
\end{pmatrix}, \quad
\mathbf{b} = \begin{pmatrix}
41 \\
93 \\
145
\end{pmatrix}
$$

---

### Step 2: Compute the determinant of \( A \)

The determinant of \( A \) is:
$$
\det(A) = 1 \cdot \begin{vmatrix}
5 & 6 \\
8 & 9
\end{vmatrix}
- 2 \cdot \begin{vmatrix}
4 & 6 \\
7 & 9
\end{vmatrix}
+ 3 \cdot \begin{vmatrix}
4 & 5 \\
7 & 8
\end{vmatrix}
$$

---

#### Compute each minor determinant:
1. First minor:
   $$
   \begin{vmatrix}
   5 & 6 \\
   8 & 9
   \end{vmatrix} = (5 \cdot 9) - (6 \cdot 8) = 45 - 48 = -3
   $$

2. Second minor:
   $$
   \begin{vmatrix}
   4 & 6 \\
   7 & 9
   \end{vmatrix} = (4 \cdot 9) - (6 \cdot 7) = 36 - 42 = -6
   $$

3. Third minor:
   $$
   \begin{vmatrix}
   4 & 5 \\
   7 & 8
   \end{vmatrix} = (4 \cdot 8) - (5 \cdot 7) = 32 - 35 = -3
   $$

---

#### Substitute back into the determinant formula:
$$
\det(A) = 1(-3) - 2(-6) + 3(-3)
$$
$$
\det(A) = -3 + 12 - 9 = 0
$$

---

### Step 3: Analyze the determinant

Since \( det(A) = 0 ), the matrix \( A \) is **not invertible**, and the system cannot be solved using the matrix inversion method.

---

### Why can't this system be solved?

When the determinant of the coefficient matrix is zero (\( det(A) = 0 )), the matrix is singular. This means the system of equations is either:
- **Dependent**: Infinitely many solutions exist (the equations are not independent).
- **Inconsistent**: No solution exists (the equations contradict each other).

Thus, Cramer's Rule and matrix inversion methods are not applicable for solving this system.

---