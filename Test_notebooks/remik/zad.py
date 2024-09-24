## Zadania

# **Przykład 1**

# Znajdź punkty przecięcia dwóch okręgów o równaniach:
# $x^2 + y^2 = 1$
# $(x-1)^2 + y^2 = 1$
#i wyświetl je na wykresie.

import sympy as sp
import matplotlib.pyplot as plt
# Definiowanie symboli
x, y = sp.symbols('x y')
# Definiowanie równań okręgów
eq1 = x**2 + y**2 - 1  # Okrąg o środku (0, 0) i promieniu 1
eq2 = (x-1)**2 + y**2 - 1  # Okrąg o środku (1, 0) i promieniu 1
# Rozwiązanie układu równań
solutions = sp.solve((eq1, eq2), (x, y))
print("Rozwiązania:", solutions)

# Wyodrębnienie rzeczywistych rozwiązań
points = [(float(sol[0]), float(sol[1])) for sol in solutions if sol[0].is_real and sol[1].is_real]
# Rysowanie okręgów i punktów przecięcia
circle1 = plt.Circle((0, 0), 1, color='blue', fill=False, label=r'$x^2 + y^2 = 1$')
circle2 = plt.Circle((1, 0), 1, color='red', fill=False, label=r'$(x-1)^2 + y^2 = 1$')
# Tworzenie wykresu
fig, ax = plt.subplots()
ax.add_artist(circle1)
ax.add_artist(circle2)
# Rysowanie punktów przecięcia (bez powtarzania etykiet w legendzie)
for i, point in enumerate(points):
    label = 'Punkt przecięcia' if i == 0 else None  # Etykieta tylko dla pierwszego punktu
    ax.plot(point[0], point[1], 'go', label=label)  # 'go' oznacza zielony kolor i okrągły marker
# Ustawienie równych proporcji na wykresie
ax.set_aspect('equal')
ax.set_xlim(-1.5, 2.5)
ax.set_ylim(-1.5, 1.5)
ax.legend(loc='best')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Przecięcie dwóch okręgów')
plt.grid(True)
plt.show()






# **Przykład 2**


# Możemy wykonywać bardziej skomplikowane operacje na zmiennych
expr1 = (x+y)**2
expr1

# Możemy rozwinąć powyższe wyrażenie
sp.expand(expr1)
