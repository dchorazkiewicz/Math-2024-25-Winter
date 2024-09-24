# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.16.4
#   kernelspec:
#     display_name: .venv
#     language: python
#     name: python3
# ---

# # Równania w matematyce
#
# ## Definicja równania
#
# **Równanie** w matematyce to formalne wyrażenie, które określa, że dwie wartości bądź wyrażenia są sobie równe. Składa się z dwóch części: lewej i prawej strony, oddzielonych znakiem równości "=". Celem rozwiązywania równań jest znalezienie wartości zmiennych, które sprawiają, że obie strony równania mają tę samą wartość.
#
#

#
# **Przykład 1**
#
# Rozpatrzmy równanie $2x + 3 = 7$. W tym przypadku mamy jedną zmienną $x$. Rozwiązując równanie, chcemy znaleźć wartość $x$, dla której lewa strona równania jest równa prawej stronie. Czyli rozwiązanie równania jest to zbiór
#
# $$
# \{x \in \mathbb{R} : 2x + 3 = 7\} = \{x \in \mathbb{R} : x = 2\}= \{2\}
# $$
#
# co czytamy jako "zbiór wszystkich liczb rzeczywistych $x$, dla których $2x + 3$ jest równe $7$".
#
#

#
#
# **Przykład 2**
#
# Rozpatrzmy równanie $x^2 - 4 = 0$. W tym przypadku mamy jedną zmienną $x$. Rozwiązując równanie, chcemy znaleźć wartość $x$, dla której lewa strona równania jest równa prawej stronie. Czyli rozwiązanie równania jest to zbiór
#
# $$
# \{x \in \mathbb{R} : x^2 - 4 = 0\}= \{x \in \mathbb{R} : x^2 = 4\} = \{x \in \mathbb{R} : x = 2 \lor x = -2\} = \{2, -2\}
# $$
#
# co czytamy jako "zbiór wszystkich liczb rzeczywistych $x$, dla których $x^2$ jest równe $4$" czyli $x = 2$ lub $x = -2$.
#
#

#
#
# **Przykład 3**
#
# Prosta równań $y=2x+1$ jest równaniem liniowym. W tym przypadku mamy dwie zmienne $x$ i $y$. Rozwiązując równanie, chcemy znaleźć wartości $x$ i $y$, dla których lewa strona równania jest równa prawej stronie. Czyli rozwiązanie równania jest to zbiór
#
# $$
# \{(x, y) \in \mathbb{R}^2 : (x \in \mathbb{R}) \land (y = 2x + 1)\} = \{(x, 2x + 1) : x \in \mathbb{R}\}
# $$
#
#

#
#
# **Przykład 4**
#
# Czasami mamy do czynienia z równaniami uwikłanymi $F(x,y)$, które nie można zapisać w postaci $y=f(x)$ lub $x=f(y)$. Rozwiązanie rówania tak jak wyżej sprowadza się do znaleznienia wszystkich par $(x,y)$ spełniających równanie $F(x,y)$ co zapisujemy
#
# $$
# \{(x, y) \in \mathbb{R}^2 : F(x, y) = 0\}
# $$
#
# Równanie okręgu $x^2 + y^2 = 1$ jest przykładem równania uwikłanego. Poszuakjmy jego rozwiązania.
# Rozpatrzmy następujące równości
#
# $$
# \begin{cases}
# y_1=+\sqrt{1-x^2}\quad \text{gdzie } x\in[-1,1]\\
# y_1=-\sqrt{1-x^2}\quad \text{gdzie } x\in[-1,1]\\
# \end{cases}
# $$
#
# w oby przypadkach mamy $y_1^2=1-x^2$ czyli $x^2+y_1^2=1$. Stąd rozwiązaniem równania $x^2+y^2=1$ jest zbiór
#
# $$
# \{(x, y) \in \mathbb{R}^2 : x^2 + y^2 = 1\} = \{(x, \sqrt{1-x^2}) : x \in [-1, 1]\}\cup\{(x,-\sqrt{1-x^2})) : x \in [-1, 1]\}
# $$

# # Teraz zobaczymy jak możemy manipulować równaniami w Pythonie

# Jeśli odwołamy się do zmiennej niezdefiniowanej w funkcji, to Python zwróci błąd
z

# możemy zdefiniować zmienną z
z = 10
z

# możeny dodać 1 do z
z = z + 1
z

