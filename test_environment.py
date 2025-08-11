#!/usr/bin/env python3
"""
PyPSA-GB-H2-sus Environment Test Script

This script tests the basic functionality of the conda environment
to ensure key libraries are working properly.
"""

import sys
import traceback

def test_basic_imports():
    """Test basic data science libraries"""
    print("Testing basic data science libraries...")
    try:
        import pandas as pd
        import numpy as np
        import matplotlib.pyplot as plt
        print(f"✓ Pandas {pd.__version__}")
        print(f"✓ NumPy {np.__version__}")
        print(f"✓ Matplotlib {plt.matplotlib.__version__}")
        return True
    except ImportError as e:
        print(f"✗ Error importing basic libraries: {e}")
        return False

def test_geopandas():
    """Test geopandas import"""
    print("\nTesting geospatial libraries...")
    try:
        import geopandas as gp
        print(f"✓ GeoPandas {gp.__version__}")
        return True
    except ImportError as e:
        print(f"✗ Error importing geopandas: {e}")
        return False

def test_pypsa():
    """Test PyPSA import"""
    print("\nTesting PyPSA...")
    try:
        import pypsa
        print(f"✓ PyPSA {pypsa.__version__}")
        return True
    except ImportError as e:
        print(f"✗ Error importing PyPSA: {e}")
        print("Note: PyPSA may have compatibility issues with current environment.")
        return False

def test_jupyter():
    """Test Jupyter availability"""
    print("\nTesting Jupyter...")
    try:
        import jupyter
        import IPython
        print(f"✓ IPython {IPython.__version__}")
        print("✓ Jupyter components available")
        return True
    except ImportError as e:
        print(f"✗ Error with Jupyter: {e}")
        return False

def test_data_loading():
    """Test basic data loading capabilities"""
    print("\nTesting data loading...")
    try:
        import pandas as pd
        # Create a simple test DataFrame
        test_data = pd.DataFrame({
            'x': [1, 2, 3],
            'y': [4, 5, 6]
        })
        print("✓ Pandas data manipulation working")
        
        # Test basic plotting
        import matplotlib.pyplot as plt
        plt.figure(figsize=(6, 4))
        plt.plot(test_data['x'], test_data['y'])
        plt.title('Test Plot')
        plt.close()  # Close to avoid display issues
        print("✓ Basic plotting functionality working")
        return True
    except Exception as e:
        print(f"✗ Error with data operations: {e}")
        return False

def main():
    """Run all tests"""
    print("PyPSA-GB-H2-sus Environment Test")
    print("=" * 40)
    
    tests = [
        test_basic_imports,
        test_geopandas,
        test_pypsa,
        test_jupyter,
        test_data_loading
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        try:
            if test():
                passed += 1
        except Exception as e:
            print(f"✗ Test failed with exception: {e}")
            traceback.print_exc()
    
    print("\n" + "=" * 40)
    print(f"Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All tests passed! Environment is ready.")
        return 0
    elif passed >= 3:
        print("⚠️  Most tests passed. Environment is mostly functional.")
        print("   Some advanced features may not work properly.")
        return 0
    else:
        print("❌ Multiple tests failed. Environment needs attention.")
        return 1

if __name__ == "__main__":
    sys.exit(main())