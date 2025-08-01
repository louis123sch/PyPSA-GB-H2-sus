# PyPSA-GB-H2-sus: Great Britain Hydrogen Network Optimization Model

## Overview

This project is a PyPSA (Python for Power System Analysis) model for analyzing hydrogen infrastructure development in Great Britain. It models three different Future Energy Scenarios (FES) 2022 pathways to 2050, optimizing hydrogen production, storage, and distribution networks across the UK.

## Project Structure

```
PyPSA-GB-H2-sus/
├── data/                          # Input data and parameters
│   ├── FES2022/                   # Future Energy Scenarios 2022 data
│   ├── LOPF_data/                 # Linear Optimal Power Flow input files
│   ├── PyPSA-GB/                  # Base PyPSA-GB model data
│   ├── capacity-splitter/         # Capacity allocation data
│   ├── generators/                # Generation technology data
│   ├── loads/                     # Demand profiles and data
│   └── network/                   # Network topology data
├── notebooks/                     # Jupyter notebooks for analysis
│   ├── 0 - Network.ipynb         # Network visualization and overview
│   ├── 1a - CT-2050.ipynb        # Consumer Transformation scenario
│   ├── 1b - LW-2050.ipynb        # Leading the Way scenario
│   ├── 1c - ST-2050.ipynb        # System Transformation scenario
│   ├── 1a-LOPF/                  # CT scenario optimization results
│   ├── 1b-LOPF/                  # LW scenario optimization results
│   └── 1c-LOPF/                  # ST scenario optimization results
└── requirements/                  # Environment setup files
    ├── PyPSA-GB_requirements.yml # Main conda environment
    └── atlite_requirements.yml   # Atlite environment for renewables
```

## Hydrogen Network Model

### Network Topology

The model represents a hydrogen backbone network for Great Britain with:

- **16 buses** representing key locations:
  - **10 Industrial Clusters**: St Fergus, Grangemouth, Teesside, Humberside, Theddlethorpe, Merseyside, Barrow, Bacton, Southampton, South Wales
  - **3 Salt Caverns**: East Yorkshire, Cheshire Basin, Wessex Basin (for hydrogen storage)
  - **3 Battery Limit Points**: Sheffield-B/L, Northampton-B/L, Luton-B/L
- **15 links** connecting the buses for hydrogen transport
- Based on Project Union's proposed hydrogen backbone infrastructure for 2030

### Geographic Coverage

The network uses two spatial resolution approaches:
- **DNO License Areas**: Distribution Network Operator boundaries
- **NUTS Level 1**: European statistical regions

*Note: Barrow Industrial Cluster is currently excluded due to insufficient publicly available data.*

## Future Energy Scenarios (FES 2022)

The model analyzes three pathways to net-zero by 2050:

### 1. Consumer Transformation (CT-2050)
- **Focus**: Consumer-led decarbonization
- **Characteristics**: High consumer adoption of low-carbon technologies
- **Hydrogen Role**: Significant in industry and heavy transport

### 2. Leading the Way (LW-2050)
- **Focus**: Coordinated action across all sectors
- **Characteristics**: Balanced approach with strong policy support
- **Hydrogen Role**: Strategic deployment across multiple sectors

### 3. System Transformation (ST-2050)
- **Focus**: System-wide transformation with infrastructure focus
- **Characteristics**: Large-scale infrastructure deployment
- **Hydrogen Role**: Central to the energy system transformation

## Technology Components

### Hydrogen Production
- **Biomass Gasification**: Renewable hydrogen from biomass feedstocks
- **Imports**: Hydrogen imports from international sources
- **Capacity**: Varies by location and scenario (0 MW to ~753 MW per site)

### Hydrogen Storage
- **Salt Caverns**: Underground storage in geological formations
- **Locations**: East Yorkshire, Cheshire Basin, Wessex Basin
- **Purpose**: Seasonal storage and system balancing

### Heat Demand Modeling
The project includes sophisticated heat demand modeling using the BDEW (German Association of Energy and Water Industries) methodology:

- **Building Types**:
  - Single Family Houses (EFH)
  - Multi-Family Houses (MFH)  
  - Commercial/Industrial (GHD)
- **Parameters**: Temperature-dependent profiles with holiday adjustments
- **Resolution**: Hourly profiles for full year (8,760 hours)

