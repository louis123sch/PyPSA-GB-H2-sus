# FES 2022 Scenarios: Hydrogen Infrastructure Pathways to 2050

This document explains the three Future Energy Scenarios (FES) 2022 pathways modeled in PyPSA-GB-H2-sus and their implications for hydrogen infrastructure development in Great Britain.

## Scenario Overview

The Future Energy Scenarios (FES) 2022, published by National Grid ESO, present credible pathways to achieving net-zero emissions by 2050. Each scenario represents different societal choices about how the energy transition unfolds.

| Scenario | Focus | Approach | Hydrogen Role |
|----------|-------|----------|---------------|
| **Consumer Transformation (CT)** | Consumer-led | Bottom-up | Targeted applications |
| **Leading the Way (LW)** | Coordinated action | Balanced | Strategic deployment |
| **System Transformation (ST)** | Infrastructure-led | Top-down | Central role |

## Consumer Transformation (CT-2050)

### Philosophy
> "Consumers take the lead in driving the energy transition through their choices and behaviors."

### Key Characteristics
- **Consumer Empowerment**: High adoption of distributed technologies
- **Local Solutions**: Community energy projects and microgrids
- **Technology Diversity**: Multiple competing technologies
- **Gradual Transition**: Evolutionary rather than revolutionary change

### Energy System Features
- **Electrification Dominant**: Heat pumps preferred for heating
- **Distributed Generation**: Rooftop solar and small-scale renewables
- **Smart Technologies**: Home energy management systems
- **Flexible Demand**: Consumer participation in demand response

### Hydrogen Applications
1. **Industrial Processes**: Steel, chemicals, refining
2. **Heavy Transport**: Trucks, buses, trains, shipping
3. **Backup Power**: Grid balancing and security
4. **Limited Heating**: Mainly in areas unsuitable for heat pumps

### Infrastructure Implications
- **Smaller Scale**: Distributed hydrogen production
- **Regional Networks**: Local distribution systems
- **Moderate Storage**: Seasonal balancing requirements
- **Gradual Build-out**: Phased infrastructure development

### Modeling Parameters (CT-2050)
- **Hydrogen Demand**: Lower overall demand growth
- **Production Mix**: Balanced between biomass and imports
- **Storage Needs**: Moderate seasonal storage
- **Network Scale**: Smaller pipeline capacities

---

## Leading the Way (LW-2050)

### Philosophy
> "Strong coordination between government, industry, and consumers accelerates the transition."

### Key Characteristics
- **Policy Leadership**: Strong government intervention and support
- **International Cooperation**: Global collaboration on technologies
- **Technology Neutrality**: Support for multiple pathways
- **Balanced Approach**: Mix of centralized and distributed solutions

### Energy System Features
- **Rapid Deployment**: Fast scaling of low-carbon technologies
- **Grid Modernization**: Major electricity network upgrades
- **Sector Coupling**: Integration across electricity, heat, and transport
- **Innovation Support**: R&D investment and demonstration projects

### Hydrogen Applications
1. **Industrial Transformation**: Large-scale industrial decarbonization
2. **Transport Hub**: Comprehensive hydrogen transport network
3. **Heating Blend**: Hydrogen blending in gas networks
4. **Export Economy**: UK becomes hydrogen exporter

### Infrastructure Implications
- **Strategic Networks**: National hydrogen backbone
- **Multi-Purpose**: Flexible infrastructure serving multiple sectors
- **Large Storage**: Significant seasonal storage capacity
- **Coordinated Development**: Synchronized build-out across regions

### Modeling Parameters (LW-2050)
- **Hydrogen Demand**: Balanced growth across sectors
- **Production Mix**: Diverse technology portfolio
- **Storage Needs**: Substantial seasonal balancing
- **Network Scale**: Medium to large pipeline capacities

---

## System Transformation (ST-2050)

### Philosophy
> "Fundamental transformation of the entire energy system with large-scale infrastructure."

