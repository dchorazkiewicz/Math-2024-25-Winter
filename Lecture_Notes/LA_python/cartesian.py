import matplotlib.pyplot as plt
import numpy as np

def cart_ortogonal():
    # Tworzenie punktów na układzie współrzędnych
    points = {
        'A': (2, 3),
        'B': (-3, 7),
        'C': (4, -5),
        'D': (-6, -2),
        'E': (0, 5),
        'F': (-4, 0)
    }

    # Ustawienia wykresu
    plt.figure(figsize=(6, 6))
    plt.axhline(0, color='black', linewidth=0.5)  # Oś X
    plt.axvline(0, color='black', linewidth=0.5)  # Oś Y

    # Etykiety osi
    plt.xlabel('X Axis')
    plt.ylabel('Y Axis')

    # Zakres osi w integerach i główne znaczniki osi w odstępach co 1
    plt.xticks(range(-10, 11, 1))
    plt.yticks(range(-10, 11, 1))
    plt.xlim(-10, 10)
    plt.ylim(-10, 10)

    # Siatka pomocnicza
    plt.grid(True, which='both', linestyle='--', linewidth=0.5)

    # Matematyczny tytuł wykresu
    plt.title('Cartesian Coordinate System with Points (X, Y)')

    # Rysowanie punktów i ich etykiet
    for label, (x, y) in points.items():
        plt.plot(x, y, 'o', markersize=5, label=f'{label} ({x}, {y})')
        plt.text(x + 0.3, y + 0.3, f'{label} ({x}, {y})', fontsize=9)

    # Wyświetlenie wykresu
    plt.show()


def cart_not_ortogonal():
    # Definicja wektorów bazowych dla nieortogonalnego układu współrzędnych
    basis_vector_1 = np.array([1, 2])  # Wektor bazowy 1
    basis_vector_2 = np.array([2, 1])  # Wektor bazowy 2

    # Funkcja przekształcająca współrzędne punktów do nowego układu współrzędnych
    def transform_point(point, basis1, basis2):
        return point[0] * basis1 + point[1] * basis2

    # Definicja punktów
    points = {
        'A': (2, 3),
        'B': (-3, 7),
        'C': (4, -5),
        'D': (-6, -2),
        'E': (0, 5),
        'F': (-4, 0)
    }
    
    # Przekształcenie punktów w nowym układzie
    transformed_points = {label: transform_point(coords, basis_vector_1, basis_vector_2) for label, coords in points.items()}

    # Ustawienia wykresu dla nowego układu współrzędnych z liniami wzdłuż wektorów bazowych
    plt.figure(figsize=(6, 6))
    plt.axhline(0, color='black', linewidth=0.5)  # Oś X
    plt.axvline(0, color='black', linewidth=0.5)  # Oś Y

    # Etykiety osi
    plt.xlabel('X Axis (New Basis)')
    plt.ylabel('Y Axis (New Basis)')

    # Zakres osi w integerach i główne znaczniki osi w odstępach co 1
    plt.xlim(-10, 10)
    plt.ylim(-10, 10)

    # Siatka pomocnicza
    plt.grid(True, which='both', linestyle='--', linewidth=0.5)

    # Matematyczny tytuł wykresu
    plt.title('Non-Orthogonal Coordinate System with Transformed Points and Basis Lines')

    # Rysowanie wektorów bazowych jako strzałki
    plt.quiver(0, 0, basis_vector_1[0], basis_vector_1[1], angles='xy', scale_units='xy', scale=1, color='blue', label="Basis Vector 1")
    plt.quiver(0, 0, basis_vector_2[0], basis_vector_2[1], angles='xy', scale_units='xy', scale=1, color='red', label="Basis Vector 2")

    # Rysowanie linii równoległych do nowych wektorów bazowych
    for i in range(-10, 11):
        # Linie równoległe do wektora bazowego 1
        plt.plot([i * basis_vector_1[0] - 20 * basis_vector_2[0], i * basis_vector_1[0] + 20 * basis_vector_2[0]],
                 [i * basis_vector_1[1] - 20 * basis_vector_2[1], i * basis_vector_1[1] + 20 * basis_vector_2[1]], 'b--', linewidth=0.5)

        # Linie równoległe do wektora bazowego 2
        plt.plot([i * basis_vector_2[0] - 20 * basis_vector_1[0], i * basis_vector_2[0] + 20 * basis_vector_1[0]],
                 [i * basis_vector_2[1] - 20 * basis_vector_1[1], i * basis_vector_2[1] + 20 * basis_vector_1[1]], 'r--', linewidth=0.5)

    # Rysowanie przekształconych punktów i ich etykiet
    for label, (x, y) in transformed_points.items():
        plt.plot(x, y, 'o', markersize=5)
        plt.text(x + 0.3, y + 0.3, f'{label} ({x:.1f}, {y:.1f})', fontsize=9)

    # Wyświetlenie wykresu
    plt.legend()
    plt.show()

