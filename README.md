# Kumpy 🐍🔧

A simple NumPy-like library for learning how to write Python extensions with C++. This project focuses on element-wise arithmetic operations and is designed as a beginner-friendly introduction to creating Python libraries that utilize C++ underneath.

## Features

- Element-wise arithmetic operations (addition, subtraction, multiplication, division)
- Scalar operations
- Simple Array class with NumPy-like interface
- C++ backend for performance
- Docker development environment with VS Code support

## Development Environment

This project includes a complete Docker development environment that you can use with VS Code Remote Containers.

### Prerequisites

- Docker
- VS Code with Remote-Containers extension

### Getting Started

1. Clone this repository
2. Open in VS Code
3. When prompted, click "Reopen in Container" or use Command Palette: "Remote-Containers: Reopen in Container"
4. The development environment will be automatically set up with all dependencies

### Manual Docker Setup

If you prefer to use Docker manually:

```bash
# Build the Docker image
docker build -t kumpy-dev .

# Run the container
docker run -it -v $(pwd):/workspace kumpy-dev
```

## Building the Extension

Once in the development environment:

```bash
# Install in development mode
pip install -e .

# Or build manually
python setup.py build_ext --inplace
```

## Usage

```python
import kumpy

# Create arrays
a = kumpy.Array([1, 2, 3, 4])
b = kumpy.Array([5, 6, 7, 8])

# Element-wise operations
c = a + b  # [6, 8, 10, 12]
d = a * 2  # [2, 4, 6, 8]

print(c)  # Array([6.0, 8.0, 10.0, 12.0])
```

## Project Structure

```
kumpy/
├── .devcontainer/
│   └── devcontainer.json    # VS Code dev container configuration
├── src/
│   └── kumpy_core.cpp       # C++ implementation
├── kumpy/
│   ├── __init__.py          # Package initialization
│   └── array.py             # Python Array class
├── tests/                   # Test files (to be added)
├── Dockerfile               # Development environment
├── setup.py                 # Build configuration
└── README.md               # This file
```

## Learning Goals

This project is designed to help you learn:

1. **Pybind11**: How to create Python bindings for C++ code
2. **NumPy C API**: Working with NumPy arrays in C++
3. **Python Extensions**: Building and packaging Python extensions
4. **Docker Development**: Using containerized development environments
5. **C++ Fundamentals**: Basic C++ programming for numerical computing

## Next Steps

1. Build and test the basic functionality
2. Add more array operations (sum, mean, etc.)
3. Implement broadcasting for operations between arrays of different shapes
4. Add comprehensive tests
5. Optimize performance with SIMD instructions
6. Package and publish to PyPI

## Contributing

This is a learning project, but contributions and suggestions are welcome!

## License

MIT License - see LICENSE file for details.
# kumpy
