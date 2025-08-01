#!/usr/bin/env python3
"""
Setup Validation Script for PyPSA-GB-H2-sus

This script validates that all required dependencies and data files
are available for running the hydrogen network optimization model.

Usage:
    python validate_setup.py
"""

import os
import sys
import warnings
from pathlib import Path

def check_python_version():
    """Check Python version compatibility."""
    print("🐍 Checking Python version...")
    version = sys.version_info
    if version.major == 3 and version.minor >= 8:
        print(f"   ✅ Python {version.major}.{version.minor}.{version.micro} - Compatible")
        return True
    else:
        print(f"   ❌ Python {version.major}.{version.minor}.{version.micro} - Requires Python 3.8+")
        return False

def check_dependencies():
    """Check required Python packages."""
    print("📦 Checking required packages...")
    
    required_packages = {
        'pypsa': 'PyPSA power system optimization',
        'pandas': 'Data manipulation and analysis',
        'numpy': 'Numerical computing',
        'matplotlib': 'Plotting and visualization',
        'cartopy': 'Geographic plotting',
        'shapely': 'Geometric operations',
        'geopandas': 'Geographic data manipulation',
        'scipy': 'Scientific computing',
        'seaborn': 'Statistical visualization',
        'jupyter': 'Jupyter notebook environment'
    }
    
    missing_packages = []
    
    for package, description in required_packages.items():
        try:
            __import__(package)
            print(f"   ✅ {package} - {description}")
        except ImportError:
            print(f"   ❌ {package} - {description} (MISSING)")
            missing_packages.append(package)
    
    return len(missing_packages) == 0, missing_packages

def check_gurobi():
    """Check Gurobi solver availability."""
    print("🔧 Checking Gurobi solver...")
    
    try:
        import gurobipy
        try:
            # Try to create a model to test license
            m = gurobipy.Model()
            m.optimize()
            print("   ✅ Gurobi installed and licensed")
            return True
        except gurobipy.GurobiError as e:
            if "license" in str(e).lower():
                print(f"   ⚠️  Gurobi installed but license issue: {e}")
                print("      Get academic license: https://www.gurobi.com/academia/")
                return False
            else:
                print(f"   ✅ Gurobi available (test optimization worked)")
                return True
    except ImportError:
        print("   ❌ Gurobi not installed")
        print("      Install: conda install gurobi")
        return False

def check_data_files():
    """Check required data files."""
    print("📁 Checking data files...")
    
    base_path = Path(__file__).parent
    required_files = [
        "data/LOPF_data/buses.csv",
        "data/LOPF_data/generators.csv", 
        "data/LOPF_data/links.csv",
        "data/LOPF_data/loads.csv",
        "data/LOPF_data/storage_units.csv",
        "data/LOPF_data/snapshots.csv",
        "notebooks/1a-LOPF/buses.csv",
        "notebooks/1b-LOPF/buses.csv", 
        "notebooks/1c-LOPF/buses.csv"
    ]
    
    missing_files = []
    
    for file_path in required_files:
        full_path = base_path / file_path
        if full_path.exists():
            print(f"   ✅ {file_path}")
        else:
            print(f"   ❌ {file_path} (MISSING)")
            missing_files.append(file_path)
    
    return len(missing_files) == 0, missing_files

def check_environment():
    """Check environment configuration."""
    print("🌍 Checking environment setup...")
    
    base_path = Path(__file__).parent
    env_file = base_path / ".env"
    
    if env_file.exists():
        print("   ✅ .env file exists")
        
        # Try to load dotenv
        try:
            from dotenv import load_dotenv
            load_dotenv(env_file)
            project_src = os.environ.get('PROJECT_SRC')
            
            if project_src:
                print(f"   ✅ PROJECT_SRC configured: {project_src}")
                if Path(project_src).exists():
                    print("   ✅ PROJECT_SRC directory exists")
                    return True
                else:
                    print("   ⚠️  PROJECT_SRC directory not found")
                    print(f"      Update .env file with correct path to notebooks directory")
                    return False
            else:
                print("   ⚠️  PROJECT_SRC not set in .env file")
                return False
                
        except ImportError:
            print("   ❌ python-dotenv not installed")
            return False
    else:
        print("   ❌ .env file missing")
        print("      Create .env file with: PROJECT_SRC=/path/to/notebooks")
        return False

def check_notebook_files():
    """Check notebook files."""
    print("📓 Checking notebook files...")
    
    base_path = Path(__file__).parent
    notebook_files = [
        "notebooks/0 - Network.ipynb",
        "notebooks/1a - CT-2050.ipynb",
        "notebooks/1b - LW-2050.ipynb", 
        "notebooks/1c - ST-2050.ipynb"
    ]
    
    missing_notebooks = []
    
    for notebook in notebook_files:
        full_path = base_path / notebook
        if full_path.exists():
            print(f"   ✅ {notebook}")
        else:
            print(f"   ❌ {notebook} (MISSING)")
            missing_notebooks.append(notebook)
    
    return len(missing_notebooks) == 0, missing_notebooks

def test_basic_functionality():
    """Test basic PyPSA functionality."""
    print("🧪 Testing basic functionality...")
    
    try:
        import pypsa
        import pandas as pd
        
        # Create a simple test network
        n = pypsa.Network()
        
        # Add a simple bus
        n.add("Bus", "test_bus")
        
        # Check if network creation worked
        if len(n.buses) == 1:
            print("   ✅ PyPSA network creation works")
            return True
        else:
            print("   ❌ PyPSA network creation failed")
            return False
            
    except Exception as e:
        print(f"   ❌ Basic functionality test failed: {e}")
        return False

def main():
    """Run all validation checks."""
    print("🚀 PyPSA-GB-H2-sus Setup Validation")
    print("=" * 50)
    
    checks = [
        ("Python Version", check_python_version),
        ("Dependencies", lambda: check_dependencies()[0]),
        ("Gurobi Solver", check_gurobi),
        ("Environment Config", check_environment), 
        ("Data Files", lambda: check_data_files()[0]),
        ("Notebook Files", lambda: check_notebook_files()[0]),
        ("Basic Functionality", test_basic_functionality)
    ]
    
    results = {}
    
    for check_name, check_func in checks:
        print()
        try:
            results[check_name] = check_func()
        except Exception as e:
            print(f"   ❌ {check_name} check failed with error: {e}")
            results[check_name] = False
    
    print("\n" + "=" * 50)
    print("📋 Validation Summary")
    print("=" * 50)
    
    all_passed = True
    for check_name, passed in results.items():
        status = "✅ PASS" if passed else "❌ FAIL"
        print(f"{status} {check_name}")
        if not passed:
            all_passed = False
    
    print("\n" + "=" * 50)
    
    if all_passed:
        print("🎉 All checks passed! You're ready to run PyPSA-GB-H2-sus")
        print("\nNext steps:")
        print("1. Start with: jupyter notebook 'notebooks/0 - Network.ipynb'")
        print("2. Run scenarios: 1a-CT, 1b-LW, or 1c-ST notebooks")
        return 0
    else:
        print("⚠️  Some checks failed. Please address the issues above.")
        print("\nFor help:")
        print("- See README.md for setup instructions")
        print("- See QUICKSTART.md for quick setup guide")
        return 1

if __name__ == "__main__":
    sys.exit(main())