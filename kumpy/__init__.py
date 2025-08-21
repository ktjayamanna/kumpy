"""
Kumpy - A simple NumPy-like library for learning C++ extensions

This is a beginner-friendly project to understand how to write Python libraries
that utilize C++ underneath, focusing on element-wise arithmetic operations.
"""

__version__ = "0.1.0"

# Import the C++ extension module
try:
    from ._core import *
except ImportError as e:
    print(f"Warning: Could not import C++ extension: {e}")
    print("You may need to build the extension first with: pip install -e .")

# Import Python wrapper functions
from .array import Array

__all__ = ["Array", "__version__"]
