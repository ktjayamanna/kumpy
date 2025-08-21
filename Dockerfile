# Use Ubuntu 22.04 as base image for better C++ toolchain support
FROM ubuntu:22.04

# Prevent interactive prompts during package installation
ENV DEBIAN_FRONTEND=noninteractive

# Set working directory
WORKDIR /workspace

# Install system dependencies
RUN apt-get update && apt-get install -y \
    # Python and pip
    python3 \
    python3-pip \
    python3-dev \
    python3-venv \
    # C++ build tools
    build-essential \
    cmake \
    g++ \
    gcc \
    make \
    # Git and development tools
    git \
    curl \
    wget \
    vim \
    nano \
    # Additional tools for debugging and development
    gdb \
    valgrind \
    pkg-config \
    # Clean up
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Create a non-root user for development
RUN useradd -m -s /bin/bash developer && \
    usermod -aG sudo developer && \
    echo "developer ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers

# Switch to the developer user
USER developer
WORKDIR /home/developer

# Set up Python environment
ENV PATH="/home/developer/.local/bin:$PATH"

# Install Python packages needed for C++ extension development
RUN pip3 install --user --upgrade pip setuptools wheel

# Install essential Python packages for numpy-like library development
RUN pip3 install --user \
    # Core packages for C++ extensions
    pybind11 \
    cython \
    # Build and packaging tools
    build \
    setuptools-scm \
    wheel \
    twine \
    # Development and testing tools
    pytest \
    pytest-cov \
    black \
    flake8 \
    mypy \
    # Documentation
    sphinx \
    # Jupyter for experimentation
    jupyter \
    ipython

# Set the working directory to the mounted volume
WORKDIR /workspace

# Set environment variables for C++ compilation
ENV CC=gcc
ENV CXX=g++

# Expose port for Jupyter if needed
EXPOSE 8888

# Default command
CMD ["/bin/bash"]
