# Geometria 1

### 1. Równanie ogólne prostej

#### a) Formalne
```python
# Równanie ogólne prostej: Ax + By + C = 0
from sympy import symbols, Eq, solve

# Definiowanie symboli
x, y, A, B, C = symbols('x y A B C')

# Równanie prostej
rownanie = Eq(A*x + B*y + C, 0)

# Rozwiązywanie równania względem y
rownanie_y = solve(rownanie, y)
rownanie_y  # wyświetla równanie prostej w zależności od parametrów
```

#### b) Konkretne wartości
```python
# Równanie prostej: 2x - 3y + 6 = 0
from sympy import symbols, Eq, solve

x, y = symbols('x y')

# Konkretne równanie
rownanie = Eq(2*x - 3*y + 6, 0)

# Rozwiązywanie równania względem y
roz = solve(rownanie, y)
roz
```

#### c) Nietrywialne
```python
# Wyznaczanie punktu przecięcia prostej z osiami układu współrzędnych
from sympy import symbols, Eq, solve

x, y = symbols('x y')

# Równanie prostej: 5x - 4y + 20 = 0
rownanie = Eq(5*x - 4*y + 20, 0)

# Punkt przecięcia z osią OX (y=0)
punkt_OX = solve(rownanie.subs(y, 0), x)

# Punkt przecięcia z osią OY (x=0)
punkt_OY = solve(rownanie.subs(x, 0), y)

punkt_OX, punkt_OY
```

### 2. Równanie kanoniczne prostej

#### a) Formalne
```python
# Równanie kanoniczne: (x - x0)/a = (y - y0)/b
from sympy import symbols, Eq

x, y, x0, y0, a, b = symbols('x y x0 y0 a b')

# Równanie kanoniczne
rownanie_kanoniczne = Eq((x - x0)/a, (y - y0)/b)
rownanie_kanoniczne
```

#### b) Konkretne wartości
```python
# Równanie kanoniczne: (x - 1)/3 = (y - 2)/4
x, y = symbols('x y')

# Podstawienie wartości
rownanie = Eq((x - 1)/3, (y - 2)/4)
rownanie
```

#### c) Nietrywialne
```python
# Znajdź równanie kanoniczne prostej przechodzącej przez punkt (3, 4) w kierunku wektora (2, -1)
x, y = symbols('x y')

# Punkt (x0, y0) i wektor kierunkowy (a, b)
x0, y0 = 3, 4
a, b = 2, -1

# Równanie kanoniczne
rownanie = Eq((x - x0)/a, (y - y0)/b)
rownanie
```

### 3. Równanie prostej w odcinkach na osiach

#### a) Formalne
```python
# Równanie w postaci odcinków: x/a + y/b = 1
from sympy import symbols, Eq

x, y, a, b = symbols('x y a b')

# Równanie prostej
rownanie_odcinki = Eq(x/a + y/b, 1)
rownanie_odcinki
```

#### b) Konkretne wartości
```python
# Równanie: x/2 + y/3 = 1
x, y = symbols('x y')

# Podstawienie
rownanie = Eq(x/2 + y/3, 1)
rownanie
```

#### c) Nietrywialne
```python
# Znajdź punkt przecięcia tej prostej z osiami, obliczając dokładne wartości
x, y = symbols('x y')

rownanie = Eq(x/2 + y/3, 1)

# Punkt przecięcia z osią OX (y=0)
punkt_OX = solve(rownanie.subs(y, 0), x)

# Punkt przecięcia z osią OY (x=0)
punkt_OY = solve(rownanie.subs(x, 0), y)

punkt_OX, punkt_OY
```

### 4. Równanie prostej ze współczynnikiem kątowym

#### a) Formalne
```python
# Równanie prostej: y = mx + c
from sympy import symbols, Eq

x, y, m, c = symbols('x y m c')

# Równanie prostej
rownanie_katowy = Eq(y, m*x + c)
rownanie_katowy
```

#### b) Konkretne wartości
```python
# Równanie: y = 2x + 5
x, y = symbols('x y')

# Podstawienie
rownanie = Eq(y, 2*x + 5)
rownanie
```

#### c) Nietrywialne
```python
# Oblicz współczynnik kierunkowy prostej przechodzącej przez punkty (1, 2) i (4, 10)
x1, y1, x2, y2 = 1, 2, 4, 10

# Obliczanie współczynnika kierunkowego m
m = (y2 - y1) / (x2 - x1)
m
```

### 5. Równanie prostej przechodzącej przez dany punkt w danym kierunku

#### a) Formalne
```python
# Równanie: (x - x0)/a = (y - y0)/b
from sympy import symbols, Eq

x, y, x0, y0, a, b = symbols('x y x0 y0 a b')

# Równanie prostej
rownanie = Eq((x - x0)/a, (y - y0)/b)
rownanie
```

#### b) Konkretne wartości
```python
# Równanie przechodzącej przez (2, 3) w kierunku (1, 2)
x, y = symbols('x y')

rownanie = Eq((x - 2)/1, (y - 3)/2)
rownanie
```

#### c) Nietrywialne
```python
# Oblicz równanie prostej, jeśli punkt (3, 4) jest dany, a kierunek to prosta y = 2x - 1
from sympy import solve

# Punkt (x0, y0)
x0, y0 = 3, 4

# Współczynnik kierunkowy z równania y = 2x - 1
m = 2

# Równanie: y - y0 = m(x - x0)
rownanie = Eq(y - y0, m*(x - x0))
rownanie
```

### 6. Równanie prostej przechodzącej przez dwa dane punkty

#### a) Formalne
```python
# Równanie: y - y1 = ((y2 - y1)/(x2 - x1)) * (x - x1)
from sympy import symbols, Eq

x, y, x1, y1, x2, y2 = symbols('x y x1 y1 x2 y2')

# Równanie prostej przez dwa punkty
m = (y2 - y1) / (x2 - x1)
rownanie = Eq(y - y1, m*(x - x1))
rownanie
```

#### b) Konkretne wartości
```python
# Równanie prostej przez punkty (1, 2) i (4, 6)
x, y = symbols('x y')

# Punkty
x1, y1 = 1, 2
x2, y2 = 4, 6

# Obliczenie współczynnika kierunkowego
m = (y2 - y1) / (x2 - x1)

# Równanie
rownanie = Eq(y - y1, m*(x - x1))
rownanie
```

#### c) Nietrywialne
```python
# Oblicz współrzędne punktu przecięcia dwóch prostych przechodzących przez różne pary punktów
from sympy import solve, Eq

x, y = symbols('x y')

# Prosta 1: przez punkty (1, 2) i (3, 6)
rownanie1 = Eq(y - 2, ((6 - 2)/(3 - 1)) * (x - 1))

# Prosta 2: przez punkty (0, 0) i (2, 3)
rownanie2 = Eq(y, (3/2) * x)

# Znajdowanie punktu przecięcia
punkt_przeciecia = solve((rownanie1, rownanie2), (x, y))
punkt_przeciecia
```
