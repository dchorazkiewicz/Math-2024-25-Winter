<style>
h2 {
    color: brown;
}

h3 {
    color: tomato;
}

</style>


# Wektory

## Definicja wektorów
Wektory są wielkościami, które posiadają zarówno wartość liczbową, jak i kierunek oraz zwrot w przestrzeni. 

Są one używane do opisu różnych wielkości fizycznych, takich jak prędkość, siła, czy natężenie pola elektrycznego. W przeciwieństwie do skalarów, które mają tylko wartość liczbową (np. masa, temperatura), wektory wymagają określenia kierunku.

W notacji:
- Wektor oznaczamy strzałką nad symbolem, np. $\vec{a}$, lub pogrubioną czcionką, np. **a**.
- Długość wektora można zapisać jako $|\vec{a}|$ lub $a$.
- Wektor o długości 1 nazywa się wektorem jednostkowym (wersorem) i zapisuje się jako $\hat{a}= \frac{\vec{a}}{|\vec{a}|}$.

**Przykład:**

- Wektor $\vec{a} = (3, 4)$ ma długość $|\vec{a}| = 5$ i odpowiadający wersor (jednostkowy wektor wzdłuż kierunku wektora $\vec{a}$) wyrażony jest przez $\hat{a} = \left(\frac{3}{5}, \frac{4}{5}\right)$.
## Długość wektora
Długość (moduł) wektora oblicza się za pomocą wzoru Pitagorasa.

**Wektory w 2D:**
Jeśli $\vec{a} = (a_x, a_y)$, to długość jest dana wzorem:
$$
|\vec{a}| = \sqrt{a_x^2 + a_y^2}
$$

**Przykład:**
Dla wektora $\vec{a} = (3, 4)$, długość wynosi:
$$
|\vec{a}| = \sqrt{3^2 + 4^2} = \sqrt{9 + 16} = 5
$$

**Wektory w 3D:**
Jeśli $\vec{a} = (a_x, a_y, a_z)$, to długość wektora wynosi:
$$
|\vec{a}| = \sqrt{a_x^2 + a_y^2 + a_z^2}
$$

**Przykład:**
Dla wektora $\vec{a} = (1, 2, 2)$, długość wynosi:
$$
|\vec{a}| = \sqrt{1^2 + 2^2 + 2^2} = \sqrt{1 + 4 + 4} = 3
$$

## Rozróżnienie między wektorami i skalarami
- **Wektory:** mają wielkość, kierunek i zwrot (np. siła, prędkość).
- **Skalary:** mają tylko wielkość (np. masa, temperatura).

## Reprezentacja we współrzędnych kartezjańskich
Wektory można reprezentować za pomocą składowych w układzie kartezjańskim.

**Wektory w 2D:**
$\vec{a} = (a_x, a_y)$

**Wektory w 3D:**
$\vec{a} = (a_x, a_y, a_z)$

Wektory bazowe $\hat{i}$, $\hat{j}$, $\hat{k}$ odpowiadają odpowiednio osiom x, y, z. Dowolny wektor można zapisać jako:
$$
\vec{a} = a_x\hat{i} + a_y\hat{j} + a_z\hat{k}
$$

## Notacje
- **Notacja wektorowa:** $\vec{a} = (a_x, a_y, a_z)$
- **Wektory jednostkowe:** $\hat{i}$, $\hat{j}$, $\hat{k}$

## Rzutowanie wektora na oś
Rzutowanie wektora $\vec{a}$ na oś wyznaczoną przez wektor $\vec{b}$:
$$
\text{Rzut} = \frac{\vec{a} \cdot \vec{b}}{|\vec{b}|}
$$

**Przykład:** 
Dla $\vec{a} = (1, 2)$ i $\vec{b} = (2, 0)$:

Rzut wektora $\vec{a}$ na oś x:
$$
\text{Rzut}_x = \frac{(1, 2) \cdot (2, 0)}{|(2, 0)|} = \frac{1 \times 2 + 2 \times 0}{\sqrt{2^2 + 0^2}} = \frac{2}{2} = 1
$$

Rzut wektora $\vec{a}$ na oś y:
$$
\text{Rzut}_y = \frac{(1, 2) \cdot (0, 1)}{|(0, 1)|} = \frac{1 \times 0 + 2 \times 1}{\sqrt{0^2 + 1^2}} = \frac{2}{1} = 2
$$

## Dzielenie odcinka w określonym stosunku
Dzieląc odcinek między punktami $A=(x_1, y_1)$ a $B=(x_2, y_2)$ w stosunku $m:n$, punkt $P$ jest dany przez:
$$
P=\left(\frac{mx_2 + nx_1}{m+n}, \frac{my_2 + ny_1}{m+n}\right)
$$

## Operacje liniowe na wektorach

Dodawanie wektorów polega na dodawaniu odpowiednich składowych:
$$
\vec{a} + \vec{b} = (a_x + b_x, a_y + b_y, a_z + b_z)
$$

