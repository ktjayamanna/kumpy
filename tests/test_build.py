#!/usr/bin/env python3
"""
Quick test to verify the build works and show what's implemented
"""

try:
    import kumpy
    print("Kumpy imported successfully!")
    
    # Test basic array creation
    a = kumpy.Array([1, 2, 3])
    print(f"Array creation works: {a}")
    
    # Test what should work
    print("\nTesting implemented features:")
    
    # Array addition should work
    b = kumpy.Array([4, 5, 6])
    try:
        result = a + b
        print(f"Array addition: {a} + {b} = {result}")
    except Exception as e:
        print(f"Array addition failed: {e}")
    
    # Scalar multiplication should work
    try:
        result = a * 2
        print(f"Scalar multiplication: {a} * 2 = {result}")
    except Exception as e:
        print(f"Scalar multiplication failed: {e}")
    
    print("\nTesting unimplemented features (should show helpful messages):")
    
    # These should show "not implemented" messages
    result = a + 5  # scalar addition
    result = a - b  # array subtraction
    
    print("\nReady to start learning! Run: python examples/learning_example.py")
    
except ImportError as e:
    print(f"Failed to import kumpy: {e}")
    print("You may need to build the extension first:")
    print("   pip install -e .")
except Exception as e:
    print(f"Unexpected error: {e}")
