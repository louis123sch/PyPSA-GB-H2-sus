# Quick Start Guide: PyPSA-GB-H2-sus

This guide will help you get the PyPSA-GB-H2-sus hydrogen network model running quickly.

## Prerequisites

- **Python 3.8+**
- **Conda** (Anaconda or Miniconda)
- **Gurobi License** (academic license available free for research)
- **Jupyter Notebook**

## Installation

### 1. Clone the Repository
```bash
git clone https://github.com/louis123sch/PyPSA-GB-H2-sus.git
cd PyPSA-GB-H2-sus
```

### 2. Set Up the Environment
```bash
# Create and activate the main environment
conda env create -f requirements/PyPSA-GB_requirements.yml
conda activate PyPSA-GB

# Optional: Create Atlite environment for renewable data
conda env create -f requirements/atlite_requirements.yml
```

### 3. Configure Gurobi
```bash
# Install Gurobi license (follow Gurobi instructions)
grbgetkey YOUR-LICENSE-KEY

# Test Gurobi installation
python -c "import gurobipy; print('Gurobi installed successfully')"
```

### 4. Set Project Path
Update the `.env` file with your notebook directory:
```bash
# Edit .env file
echo "PROJECT_SRC=$(pwd)/notebooks" > .env
```

## Quick Run

### 1. Explore the Network
Start with the network overview:
```bash
jupyter notebook "notebooks/0 - Network.ipynb"
```

This notebook shows:
- Hydrogen network topology
- Geographic locations of industrial clusters
- Salt cavern storage sites
- Network connections

### 2. Run a Scenario
Choose one of the three FES 2022 scenarios:

#### Consumer Transformation (CT-2050)
```bash
jupyter notebook "notebooks/1a - CT-2050.ipynb"
```

#### Leading the Way (LW-2050)
```bash
jupyter notebook "notebooks/1b - LW-2050.ipynb"
```

#### System Transformation (ST-2050)
```bash
jupyter notebook "notebooks/1c - ST-2050.ipynb"
```

### 3. Understand the Results
Each scenario notebook will:
1. Load input data from the corresponding LOPF folder
2. Build the PyPSA network model
3. Run optimization using Gurobi solver
4. Display results and visualizations

## Expected Outputs

### Network Visualizations
- Geographic maps showing hydrogen infrastructure
- Network topology with buses and links
- Technology deployment by location

### Optimization Results
- Optimal hydrogen production by technology
- Storage charging/discharging patterns
- Network flow patterns
- System costs and investments

### Economic Analysis
- Total system costs
- Technology competition results
- Regional investment patterns
- Hydrogen price formation

## Data Structure

### Input Files (in `data/LOPF_data/`)
- `buses.csv`: Network nodes with coordinates
- `generators.csv`: Production technologies
- `loads.csv`: Hydrogen demand centers
- `storage_units.csv`: Salt cavern storage
- `links.csv`: Pipeline connections
- `snapshots.csv`: Time periods (8,760 hours)

### Scenario-Specific Data (in `notebooks/1x-LOPF/`)
Each scenario has its own folder with customized parameters:
- Different demand projections
- Varying technology costs
- Scenario-specific assumptions

## Common Issues & Solutions

### 1. Gurobi License Issues
```bash
# Check license status
gurobi.sh
> grbgetkey --info

# Common fix for academic licenses
grbgetkey YOUR-ACADEMIC-KEY
```

### 2. Path Configuration
If you get path errors:
```python
# Check current path in notebook
import os
print(os.getcwd())

# Update .env file if needed
PROJECT_SRC=/full/path/to/notebooks
```

### 3. Missing Dependencies
```bash
# Install missing packages
conda install -c conda-forge package-name

# Or using pip
pip install package-name
```

### 4. Memory Issues
For large scenarios:
```python
# In notebook, increase memory
%config InlineBackend.figure_format = 'svg'  # Reduce memory usage
```

## Understanding the Model

### Key Concepts
1. **Buses**: Geographic nodes (16 total)
   - Industrial clusters
   - Salt cavern storage sites
   - Battery limit points

2. **Technologies**: 
   - Biomass gasification (production)
   - Hydrogen imports (supply)
   - Salt cavern storage (balancing)

3. **Scenarios**: Three pathways to 2050
   - Consumer Transformation (CT)
   - Leading the Way (LW)
   - System Transformation (ST)

### Time Resolution
- **Annual Model**: Representative year for 2050
- **Hourly Resolution**: 8,760 timesteps
- **Seasonal Patterns**: Heat demand varies with temperature

## Next Steps

### Analyze Results
1. Compare scenarios side-by-side
2. Examine regional differences
3. Analyze technology competition
4. Study storage operation patterns

### Modify the Model
1. Adjust technology costs
2. Change demand projections
3. Add new technologies
4. Modify network topology

### Advanced Analysis
1. Sensitivity analysis on key parameters
2. Scenario comparison across multiple metrics
3. Geographic analysis of investment patterns
4. Temporal analysis of system operation

## Getting Help

### Documentation
- `README.md`: Project overview
- `TECHNICAL.md`: Detailed methodology
- Notebook markdown cells: Inline explanations

### PyPSA Resources
- [PyPSA Documentation](https://pypsa.org/)
- [PyPSA Examples](https://github.com/PyPSA/PyPSA/tree/master/examples)
- [PyPSA Community Forum](https://github.com/PyPSA/PyPSA/discussions)

### Gurobi Resources
- [Gurobi Documentation](https://www.gurobi.com/documentation/)
- [Academic License](https://www.gurobi.com/academia/academic-program-and-licenses/)

---

**Ready to start?** Begin with `notebooks/0 - Network.ipynb` to explore the hydrogen network model!