# Problem z takim podejściem że nie pozwala nam na manipulowaniem symbolami! Powyższa definicja przypisuje do symbolu wartość numeryczną a nie symboliczną. W Pythonie mamy do dyspozycji bibliotekę `sympy` która pozwala na manipulowanie symbolami.
# Poniżej wprowadzimy kilka przykładów jak możemy manipulować symbolami, równaniami w Pythonie.

# +
# Najpierw wczytujemy bibliotekę sympy (Symbolic Python)
import sympy as sp

# Definiujemy zmienne x i y jako symbole
x, y = sp.symbols('x y')
# -

x # x jest teraz symbolem

x+y # Python zwraca x + y jako wyrażenie nie jako wartość liczbową

# Możemy wykonywać bardziej skomplikowane operacje na zmiennych
expr1 = (x+y)**2
expr1

# Możemy rozwinąć powyższe wyrażenie
sp.expand(expr1)

# a co w przypadku jeszcze bardziej skomplikowanych wyrażeń?
expr2=(x+y)**5
expr2

expr2_expanded = sp.expand(expr2)
expr2_expanded

# możemy podstawić konkretne wartości do zmiennych np x=2
expr2_expanded.subs(x,2)

# W sympy możemy definiować równania
eq1 = sp.Eq(x**2, 1)
eq1

# możemy zapytać o rozwiązania równania
sol_eq1 = sp.solve(eq1)
sol_eq1

# przykład równania kwadratowego
eq2 = sp.Eq(x**2 - 4*x + 3, 0)
eq2

# rozwiązania równania kwadratowego
sol_eq2 = sp.solve(eq2)
sol_eq2

# równanie kwadratowe z dwoma niewiadomymi
eq3 = sp.Eq(x**2 + y**2, 1)
eq3

# rozwiązania równania kwadratowego z dwoma niewiadomymi
sol_eq3 = sp.solve(eq3,y) # rozwiązania równania z y jako funkcja od x
sol_eq3

# możemy wyświetlić rozwiązania równania w bardziej czytelny sposób
sol_eq3[0]


sol_eq3[1]

import matplotlib.pyplot as plt
plt.rcParams['figure.figsize'] = [3, 3] # ustawienie rozmiaru wykresu oraz aspect_ratio=1
# Możemy również narysować rozwiązania równania na płaszczyźnie aspect_ratio=1
sp.plot_implicit(eq3, (x, -2, 2), (y, -2, 2))

ellipse = sp.Eq(x**2/4 + y**2, 1)
ellipse

# Możemy również narysować rozwiązania równania na płaszczyźnie aspect_ratio=1
sp.plot_implicit(ellipse, (x, -3, 3), (y, -3, 3))

# +
prosta = sp.Eq(y, 2*x-1)
okrag = sp.Eq(x**2 + y**2, 1)
# Rysowanie okręgu i elipsy na jednym wykresie
p1 = sp.plot_implicit(prosta, (x, -2, 2), (y, -2, 2), show=False)
p2 = sp.plot_implicit(okrag, (x, -2, 2), (y, -2, 2), show=False)

# Dodanie wykresów do jednego
p1.extend(p2)
p1.show()
# -

# Zobaczmy gdzie przecinają się okrąg i prosta
sp.solve([prosta, okrag])

# +
# Jak sprawdzić czy dwa równania są równoważne?
# zapiszemy to samo w innej postaci

r1=sp.Eq(x + y, 1)
r1

# -

r2=sp.Eq(2*x - 2, -2*y)
r2

# Nie możemy porównać w sposób naturalny dwóch równań, ale możemy sprawdzić czy są równoważne
r1==r2

# Ale jeśli zrobimy wyrażenie
ratio=(r1.lhs-r1.rhs)/(r2.lhs-r2.rhs)
ratio

# stała oznacza, że równania są równoważne
sp.simplify(ratio) 

# Możemy definiować funkcje
f=(x+1)**2
g=sp.sin(x)

# Możemy wyświetlić funkcje
f

# Możemy dodać funkcje
f+g

# Możemy różniczkować funkcje
f.diff(x)

# Możemy całkować funkcje
f.integrate(x)

# możemy rysoać funkcje
sp.plot(g, (x, -5, 5))

# Możemy też definiować ogólne funkcje
f, g = sp.symbols('f g', cls=sp.Function)
f(x)+g(x)


# możemy zobaczyć jedną z reguł całkowania
sp.expand(sp.integrate(f(x)+g(x), x))


