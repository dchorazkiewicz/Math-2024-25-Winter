## 11. Vectors I

1. By what number should vector $\mathbf{a} = [3, 4]$ be multiplied so that its length is equal to 1?

2. Calculate the length of vector $\mathbf{b} = [1, 1]$ and find the unit vector of this vector.

3. Plot the vector and the unit vector from the previous exercise.

4. Calculate the length of vector $\mathbf{c} = [1, 2, 3]$ and find the unit vector of this vector.

5. Find the Cartesian coordinates of vector $\mathbf{v} = [2, 3, 4]$ in the basis $\{\mathbf{b_1} = [1, 0, 1], \mathbf{b_2} = [0, 1, 0], \mathbf{b_3} = [1, 0, -1]\}$.

---

# Solutions to Vector Problems

## **1. Problem**
### **Question:**
By what number should vector $\mathbf{a} = [3, 4]$ be multiplied so that its length is equal to 1?

### **Solution:**
1. Calculate the length of $\mathbf{a}$:
   $$
   \|\mathbf{a}\| = \sqrt{3^2 + 4^2} = \sqrt{9 + 16} = \sqrt{25} = 5
   $$

2. To make the length 1, divide $\mathbf{a}$ by its magnitude:
   $$
   \mathbf{u_a} = \frac{\mathbf{a}}{\|\mathbf{a}\|} = \frac{[3, 4]}{5} = \left[\frac{3}{5}, \frac{4}{5}\right]
   $$

3. The number by which $\mathbf{a}$ should be multiplied:
   $$
   \frac{1}{5}
   $$

**Answer:**
The vector $\mathbf{a}$ should be multiplied by $\frac{1}{5}$.

---

## **2. Problem**
### **Question:**
Calculate the length of vector $\mathbf{b} = [1, 1]$ and find the unit vector of this vector.

### **Solution:**
1. Calculate the length of $\mathbf{b}$:
   $$
   \|\mathbf{b}\| = \sqrt{1^2 + 1^2} = \sqrt{1 + 1} = \sqrt{2}
   $$

2. Calculate the unit vector:
   $$
   \mathbf{u_b} = \frac{\mathbf{b}}{\|\mathbf{b}\|} = \frac{[1, 1]}{\sqrt{2}} = \left[\frac{1}{\sqrt{2}}, \frac{1}{\sqrt{2}}\right]
   $$

**Answer:**
The length of $\mathbf{b}$ is $\sqrt{2}$, and the unit vector is:
$$
\mathbf{u_b} = \left[\frac{1}{\sqrt{2}}, \frac{1}{\sqrt{2}}\right]
$$

---

## **3. Problem**
### **Question:**
Plot the vector $\mathbf{b} = [1, 1]$ and its unit vector from the previous exercise.

### **Solution:**
- The original vector $\mathbf{b} = [1, 1]$ starts at $(0, 0)$ and ends at $(1, 1)$.
- The unit vector $\mathbf{u_b} = \left[\frac{1}{\sqrt{2}}, \frac{1}{\sqrt{2}}\right]$ points in the same direction but has a length of 1.

**Graph:**
The graph below illustrates:
- **Blue Vector:** Original vector $\mathbf{b}$.
- **Red Vector:** Unit vector $\mathbf{u_b}$.

---

## **4. Problem**
### **Question:**
Calculate the length of vector $\mathbf{c} = [1, 2, 3]$ and find the unit vector of this vector.

### **Solution:**
1. Calculate the length of $\mathbf{c}$:
   $$
   \|\mathbf{c}\| = \sqrt{1^2 + 2^2 + 3^2} = \sqrt{1 + 4 + 9} = \sqrt{14}
   $$

2. Calculate the unit vector:
   $$
   \mathbf{u_c} = \frac{\mathbf{c}}{\|\mathbf{c}\|} = \frac{[1, 2, 3]}{\sqrt{14}} = \left[\frac{1}{\sqrt{14}}, \frac{2}{\sqrt{14}}, \frac{3}{\sqrt{14}}\right]
   $$

