#!/bin/bash

# check if pyenv is installed
if [ -d "$HOME/.pyenv" ]; then
  export PYENV_ROOT="$HOME/.pyenv"
  export PATH="$PYENV_ROOT/bin:$PATH"
  eval "$(pyenv init -)"
fi

# pyenv: check if python 3.11.9 is installed if not install it
if ! pyenv versions | grep -q 3.11.9; then
  pyenv install 3.11.9
fi

# set the local Python version to 3.11.9 for the current directory
pyenv local 3.11.9

# set the project directory (use current directory)
PROJECT_DIR=$(pwd)

# check if virtualenv exists in the project directory
if [ ! -d "$PROJECT_DIR/.venv" ]; then
  # Create virtual environment using the specified Python version
  python -m venv "$PROJECT_DIR/.venv"
fi

# activate the virtualenv
source "$PROJECT_DIR/.venv/bin/activate"

# install poetry in the virtualenv
pip install poetry

# check if pyproject.toml exists, if not, initialize a new Poetry project
if [ ! -f "$PROJECT_DIR/pyproject.toml" ]; then
  # Initialize a new Poetry project (you can add --no-interaction if you want to skip the interactive prompts)
  poetry init --no-interaction --name "$(basename "$PROJECT_DIR")" --description "Math project" --author "Math"
fi

# install dependencies if pyproject.toml exists
if [ -f "$PROJECT_DIR/pyproject.toml" ]; then
  poetry install
fi

