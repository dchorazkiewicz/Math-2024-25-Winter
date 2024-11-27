# Exercises 2024/2025

# Remik: Sequences and Series

1. Determine the type of the sequence: $4, 4, 4, 4, 4, 4,\ldots$.

2. Calculate the fifth term of an arithmetic sequence if the fourth term is $20$ and the sixth term is $28$.

3. Find the value of the eighth term of a geometric sequence where the seventh term is $9$ and the ninth term is $1$.

4. For the sequence with the general formula $a_n = 2n - 10$, determine how many terms of the sequence are negative.

5. Provide the recursive formula $a_{n+1} = a_n + \ldots$ for an arithmetic sequence where the first term is $5$ and the tenth term is $23$.

6. Calculate the sum of the terms of the geometric sequence $-1 + 2 - 4 + \ldots - 64$.

7. Prove that the sequence $a_n = 2n^2 - 1$ is not an arithmetic sequence.

8. An arithmetic sequence consists of $200$ terms. The first term is $-10$, and the last term is $60$. Find the sum of this sequence.

9. Calculate the value of the expression $1 + 2 + 4 + 8 + \ldots + 2^{10}$.

10. For what values of the parameter $n$ is the sequence $(n^2 - 1), (3n + 1), (2n^2 - 6)$ an arithmetic sequence?

11. Insert two numbers between $4$ and $108$ such that they form a geometric sequence.

12. Prove that in an arithmetic sequence, each term $a_n$ is the arithmetic mean of its neighbors, which can be expressed as:

    $$
    a_n = \frac{a_{n-1} + a_{n+1}}{2}.
    $$

13. Prove that in a geometric sequence, each term $a_n$ is the geometric mean of its neighbors, which can be expressed as:

    $$
    a_n^2 = a_{n-1} \cdot a_{n+1}.
    $$

# Remik: Derivatives

1. Compute derivatives of functions:
   1. $y(x) = -3x+3$
   2. $y(x) = \pi x + \sin(1)$
   3. $y(x) = \sin(2)$
   4. $y(x) = x^7$
   5. $y(x) = 2x^3 - 3x^2 + 8x - 9$
   6. $y(x) = ax^2 + 2ax + a$
   7. $y(x) = 6 x^{1/3}$
   8. $y(x) = x^{\pi}$
   9. $y(x) = \sqrt{x}$
   10. $y(x) = \cos(x) + \sin(x)$
   11. $y(x) = \exp(x)$
   12. $y(x) = \ln(x)$
   13. $y(x) = 2\sin(x) \cos(x)$
   14. $y(x) = x\sin(x)$
   15. $y(x) = xe^x$
   16. $y(x) = \ln(x) \exp(x)$
   17. $y(x) = (x+1)(x+1)$
   18. $y(x) = (x+1)\exp(x)$
   19. $y(x) = \ln(-x)$
   20. $y(x) = \sin(-x)$
   21. $y(x) = \sin(x^2)$
   22. $y(x) = \exp(-2x)$
   23. $y(x) = \exp(-3\sin(x))$
   24. $y(x) = \frac{1}{x+1}$
   25. $y(x) = \frac{x}{x+1}$
   26. $y(x) = \frac{1}{\sin(x)}$
   27. $y(x) = \frac{1}{1+\sin(x)}$
   28. $y(x) = \frac{1}{\sin(x^2)}$
   29. $y(x) = \frac{1}{\sin(x^2)+1}$
   30. $y(x) = \sqrt{x+1}$
   31. $y(x) = \log_{10}x$
   32. $y(x) = 10^x$
   33. $y(x) = x^x$
   34. $y(x) = \arccos(x)$

2. Compute the derivative using the definition of the difference quotient for:
   - $3x+1$
   - $x^2+1$
   - a constant $a$

3. Manually compute the velocity and acceleration as functions of time for the following motions. What were the position, velocity, and acceleration at the fifth second?
   - $x(t) = 150 + 50t - 4.5t^2$
   - $x(t) = \sin(t)$
   - $x(t) = t - \frac{1}{t+1}$

