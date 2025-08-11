#!/bin/bash
# PyPSA-GB-H2-sus Setup Script
# This script helps set up the conda environment for the project

set -e  # Exit on any error

echo "PyPSA-GB-H2-sus Setup Script"
echo "=============================="

# Check if conda is available
if ! command -v conda &> /dev/null; then
    echo "Error: conda is not installed or not in PATH"
    echo "Please install Anaconda or Miniconda first"
    exit 1
fi

echo "✓ Conda found: $(conda --version)"

# Check if environment already exists
if conda env list | grep -q "^PyPSA-GB "; then
    echo "⚠️  PyPSA-GB environment already exists"
    read -p "Do you want to remove it and recreate? (y/N): " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        echo "Removing existing environment..."
        conda env remove -n PyPSA-GB -y
    else
        echo "Using existing environment"
        ENV_EXISTS=true
    fi
fi

# Create environment if it doesn't exist
if [ "$ENV_EXISTS" != "true" ]; then
    echo "Creating conda environment from requirements file..."
    conda env create -f requirements/PyPSA-GB_requirements.yml
    
    echo "Installing additional dependencies..."
    source "$(conda info --base)/etc/profile.d/conda.sh"
    conda activate PyPSA-GB
    
    # Install compatible geopandas version
    echo "Installing GeoPandas..."
    conda install -c conda-forge geopandas=0.10 -y
    
    # Try to fix xarray compatibility
    echo "Fixing xarray compatibility..."
    conda install "xarray<2022.12" -y
fi

# Activate environment and test
echo "Testing environment..."
source "$(conda info --base)/etc/profile.d/conda.sh"
conda activate PyPSA-GB

# Run the test script
if [ -f "test_environment.py" ]; then
    python test_environment.py
else
    echo "Test script not found, running basic test..."
    python -c "
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import geopandas as gp
print('Basic libraries working!')
"
fi

echo ""
echo "Setup complete!"
echo ""
echo "To use the environment:"
echo "  conda activate PyPSA-GB"
echo "  jupyter notebook"
echo ""
echo "Then navigate to the notebooks/ directory to start analyzing."