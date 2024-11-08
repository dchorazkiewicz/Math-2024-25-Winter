The initial matrix is:

$$
\mathbf{A} = \begin{pmatrix}
2 & 3 & 1 & 5 \\
-1 & 1 & -1 & 2 \\
3 & 0 & 2 & 1 \\
4 & 1 & 3 & 2
\end{pmatrix}
$$

We perform the following column operations:

1. Add the second column to the first column.
2. Add the second column to the third column.
3. Subtract twice the second column from the fourth column.

After these operations, matrix \(\mathbf{A}'\) becomes:

$$
\mathbf{A}' = \begin{pmatrix}
5 & 3 & 4 & -1 \\
0 & 1 & 0 & 0 \\
3 & 0 & 2 & 1 \\
5 & 1 & 4 & 0
\end{pmatrix}
$$

Now, we calculate the determinant of \(\mathbf{A}'\) by expanding along the second row (as it contains several zeros):

$$
\det(\mathbf{A}') = 1 \cdot \det \begin{pmatrix} 5 & 4 & -1 \\ 3 & 2 & 1 \\ 5 & 4 & 0 \end{pmatrix}
$$

We now compute the determinant of the \(3 \times 3\) matrix:

$$
\det \begin{pmatrix} 5 & 4 & -1 \\ 3 & 2 & 1 \\ 5 & 4 & 0 \end{pmatrix}
$$

Expanding along the first row:

$$
= 5 \cdot \det \begin{pmatrix} 2 & 1 \\ 4 & 0 \end{pmatrix} - 4 \cdot \det \begin{pmatrix} 3 & 1 \\ 5 & 0 \end{pmatrix} + (-1) \cdot \det \begin{pmatrix} 3 & 2 \\ 5 & 4 \end{pmatrix}
$$

Calculating the determinants of the smaller \(2 \times 2\) matrices:

1. $$\det \begin{pmatrix} 2 & 1 \\ 4 & 0 \end{pmatrix} = 2 \cdot 0 - 1 \cdot 4 = -4$$
2. $$\det \begin{pmatrix} 3 & 1 \\ 5 & 0 \end{pmatrix} = 3 \cdot 0 - 1 \cdot 5 = -5$$
3. $$\det \begin{pmatrix} 3 & 2 \\ 5 & 4 \end{pmatrix} = 3 \cdot 4 - 2 \cdot 5 = 12 - 10 = 2$$

Substituting these values:

$$
= 5 \cdot (-4) - 4 \cdot (-5) - 1 \cdot 2
$$

$$
= -20 + 20 - 2 = -2
$$

Thus, the determinant of matrix \(\mathbf{A}\) is:

$$
\det(\mathbf{A}) = -2
$$
