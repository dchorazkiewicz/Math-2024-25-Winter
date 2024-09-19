#!/bin/bash

# Tworzenie katalogów na notatniki
mkdir -p Notebooks_PL
mkdir -p Notebooks_EN

# Make subdirectories for Polish version
cd Notebooks_PL
mkdir -p 01_Algebra_Liniowa/PY
mkdir -p 01_Algebra_Liniowa/Notebooks
mkdir -p 02_Geometria_Analityczna/PY
mkdir -p 02_Geometria_Analityczna/Notebooks
mkdir -p 03_Analiza_Matematyczna/PY
mkdir -p 03_Analiza_Matematyczna/Notebooks

############################################
# Algebra Liniowa
cd 01_Algebra_Liniowa/PY

touch 01_a_Macierze_definicje.py
touch 01_b_Macierze_dzialania.py
touch 02___Uklady_Rownan_Liniowych.py
touch 03_a_Wektory_definicje.py
touch 04_b_Wektory_dzialania.py

############################################
# Geometria Analityczna
cd ../../02_Geometria_Analityczna/PY

touch 05_Proste.py
touch 06_Krzywe_Stozkowe.py
touch 07_Plaszczyzny_W_Przestrzeni.py
touch 08_Powierzchnie_Drugiego_Rzedu.py
touch 09_Podstawy_Rachunku_Tensorowego.py

############################################
# Analiza Matematyczna
cd ../../03_Analiza_Matematyczna/PY
# Teoria mnogości
touch 10_a_Ciagi_definicje.py
touch 10_b_Ciagi_granica.py
touch 11_a_Funkcje_definicje.py
touch 11_b_Funkcje_granica_i_ciaglosc.py
touch 12_Pochodna_Funkcji.py
touch 13_Rozniczka_i_Zastosowania.py
touch 14_Zastosowania_Rachunku_Rozniczkowego.py
touch 15_Calka_Nieoznaczona.py
touch 16_Metody_calkowania_I.py
touch 17_Metody_calkowania_II.py
touch 18_Calka_Oznaczona.py
touch 19_Calki_Niewlasciwe.py
touch 20_Zastosowania_Calek_Oznaczonych.py
touch 21_Szeregi_Liczbowe.py
touch 22_Zbieznosc_Szeregow.py
touch 23_Szeregi_Funkcyjne.py
touch 24_Szeregi_Taylora_i_Maclaurina.py
touch 25_Szeregi_Fouriera.py

############################################
# English Version
cd ../../../Notebooks_EN

mkdir -p 01_Linear_Algebra/PY
mkdir -p 01_Linear_Algebra/Notebooks
mkdir -p 02_Analytical_Geometry/PY
mkdir -p 02_Analytical_Geometry/Notebooks
mkdir -p 03_Mathematical_Analysis/PY
mkdir -p 03_Mathematical_Analysis/Notebooks

############################################
# Linear Algebra
cd 01_Linear_Algebra/PY

touch 01_a_Matrices_definitions.py
touch 01_b_Matrices_operations.py
touch 02_Systems_of_Linear_Equations.py
touch 03_a_Vectors_definitions.py
touch 04_b_Vectors_operations.py

############################################
# Analytical Geometry
cd ../../02_Analytical_Geometry/PY

touch 05_Lines.py
touch 06_Conic_Curves.py
touch 07_Planes_in_Space.py
touch 08_Second_Order_Surfaces.py
touch 09_Basics_of_Tensor_Calculus.py

############################################
# Mathematical Analysis
cd ../../03_Mathematical_Analysis/PY

touch 10_a_Sequences_definitions.py
touch 10_b_Sequences_limit.py
touch 11_a_Functions_definitions.py
touch 11_b_Functions_limit_and_continuity.py
touch 12_Function_Derivative.py
touch 13_Differential_and_Applications.py
touch 14_Applications_of_Differential_Calculus.py
touch 15_Indefinite_Integral.py
touch 16_Integration_Methods_I.py
touch 17_Integration_Methods_II.py
touch 18_Definite_Integral.py
touch 19_Improper_Integrals.py
touch 20_Applications_of_Defined_Integrals.py
touch 21_Number_Series.py
touch 22_Series_Convergence.py
touch 23_Functional_Series.py
touch 24_Taylor_and_Maclaurin_Series.py
touch 25_Fourier_Series.py

# List the directories and files
ls -la
