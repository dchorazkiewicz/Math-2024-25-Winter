<style>
h2 {
    color: brown;
}

h3 {
    color: tomato;
}

</style>

# Płaszczyzny i proste w przestrzeni

## Płaszczyzny w przestrzeni

Płaszczyzna w przestrzeni trójwymiarowej to zbiór punktów, które spełniają określone równanie. Płaszczyzny można opisywać różnymi rodzajami równań, w zależności od dostępnych informacji, takich jak punkty, przez które przechodzą, czy wektory normalne.

### 1. Równanie wektorowe płaszczyzny

**Równanie wektorowe** płaszczyzny określa zbiór punktów $\vec{r}$ w przestrzeni przy pomocy wektora normalnego $\vec{n}$ i punktu $\vec{r_0}$ leżącego na płaszczyźnie:
$$
\vec{r} = \vec{r_0} + s\vec{v_1} + t\vec{v_2}
$$
gdzie $\vec{v_1}$ i $\vec{v_2}$ są wektorami kierunkowymi płaszczyzny, a $s$ i $t$ są parametrami.

### 2. Równanie ogólne płaszczyzny

**Równanie ogólne płaszczyzny** ma postać:
$$
Ax + By + Cz + D = 0
$$
gdzie $A$, $B$, $C$ to współczynniki określające wektor normalny $\vec{n} = (A, B, C)$, a $D$ jest wyrazem wolnym.

**Przykład:**
Dla płaszczyzny danej równaniem $2x - 3y + z - 4 = 0$, wektor normalny to $\vec{n} = (2, -3, 1)$.

### 3. Równanie płaszczyzny przechodzącej przez trzy punkty

Równanie płaszczyzny przechodzącej przez trzy punkty $(x_1, y_1, z_1)$, $(x_2, y_2, z_2)$, $(x_3, y_3, z_3)$ można wyznaczyć, używając wyznacznika:
$$
\begin{vmatrix} x - x_1 & y - y_1 & z - z_1 \\ x_2 - x_1 & y_2 - y_1 & z_2 - z_1 \\ x_3 - x_1 & y_3 - y_1 & z_3 - z_1 \end{vmatrix} = 0
$$

**Przykład:**
Dla punktów $(1, 0, 0)$, $(0, 1, 0)$, $(0, 0, 1)$, równanie płaszczyzny to:
$$
x + y + z = 1
$$

### 4. Równanie płaszczyzny w odcinkach na osiach współrzędnych

Jeśli płaszczyzna przecina osie współrzędnych w punktach $(a, 0, 0)$, $(0, b, 0)$, $(0, 0, c)$, jej równanie ma postać:
$$
\frac{x}{a} + \frac{y}{b} + \frac{z}{c} = 1
$$

**Przykład:**
Dla $a = 2$, $b = 3$, $c = 4$, równanie płaszczyzny to:
$$
\frac{x}{2} + \frac{y}{3} + \frac{z}{4} = 1
$$

## Szczególne przypadki położenia płaszczyzn

1. **Płaszczyzny równoległe**: Mają równoległe wektory normalne, tj. $\vec{n_1} \parallel \vec{n_2}$.
2. **Płaszczyzny prostopadłe**: Wektory normalne są prostopadłe, tj. $\vec{n_1} \cdot \vec{n_2} = 0$.

## Kąt między dwiema płaszczyznami

Kąt $\theta$ między dwiema płaszczyznami z wektorami normalnymi $\vec{n_1} = (A_1, B_1, C_1)$ i $\vec{n_2} = (A_2, B_2, C_2)$ wyraża wzór:
$$
\cos \theta = \frac{\vec{n_1} \cdot \vec{n_2}}{|\vec{n_1}| |\vec{n_2}|}
$$

**Przykład:**
Dla $\vec{n_1} = (2, -3, 1)$ i $\vec{n_2} = (1, 4, -2)$:
$$
\cos \theta = \frac{2 \cdot 1 + (-3) \cdot 4 + 1 \cdot (-2)}{\sqrt{2^2 + (-3)^2 + 1^2} \cdot \sqrt{1^2 + 4^2 + (-2)^2}} = \frac{-14}{\sqrt{14} \cdot \sqrt{21}}
$$

## Warunki równoległości i prostopadłości dwóch płaszczyzn

- **Równoległość**: $\vec{n_1} \parallel \vec{n_2}$.
- **Prostopadłość**: $\vec{n_1} \cdot \vec{n_2} = 0$.

## Prosta w przestrzeni

### Rodzaje równań prostej w przestrzeni

1. **Równanie parametryczne**: Prosta przechodząca przez punkt $(x_0, y_0, z_0)$ i mająca kierunek $\vec{d} = (a, b, c)$ ma równanie:
   $$
   \vec{r}(t) = \vec{r_0} + t\vec{d}
   $$