**Answer:**
The length of $\mathbf{c}$ is $\sqrt{14}$, and the unit vector is:
$$
\mathbf{u_c} = \left[\frac{1}{\sqrt{14}}, \frac{2}{\sqrt{14}}, \frac{3}{\sqrt{14}}\right]
$$

---

## **5. Problem**
### **Question:**
Find the Cartesian coordinates of vector $\mathbf{v} = [2, 3, 4]$ in the basis:
$$
\mathbf{b_1} = [1, 0, 1], \quad \mathbf{b_2} = [0, 1, 0], \quad \mathbf{b_3} = [1, 0, -1]
$$

### **Solution:**
1. Define the transformation:
   $$
   \mathbf{v} = c_1 \mathbf{b_1} + c_2 \mathbf{b_2} + c_3 \mathbf{b_3}
   $$

2. This corresponds to solving:
   $$
   \begin{bmatrix} 
   1 & 0 & 1 \\ 
   0 & 1 & 0 \\ 
   1 & 0 & -1 
   \end{bmatrix} 
   \begin{bmatrix} 
   c_1 \\ 
   c_2 \\ 
   c_3 
   \end{bmatrix} =
   \begin{bmatrix} 
   2 \\ 
   3 \\ 
   4 
   \end{bmatrix}
   $$

**Answer:**
The Cartesian coordinates of $\mathbf{v}$ in the given basis are:
$$
[3, 3, -1]
$$

## 12. Vectors II

1. Perform the addition of vector $[2, 1]$ to vector $[-1, 1]$. Plot both vectors and their sum on a graph.

2. Calculate the area of the triangle spanned by vectors $[2, 1]$ and $[-1, 1]$.

3. Calculate the volume of the parallelepiped spanned by vectors $[2, 1]$, $[-1, 1]$, and $[1, 2]$.

4. Check if vectors $[2, 1]$ and $[-1, 1]$ are perpendicular.

5. Calculate the angle in degrees between vectors $[4, 2, 1]$ and $[1, 3, 2]$.

6. For three-dimensional vectors: $\mathbf{a} = [a_x, a_y, a_z]$, $\mathbf{b} = [b_x, b_y, b_z]$, $\mathbf{c} = [c_x, c_y, c_z]$, prove that the following identity is satisfied:

$$
\mathbf{a} \times (\mathbf{b} \times \mathbf{c}) = (\mathbf{a} \cdot \mathbf{c}) \mathbf{b} - (\mathbf{a} \cdot \mathbf{b}) \mathbf{c}.
$$

---

# Solutions to Vectors II Problems

## **1. Problem**
### **Question:**
Perform the addition of vector $\mathbf{u} = [2, 1]$ to vector $\mathbf{v} = [-1, 1]$. Plot both vectors and their sum on a graph.

### **Solution:**
1. Calculate the sum:
   $$
   \mathbf{u} + \mathbf{v} = [2, 1] + [-1, 1] = [1, 2]
   $$

2. Plot:
   - $\mathbf{u} = [2, 1]$: Starts at $(0, 0)$ and ends at $(2, 1)$.
   - $\mathbf{v} = [-1, 1]$: Starts at $(0, 0)$ and ends at $(-1, 1)$.
   - $\mathbf{u} + \mathbf{v} = [1, 2]$: Starts at $(0, 0)$ and ends at $(1, 2)$.

**Graph:**
The graph shows $\mathbf{u}$ (blue), $\mathbf{v}$ (red), and their sum $\mathbf{u} + \mathbf{v}$ (green).

---

## **2. Problem**
### **Question:**
Calculate the area of the triangle spanned by vectors $\mathbf{u} = [2, 1]$ and $\mathbf{v} = [-1, 1]$.

### **Solution:**
1. Compute the magnitude of the cross product:
   $$
   \|\mathbf{u} \times \mathbf{v}\| = |(2 \cdot 1) - (1 \cdot -1)| = |2 - (-1)| = 3
   $$

2. Area of the triangle:
   $$
   \text{Area} = \frac{1}{2} \|\mathbf{u} \times \mathbf{v}\| = \frac{1}{2} \cdot 3 = 1.5
   $$

