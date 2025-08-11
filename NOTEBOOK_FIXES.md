# Notebook Fixes for PyPSA-GB-H2-sus

## Fixed Issues

### 1. Shapefile Loading in Network Notebook

**Issue**: The notebook tries to load `.shx` file instead of `.shp` file:
```python
s = gp.read_file('../data/network/GIS/01 ESO - DNO License Areas/DNO_License_Areas_20200506.shx')
```

**Fix**: Change to load the main shapefile:
```python
s = gp.read_file('../data/network/GIS/01 ESO - DNO License Areas/DNO_License_Areas_20200506.shp')
```

### 2. Environment Path Issues

**Issue**: The `.env` file contained Windows paths
**Fix**: Updated to use Unix-style paths in `.env`

### 3. GeoPandas Compatibility

**Issue**: Version conflicts between shapely and geopandas
**Fix**: Installed compatible versions:
- `geopandas=0.10`  
- `shapely=1.8`

### 4. PyPSA Import Issues

**Issue**: PyPSA fails to import due to xarray compatibility
**Status**: Partially resolved - basic environment works, but PyPSA still has issues

## Quick Fix Instructions

To fix the Network notebook:

1. Open `notebooks/0 - Network.ipynb`
2. In cell that loads shapefile, change:
   ```python
   # From:
   s = gp.read_file('../data/network/GIS/01 ESO - DNO License Areas/DNO_License_Areas_20200506.shx')
   
   # To:
   s = gp.read_file('../data/network/GIS/01 ESO - DNO License Areas/DNO_License_Areas_20200506.shp')
   ```

3. The notebook should now run successfully for geospatial visualization.