2. **Równanie wektorowe**: Prosta opisana przy pomocy wektora kierunkowego $\vec{d}$ i punktu początkowego $\vec{r_0}$:
   $$
   \vec{r} = \vec{r_0} + t\vec{d}
   $$

3. **Równanie kanoniczne**: Zależność między współrzędnymi punktów na prostej:
   $$
   \frac{x - x_0}{a} = \frac{y - y_0}{b} = \frac{z - z_0}{c}
   $$

### Względne położenie prostej i płaszczyzny, dwóch prostych

1. **Prosta i płaszczyzna równoległe**: Jeśli wektor kierunkowy prostej jest prostopadły do wektora normalnego płaszczyzny.
2. **Prosta leży w płaszczyźnie**: Jeśli punkt prostej spełnia równanie płaszczyzny.
3. **Proste równoległe**: Mają proporcjonalne wektory kierunkowe.
4. **Proste przecinające się**: Punkt wspólny spełnia równania obu prostych.
5. **Proste skośne**: Nie są równoległe ani nie przecinają się.

### Kąt między prostą a płaszczyzną

Kąt $\theta$ między prostą z wektorem kierunkowym $\vec{d}$ a płaszczyzną z wektorem normalnym $\vec{n}$ oblicza się ze wzoru:
$$
\sin \theta = \frac{|\vec{d} \cdot \vec{n}|}{|\vec{d}| |\vec{n}|}
$$

---

# Powierzchnie drugiego rzędu

Powierzchnie drugiego rzędu, takie jak elipsoidy, kule, hiperboloidy i paraboloidy, są trójwymiarowymi odpowiednikami krzywych stożkowych. Ich równania opisują różnorodne kształty spotykane w geometrii analitycznej i fizyce.

## Równania ogólne powierzchni drugiego rzędu

### 1. Elipsoida

**Równanie elipsoidy** o półosiach $a$, $b$, $c$ i środku w $(h, k, l)$ ma postać:
$$
\frac{(x - h)^2}{a^2} + \frac{(y - k)^2}{b^2} + \frac{(z - l)^2}{c^2} = 1
$$

**Przykład:**
Elipsoida z półosiami $a = 3$, $b = 2$, $c = 1$ ma równanie:
$$
\frac{x^2}{9} + \frac{y^2}{4} + z^2 = 1
$$

### 2. Kula

**Równanie kuli** o promieniu $r$ i środku w $(h, k, l)$:
$$
(x - h)^2 + (y - k)^2 + (z - l)^2 = r^2
$$

**Przykład:**
Kula o środku $(0, 0, 0)$ i promieniu $5$:
$$
x^2 + y^2 + z^2 = 25
$$

### 3. Hiperboloid

**Równanie hiperboloidy jednopowłokowej**:
$$
\frac{x^2}{a^2} + \frac{y^2}{b^2} - \frac{z^2}{c^2} = 1
$$

**Równanie hiperboloidy dwupowłokowej**:
$$
\frac{x^2}{a^2} - \frac{y^2}{b^2} - \frac{z^2}{c^2} = 1
$$

## Powierzchnie obrotowe

Powierzchnie obrotowe powstają przez obrót krzywej wokół osi. Przykłady obejmują paraboloidy, hiperboloidy obrotowe oraz powierzchnie stożkowe.

**Przykład:**
Paraboloida obrotowa opisana równaniem:
$$
z = x^2 + y^2
$$
powstaje przez obrót paraboli wokół osi z.

## Zadania

**Zadanie 1:** Znajdź równanie płaszczyzny przechodzącej przez punkty $(1, 0, 0)$, $(0, 2, 0)$, $(0, 0, 3)$.

**Rozwiązanie:**
Używamy równania wyznacznika:
$$
\begin{vmatrix} x - 1 & y & z \\ -1 & 2 & 0 \\ -1 & 0 & 3 \end{vmatrix} = 0 \implies x + y + z = 1
$$

**Zadanie 2:** Wyznacz kąt między prostą $x = 1 + 2t$, $y = 3 - t$, $z = -2 + 4t$ a płaszczyzną $x - y + z = 5$.

**Rozwiązanie:**
Wektor kierunkowy prostej $\vec{d} = (2, -1, 4)$, wektor normalny płaszczyzny $\vec{n} = (1, -1, 1)$. Kąt między prostą a płaszczyzną:
$$
\sin \theta = \frac{|2 \times 1 + (-1) \times (-1) + 4 \times 1|}{\sqrt{2^2 + (-1)^2 + 4^2} \cdot \sqrt{1^2 + (-1)^2 + 1^2}}
$$

**Zadanie 3:** Znajdź równanie elipsoidy z półosiami $4$, $3$, i $2$, przesuniętej o $(1, -1, 1)$.

**Rozwiązanie:**
Równanie elipsoidy to:
$$
\frac{(x - 1)^2}{16} + \frac{(y + 1)^2}{9} + \frac{(z - 1)^2}{4} = 1
$$