**Answer:**
The area of the triangle is $1.5$ square units.

---

## **3. Problem**
### **Question:**
Calculate the volume of the parallelepiped spanned by vectors $\mathbf{u} = [2, 1]$, $\mathbf{v} = [-1, 1]$, and $\mathbf{w} = [1, 2]$.

### **Solution:**
1. Create a matrix with $\mathbf{u}$, $\mathbf{v}$, and $\mathbf{w}$ as columns:
   $$
   \begin{bmatrix}
   2 & -1 & 1 \\
   1 & 1 & 2 \\
   0 & 0 & 0
   \end{bmatrix}
   $$

2. Compute the determinant:
   $$
   \text{det} = 0
   $$

3. The determinant being zero indicates that the vectors are coplanar.

**Answer:**
The volume of the parallelepiped is $0$.

---

## **4. Problem**
### **Question:**
Check if vectors $\mathbf{u} = [2, 1]$ and $\mathbf{v} = [-1, 1]$ are perpendicular.

### **Solution:**
1. Compute the dot product:
   $$
   \mathbf{u} \cdot \mathbf{v} = (2 \cdot -1) + (1 \cdot 1) = -2 + 1 = -1
   $$

2. Since the dot product is not zero:
   $$
   \mathbf{u} \cdot \mathbf{v} \neq 0
   $$

**Answer:**
The vectors are not perpendicular.

---

## **5. Problem**
### **Question:**
Calculate the angle in degrees between vectors $\mathbf{a} = [4, 2, 1]$ and $\mathbf{b} = [1, 3, 2]$.

### **Solution:**
1. Compute the dot product:
   $$
   \mathbf{a} \cdot \mathbf{b} = (4 \cdot 1) + (2 \cdot 3) + (1 \cdot 2) = 4 + 6 + 2 = 12
   $$

2. Compute the magnitudes:
   $$
   \|\mathbf{a}\| = \sqrt{4^2 + 2^2 + 1^2} = \sqrt{16 + 4 + 1} = \sqrt{21}
   $$
   $$
   \|\mathbf{b}\| = \sqrt{1^2 + 3^2 + 2^2} = \sqrt{1 + 9 + 4} = \sqrt{14}
   $$

3. Compute the cosine of the angle:
   $$
   \cos\theta = \frac{\mathbf{a} \cdot \mathbf{b}}{\|\mathbf{a}\| \|\mathbf{b}\|} = \frac{12}{\sqrt{21} \cdot \sqrt{14}}
   $$

4. Compute the angle:
   $$
   \theta = \cos^{-1}\left(\frac{12}{\sqrt{21} \cdot \sqrt{14}}\right) \approx 45.58^\circ
   $$

**Answer:**
The angle between the vectors is approximately $45.58^\circ$.

---

## **6. Problem**
### **Question:**
For three-dimensional vectors, prove the identity:
$$
\mathbf{a} \times (\mathbf{b} \times \mathbf{c}) = (\mathbf{a} \cdot \mathbf{c})\mathbf{b} - (\mathbf{a} \cdot \mathbf{b})\mathbf{c}
$$

### **Solution:**
1. Compute $\mathbf{b} \times \mathbf{c}$, then $\mathbf{a} \times (\mathbf{b} \times \mathbf{c})$.
2. Compute the RHS:
   $$
   (\mathbf{a} \cdot \mathbf{c})\mathbf{b} - (\mathbf{a} \cdot \mathbf{b})\mathbf{c}
   $$

3. Simplify both sides:
   $$
   \text{LHS} = \text{RHS}
   $$

**Answer:**
The identity is proven.

## 13. Vectors III

1. Divide the line segment connecting points $A(-1, 2)$ and $B(3, -2)$ in the ratio $1:3$. Illustrate the result on a graph.

2. Project vector $\mathbf{a} = (3, 4)$ onto the $OX$ and $OY$ axes. Illustrate the result on a graph.

3. Project vector $\mathbf{a} = (2, 3)$ onto vector $\mathbf{b} = (1, 1)$. Illustrate the result on a graph.

