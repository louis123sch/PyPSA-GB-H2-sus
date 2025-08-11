# PyPSA-GB-H2-sus: Great Britain Hydrogen Supply Scenarios

This repository contains analysis notebooks for hydrogen supply scenarios in Great Britain using PyPSA (Python for Power System Analysis).

## Project Structure

- `data/` - Contains network data, generators, loads, and capacity information
- `notebooks/` - Jupyter notebooks for different analysis scenarios:
  - `0 - Network.ipynb` - Network overview and visualization
  - `1a - CT-2050.ipynb` - Consumer Transformation 2050 scenario
  - `1b - LW-2050.ipynb` - Leading the Way 2050 scenario  
  - `1c - ST-2050.ipynb` - System Transformation 2050 scenario
- `requirements/` - Conda environment files

## Setup Instructions

### Prerequisites
- Anaconda or Miniconda installed
- Git (to clone the repository)

### Environment Setup

1. Clone the repository:
```bash
git clone https://github.com/louis123sch/PyPSA-GB-H2-sus.git
cd PyPSA-GB-H2-sus
```

2. Create the conda environment:
```bash
conda env create -f requirements/PyPSA-GB_requirements.yml
```

3. Activate the environment:
```bash
conda activate PyPSA-GB
```

4. Install additional dependencies if needed:
```bash
# If geopandas is missing (common issue)
conda install -c conda-forge geopandas

# If PyPSA import fails, try updating xarray compatibility
conda install "xarray<2022.12"
```

### Running the Notebooks

1. Start Jupyter:
```bash
jupyter notebook
```

2. Navigate to the `notebooks/` directory and open any of the analysis notebooks.

## Known Issues

- **GeoPandas/GDAL conflicts**: The environment may have dependency conflicts with geospatial libraries. If you encounter import errors, try installing compatible versions manually.
- **PyPSA import errors**: Some versions of PyPSA may not be compatible with newer xarray versions. Downgrading xarray usually resolves this.
- **Path issues**: The `.env` file has been updated to use Unix-style paths suitable for Linux/macOS environments.

## Data Sources

The project analyzes hydrogen infrastructure scenarios based on:
- Industrial clusters
- Salt cavern storage sites
- Project Union hydrogen backbone proposals
- Future Energy Scenarios (FES) data

## Analysis Scenarios

1. **Consumer Transformation (CT-2050)**: Focus on consumer behavior changes
2. **Leading the Way (LW-2050)**: Rapid decarbonization scenario
3. **System Transformation (ST-2050)**: Whole system transformation approach

Each scenario includes Linear Optimal Power Flow (LOPF) optimization and output analysis.