**Przykład:**
Dla $\vec{a} = (1, 2)$ i $\vec{b} = (3, 4)$:
$$
\vec{a} + \vec{b} = (1 + 3, 2 + 4) = (4, 6)
$$


Mnożenie wektora przez liczbę skalar $m$ zmienia jego długość, ale nie kierunek:
$$
m\vec{a} = (ma_x, ma_y, ma_z)
$$

**Przykład:**
Dla $\vec{a} = (2, -1)$ i $m = 3$:
$$
3\vec{a} = (3 \cdot 2, 3 \cdot (-1)) = (6, -3)
$$

## Baza. Znajdowanie współrzędnych wektora w nowej bazie

**Baza** to zestaw wektorów jednostkowych, które definiują przestrzeń i pozwalają reprezentować dowolny wektor w tej przestrzeni. W standardowym układzie kartezjańskim w 3D używamy bazy $\{\hat{i}, \hat{j}, \hat{k}\}$, które odpowiadają osiom $x$, $y$, $z$. Każdy wektor $\vec{a}$ można zapisać jako kombinację liniową tych wektorów bazowych:

$$
\vec{a} = a_x\hat{i} + a_y\hat{j} + a_z\hat{k}
$$

**Znajdowanie współrzędnych wektora w nowej bazie** wymaga transformacji współrzędnych za pomocą macierzy przejścia z jednej bazy do drugiej. Jeśli mamy nową bazę $\{\vec{e_1}, \vec{e_2}, \vec{e_3}\}$, możemy przekształcić współrzędne wektora, używając macierzy zawierającej te wektory bazowe jako kolumny. Proces ten umożliwia analizę wektorów w kontekście bardziej dogodnym do danego problemu (np. w bazie ortogonalnej lub ukośnej).

### Przykład:
Dany jest wektor $\vec{a} = (1, 2, 3)$ oraz nowa baza $\{\vec{e_1}, \vec{e_2}, \vec{e_3}\}$, gdzie:

$$
\vec{e_1} = (1, 0, 1), \quad \vec{e_2} = (1, 0, -1), \quad \vec{e_3} = (0, 1, 0)
$$

Aby znaleźć współrzędne wektora $\vec{a}$ w nowej bazie, musimy rozwiązać układ równań:

$$
\begin{bmatrix} 1 & 1 & 0 \\ 0 & 0 & 1 \\ 1 & -1 & 0 \end{bmatrix} \begin{bmatrix} x \\ y \\ z \end{bmatrix} = \begin{bmatrix} 1 \\ 2 \\ 3 \end{bmatrix}
$$

Rozwiązanie to $x = 2$, $y = 3$, $z = 1$.

## Baza ortonormalna

**Baza ortonormalna** to baza, w której wszystkie wektory bazowe są jednostkowe (wielkości 1) i prostopadłe do siebie. W bazie ortonormalnej iloczyn skalarny dwóch różnych wektorów bazowych wynosi zero, a iloczyn skalarny wektora bazowego z samym sobą wynosi jeden.

**Przykład:**

Dla bazy ortonormalnej $\{\hat{i}, \hat{j}, \hat{k}\}$:

$$
\hat{i} = (1, 0, 0), \quad \hat{j} = (0, 1, 0), \quad \hat{k} = (0, 0, 1)
$$

W tej bazie iloczyn skalarny dwóch różnych wektorów bazowych wynosi zero, a iloczyn skalarny wektora bazowego z samym sobą wynosi jeden:

Rozwiązując ten układ równań, otrzymujemy współrzędne wektora $\vec{a}$ w nowej bazie.

## Iloczyn skalarny dwóch wektorów, jego własności i zastosowania

**Iloczyn skalarny** (dot product) to operacja mnożenia dwóch wektorów, której wynikiem jest skalar. Definicja iloczynu skalarnego dwóch wektorów $\vec{a}$ i $\vec{b}$ jest dana wzorem:

$$
\vec{a} \cdot \vec{b} = |\vec{a}| |\vec{b}| \cos \theta
$$

gdzie $\theta$ jest kątem między wektorami. Alternatywnie, iloczyn skalarny można wyrazić za pomocą ich składowych:

$$
\vec{a} \cdot \vec{b} = a_xb_x + a_yb_y + a_zb_z
$$

**Własności:**
- Iloczyn skalarny jest przemienny: $\vec{a} \cdot \vec{b} = \vec{b} \cdot \vec{a}$.
- Jeśli $\vec{a} \cdot \vec{b} = 0$, wektory są prostopadłe.

