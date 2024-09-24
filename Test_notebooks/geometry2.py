# Krzywe drugiego rzędu

# ## Wprowadzenie
# Krzywe drugiego rzędu, zwane także krzywymi stożkowymi, obejmują okręgi, elipsy, hiperbole i parabole.
# Są to krzywe, które można otrzymać jako przecięcie płaszczyzny z powierzchnią stożkową.

import numpy as np
import matplotlib.pyplot as plt

# ## Równania kanoniczne krzywych drugiego rzędu

# ### 1. Równanie kanoniczne okręgu
# **Równanie okręgu** o środku w punkcie (h, k) i promieniu r ma postać:
# (x - h)^2 + (y - k)^2 = r^2

# Przykład: Okrąg o środku w punkcie (2, -3) i promieniu 4
def plot_circle(h, k, r):
    theta = np.linspace(0, 2 * np.pi, 100)
    x = h + r * np.cos(theta)
    y = k + r * np.sin(theta)
    plt.figure(figsize=(6, 6))
    plt.plot(x, y, label=f"Okrąg o środku ({h}, {k}) i promieniu {r}")
    plt.scatter([h], [k], color='red', label='Środek okręgu')
    plt.axhline(0, color='black', lw=0.5)
    plt.axvline(0, color='black', lw=0.5)
    plt.title("Wizualizacja okręgu")
    plt.legend()
    plt.grid(True)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.show()

# Wizualizacja przykładu okręgu
plot_circle(2, -3, 4)

# ### 2. Równanie kanoniczne elipsy
# **Równanie elipsy** o półosiach a (oś pozioma) i b (oś pionowa), oraz środku w (h, k):
# (x - h)^2/a^2 + (y - k)^2/b^2 = 1

# Przykład: Elipsa o półosiach a = 3 i b = 2, oraz środku w (0, 0)
def plot_ellipse(h, k, a, b):
    theta = np.linspace(0, 2 * np.pi, 100)
    x = h + a * np.cos(theta)
    y = k + b * np.sin(theta)
    plt.figure(figsize=(6, 6))
    plt.plot(x, y, label=f"Elipsa o półosiach {a}, {b}")
    plt.scatter([h], [k], color='red', label='Środek elipsy')
    plt.axhline(0, color='black', lw=0.5)
    plt.axvline(0, color='black', lw=0.5)
    plt.title("Wizualizacja elipsy")
    plt.legend()
    plt.grid(True)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.show()

# Wizualizacja przykładu elipsy
plot_ellipse(0, 0, 3, 2)

# ### 3. Równanie kanoniczne hiperboli
# **Równanie hiperboli** o półosiach a i b, oraz środku w (h, k):
# (x - h)^2/a^2 - (y - k)^2/b^2 = 1 lub (y - k)^2/b^2 - (x - h)^2/a^2 = 1

# Przykład: Hiperbola o półosiach a = 3 i b = 2, oraz środku w (0, 0)
def plot_hyperbola(h, k, a, b, horizontal=True):
    x = np.linspace(-10, 10, 400)
    if horizontal:
        y = np.sqrt((x - h) ** 2 / a ** 2 - 1) * b
    else:
        y = np.sqrt((x - h) ** 2 / b ** 2 - 1) * a
    
    plt.figure(figsize=(10, 6))
    plt.plot(x, y + k, label="Hiperbola (część dodatnia)")
    plt.plot(x, -y + k, label="Hiperbola (część ujemna)")
    plt.axhline(0, color='black', lw=0.5)
    plt.axvline(0, color='black', lw=0.5)
    plt.title("Wizualizacja hiperboli")
    plt.legend()
    plt.grid(True)
    plt.show()

# Wizualizacja przykładu hiperboli
plot_hyperbola(0, 0, 3, 2)

# ### 4. Równanie kanoniczne paraboli
# **Równanie paraboli** o wierzchołku w (h, k) i osi symetrii równoległej do osi y:
# (y - k) = a(x - h)^2

# Przykład: Parabola o wierzchołku (1, -2) i otwierająca się w górę
def plot_parabola(h, k, a, vertical=True):
    x = np.linspace(-10, 10, 400)
    if vertical:
        y = a * (x - h) ** 2 + k
    else:
        y = (x - h) / a + k
    
    plt.figure(figsize=(10, 6))
    plt.plot(x, y, label=f"Parabola o wierzchołku ({h}, {k})")
    plt.axhline(0, color='black', lw=0.5)
    plt.axvline(0, color='black', lw=0.5)
    plt.title("Wizualizacja paraboli")
    plt.legend()
    plt.grid(True)
    plt.show()

# Wizualizacja przykładu paraboli
plot_parabola(1, -2, 2)
