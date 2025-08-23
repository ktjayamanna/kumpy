#!/usr/bin/env python3
"""
Basic usage examples for Kumpy
"""

import kumpy
import sys
import os

# Add the parent directory to the path so we can import kumpy
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))


def main():
    print("Welcome to Kumpy - A NumPy-like library with C++ backend! 🔧")
    print("=" * 60)

    # Create some arrays
    print("\n1. Creating Arrays:")
    a = kumpy.Array([1, 2, 3, 4])
    b = kumpy.Array([5, 6, 7, 8])
    print(f"a = {a}")
    print(f"b = {b}")
  
    # Basic properties
    print("\nArray properties:")
    print(f"a.shape = {a.shape}")
    print(f"a.size = {a.size}")
    
    # Element-wise operations
    print("\n2. Element-wise Operations:")
    
    # Addition
    c = a + b
    print(f"a + b = {c}")
    
    # Subtraction
    d = b - a
    print(f"b - a = {d}")
    
    # Multiplication
    e = a * b
    print(f"a * b = {e}")
    
    # Division
    f = b / a
    print(f"b / a = {f}")

    # Division by zero
    try:
        g = a / kumpy.Array([0, 0, 0, 0])
        print(f"a / 0 = {g}")
    except RuntimeError as e:
        print("Division by zero caught!")
    
    # Scalar operations
    print("\n3. Scalar Operations:")
    g = a * 2
    print(f"a * 2 = {g}")
    
    h = a + 10
    print(f"a + 10 = {h}")
    
    i = a / 2
    print(f"a / 2 = {i}")
    
    # Show data as lists
    print("\n4. Data as Python lists:")
    print(f"a.tolist() = {a.tolist()}")
    print(f"b.tolist() = {b.tolist()}")
    print(f"c.tolist() = {c.tolist()}")

    print("\n All examples completed successfully!")


if __name__ == "__main__":
    main()