4. Using the functions from the previous task, plot _x, v, a_ on the same graph for each case above (don't forget to include a legend to distinguish the lines). Do the values at $t=5$ match your manual calculations?

5. Given certain functions $f$ and $g$ such that $g(0) = 0$, $g'(0) = 2$, and $f'(0) = 4$, find the derivative of the composite function $f(g(x))$ at the point $x=0$.

6. Using L'Hospital's Rule, find the improper limits:
   - $\lim_{x\to 0} \frac{\sin{x}}{x}$
   - $\lim_{x\to 0} \frac{1-\cos{x}}{x^2}$
   - $\lim_{x\to 0} \frac{\sqrt{1+x} - 1}{x}$
   - $\lim_{x\to \infty} \frac{\ln x}{x}$
   - $\lim_{x\to \infty} \frac{\exp(x)}{x}$
   - $\lim_{x\to \infty} \exp(x) \cdot \frac{1}{x}$

7. Why can't L'Hospital's Rule be used to compute the following limit?
   - $\lim_{x\to 0} \frac{x+1}{x-1}$

8. Generalize the Leibniz rule to the case of the derivative of the product of three functions: $(f \cdot g \cdot h)'$.

Link: https://www.geogebra.org/m/GAcTpGCh 

---
 
## Limits of Numerical Sequences and Functions

### 1.1 Infinite Numerical Sequences

2. Determine if the following sequences are convergent or divergent:
    * $a_n = \frac{1}{n}$
    * $b_n = (-1)^n \cdot \frac{1}{n}$
    * $c_n = n^2$

### 1.2 Limit of a Numerical Sequence

3. Calculate the limit of the following sequences:
    * $a_n = \frac{2n + 3}{n + 5}$
    * $b_n = \sqrt{n^2 + n} - n$
    * $c_n = \left(1 + \frac{1}{n}\right)^n$

### 1.3 Infinitesimal and Infinitely Large Sequences

5. Classify the following sequences as infinitesimal, finite, or infinitely large:
    * $a_n = \frac{1}{n^2}$
    * $b_n = n^3$
    * $c_n = \ln(n)$

## 2. Limit of a Function

8. Calculate the following limits:
    * $\lim_{x \to 2} \frac{x^2 - 4}{x - 2}$
    * $\lim_{x \to 0} \frac{\sin(x)}{x}$
    * $\lim_{x \to \infty} \frac{x}{e^x}$

## 5. Important Limits

13. Calculate the following important limits:
    * $\lim_{x \to 0} \frac{\sin(x)}{x}$
    * $\lim_{x \to \infty} (1 + \frac{1}{x})^x$

## 6. Continuity of Functions

15. Determine whether the following functions are continuous:
    * $f(x) = x^2$
    * $g(x) = \frac{1}{x}$
    * $h(x) = |x|$

## 7. Classification of Points of Discontinuity

17. Classify the points of discontinuity of the following functions:
    * $f(x) = \frac{1}{x}$
    * $g(x) = \lfloor x \rfloor$ (floor function)
    * $h(x) = \begin{cases} 
      x^2 & \text{if } x \neq 0, \\
      1 & \text{if } x = 0
      \end{cases}$

## 8. Graphs of Functions Near Points of Discontinuity

18. Sketch the graph of the following functions and describe their behavior near points of discontinuity:
    * $f(x) = \frac{1}{x}$
    * $g(x) = \lfloor x \rfloor$
    * $h(x) = \begin{cases} 
      x^2 & \text{if } x \neq 0, \\
      1 & \text{if } x = 0
      \end{cases}$


# Exercises: Differential Calculus of Functions of One Variable

## 1. Derivative of a Function
1. Compute the derivative using the definition for the following functions:
   - $f(x) = x^2 + 3x + 2$
   - $f(x) = \sqrt{x}$
   - $f(x) = \frac{1}{x}$

2. Interpret the derivative geometrically for $f(x) = x^3$ at $x = 1$.

3. Find the physical significance of the derivative for $s(t) = 5t^2$ (distance as a function of time).

---

## 2. Differentiation Rules
1. Differentiate the following functions:
   - $y = 3x^4 - 7x^3 + 5x^2 - 1$
   - $y = \sin(x) + \cos(2x)$
   - $y = x^5 e^x$

2. Find the derivative of:
   - $f(x) = \ln(\sin(x))$
   - $g(x) = \frac{x^2 + 1}{x-1}$

---

## 3. Differentiation of Composite Functions
1. Find the derivative of:
   - $f(x) = \sin(x^2)$
   - $f(x) = \ln(\sqrt{x+1})$
   - $f(x) = e^{\cos(x)}$

---

## 4. Parametric and Implicit Differentiation
1. For the parametric equations $x = t^2, y = t^3$, find $\frac{dy}{dx}$.
2. Differentiate implicitly: $x^2 + y^2 = 1$.

---

## 5. Derivatives of Exponential and Logarithmic Functions
1. Compute the derivative of:
   - $f(x) = e^x$
   - $g(x) = x^x$
   - $h(x) = \log_{10}(x)$

2. Prove that the derivative of $\ln(x)$ is $\frac{1}{x}$ using the definition of the derivative.

---

## 6. Differential of a Function
1. Find the differential of $y = x^3 - 2x^2 + 5x$.
2. Approximate $\sqrt{4.01}$ using the differential of $f(x) = \sqrt{x}$ at $x = 4$.

---

## 7. Theorems on Differentiable Functions
1. Prove Rolle’s Theorem for $f(x) = x^2 - 4x + 3$ on $[1, 3]$.
2. Verify Lagrange's Mean Value Theorem for $f(x) = x^2$ on $[0, 2]$.
3. Apply Cauchy’s Mean Value Theorem to $f(x) = e^x$ and $g(x) = x^2$ on $[1, 2]$.

---

## 8. L’Hopital’s Rule
1. Compute the following limits using L’Hopital’s Rule:
   - $\lim_{x \to 0} \frac{\sin(x)}{x}$
   - $\lim_{x \to \infty} \frac{\ln(x)}{x}$
   - $\lim_{x \to 0} \frac{1 - \cos(x)}{x^2}$
   - $\lim_{x \to 0^+} x \ln(x)$

---

## 9. Applications of Differential Calculus
1. **Monotonicity:**
   - Determine the intervals of increase and decrease for $f(x) = x^3 - 6x^2 + 9x + 1$.

2. **Extrema:**
   - Find the local maxima and minima of $f(x) = \sin(x) + \cos(x)$ on $[0, 2\pi]$.

3. **Convexity and Inflection Points:**
   - Determine the intervals of concavity and inflection points for $f(x) = x^4 - 4x^3 + 6x^2$.

4. **Asymptotes:**
   - Find the vertical and horizontal asymptotes of $f(x) = \frac{x}{x-1}$.

---

## 10. Function Analysis and Graph Construction
1. Analyze the function $f(x) = \frac{x^2 - 1}{x^2 + 1}$:
   - Find the domain, asymptotes, intervals of increase/decrease, local extrema, concavity, and inflection points.
   - Sketch the graph of the function.

2. Repeat the analysis for $f(x) = e^{-x^2}$.