4. Project vector $\mathbf{b} = (1, 1)$ onto vector $\mathbf{a} = (2, 3)$. Illustrate the result on a graph.

---

# Solutions to Vectors III Problems

## **1. Problem**
### **Question:**
Divide the line segment connecting points $A(-1, 2)$ and $B(3, -2)$ in the ratio $1:3$. Illustrate the result on a graph.

### **Solution:**
To divide the line segment in the ratio $m:n$, the coordinates of the dividing point $P$ are given by:
$$
P_x = \frac{m \cdot x_2 + n \cdot x_1}{m + n}, \quad P_y = \frac{m \cdot y_2 + n \cdot y_1}{m + n}
$$

Substituting the given points and ratio:
1. $P_x = \frac{1 \cdot 3 + 3 \cdot (-1)}{1 + 3} = \frac{3 - 3}{4} = 0$
2. $P_y = \frac{1 \cdot (-2) + 3 \cdot 2}{1 + 3} = \frac{-2 + 6}{4} = 1$

**Answer:**
The dividing point is $P(0, 1)$.

---

## **2. Problem**
### **Question:**
Project vector $\mathbf{a} = (3, 4)$ onto the $OX$ and $OY$ axes. Illustrate the result on a graph.

### **Solution:**
1. **Projection onto the $OX$ axis:**
   $$
   \mathbf{a_x} = (3, 0)
   $$

2. **Projection onto the $OY$ axis:**
   $$
   \mathbf{a_y} = (0, 4)
   $$

**Answer:**
The projections of $\mathbf{a}$ are:
- Onto $OX$: $\mathbf{a_x} = (3, 0)$
- Onto $OY$: $\mathbf{a_y} = (0, 4)$

---

## **3. Problem**
### **Question:**
Project vector $\mathbf{a} = (2, 3)$ onto vector $\mathbf{b} = (1, 1)$. Illustrate the result on a graph.

### **Solution:**
The projection formula is:
$$
\text{proj}_{\mathbf{b}} \mathbf{a} = \frac{\mathbf{a} \cdot \mathbf{b}}{\|\mathbf{b}\|^2} \mathbf{b}
$$

1. Compute the dot product:
   $$
   \mathbf{a} \cdot \mathbf{b} = (2 \cdot 1) + (3 \cdot 1) = 5
   $$

2. Compute $\|\mathbf{b}\|^2$:
   $$
   \|\mathbf{b}\|^2 = 1^2 + 1^2 = 2
   $$

3. Compute the projection:
   $$
   \text{proj}_{\mathbf{b}} \mathbf{a} = \frac{5}{2} \mathbf{b} = \frac{5}{2} [1, 1] = \left[\frac{5}{2}, \frac{5}{2}\right]
   $$

**Answer:**
The projection of $\mathbf{a}$ onto $\mathbf{b}$ is:
$$
\text{proj}_{\mathbf{b}} \mathbf{a} = \left(\frac{5}{2}, \frac{5}{2}\right)
$$

---

## **4. Problem**
### **Question:**
Project vector $\mathbf{b} = (1, 1)$ onto vector $\mathbf{a} = (2, 3)$. Illustrate the result on a graph.

### **Solution:**
The projection formula is:
$$
\text{proj}_{\mathbf{a}} \mathbf{b} = \frac{\mathbf{b} \cdot \mathbf{a}}{\|\mathbf{a}\|^2} \mathbf{a}
$$

1. Compute the dot product:
   $$
   \mathbf{b} \cdot \mathbf{a} = (1 \cdot 2) + (1 \cdot 3) = 5
   $$

2. Compute $\|\mathbf{a}\|^2$:
   $$
   \|\mathbf{a}\|^2 = 2^2 + 3^2 = 4 + 9 = 13
   $$

3. Compute the projection:
   $$
   \text{proj}_{\mathbf{a}} \mathbf{b} = \frac{5}{13} \mathbf{a} = \frac{5}{13} [2, 3] = \left[\frac{10}{13}, \frac{15}{13}\right]
   $$

