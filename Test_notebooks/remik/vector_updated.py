
# Wektory

## Definicja wektorów
# Wektory są wielkościami, które posiadają zarówno wartość liczbową, jak i kierunek oraz zwrot w przestrzeni. 
# Są one używane do opisu różnych wielkości fizycznych, takich jak prędkość, siła, czy natężenie pola elektrycznego. 
# W przeciwieństwie do skalarów, które mają tylko wartość liczbową (np. masa, temperatura), wektory wymagają określenia kierunku.
#
# W notacji:
# - Wektor oznaczamy strzałką nad symbolem, np. \vec{a}, lub pogrubioną czcionką, np. **a**.
# - Długość wektora można zapisać jako |\vec{a}| lub a.
# - Wektor o długości 1 nazywa się wektorem jednostkowym (wersorem) i zapisuje się jako \hat{a}= \frac{\vec{a}}{|\vec{a}|}.
#
# **Przykład:**
#
# - Wektor \vec{a} = (3, 4) ma długość |\vec{a}| = 5 i odpowiadający wersor (jednostkowy wektor wzdłuż kierunku wektora \vec{a}) wyrażony jest przez \hat{a} = \left(\frac{3}{5}, \frac{4}{5}\right).

## Długość wektora
# Długość (moduł) wektora oblicza się za pomocą wzoru Pitagorasa.
#
# **Wektory w 2D:**
# Jeśli \vec{a} = (a_x, a_y), to długość jest dana wzorem:
# |\vec{a}| = \sqrt{a_x^2 + a_y^2}
#
# **Przykład:**
# Dla wektora \vec{a} = (3, 4), długość wynosi:
# |\vec{a}| = \sqrt{3^2 + 4^2} = \sqrt{9 + 16} = 5
#
# **Wektory w 3D:**
# Jeśli \vec{a} = (a_x, a_y, a_z), to długość wektora wynosi:
# |\vec{a}| = \sqrt{a_x^2 + a_y^2 + a_z^2}
#
# **Przykład:**
# Dla wektora \vec{a} = (1, 2, 2), długość wynosi:
# |\vec{a}| = \sqrt{1^2 + 2^2 + 2^2} = \sqrt{1 + 4 + 4} = 3

## Rozróżnienie między wektorami i skalarami
# - **Wektory:** mają wielkość, kierunek i zwrot (np. siła, prędkość).
# - **Skalary:** mają tylko wielkość (np. masa, temperatura).

## Reprezentacja we współrzędnych kartezjańskich
# Wektory można reprezentować za pomocą składowych w układzie kartezjańskim.
#
# **Wektory w 2D:**
# \vec{a} = (a_x, a_y)
#
# **Wektory w 3D:**
# \vec{a} = (a_x, a_y, a_z)
#
# Wektory bazowe \hat{i}, \hat{j}, \hat{k} odpowiadają odpowiednim osiom współrzędnych.

# Implementacje w Pythonie poniżej:

import numpy as np

def calculate_vector_length(vector):
    """Oblicza długość (moduł) wektora."""
    return np.linalg.norm(vector)

# Przykład 1: Obliczanie długości wektora w 2D
vector_2d = np.array([3, 4])
length_2d = calculate_vector_length(vector_2d)
print(f"Długość wektora {vector_2d} wynosi: {length_2d}")

# Przykład 2: Obliczanie długości wektora w 3D
vector_3d = np.array([1, 2, 2])
length_3d = calculate_vector_length(vector_3d)
print(f"Długość wektora {vector_3d} wynosi: {length_3d}")

def unit_vector(vector):
    """Zwraca wektor jednostkowy."""
    return vector / calculate_vector_length(vector)

# Obliczanie wersora (wektora jednostkowego)
unit_2d = unit_vector(vector_2d)
print(f"Wersor wektora {vector_2d} to: {unit_2d}")

# Operacje na wektorach
vector_a = np.array([3, 4, 5])
vector_b = np.array([1, 0, 2])

# Dodawanie wektorów
sum_vectors = vector_a + vector_b
print(f"Suma wektorów {vector_a} i {vector_b} to: {sum_vectors}")

# Iloczyn skalarny (dot product)
dot_product = np.dot(vector_a, vector_b)
print(f"Iloczyn skalarny wektorów {vector_a} i {vector_b} wynosi: {dot_product}")

# Iloczyn wektorowy (cross product)
cross_product = np.cross(vector_a, vector_b)
print(f"Iloczyn wektorowy wektorów {vector_a} i {vector_b} wynosi: {cross_product}")