**Zastosowania:**
- Obliczanie kąta między wektorami wg wzoru $\cos \theta = \frac{\vec{a} \cdot \vec{b}}{|\vec{a}| |\vec{b}|}$.
- Sprawdzanie prostopadłości.
- Znajdowanie rzutów wektorów na inne wektory wg wzoru $\text{Rzut} = \frac{\vec{a} \cdot \vec{b}}{|\vec{b}|}$.
- W fizyce: obliczanie pracy wykonanej przez siłę $\vec{F}= (F_x, F_y, F_z)$ działającą wzdłuż przemieszczenia $\vec{d}= (d_x, d_y, d_z)$ wg wzoru $W = \vec{F} \cdot \vec{d}= |\vec{F}| |\vec{d}| \cos \theta= F_xd_x + F_yd_y + F_zd_z$.

## Iloczyn wektorowy wektorów, jego własności i zastosowania

**Iloczyn wektorowy** (cross product) dwóch wektorów $\vec{a}$ i $\vec{b}$ daje nowy wektor $\vec{c}$, który jest prostopadły do płaszczyzny wyznaczonej przez $\vec{a}$ i $\vec{b}$. Długość $\vec{c}$ jest dana wzorem:

$$
|\vec{c}| = |\vec{a}| |\vec{b}| \sin \theta
$$

gdzie $\theta$ jest kątem między wektorami. Kierunek wektora $\vec{c}$ określa reguła prawej dłoni.

**Definicja:**
Iloczyn wektorowy dwóch wektorów $\vec{a} = (a_x, a_y, a_z)$ i $\vec{b} = (b_x, b_y, b_z)$ jest dany wzorem w ktrym widać cykliczną permutację składowych wektorów $(x\to y \to z \to x)$:
$$
\vec{c}=\vec{a} \times \vec{b} = (a_yb_z - a_zb_y, a_zb_x - a_xb_z, a_xb_y - a_yb_x)=(c_x, c_y, c_z)
$$
lub w postaci wyznacznikowej
$$
\vec{a} \times \vec{b} = \begin{vmatrix} \hat{i} & \hat{j} & \hat{k} \\ a_x & a_y & a_z \\ b_x & b_y & b_z \end{vmatrix}
$$

Trochę to zabawne, że aby policzyć iloczyny wektorowy i otrzymać finalny wektor używamy wyznacznika (skalara) z macierzy (tensor drugiego rzędu), wierszami której są wektory bazowe (wektory) i składowe wektorów (skalary).

**Własności:**
- Iloczyn wektorowy jest antyprzemienny: $\vec{a} \times \vec{b} = -\vec{b} \times \vec{a}$.
- Iloczyn wektorowy dwóch równoległych wektorów wynosi zero: $\vec{a} \times \vec{b} = 0$ dla $\vec{a} \parallel \vec{b}$.
- Jest rozdzielny względem dodawania: $\vec{a} \times (\vec{b} + \vec{c}) = \vec{a} \times \vec{b} + \vec{a} \times \vec{c}$.

**Zastosowania:**
- W fizyce: moment siły (moment obrotowy) to iloczyn wektorowy wektora siły i ramienia $\vec{M} = \vec{r} \times \vec{F}$.
- Obliczanie pola równoległoboku rozpiętego na dwóch wektorach $Area=\vec{a} \times \vec{b} = |\vec{a}| |\vec{b}| \sin \theta$
- Obliczanie pola trójkąta rozpiętego na dwóch wektorach $\vec{a}$ i $\vec{b}$: $Area = \frac{1}{2} |\vec{a} \times \vec{b}|$.

## Iloczyn mieszany wektorów, jego własności i zastosowania

**Iloczyn mieszany** (triple product) trzech wektorów $\vec{a}$, $\vec{b}$ i $\vec{c}$ to iloczyn skalarny jednego z wektorów z iloczynem wektorowym pozostałych dwóch:

$$
\vec{a} \cdot (\vec{b} \times \vec{c})
$$

Wartość bezwzględna tego wyrażenia jest równa objętości równoległościanu rozpiętego na wektorach $\vec{a}$, $\vec{b}$ i $\vec{c}$.

**Własności:**
- Iloczyn mieszany jest przemienny względem cyklicznych permutacji: $\vec{a} \cdot (\vec{b} \times \vec{c}) = \vec{b} \cdot (\vec{c} \times \vec{a}) = \vec{c} \cdot (\vec{a} \times \vec{b})$.
- Jest równy zeru, jeśli wektory są współpłaszczyznowe.

**Obliczanie objętości równoległościanów i czworościanów**

Iloczyn mieszany wektorów jest używany do obliczania objętości równoległościanów i czworościanów. Dla trzech wektorów $\vec{a}$, $\vec{b}$ i $\vec{c}$, objętość równoległościanu jest dana wzorem:

$$
V = |\vec{a} \cdot (\vec{b} \times \vec{c})|
$$
(uwaga: | | oznacza tutaj wartość bezwzględną, a nie długość!)

**Sprawdzanie współpłaszczyznowości trzech wektorów.**

Jeśli iloczyn mieszany trzech wektorów jest równy zeru, oznacza to, że wektory są współpłaszczyznowe. W przeciwnym razie, tworzą one czworościan.