**Answer:**
The projection of $\mathbf{b}$ onto $\mathbf{a}$ is:
$$
\text{proj}_{\mathbf{a}} \mathbf{b} = \left(\frac{10}{13}, \frac{15}{13}\right)
$$

## 14. Equations of Lines on a Plane

1. The line passes through points $A(1, 2)$ and $B(3, 4)$. Find the equation of the line.

2. The line passes through point $A(1, 2)$ and is parallel to the line $y = 2x + 3$. Find the equation of the line.

3. The line passes through point $A(1, 2)$ and is perpendicular to the line $y = 2x + 3$. Find the equation of the line.

4. We have two lines $y = 2x + 3$ and $y = 3x + 2$. Find the intersection point of these lines and calculate the angle between them.

5. Write the equation of the line passing through point $A(1, 2)$ and parallel to the vector $\mathbf{v} = [2, 3]$.

6. We have the line $y = 2x + 3$. Find an example of a line perpendicular and parallel to it.

7. We have the line $y = 2x + 3$ and point $A(1, 2)$. Find the distance from point $A$ to the line.

8. The line intersects the coordinate axes at points $A(2, 0)$ and $B(0, 3)$. Find the equation of the line.

9. Calculate the angle between the line $y = x + 3$ and the $Ox$ axis.

10. Provide a vector perpendicular to the line $x + y + 1 = 0$.

---

# Solutions to Equations of Lines on a Plane

## **1. Problem**
### **Question:**
The line passes through points $A(1, 2)$ and $B(3, 4)$. Find the equation of the line.

### **Solution:**
1. Compute the slope:
   $$
   m = \frac{y_2 - y_1}{x_2 - x_1} = \frac{4 - 2}{3 - 1} = 1
   $$

2. Write the line equation:
   Using the point-slope form:
   $$
   y - y_1 = m(x - x_1)
   $$
   Substituting $m = 1$ and $(x_1, y_1) = (1, 2)$:
   $$
   y - 2 = 1(x - 1)
   $$
   Simplify:
   $$
   y = x + 1
   $$

**Answer:**
The equation of the line is:
$$
y = x + 1
$$

---

## **2. Problem**
### **Question:**
The line passes through point $A(1, 2)$ and is parallel to the line $y = -2x + 3$. Find the equation of the line.

### **Solution:**
1. A parallel line has the same slope as the given line:
   $$
   m = -2
   $$

2. Write the line equation:
   Using the point-slope form:
   $$
   y - y_1 = m(x - x_1)
   $$
   Substituting $m = -2$ and $(x_1, y_1) = (1, 2)$:
   $$
   y - 2 = -2(x - 1)
   $$
   Simplify:
   $$
   y = -2x + 4
   $$

**Answer:**
The equation of the line is:
$$
y = -2x + 4
$$

---

## **3. Problem**
### **Question:**
The line passes through point $A(1, 2)$ and is perpendicular to the line $y = 2x + 3$. Find the equation of the line.

### **Solution:**
1. A perpendicular line has a slope:
   $$
   m = -\frac{1}{2}
   $$

2. Write the line equation:
   Using the point-slope form:
   $$
   y - y_1 = m(x - x_1)
   $$
   Substituting $m = -\frac{1}{2}$ and $(x_1, y_1) = (1, 2)$:
   $$
   y - 2 = -\frac{1}{2}(x - 1)
   $$
   Simplify:
   $$
   y = -\frac{1}{2}x + \frac{5}{2}
   $$

**Answer:**
The equation of the line is:
$$
y = -\frac{1}{2}x + \frac{5}{2}
$$

---

## **4. Problem**
### **Question:**
We have two lines $y = 2x + 3$ and $y = 3x + 2$. Find the intersection point of these lines and calculate the angle between them.

### **Solution:**
1. Find the intersection point:
   Solve the equations:
   $$
   2x + 3 = 3x + 2
   $$
   $$
   x = 1, \quad y = 2(1) + 3 = 5
   $$
   Intersection point:
   $$
   (1, 5)
   $$

