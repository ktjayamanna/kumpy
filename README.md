# Kumpy Learning Guide

Welcome to your C++ and Python integration learning journey! This guide will help you understand how to implement the missing functionality step by step.

## What's Already Implemented (Your Examples)

**Array Addition** (`add_arrays`) - Study this as your main example
**Scalar Multiplication** (`multiply_scalar`) - Study this for scalar operations
**KumpyArray class** - The C++ array container
**Python Array wrapper** - The Python interface

## What You Need to Implement (Your Exercises)

1. **Scalar Addition** (`add_scalar`)
2. **Array Subtraction** (`subtract_arrays`)
3. **Array Multiplication** (`multiply_arrays`)
4. **Array Division** (`divide_arrays`)
5. **Scalar Subtraction** (`subtract_scalar`)
6. **Scalar Division** (`divide_scalar`)

## Step-by-Step Learning Process

### Step 1: Build and Test Current State
```bash
# Build the extension
pip install -e .

# Test what works
python examples/learning_example.py
```

### Step 2: Study the Working Examples

Open `src/kumpy_core.cpp` and look at these two functions:

**Array Addition (lines ~91-105):**
```cpp
KumpyArray add_arrays(const KumpyArray& a, const KumpyArray& b) {
    if (a.size() != b.size()) {
        throw std::runtime_error("Arrays must have the same size");
    }
    
    std::vector<double> result_data(a.size());
    for (size_t i = 0; i < a.size(); i++) {
        result_data[i] = a[i] + b[i];  // ← The key operation
    }
    
    return KumpyArray(result_data);
}
```

**Scalar Multiplication (lines ~155-162):**
```cpp
KumpyArray multiply_scalar(const KumpyArray& a, double scalar) {
    std::vector<double> result_data(a.size());
    for (size_t i = 0; i < a.size(); i++) {
        result_data[i] = a[i] * scalar;  // <- The key operation
    }
    return KumpyArray(result_data);
}
```

### Step 3: Implement Your First Function

Start with **scalar addition** (`add_scalar`). Find this in the file:

```cpp
KumpyArray add_scalar(const KumpyArray& a, double scalar) {
    // TODO: Your implementation here
    throw std::runtime_error("add_scalar not implemented yet - this is your exercise!");
}
```

Replace it with:
```cpp
KumpyArray add_scalar(const KumpyArray& a, double scalar) {
    std::vector<double> result_data(a.size());
    for (size_t i = 0; i < a.size(); i++) {
        result_data[i] = a[i] + scalar;  // <- Change * to +
    }
    return KumpyArray(result_data);
}
```

### Step 4: Test Your Implementation
```bash
# Rebuild
pip install -e .

# Test
python examples/learning_example.py
```

You should see scalar addition working now!

### Step 5: Continue with the Rest

Follow the same pattern for:
- `subtract_arrays`: Use `-` instead of `+`
- `multiply_arrays`: Use `*` instead of `+`
- `divide_arrays`: Use `/` instead of `+` (but check for zero!)
- `subtract_scalar`: Use `-` instead of `*`
- `divide_scalar`: Use `/` instead of `*` (but check for zero!)

## Key C++ Concepts You're Learning

1. **Function Parameters**: `const KumpyArray& a` (reference, no copying)
2. **STL Vectors**: `std::vector<double>` for dynamic arrays
3. **Loops**: `for (size_t i = 0; i < a.size(); i++)`
4. **Error Handling**: `throw std::runtime_error(...)`
5. **Object Construction**: `return KumpyArray(result_data)`

## Key Python-C++ Integration Concepts

1. **Pybind11 Binding**: How C++ functions become Python functions
2. **Object Wrapping**: How `KumpyArray` becomes `Array`
3. **Exception Handling**: How C++ exceptions become Python exceptions
4. **Memory Management**: Pybind11 handles this automatically!

## Common Mistakes to Avoid

1. **Division by Zero**: Always check `if (scalar == 0.0)` or `if (b[i] == 0.0)`
2. **Size Mismatch**: Always check `if (a.size() != b.size())`
3. **Syntax Errors**: C++ is strict about semicolons and braces
4. **Rebuild**: Always run `pip install -e .` after changing C++ code

## Success Criteria

When you're done, `python examples/learning_example.py` should show:
- All operations working
- Success messages for everything
- No "not implemented" messages

## Next Steps After Completion

1. Add more operations (sum, mean, etc.)
2. Implement 2D array support
3. Add broadcasting for different sized arrays
4. Optimize with SIMD instructions
5. Add comprehensive tests

