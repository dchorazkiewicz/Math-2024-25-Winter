# Examples of solutions to the exercises in the lecture notes

## Basic operations

We have two matrices $A$ and $B$ defined as


$$
A = 
\begin{pmatrix}
1 & 2 
\\ 
3 & 4 
\end{pmatrix}
\quad
\text{and}
\quad
B =
\begin{pmatrix}
5 & 6\\
7 & 8
\end{pmatrix}
$$


Addition of the two matrices is given by


$$A + B =
\begin{pmatrix}
1 + 5 & 2 + 6\\
3 + 7 & 4 + 8
\end{pmatrix}=
\begin{pmatrix}
6 & 8\\
10 & 12
\end{pmatrix}
$$


Multiplication by scalar $3$ is given by

$$
3 A =
\begin{bmatrix}
3 \cdot 1 & 3 \cdot 2\\
3 \cdot 3 & 3 \cdot 4
\end{bmatrix}=
\begin{bmatrix}
3 & 6\\
9 & 12
\end{bmatrix}
$$

Multiplication of the two matrices is given by

$$
A B =
\begin{bmatrix}
1 \cdot 5 + 2 \cdot 7 & 1 \cdot 6 + 2 \cdot 8\\
3 \cdot 5 + 4 \cdot 7 & 3 \cdot 6 + 4 \cdot 8
\end{bmatrix}=
\begin{bmatrix}
19 & 22\\
43 & 50
\end{bmatrix}
$$

## Determinants

The determinant of a $2 \times 2$ matrix

$$
A =
\begin{bmatrix}
2 & 1\\
-3 & 2
\end{bmatrix}
$$

is given by

$$
\text{det}(A) = 2 \cdot 2 - 1 \cdot (-3) = 4 + 3 = 7
$$

## Laplace expansion

The Laplace expansion of the determinant of a $3 \times 3$ matrix

$$
A =
\begin{bmatrix}
1 & 2 & 3\\
4 & 5 & 6\\
0 & 0 & 9
\end{bmatrix}
$$

We will choose the third row for the expansion. The determinant is then given by

$$
\text{det}(A) = 0 \cdot C_{31} + 0 \cdot C_{32} + 9 \cdot C_{33}
$$

where $C_{33}$ is the determinant of the $2 \times 2$ matrix

$$
C_{33} =
\begin{vmatrix}
1 & 2\\
4 & 5
\end{vmatrix}
$$

so that

$$
\text{det}(A) = 9 \cdot (1 \cdot 5 - 2 \cdot 4) = 9 \cdot (5 - 8) = 9 \cdot (-3) = -27
$$

## Inverse matrix using Gauss-Jordan elimination

The inverse of a $3 \times 3$ matrix

$$
A =
\begin{bmatrix}
1 & 0 & 1\\
3 & 1 & 0\\
2 & 2 & 0
\end{bmatrix}
$$

We will start by augmenting the matrix with the identity matrix

$$
\begin{bmatrix}
1 & 0 & 1 & | & 1 & 0 & 0\\
3 & 1 & 0 & | & 0 & 1 & 0\\
2 & 2 & 0 & | & 0 & 0 & 1
\end{bmatrix}
$$

and then perform row operations to obtain the identity matrix on the left side of the augmented matrix. The right side will then be the inverse matrix.

The steps are:

1. $R_3 \to R_3 - 2R_1$

$$
\begin{bmatrix}
1 & 0 & 1 & | & 1 & 0 & 0\\
3 & 1 & 0 & | & 0 & 1 & 0\\
0 & 2 & -2 & | & -2 & 0 & 1
\end{bmatrix}
$$

2. $R_2 \to R_2 - 3R_1$

$$
\begin{bmatrix}
1 & 0 & 1 & | & 1 & 0 & 0\\
0 & 1 & -3 & | & -3 & 1 & 0\\
0 & 2 & -2 & | & -2 & 0 & 1
\end{bmatrix}
$$

3. $R_3 \to R_3 - 2R_2$

$$
\begin{bmatrix}
1 & 0 & 1 & | & 1 & 0 & 0\\
0 & 1 & -3 & | & -3 & 1 & 0\\
0 & 0 & 4 & | & 4 & -2 & 1
\end{bmatrix}
$$

4. $R_3 \to \frac{1}{4}R_3$

$$
\begin{bmatrix}
1 & 0 & 1 & | & 1 & 0 & 0\\
0 & 1 & -3 & | & -3 & 1 & 0\\
0 & 0 & 1 & | & 1 & -\frac{1}{2} & \frac{1}{4}
\end{bmatrix}
$$

5. $R_1 \to R_1 - R_3$

$$
\begin{bmatrix}
1 & 0 & 0 & | & 0 & \frac{1}{2} & -\frac{1}{4}\\
0 & 1 & -3 & | & -3 & 1 & 0\\
0 & 0 & 1 & | & 1 & -\frac{1}{2} & \frac{1}{4}
\end{bmatrix}
$$

6. $R_2 \to R_2 + 3R_3$

$$
\begin{bmatrix}
1 & 0 & 0 & | & 0 & \frac{1}{2} & -\frac{1}{4}\\
0 & 1 & 0 & | & 0 & \frac{1}{2} & \frac{3}{4}\\
0 & 0 & 1 & | & 1 & -\frac{1}{2} & \frac{1}{4}
\end{bmatrix}
$$

### Final Inverse Matrix

$$
A^{-1} =
\begin{bmatrix}
0 & \frac{1}{2} & -\frac{1}{4}\\
0 & \frac{1}{2} & \frac{3}{4}\\
1 & -\frac{1}{2} & \frac{1}{4}
\end{bmatrix}
$$

### Verification

Multiply the original matrix with the inverse to confirm the result:

$$
AA^{-1} =
\begin{bmatrix}
1 & 0 & 1\\
3 & 1 & 0\\
2 & 2 & 0
\end{bmatrix}
\begin{bmatrix}
0 & \frac{1}{2} & -\frac{1}{4}\\
0 & \frac{1}{2} & \frac{3}{4}\\
1 & -\frac{1}{2} & \frac{1}{4}
\end{bmatrix}
=
\begin{bmatrix}
1 & 0 & 0\\
0 & 1 & 0\\
0 & 0 & 1
\end{bmatrix}
$$