2. Find the angle between the lines:
   The slopes are $m_1 = 2$ and $m_2 = 3$. The angle $\theta$ is given by:
   $$
   \tan\theta = \left| \frac{m_2 - m_1}{1 + m_1 \cdot m_2} \right|
   $$
   Substituting:
   $$
   \tan\theta = \left| \frac{3 - 2}{1 + (2 \cdot 3)} \right| = \frac{1}{7}
   $$
   $$
   \theta = \tan^{-1}\left(\frac{1}{7}\right)
   $$
   Approximation:
   $$
   \theta \approx 8.13^\circ
   $$

**Answer:**
The intersection point is $(1, 5)$, and the angle between the lines is approximately $8.13^\circ$.

---

## **5. Problem**
### **Question:**
Write the equation of the line passing through point $A(1, 2)$ and parallel to the vector $\mathbf{v} = [2, 3]$.

### **Solution:**
1. The slope of the line is the ratio of the vector components:
   $$
   m = \frac{3}{2}
   $$

2. Write the line equation:
   Using the point-slope form:
   $$
   y - y_1 = m(x - x_1)
   $$
   Substituting $m = \frac{3}{2}$ and $(x_1, y_1) = (1, 2)$:
   $$
   y - 2 = \frac{3}{2}(x - 1)
   $$
   Simplify:
   $$
   y = \frac{3}{2}x + \frac{1}{2}
   $$

**Answer:**
The equation of the line is:
$$
y = \frac{3}{2}x + \frac{1}{2}
$$

---

## **6. Problem**
### **Question:**
We have the line $y = 2x + 3$. Find an example of a line perpendicular and parallel to it.

### **Solution:**
1. **Parallel line:** $y = 2x - 1$.
2. **Perpendicular line:** $y = -\frac{1}{2}x + 4$.

**Answer:**
The parallel line is $y = 2x - 1$, and the perpendicular line is $y = -\frac{1}{2}x + 4$.

---

## **7. Problem**
### **Question:**
Find the distance from point $A(1, 2)$ to the line $y = 2x + 3$.

### **Solution:**
The distance from a point $(x_0, y_0)$ to a line $ax + by + c = 0$ is:
$$
d = \frac{|ax_0 + by_0 + c|}{\sqrt{a^2 + b^2}}
$$
Rewrite the line as $-2x + y - 3 = 0$. Substituting $a = -2$, $b = 1$, $c = -3$, and $(x_0, y_0) = (1, 2)$:
$$
d = \frac{|-2(1) + 1(2) - 3|}{\sqrt{(-2)^2 + 1^2}} = \frac{|-2 + 2 - 3|}{\sqrt{4 + 1}} = \frac{3}{\sqrt{5}}
$$

**Answer:**
The distance is $\frac{3}{\sqrt{5}}$.

---

## **8. Problem**
### **Question:**
The line intersects the coordinate axes at points $A(2, 0)$ and $B(0, 3)$. Find the equation of the line.

### **Solution:**
The slope is:
$$
m = \frac{y_2 - y_1}{x_2 - x_1} = \frac{3 - 0}{0 - 2} = -\frac{3}{2}
$$
The line equation is:
$$
y - 0 = -\frac{3}{2}(x - 2)
$$
Simplify:
$$
y = -\frac{3}{2}x + 3
$$

**Answer:**
The equation of the line is $y = -\frac{3}{2}x + 3$.

---

## **9. Problem**
### **Question:**
Calculate the angle between the line $y = x + 3$ and the $Ox$ axis.

### **Solution:**
The slope of the line is $m = 1$. The angle is:
$$
\theta = \tan^{-1}(m) = \tan^{-1}(1) = 45^\circ
$$

**Answer:**
The angle is $45^\circ$.

---

## **10. Problem**
### **Question:**
Provide a vector perpendicular to the line $x + y + 1 = 0$.

### **Solution:**
The normal vector of the line is:
$$
\mathbf{n} = (1, 1)
$$

**Answer:**
A vector perpendicular to the line is $\mathbf{n} = (1, 1)$.