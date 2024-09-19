# print working directory
pwd
# wyświetl zawartość katalogu razem z ukrytymi plikami
ls -la

# activate the virtual environment
source .venv/bin/activate

# check the version of jupytext
jupytext --version

# convert example_integral_calculation.py to ipynb

jupytext --to notebook Test_notebooks/example_integral_calculation.py