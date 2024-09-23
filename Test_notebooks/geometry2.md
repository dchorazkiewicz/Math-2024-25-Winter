<style>
h2 {
    color: brown;
}

h3 {
    color: tomato;
}

</style>

# Krzywe drugiego rzędu

## Wprowadzenie

Krzywe drugiego rzędu, zwane także krzywymi stożkowymi, obejmują okręgi, elipsy, hiperbole i parabole. Są to krzywe, które można otrzymać jako przecięcie płaszczyzny z powierzchnią stożkową. Każda z tych krzywych ma swoje specyficzne równanie kanoniczne, które można przekształcić z ogólnej postaci za pomocą odpowiednich przesunięć i obrotów osi układu współrzędnych.

## Równania kanoniczne krzywych drugiego rzędu

### 1. Równanie kanoniczne okręgu

**Równanie okręgu** o środku w punkcie $(h, k)$ i promieniu $r$ ma postać:
$$
(x - h)^2 + (y - k)^2 = r^2
$$

**Przykład:**
Dla okręgu o środku w punkcie $(2, -3)$ i promieniu $4$, równanie to:
$$
(x - 2)^2 + (y + 3)^2 = 16
$$

### 2. Równanie kanoniczne elipsy

**Równanie elipsy** o półosiach $a$ (oś pozioma) i $b$ (oś pionowa), oraz środku w $(h, k)$ jest dane wzorem:
$$
\frac{(x - h)^2}{a^2} + \frac{(y - k)^2}{b^2} = 1
$$

**Przykład:**
Elipsa o półosiach $a = 3$ i $b = 2$, oraz środku w $(0, 0)$, ma równanie:
$$
\frac{x^2}{3^2} + \frac{y^2}{2^2} = 1
$$

### 3. Równanie kanoniczne hiperboli

**Równanie hiperboli** o półosiach $a$ (oś rzeczywista) i $b$ (oś urojona), oraz środku w $(h, k)$ jest dane wzorem:
$$
\frac{(x - h)^2}{a^2} - \frac{(y - k)^2}{b^2} = 1
$$

lub

$$
\frac{(y - k)^2}{b^2} - \frac{(x - h)^2}{a^2} = 1
$$

w zależności od orientacji osi.

**Przykład:**
Hiperbola o półosiach $a = 3$ i $b = 2$, oraz środku w $(0, 0)$ ma równanie:
$$
\frac{x^2}{3^2} - \frac{y^2}{2^2} = 1
$$

### 4. Równanie kanoniczne paraboli

**Równanie paraboli** o wierzchołku w $(h, k)$ i osi symetrii równoległej do osi $y$ jest dane wzorem:
$$
(y - k) = a(x - h)^2
$$

Dla paraboli o osi symetrii równoległej do osi $x$, równanie to:
$$
(x - h) = a(y - k)^2
$$

**Przykład:**
Parabola o wierzchołku $(1, -2)$ i otwierająca się w górę ma równanie:
$$
(y + 2) = 2(x - 1)^2
$$

## Równania krzywych drugiego rzędu z przesuniętym środkiem

Równania krzywych drugiego rzędu mogą być przesunięte względem środka układu współrzędnych. W takich przypadkach stosuje się przekształcenie współrzędnych, aby doprowadzić równanie do formy kanonicznej. Przesunięcie środka z $(0, 0)$ do $(h, k)$ powoduje zamianę zmiennych $x$ i $y$ na $x - h$ oraz $y - k$.

**Przykład:**
Równanie okręgu przesuniętego z $(0, 0)$ na $(2, -3)$:
$$
x^2 + y^2 = 16 \quad \text{staje się} \quad (x - 2)^2 + (y + 3)^2 = 16
$$

## Redukcja ogólnego równania krzywej drugiego rzędu do postaci kanonicznej

### Ogólne równanie krzywej drugiego rzędu

Ogólne równanie krzywej drugiego rzędu ma postać:
$$
Ax^2 + Bxy + Cy^2 + Dx + Ey + F = 0
$$

### Kroki redukcji do formy kanonicznej:

1. **Przesunięcie środka**: Przesunięcie współrzędnych, aby środek krzywej znajdował się w punkcie $(0, 0)$. 

   **Zmiana zmiennych:**
   $$
   x' = x - h, \quad y' = y - k
   $$

2. **Rotacja układu współrzędnych**: Obliczenie kąta rotacji $\theta$, aby wyeliminować człon mieszany $Bxy$.

   **Zmiana zmiennych:**
   $$
   x'' = x'\cos \theta - y'\sin \theta, \quad y'' = x'\sin \theta + y'\cos \theta
   $$

   Kąt $\theta$ oblicza się z równania:
   $$
   \tan 2\theta = \frac{B}{A - C}
   $$

3. **Sprowadzenie do postaci kanonicznej**: Po przesunięciu i rotacji, równanie przyjmuje jedną z form kanonicznych: okręgu, elipsy, hiperboli lub paraboli.

**Przykład:**

Rozważmy równanie $2x^2 + 3y^2 - 4x - 6y - 8 = 0$.

1. **Przesunięcie środka**:
   
   Znajdujemy nowe współrzędne środka poprzez przesunięcie.

2. **Rotacja układu**:

   W tym przypadku rotacja nie jest wymagana, ponieważ nie ma terminu $Bxy$.

3. **Redukcja**:

   Równanie zostaje uproszczone do postaci kanonicznej, która reprezentuje elipsę, hiperbolę lub parabolę, w zależności od wartości współczynników $A$, $B$, i $C$.

## Zadania

**Zadanie 1:** Sprowadź równanie $x^2 + 4xy + 4y^2 - 2x + 2y - 5 = 0$ do postaci kanonicznej.

**Rozwiązanie:**

1. Przesunięcie układu współrzędnych w celu wyeliminowania członów liniowych.

2. Obliczenie kąta obrotu i zastosowanie rotacji w celu wyeliminowania terminu $Bxy$.

3. Redukcja równania do postaci elipsy.

**Zadanie 2:** Wyznacz równanie okręgu przesuniętego o wektor $(3, -2)$ względem okręgu jednostkowego o równaniu $x^2 + y^2 = 1$.

**Rozwiązanie:**

Równanie przesuniętego okręgu to:
$$
(x - 3)^2 + (y + 2)^2 = 1
$$

**Zadanie 3:** Znajdź równanie paraboli przechodzącej przez punkt $(0, 0)$ z wierzchołkiem w punkcie $(2, -3)$ i otwierającej się w prawo.

**Rozwiązanie:**

Równanie paraboli ma postać:
$$
(x - 2) = a(y + 3)^2
$$

Podstawiając punkt $(0, 0)$, znajdujemy współczynnik $a$ i finalne równanie paraboli.

