# Technical Documentation: PyPSA-GB-H2-sus Modeling Methodology

## Model Architecture

### PyPSA Framework
The model is built using PyPSA (Python for Power System Analysis), which provides:
- **Linear Programming**: Optimization using mixed-integer linear programming
- **Network Modeling**: Graph-based representation of energy infrastructure
- **Temporal Resolution**: Multi-period optimization with hourly timesteps
- **Technology Integration**: Multiple energy carriers and conversion technologies

### Mathematical Formulation

The optimization problem is formulated as a Linear Optimal Power Flow (LOPF):

```
minimize: Total System Cost = Investment Costs + Operating Costs

subject to:
- Energy balance at each bus
- Transmission capacity constraints
- Generation capacity constraints
- Storage operation constraints
- Demand satisfaction requirements
```

## Network Components

### 1. Buses (Network Nodes)
Each bus represents a geographic location where hydrogen can be:
- Produced (via generation technologies)
- Consumed (by demand centers)
- Stored (in salt caverns)
- Transported (via pipeline connections)

**Key Attributes**:
- `name`: Location identifier
- `carrier`: Energy carrier (Hydrogen)
- `x, y`: Geographic coordinates (OSGB projection)

### 2. Generators (Production Technologies)

#### Biomass Gasification
- **Technology**: Thermochemical conversion of biomass to hydrogen
- **Capacity Range**: 0-753 MW per site
- **Availability**: Continuous operation (p_max_pu = 1.0)
- **Locations**: Distributed across industrial clusters

#### Hydrogen Imports
- **Source**: International hydrogen imports
- **Flexibility**: Can be activated based on economic optimization
- **Strategic Value**: Provides supply security and price competition

### 3. Links (Transport Infrastructure)
Pipeline connections between hydrogen hubs:
- **Capacity**: Optimized based on flow requirements
- **Efficiency**: Assumes minimal transport losses
- **Bidirectional**: Flow can occur in either direction
- **Investment**: Capital costs for pipeline construction

### 4. Storage Units (Salt Caverns)

#### Underground Hydrogen Storage
- **Technology**: Solution-mined salt caverns
- **Capacity**: Optimized based on seasonal balancing needs
- **Efficiency**: Round-trip efficiency considering compression/decompression
- **Cycling**: Daily and seasonal storage operation

**Storage Locations**:
1. **East Yorkshire**: Coastal location near Humberside cluster
2. **Cheshire Basin**: Central England strategic position
3. **Wessex Basin**: Southern England coverage

### 5. Loads (Demand Centers)

#### Industrial Hydrogen Demand
- **Sectors**: Steel, chemicals, refining, cement
- **Profiles**: Based on industrial operation patterns
- **Growth**: Scaled according to FES 2022 projections

#### Heat Demand (via Hydrogen)
Using BDEW methodology for thermal profiles:
- **Residential**: Single and multi-family houses
- **Commercial**: Offices, retail, services
- **Industrial**: Process heat applications

## Scenario Definitions

### Consumer Transformation (CT-2050)
**Philosophy**: Bottom-up decarbonization driven by consumer choices

**Key Assumptions**:
- High adoption of heat pumps in residential sector
- Moderate hydrogen demand growth
- Distributed energy resources
- Consumer-driven technology selection

**Hydrogen Role**:
- Industrial applications remain primary demand
- Limited residential heating use
- Transport applications in heavy-duty vehicles

### Leading the Way (LW-2050)
**Philosophy**: Coordinated action with strong policy support

**Key Assumptions**:
- Balanced technology deployment
- Strong government intervention
- International cooperation
- Technology-neutral policies

**Hydrogen Role**:
- Strategic deployment across sectors
- Significant industrial demand
- Growing transport sector use
- Export potential development

### System Transformation (ST-2050)
**Philosophy**: System-wide transformation with infrastructure focus

**Key Assumptions**:
- Large-scale infrastructure deployment
- Centralized planning approach
- Major network investments
- Technology convergence

**Hydrogen Role**:
- Central to energy system architecture
- Large-scale production facilities
- Extensive transport networks
- Seasonal storage critical

## Data Processing Pipeline

### 1. FES 2022 Data Integration
```
FES Workbook → Data Extraction → Regional Allocation → Technology Mapping
```

**Process**:
- Extract scenario-specific demand projections
- Allocate national totals to regional level
- Map to network bus locations
- Create hourly demand profiles

### 2. Heat Demand Profile Generation
```
Temperature Data → BDEW Algorithm → Building Type Profiles → Aggregated Demand
```

**BDEW Parameters**:
- **Building Classes**: Thermal efficiency categories
- **Wind Classes**: Exposure to wind effects  
- **Holiday Calendar**: UK-specific holiday impacts
- **Temperature Sensitivity**: Heating degree day correlation

### 3. Geographic Data Processing
```
Coordinate Systems: WGS84 → OSGB → PyPSA Network
```

