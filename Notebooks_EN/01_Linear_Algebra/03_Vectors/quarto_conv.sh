#!/bin/bash

# Sprawdź, czy podano argument
if [ "$#" -ne 1 ]; then
  echo "Użycie: $0 [ipynb_to_qmd|qmd_to_ipynb]"
  exit 1
fi

# Kierunek tłumaczenia
direction=$1

# Funkcja tłumaczenia z ipynb do qmd
ipynb_to_qmd() {
  for file in *.ipynb; do
    if [ -f "$file" ]; then
      base_name=$(basename "$file" .ipynb)
      output_file="trans_$base_name.qmd"
      echo "Tłumaczenie $file na $output_file"
      quarto convert "$file" -o "$output_file"
    fi
  done
}

# Funkcja tłumaczenia z qmd do ipynb
qmd_to_ipynb() {
  for file in *.qmd; do
    if [ -f "$file" ]; then
      base_name=$(basename "$file" .qmd)
      output_file="$base_name.ipynb"
      echo "Tłumaczenie $file na $output_file"
      quarto convert "$file" -o "$output_file"
    fi
  done
}

# Wybór operacji na podstawie argumentu
if [ "$direction" == "ipynb_to_qmd" ]; then
  ipynb_to_qmd
elif [ "$direction" == "qmd_to_ipynb" ]; then
  qmd_to_ipynb
else
  echo "Nieznana operacja: $direction"
  echo "Użycie: $0 [ipynb_to_qmd|qmd_to_ipynb]"
  exit 1
fi
