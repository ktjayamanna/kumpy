from setuptools import setup, Extension
from pybind11.setup_helpers import Pybind11Extension, build_ext
from pybind11 import get_cmake_dir
import pybind11

# Define the extension module
ext_modules = [
    Pybind11Extension(
        "kumpy._core",
        [
            "src/kumpy_core.cpp",
        ],
        include_dirs=[
            # Path to pybind11 headers
            pybind11.get_include(),
        ],
        language='c++',
        cxx_std=17,
    ),
]

setup(
    name="kumpy",
    version="0.1.0",
    author="Kaveen Jayamanna",
    author_email="kaveen.jayamanna@gmail.com",
    description="A simple NumPy-like library for learning C++ extensions",
    long_description=open("README.md").read() if open("README.md") else "",
    long_description_content_type="text/markdown",
    url="https://github.com/ktjayamanna/kumpy",
    packages=["kumpy"],
    ext_modules=ext_modules,
    cmdclass={"build_ext": build_ext},
    zip_safe=False,
    python_requires=">=3.7",
    install_requires=[
        "pybind11>=2.6.0",
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: C++",
    ],
)