## Data Flow and Methodology

### 1. Input Data Preparation
```
FES2022 Data → Processing Scripts → LOPF Input Files
```

### 2. Network Components
The optimization model includes:
- **buses.csv**: Network nodes with coordinates
- **generators.csv**: Hydrogen production technologies
- **generators-p_max_pu.csv**: Availability factors
- **links.csv**: Network connections
- **loads.csv**: Hydrogen demand centers
- **loads-p_set.csv**: Demand time series
- **storage_units.csv**: Salt cavern storage facilities
- **snapshots.csv**: Temporal resolution definition

### 3. Optimization Process
```
Input Data → PyPSA Network → Gurobi Solver → Optimal Results
```

The Linear Optimal Power Flow (LOPF) optimization determines:
- Optimal hydrogen production levels
- Storage charging/discharging schedules
- Network flow patterns
- System costs and investments

## Software Requirements

### Core Dependencies
- **Python 3.8.5**
- **PyPSA**: Power system optimization framework
- **Gurobi**: Commercial optimization solver
- **Pandas/NumPy**: Data manipulation
- **Matplotlib/Seaborn**: Visualization
- **Cartopy**: Geographic plotting

### Optional Dependencies
- **Atlite**: Renewable energy time series generation
- **demandlib**: Heat demand profile generation

## Setup Instructions

### 1. Environment Setup
```bash
# Create conda environment
conda env create -f requirements/PyPSA-GB_requirements.yml
conda activate PyPSA-GB

# For renewable energy data processing (optional)
conda env create -f requirements/atlite_requirements.yml
```

### 2. Configuration
Update the `.env` file with your project path:
```
PROJECT_SRC=/path/to/your/notebooks/directory
```

### 3. Gurobi License
Ensure you have a valid Gurobi license for optimization:
- Academic license available for research use
- Commercial license required for business applications

## Usage

### Running Scenarios

1. **Network Overview**:
   ```bash
   jupyter notebook "0 - Network.ipynb"
   ```

2. **Individual Scenarios**:
   ```bash
   # Consumer Transformation
   jupyter notebook "1a - CT-2050.ipynb"
   
   # Leading the Way  
   jupyter notebook "1b - LW-2050.ipynb"
   
   # System Transformation
   jupyter notebook "1c - ST-2050.ipynb"
   ```

### Output Analysis

Each scenario generates:
- **Optimization Results**: In respective `1x-LOPF/` directories
- **Network Visualizations**: Geographic plots of the hydrogen network
- **Capacity Analysis**: Optimal technology deployment
- **Cost Analysis**: System costs and investment requirements
- **Flow Analysis**: Hydrogen transport patterns

## Key Features

### Spatial Analysis
- **GIS Integration**: Geographic visualization of network components
- **Regional Resolution**: DNO areas and NUTS-1 regions
- **Coordinate System**: OSGB (Ordnance Survey Great Britain) projection

### Temporal Resolution
- **Snapshots**: Hourly resolution (8,760 hours/year)
- **Seasonal Patterns**: Heat demand varies with temperature
- **Holiday Effects**: Demand profiles account for UK holidays

### Optimization Capabilities
- **Multi-Scenario Analysis**: Compare different pathways
- **Technology Competition**: Optimal technology mix
- **Network Planning**: Transmission capacity optimization
- **Storage Optimization**: Seasonal storage operation

## Research Applications

This model is suitable for:
- **Policy Analysis**: Evaluating hydrogen strategy options
- **Infrastructure Planning**: Optimal network development
- **Technology Assessment**: Comparing production pathways
- **Academic Research**: Hydrogen system optimization studies

## Limitations

- Barrow Industrial Cluster excluded (insufficient data)
- Based on 2022 FES assumptions
- Simplified network topology (16 buses vs. full grid)
- Single year analysis (typical meteorological year)

## References

- **FES 2022**: National Grid ESO Future Energy Scenarios
- **Project Union**: UK hydrogen backbone proposal
- **PyPSA**: https://pypsa.org/
- **BDEW**: German heat demand methodology

---

*This project was developed as part of a dissertation at the University of Edinburgh, focusing on hydrogen infrastructure optimization for Great Britain's energy transition.*