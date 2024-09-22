<style>
h2 {
    color: brown;
}

h3 {
    color: tomato;
}

</style>

# Równania prostych na płaszczyźnie

## Wprowadzenie

Równania prostych są jednym z podstawowych narzędzi w geometrii analitycznej. Opisują one zależność między współrzędnymi punktów leżących na prostej w układzie kartezjańskim. Istnieje kilka form równań prostych, w zależności od dostępnych informacji, takich jak współczynnik kierunkowy, punkty leżące na prostej, czy sposób przecięcia z osiami współrzędnych.

## Rodzaje równań prostych na płaszczyźnie

### 1. Równanie ogólne prostej

**Równanie ogólne prostej** jest zapisane w postaci:
$$
Ax + By + C = 0
$$
gdzie $A$, $B$, i $C$ są stałymi. Jest to najogólniejsza forma równania prostej, która może opisywać każdą prostą na płaszczyźnie.

**Przykład:**
Prosta dana równaniem $3x - 4y + 5 = 0$.

### 2. Równanie kanoniczne prostej

**Równanie kanoniczne prostej** ma postać:
$$
\frac{x - x_0}{a} = \frac{y - y_0}{b}
$$
gdzie $(x_0, y_0)$ to punkt na prostej, a wektor $\vec{d} = (a, b)$ jest wektorem kierunkowym prostej.

**Przykład:**
Prosta przechodząca przez punkt $(1, 2)$ i mająca kierunek wyznaczony przez wektor $(3, 4)$ ma równanie:
$$
\frac{x - 1}{3} = \frac{y - 2}{4}
$$

### 3. Równanie prostej w odcinkach na osiach układu współrzędnych

**Równanie prostej w odcinkach** jest szczególnym przypadkiem, w którym prosta przecina osie układu współrzędnych w punktach $(a, 0)$ i $(0, b)$. Równanie tej prostej można zapisać jako:
$$
\frac{x}{a} + \frac{y}{b} = 1
$$

**Przykład:**
Dla $a = 2$ i $b = 3$, równanie prostej to:
$$
\frac{x}{2} + \frac{y}{3} = 1
$$

### 4. Równanie prostej ze współczynnikiem kątowym

**Równanie prostej ze współczynnikiem kątowym** $m$ (nachylenie prostej) ma postać:
$$
y = mx + c
$$
gdzie $m$ to współczynnik kątowy, a $c$ to wyraz wolny, określający punkt przecięcia prostej z osią $y$.

**Przykład:**
Dla $m = 2$ i $c = -3$, równanie prostej to:
$$
y = 2x - 3
$$

### 5. Równanie prostej przechodzącej przez dany punkt w danym kierunku

Równanie prostej przechodzącej przez punkt $(x_0, y_0)$ i mającej kierunek określony przez wektor $(a, b)$ można zapisać jako:
$$
\frac{x - x_0}{a} = \frac{y - y_0}{b}
$$

**Przykład:**
Prosta przechodząca przez $(2, 3)$ i kierunek $(4, -1)$ ma równanie:
$$
\frac{x - 2}{4} = \frac{y - 3}{-1}
$$

### 6. Równanie prostej przechodzącej przez dwa dane punkty

Jeśli prosta przechodzi przez punkty $(x_1, y_1)$ i $(x_2, y_2)$, to jej równanie jest:
$$
\frac{y - y_1}{y_2 - y_1} = \frac{x - x_1}{x_2 - x_1}
$$

**Przykład:**
Prosta przez punkty $(1, 2)$ i $(3, 4)$ ma równanie:
$$
\frac{y - 2}{4 - 2} = \frac{x - 1}{3 - 1} \implies y - 2 = x - 1 \implies y = x + 1
$$

## Względne położenie prostych na płaszczyźnie

Proste mogą być:
1. **Równoległe**: Mają ten sam współczynnik kierunkowy $m$.
2. **Prostopadłe**: Iloczyn ich współczynników kierunkowych wynosi $-1$ ($m_1 \cdot m_2 = -1$).
3. **Przecinające się**: Mają różne współczynniki kierunkowe.

## Przecięcie dwóch prostych

Punkt przecięcia dwóch prostych można znaleźć, rozwiązując układ równań prostych.

**Przykład:**

Znajdź punkt przecięcia prostych $y = 2x + 1$ i $y = -x + 4$:

$$
2x + 1 = -x + 4
$$

$$
3x = 3 \implies x = 1
$$

Podstawiając $x = 1$ do pierwszego równania:

$$
y = 2 \times 1 + 1 = 3
$$

Punkt przecięcia to $(1, 3)$.

## Kąt między dwiema prostymi

Kąt $\theta$ między prostymi $y = m_1x + c_1$ i $y = m_2x + c_2$ można obliczyć z zależności:

$$
\tan \theta = \left|\frac{m_1 - m_2}{1 + m_1 m_2}\right|
$$

**Przykład:**

Dla prostych $y = 2x + 1$ i $y = -x + 4$:

$$
\tan \theta = \left|\frac{2 - (-1)}{1 + 2 \times (-1)}\right| = \left|\frac{3}{-1}\right| = 3
$$

## Warunki równoległości i prostopadłości dwóch prostych

1. **Równoległość**: Proste są równoległe, gdy ich współczynniki kierunkowe są równe: $m_1 = m_2$.

   **Przykład**: Proste $y = 2x + 3$ i $y = 2x - 5$ są równoległe.

2. **Prostopadłość**: Proste są prostopadłe, gdy iloczyn ich współczynników kierunkowych wynosi $-1$: $m_1 \cdot m_2 = -1$.

   **Przykład**: Proste $y = 2x + 1$ i $y = -\frac{1}{2}x + 4$ są prostopadłe.

## Zadania

**Zadanie 1:** Znajdź równanie prostej przechodzącej przez punkt $(3, 4)$, która jest równoległa do prostej $2x - y + 5 = 0$.

**Rozwiązanie:**

Równanie prostej ma formę $2x - y + c = 0$. Podstawiając punkt $(3, 4)$:

$$
2 \times 3 - 4 + c = 0 \implies c = -2
$$

Równanie prostej: $2x - y - 2 = 0$.

**Zadanie 2:** Wyznacz kąt między prostymi $y = 3x + 2$ i $y = -\frac{1}{3}x + 1$.

**Rozwiązanie:**

$$
\tan \theta = \left|\frac{3 - (-\frac{1}{3})}{1 + 3 \cdot (-\frac{1}{3})}\right| = \left|\frac{3 + \frac{1}{3}}{0}\right| = \infty
$$

**Zadanie 3:** Znajdź punkt przecięcia prostych $x + 2y = 5$ i $2x - y = 4$.

**Rozwiązanie:**

Rozwiązujemy układ równań:

$$
x + 2y = 5 \quad (1)
$$

$$
2x - y = 4 \quad (2)
$$

Z (1): $x = 5 - 2y$. Podstawiamy do (2):

$$
2(5 - 2y) - y = 4 \implies 10 - 4y - y = 4 \implies 5y = 6 \implies y = \frac{6}{5}, x = 5 - 2 \times \frac{6}{5} = \frac{7}{5}
$$

Punkt przecięcia to $(\frac{7}{5}, \frac{6}{5})$.

