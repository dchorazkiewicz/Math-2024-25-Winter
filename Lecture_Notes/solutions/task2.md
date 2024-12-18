# Matrix Calculations and Solutions

## 5. Inverse of a Matrix from the formula

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


## **5. Solutions**

### **1. Matrix \( A \):**
Given:
$$
A = \begin{bmatrix} 2 & 0 & 1 \\ 0 & 1 & 0 \\ 1 & 2 & 0 \end{bmatrix}
$$
- **Determinant:**
  $$
  \det(A) = -1
  $$
- **Adjoint Matrix:**
  $$
  \text{adj}(A) = \begin{bmatrix} 0 & 0 & -1 \\ 2 & -1 & -4 \\ -1 & 0 & 2 \end{bmatrix}
  $$
- **Inverse Matrix:**
  $$
  A^{-1} = \begin{bmatrix} 0 & -2 & 1 \\ 0 & 1 & 0 \\ 1 & 4 & -2 \end{bmatrix}
  $$

---

### **2. Matrix \( B \):**
Given:
$$
B = \begin{bmatrix} 4 & -3 & 7 \\ -1 & 6 & 3 \\ 2 & 9 & 1 \end{bmatrix}
$$
- **Rank:**
  $$
  \text{rank}(B) = 3
  $$

---
## 6. Inverse of a Matrix using the Gauss Method

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


## **6. Solutions**

### **1. Matrix \( A \):**
Given:
$$
A = \begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix}
$$
- **Determinant:**
  $$
  \det(A) = -2
  $$
- **Inverse Matrix:**
  $$
  A^{-1} = \begin{bmatrix} -2 & 1 \\ 1.5 & -0.5 \end{bmatrix}
  $$

---

### **2. Matrix \( B \):**
Given:
$$
B = \begin{bmatrix} 1 & 2 & 3 \\ 4 & 5 & 1 \\ 2 & 3 & 2 \end{bmatrix}
$$
- **Rank:**
  $$
  \text{rank}(B) = 3
  $$

---

### **3. Matrix \( C \):**
Given:
$$
C = \begin{bmatrix} 0 & 0 & 1 \\ 1 & 0 & 0 \\ 1 & 1 & 0 \end{bmatrix}
$$
- **Rank:**
  $$
  \text{rank}(C) = 3
  $$

  ## 7. Linear Equations old school

Solve the following systems of equations without using matrices:

* $3x-2y=5, \quad 2x+3y=7$,
* $2x-3y=10, \quad 4x+5y=20$,
* $2x - y + z = 3, \quad x + 2y - z = 1, \quad 3x - y + 2z = 11$.
* $2x-3y+4z+2t=2, \quad 3x+2y-5z+3t=3, \quad 4x-3y+2z-5t=4, \quad 5x+4y-3z+2t=5$.
  
  # 7. Solutions

## **1. System**
Given:
$$
3x - 2y = 5 \quad \text{and} \quad 2x + 3y = 7
$$
**Solution:**
- $x = \frac{29}{13}$
- $y = \frac{11}{13}$

---

## **2. System**
Given:
$$
2x - 3y = 10 \quad \text{and} \quad 4x + 5y = 20
$$
**Solution:**
- $x = 5$
- $y = 0$

---

## **3. System**
Given:
$$
2x - y + z = 3, \quad x + 2y - z = 1, \quad 3x - y + 2z = 11
$$
**Solution:**
- $x = -\frac{1}{4}$
- $y = \frac{19}{4}$
- $z = \frac{33}{4}$

---

## **4. System**
Given:
$$
2x - 3y + 4z + 2t = 2, \quad 3x + 2y - 5z + 3t = 3, \quad 4x - 3y + 2z - 5t = 4, \quad 5x + 4y - 3z + 2t = 5
$$
**Solution:**
- $x = 1$
- $y = 0$
- $z = 0$
- $t = 0$

## 8. Linear equations by Cramer's Rule

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

## **8. Solutions**

### **1. System**
Given:
$$
\begin{cases}
2x_1 - 3x_2 = 7 \\
3x_1 + 5x_2 = 2
\end{cases}
$$
**Steps:**
1. Compute the determinant of the coefficient matrix:
   $$
   \Delta = \begin{vmatrix} 2 & -3 \\ 3 & 5 \end{vmatrix} = 19
   $$
2. Compute $\Delta_1$ and $\Delta_2$:
   $$
   \Delta_1 = \begin{vmatrix} 7 & -3 \\ 2 & 5 \end{vmatrix} = 41, \quad \Delta_2 = \begin{vmatrix} 2 & 7 \\ 3 & 2 \end{vmatrix} = -17
   $$
3. Solve:
   $$
   x_1 = \frac{\Delta_1}{\Delta} = \frac{41}{19}, \quad x_2 = \frac{\Delta_2}{\Delta} = \frac{-17}{19}
   $$

**Solution:**
$$
x_1 = \frac{41}{19}, \quad x_2 = \frac{-17}{19}
$$

---

### **2. System**
Given:
$$
\begin{cases}
2x + y - z = 1 \\
x - y + 2z = 4 \\
3x - 2z = -1
\end{cases}
$$
**Solution:**
$$
x = 1, \quad y = 1, \quad z = 2
$$

---

### **3. System**
Given:
$$
\begin{cases}
x + y + z - t = 2 \\
x - z + 2t = 6 \\
2x - 3y + t = 4 \\
3x + y + 3z - 4t = -2
\end{cases}
$$
**Solution:**
$$
x = \frac{1}{2}, \quad y = 1, \quad z = \frac{13}{2}, \quad t = 6
$$

---

### **4. Why can't this system be solved using Cramer's rule?**
Given:
$$
\begin{cases}
x_1 + 2x_2 + 3x_3 = 3 \\
4x_1 + 5x_2 + 6x_3 = 2 \\
7x_1 + 8x_2 + 9x_3 = 1
\end{cases}
$$
**Reason:**
The determinant of the coefficient matrix is:
$$
\text{det} = 0
$$
Since the determinant is zero, the system cannot be solved using Cramer's rule.

---
## 9. Linear equations by Gauss Elimination

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

## **9. Solutions**

### **System**
Given:
$$
\begin{cases}
x + 2y - 2z = 4 \\
2x + y + 2z = 0 \\
3x + 2y + z = 1
\end{cases}
$$
**Solution:**
$$
x = -2, \quad y = \frac{10}{3}, \quad z = \frac{1}{3}
$$

---
## 10. Linear equations by Matrix Inversion

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

## **10. Solutions**

### **1. System**
Given:
$$
\begin{cases}
x + 2y + 3z = 5 \\
2y + 3z = 4 \\
3z = 3
\end{cases}
$$
**Solution:**
$$
x = 1, \quad y = \frac{1}{2}, \quad z = 1
$$

---

### **2. System**
Given:
$$
\begin{cases}
x_1 + 2x_2 + 3x_3 = 41 \\
4x_1 + 5x_2 + 6x_3 = 93 \\
7x_1 + 8x_2 + 9x_3 = 145
\end{cases}
$$
**Reason:**
The coefficient matrix is not invertible because its determinant is zero.

---