### Key Characteristics
- **System Redesign**: Complete overhaul of energy infrastructure
- **Centralized Planning**: Top-down coordination and investment
- **Large-Scale Deployment**: Massive infrastructure projects
- **Technology Convergence**: Integrated multi-energy systems

### Energy System Features
- **Massive Renewables**: Very high renewable electricity capacity
- **Hydrogen Central**: Hydrogen as primary energy carrier
- **System Integration**: Full coupling of electricity, gas, heat, transport
- **Infrastructure Investment**: Major network expansion and modernization

### Hydrogen Applications
1. **Energy Storage**: Large-scale seasonal energy storage
2. **Industrial Backbone**: Hydrogen replaces natural gas
3. **Transport Fuel**: Comprehensive hydrogen mobility
4. **Heating Networks**: District heating with hydrogen
5. **Power Generation**: Hydrogen power plants for flexibility

### Infrastructure Implications
- **National Networks**: Extensive hydrogen transmission system
- **Massive Storage**: Very large underground storage facilities
- **Integrated Systems**: Connected electricity-hydrogen networks
- **Import Infrastructure**: Major international hydrogen imports

### Modeling Parameters (ST-2050)
- **Hydrogen Demand**: Highest overall demand
- **Production Mix**: Large-scale facilities dominate
- **Storage Needs**: Maximum seasonal storage capacity
- **Network Scale**: Largest pipeline capacities

---

## Comparative Analysis

### Hydrogen Demand Growth
```
CT-2050: Moderate, targeted applications
LW-2050: Steady, broad-based growth  
ST-2050: Rapid, system-wide adoption
```

### Infrastructure Investment
```
CT-2050: Gradual, distributed investment
LW-2050: Coordinated, strategic investment
ST-2050: Massive, centralized investment
```

### Technology Preferences
```
CT-2050: Technology diversity, consumer choice
LW-2050: Technology neutrality, competitive deployment
ST-2050: Technology convergence, system optimization
```

## Scenario Implications for the UK

### Economic Impacts
- **CT**: Lower infrastructure costs, higher operational flexibility
- **LW**: Balanced investment profile, export opportunities
- **ST**: High upfront investment, long-term cost reductions

### Environmental Outcomes
- **CT**: Gradual emissions reduction, distributed benefits
- **LW**: Coordinated decarbonization, international leadership
- **ST**: Rapid decarbonization, system-wide transformation

### Social Considerations
- **CT**: Consumer empowerment, local ownership
- **LW**: Balanced stakeholder engagement, just transition
- **ST**: Centralized benefits, potential regional disparities

## Modeling Differences in PyPSA-GB-H2-sus

### Demand Profiles
Each scenario uses different demand projections based on FES 2022 data:
- **Technology penetration rates**
- **Sectoral growth assumptions**
- **Regional distribution patterns**

### Technology Deployment
Scenario-specific parameters for:
- **Biomass gasification capacity**
- **Import potential**
- **Storage requirements**
- **Network expansion needs**

### Economic Assumptions
Different cost trajectories reflecting:
- **Learning curve effects**
- **Scale economies**
- **Policy support levels**
- **International market development**

## Key Insights

### Technology Competition
- **CT**: Local technologies compete with centralized solutions
- **LW**: Balanced competition drives cost reductions
- **ST**: Large-scale technologies dominate through economies of scale

### Regional Development
- **CT**: Distributed development across regions
- **LW**: Strategic regional specialization
- **ST**: Concentrated development in key industrial clusters

### International Trade
- **CT**: Limited hydrogen trade, self-sufficiency focus
- **LW**: Moderate imports/exports, strategic partnerships
- **ST**: Significant hydrogen trade, global market integration

---

These scenarios provide a comprehensive framework for understanding how different societal choices and policy approaches could shape the development of hydrogen infrastructure in Great Britain by 2050. The PyPSA-GB-H2-sus model quantifies these differences through detailed techno-economic optimization.