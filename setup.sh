#!/bin/bash

# Funkcja tworząca katalog i plik README.md z tytułem
create_dir_with_readme() {
    dirname="$1"
    mkdir -p "$dirname"
    echo "# $dirname" > "$dirname/readme.md"
}

# Tworzenie katalogów na notatniki
create_dir_with_readme -p Notebooks_PL
create_dir_with_readme -p Notebooks_EN

# Przejście do katalogu Notebooks_PL
cd Notebooks_PL

# Tworzenie podkatalogów dla wersji polskiej
create_dir_with_readme 01_Algebra_Liniowa
create_dir_with_readme 02_Geometria_Analityczna
create_dir_with_readme 03_Analiza_Matematyczna

############################################
# Algebra Liniowa
cd 01_Algebra_Liniowa

create_dir_with_readme 01_Macierze
create_dir_with_readme 02_Uklady_Rownan_Liniowych
create_dir_with_readme 03_Wektory_definicje
create_dir_with_readme 04_Wektory_dzialania

cd ..

############################################
# Geometria Analityczna
cd 02_Geometria_Analityczna

create_dir_with_readme 05_Proste
create_dir_with_readme 06_Krzywe_Stozkowe
create_dir_with_readme 07_Plaszczyzny_W_Przestrzeni
create_dir_with_readme 08_Powierzchnie_Drugiego_Rzedu
create_dir_with_readme 09_Podstawy_Rachunku_Tensorowego

cd ..

############################################
# Analiza Matematyczna
cd 03_Analiza_Matematyczna

create_dir_with_readme 10_Ciagi
create_dir_with_readme 11_Funkcje
create_dir_with_readme 12_Pochodna_Funkcji
create_dir_with_readme 13_Rozniczka_i_Zastosowania
create_dir_with_readme 14_Zastosowania_Rachunku_Rozniczkowego
create_dir_with_readme 15_Calka_Nieoznaczona
create_dir_with_readme 16_Metody_calkowania_I
create_dir_with_readme 17_Metody_calkowania_II
create_dir_with_readme 18_Calka_Oznaczona
create_dir_with_readme 19_Calki_Niewlasciwe
create_dir_with_readme 20_Zastosowania_Calek_Oznaczonych
create_dir_with_readme 21_Szeregi_Liczbowe
create_dir_with_readme 22_Zbieznosc_Szeregow
create_dir_with_readme 23_Szeregi_Funkcyjne
create_dir_with_readme 24_Szeregi_Taylora_i_Maclaurina
create_dir_with_readme 25_Szeregi_Fouriera

cd ../..

############################################
# Przejście do katalogu Notebooks_EN
cd Notebooks_EN

# Tworzenie podkatalogów dla wersji angielskiej
create_dir_with_readme 01_Linear_Algebra
create_dir_with_readme 02_Analytical_Geometry
create_dir_with_readme 03_Mathematical_Analysis

############################################
# Linear Algebra
cd 01_Linear_Algebra

create_dir_with_readme 01_Matrices
create_dir_with_readme 02_Systems_of_Linear_Equations
create_dir_with_readme 03_Vectors_definitions
create_dir_with_readme 04_Vectors_operations

cd ..

############################################
# Analytical Geometry
cd 02_Analytical_Geometry

create_dir_with_readme 05_Lines
create_dir_with_readme 06_Conic_Curves
create_dir_with_readme 07_Planes_in_Space
create_dir_with_readme 08_Second_Order_Surfaces
create_dir_with_readme 09_Basics_of_Tensor_Calculus

cd ..

############################################
# Mathematical Analysis
cd 03_Mathematical_Analysis

create_dir_with_readme 10_Sequences
create_dir_with_readme 11_Functions
create_dir_with_readme 12_Function_Derivative
create_dir_with_readme 13_Differential_and_Applications
create_dir_with_readme 14_Applications_of_Differential_Calculus
create_dir_with_readme 15_Indefinite_Integral
create_dir_with_readme 16_Integration_Methods_I
create_dir_with_readme 17_Integration_Methods_II
create_dir_with_readme 18_Definite_Integral
create_dir_with_readme 19_Improper_Integrals
create_dir_with_readme 20_Applications_of_Definite_Integrals
create_dir_with_readme 21_Number_Series
create_dir_with_readme 22_Series_Convergence
create_dir_with_readme 23_Functional_Series
create_dir_with_readme 24_Taylor_and_Maclaurin_Series
create_dir_with_readme 25_Fourier_Series

cd ../..

# Wyświetlenie listy katalogów i plików
ls -la
