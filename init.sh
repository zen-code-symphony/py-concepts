#!/bin/bash

VENV_DIR="venv"

# Check if virtual environment exists.
if [ ! -d "$VENV_DIR" ]; then
    # Create Python virtual environment and activate.
    python -m venv "$VENV_DIR" && source "$VENV_DIR/bin/activate"

    # Upgrade pip and install the Python dependencies.
    python -m pip install --upgrade pip
    python -m pip install -r requirements.txt
else
    echo "Virtual environment already exists. Skipping creation."
fi

# Check if pre-commit hooks are installed.
if [ ! -f .git/hooks/pre-commit ]; then
    # Set up the git hook scripts.
    pre-commit install
    pre-commit install --hook-type commit-msg
else
    echo "pre-commit hooks already installed for this Git repository. Skipping installation."
fi
