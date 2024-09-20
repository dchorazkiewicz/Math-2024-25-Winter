#!/bin/bash

# Tworzenie katalogów na notatniki
mkdir -p Notebooks_PL
mkdir -p Notebooks_EN

# Make subdirectories for Polish version
cd Notebooks_PL
mkdir -p 01_Algebra_Liniowa
mkdir -p 02_Geometria_Analityczna
mkdir -p 03_Analiza_Matematyczna

############################################
# Algebra Liniowa
cd 01_Algebra_Liniowa

mkdir -p  01_Macierze
mkdir -p  02_Uklady_Rownan_Liniowych
mkdir -p  03_Wektory_definicje
mkdir -p  04_Wektory_dzialania

############################################
# Geometria Analityczna
cd ../02_Geometria_Analityczna

mkdir -p  05_Proste
mkdir -p  06_Krzywe_Stozkowe
mkdir -p  07_Plaszczyzny_W_Przestrzeni
mkdir -p  08_Powierzchnie_Drugiego_Rzedu
mkdir -p  09_Podstawy_Rachunku_Tensorowego

############################################
# Analiza Matematyczna
cd ../03_Analiza_Matematyczna
# Teoria mnogości
mkdir -p  10_Ciagi
mkdir -p  11_Funkcje
mkdir -p  12_Pochodna_Funkcji
mkdir -p  13_Rozniczka_i_Zastosowania
mkdir -p  14_Zastosowania_Rachunku_Rozniczkowego
mkdir -p  15_Calka_Nieoznaczona
mkdir -p  16_Metody_calkowania_I
mkdir -p  17_Metody_calkowania_II
mkdir -p  18_Calka_Oznaczona
mkdir -p  19_Calki_Niewlasciwe
mkdir -p  20_Zastosowania_Calek_Oznaczonych
mkdir -p  21_Szeregi_Liczbowe
mkdir -p  22_Zbieznosc_Szeregow
mkdir -p  23_Szeregi_Funkcyjne
mkdir -p  24_Szeregi_Taylora_i_Maclaurina
mkdir -p  25_Szeregi_Fouriera

############################################
# English Version
cd ../../Notebooks_EN

mkdir -p 01_Linear_Algebra
mkdir -p 02_Analytical_Geometry
mkdir -p 03_Mathematical_Analysis

############################################
# Linear Algebra
cd 01_Linear_Algebra

mkdir -p  01_Matrices
mkdir -p  02_Systems_of_Linear_Equations
mkdir -p  03_Vectors_definitions
mkdir -p  04_Vectors_operations

############################################
# Analytical Geometry
cd ../02_Analytical_Geometry

mkdir -p  05_Lines
mkdir -p  06_Conic_Curves
mkdir -p  07_Planes_in_Space
mkdir -p  08_Second_Order_Surfaces
mkdir -p  09_Basics_of_Tensor_Calculus

############################################
# Mathematical Analysis
cd ../03_Mathematical_Analysis

mkdir -p  10_Sequences
mkdir -p  11_Functions
mkdir -p  12_Function_Derivative
mkdir -p  13_Differential_and_Applications
mkdir -p  14_Applications_of_Differential_Calculus
mkdir -p  15_Indefinite_Integral
mkdir -p  16_Integration_Methods_I
mkdir -p  17_Integration_Methods_II
mkdir -p  18_Definite_Integral
mkdir -p  19_Improper_Integrals
mkdir -p  20_Applications_of_Definite_Integrals
mkdir -p  21_Number_Series
mkdir -p  22_Series_Convergence
mkdir -p  23_Functional_Series
mkdir -p  24_Taylor_and_Maclaurin_Series
mkdir -p  25_Fourier_Series

# List the directories and files
ls -la
