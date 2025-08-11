# Basic Environment Test Notebook

This notebook demonstrates that the PyPSA-GB-H2-sus environment is working correctly.

## Import Libraries

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import geopandas as gp
print("✓ All basic libraries imported successfully")
```

## Test Data Processing

```python
# Create sample data similar to what's used in the project
sample_data = pd.DataFrame({
    'bus_name': ['Industrial_1', 'Industrial_2', 'Salt_Cavern_1'], 
    'x_coord': [0.0, 1.0, 0.5],
    'y_coord': [51.5, 52.0, 51.8],
    'capacity_mw': [100, 150, 200]
})

print("Sample hydrogen infrastructure data:")
print(sample_data)
```

## Test Plotting

```python
# Create a simple plot
plt.figure(figsize=(8, 6))
plt.scatter(sample_data['x_coord'], sample_data['y_coord'], 
           s=sample_data['capacity_mw'], alpha=0.7)
plt.xlabel('Longitude')
plt.ylabel('Latitude') 
plt.title('Sample Hydrogen Infrastructure Locations')
plt.grid(True, alpha=0.3)
plt.show()
```

## Check Environment Status

```python
# Run the environment test
exec(open('test_environment.py').read())
```

If all cells run successfully, your environment is ready for the main analysis notebooks!