**Spatial Resolution**:
- **DNO Areas**: 14 distribution network regions
- **NUTS-1**: 12 European statistical regions
- **Industrial Clusters**: Point locations with capacity data

## Optimization Process

### 1. Network Construction
```python
import pypsa

# Create network
n = pypsa.Network()

# Add components
n.import_from_csv_folder("LOPF_data/")

# Set solver options
n.optimize(solver_name="gurobi")
```

### 2. Solver Configuration
**Gurobi Parameters**:
- `Method`: Dual simplex algorithm
- `Threads`: Multi-core optimization
- `MIPGap`: Solution optimality tolerance
- `TimeLimit`: Maximum solving time

### 3. Result Processing
**Output Variables**:
- `generators_p`: Production dispatch
- `storage_units_p`: Storage operation
- `links_p0/p1`: Pipeline flows
- `buses_marginal_price`: Locational prices

## Economic Modeling

### Cost Components

#### Capital Costs (CAPEX)
- **Generation**: €/MW for production technologies
- **Storage**: €/MWh for cavern development
- **Transmission**: €/MW-km for pipeline construction

#### Operating Costs (OPEX)
- **Fixed O&M**: Annual maintenance costs
- **Variable O&M**: Production-dependent costs
- **Fuel Costs**: Biomass feedstock prices

#### Financial Parameters
- **Discount Rate**: 7% real (typical for energy infrastructure)
- **Lifetime**: Technology-specific depreciation periods
- **Annualization**: Convert CAPEX to annual equivalent

### Economic Assumptions
Based on FES 2022 techno-economic parameters:
- **Biomass Gasification**: €800-1200/kW
- **Salt Cavern Storage**: €5-15/kWh
- **Pipeline Transport**: €0.5-2.0 million/km

## Temporal Modeling

### Snapshot Definition
```python
snapshots = pd.date_range(
    start="2050-01-01 00:00",
    end="2050-12-31 23:00", 
    freq="H"
)
```

### Seasonal Patterns
- **Winter**: High heat demand, storage discharge
- **Summer**: Low heat demand, storage charging
- **Transitions**: Moderate demand, storage balancing

### Operational Constraints
- **Ramping**: Generator start-up/shut-down limits
- **Minimum Load**: Operational minimum for biomass plants
- **Storage Cycles**: Maximum charge/discharge rates

## Validation and Calibration

### Data Validation
- **Energy Balance**: Total production = consumption + losses
- **Capacity Factors**: Realistic utilization rates
- **Geographic Consistency**: Coordinate system accuracy

### Model Calibration
- **Demand Profiles**: Validate against historical patterns
- **Technology Costs**: Benchmark against literature
- **Network Topology**: Check against Project Union proposal

### Sensitivity Analysis
- **Technology Costs**: ±20% variations
- **Demand Growth**: Alternative scenarios
- **Policy Assumptions**: Carbon pricing impacts

## Results Interpretation

### Key Performance Indicators

#### System Metrics
- **Total System Cost**: Investment + operation (€/year)
- **Hydrogen Price**: Weighted average (€/MWh)
- **Storage Utilization**: Capacity factor (%)
- **Network Utilization**: Peak/average flows

#### Technology Metrics
- **Capacity Deployment**: Optimal technology mix (MW)
- **Generation Mix**: Production by technology (%)
- **Capacity Factors**: Technology utilization rates
- **Investment Priorities**: Geographic deployment patterns

#### Network Metrics
- **Transmission Flows**: Inter-regional hydrogen trade
- **Congestion Analysis**: Bottleneck identification
- **Storage Arbitrage**: Value of seasonal storage
- **Import Dependence**: Share of imported hydrogen

### Scenario Comparison
- **Investment Requirements**: Total capital needs by scenario
- **Technology Competition**: Winning technologies per scenario
- **Regional Differences**: Geographic deployment patterns
- **System Flexibility**: Storage and network requirements

## Limitations and Assumptions

### Model Limitations
- **Single Representative Year**: No inter-annual variability
- **Perfect Foresight**: Optimization assumes known future
- **Linear Approximation**: No non-linear constraints
- **Steady State**: No dynamic system behavior

### Data Limitations
- **Barrow Cluster**: Excluded due to data availability
- **Regional Resolution**: Limited to 16 network nodes
- **Technology Parameters**: Based on 2022 projections
- **Demand Uncertainty**: Single scenario per pathway

### Future Extensions
- **Stochastic Optimization**: Uncertainty handling
- **Multi-Year Modeling**: Investment timing optimization
- **Non-Linear Constraints**: Detailed technology modeling
- **Sector Coupling**: Integration with electricity and gas systems

---

*This technical documentation provides the detailed methodology behind the PyPSA-GB-H2-sus model for analyzing hydrogen infrastructure scenarios in Great Britain.*