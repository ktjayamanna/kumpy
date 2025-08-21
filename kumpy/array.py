"""
Array class for Kumpy - Python wrapper around C++ implementation
"""

from typing import Union, List, Tuple
try:
    from ._core import KumpyArray, add_arrays, subtract_arrays, multiply_arrays, divide_arrays
    from ._core import add_scalar, subtract_scalar, multiply_scalar, divide_scalar
except ImportError as e:
    print(f"Warning: Could not import C++ extension: {e}")
    print("You may need to build the extension first with: pip install -e .")
    # Create dummy classes for development
    class KumpyArray:
        def __init__(self, *args, **kwargs):
            raise ImportError("C++ extension not available")

class Array:
    """
    A simple array class that wraps C++ implementation for element-wise operations.

    This is designed to be a learning tool for understanding how to create
    Python extensions with C++.
    """

    def __init__(self, data: Union[List, Tuple, List[List], 'Array']):
        """
        Initialize a Kumpy array.

        Args:
            data: Input data as list, tuple, nested list, or another Array
        """
        if isinstance(data, Array):
            self._core_array = data._core_array
        elif isinstance(data, (list, tuple)):
            # Check if it's a nested list (2D)
            if data and isinstance(data[0], (list, tuple)):
                # Convert to list of lists of floats
                float_data = [[float(x) for x in row] for row in data]
                self._core_array = KumpyArray(float_data)
            else:
                # 1D data
                float_data = [float(x) for x in data]
                self._core_array = KumpyArray(float_data)
        else:
            raise TypeError("Data must be a list, tuple, nested list, or Array")

    @property
    def data(self) -> List[float]:
        """Get the underlying data as a Python list."""
        return self._core_array.data()
    
    @property
    def shape(self) -> Tuple[int, ...]:
        """Get the shape of the array."""
        return tuple(self._core_array.shape())

    @property
    def size(self) -> int:
        """Get the total number of elements."""
        return self._core_array.size()

    def __repr__(self) -> str:
        return f"Array({self.tolist()})"

    def __str__(self) -> str:
        return repr(self._core_array)

    def __len__(self) -> int:
        return self._core_array.size()

    def __getitem__(self, key):
        if isinstance(key, int):
            return self._core_array[key]
        else:
            # For slicing, convert to list and slice
            data_list = self.tolist()
            return Array(data_list[key])

    def __setitem__(self, key, value):
        if isinstance(key, int):
            self._core_array[key] = float(value)
        else:
            raise NotImplementedError("Slice assignment not yet implemented")

    def tolist(self) -> List:
        """Convert array to Python list."""
        return self._core_array.data()

    # Element-wise arithmetic operations using C++ implementation
    def __add__(self, other):
        """Element-wise addition - FULLY IMPLEMENTED as example."""
        try:
            if isinstance(other, Array):
                # This one IS implemented - it should work!
                result_core = add_arrays(self._core_array, other._core_array)
                result = Array.__new__(Array)
                result._core_array = result_core
                return result
            elif isinstance(other, (int, float)):
                result_core = add_scalar(self._core_array, float(other))
                result = Array.__new__(Array)
                result._core_array = result_core
                return result
            else:
                return NotImplemented
        except RuntimeError as e:
            if "not implemented yet" in str(e):
                print(f"{e}")
                print("Hint: Check src/kumpy_core.cpp to implement this function!")
                return None
            else:
                raise

    def __sub__(self, other):
        """Element-wise subtraction - NOT YET IMPLEMENTED."""
        try:
            if isinstance(other, Array):
                result_core = subtract_arrays(self._core_array, other._core_array)
                result = Array.__new__(Array)
                result._core_array = result_core
                return result
            elif isinstance(other, (int, float)):
                result_core = subtract_scalar(self._core_array, float(other))
                result = Array.__new__(Array)
                result._core_array = result_core
                return result
            else:
                return NotImplemented
        except RuntimeError as e:
            if "not implemented yet" in str(e):
                print(f"{e}")
                print("Hint: Check src/kumpy_core.cpp to implement this function!")
                return None
            else:
                raise

    def __mul__(self, other):
        """Element-wise multiplication."""
        try:
            if isinstance(other, Array):
                result_core = multiply_arrays(self._core_array, other._core_array)
                result = Array.__new__(Array)
                result._core_array = result_core
                return result
            elif isinstance(other, (int, float)):
                # This one IS implemented - it should work!
                result_core = multiply_scalar(self._core_array, float(other))
                result = Array.__new__(Array)
                result._core_array = result_core
                return result
            else:
                return NotImplemented
        except RuntimeError as e:
            if "not implemented yet" in str(e):
                print(f"{e}")
                print(" Hint: Check src/kumpy_core.cpp to implement this function!")
                return None
            else:
                raise

    def __truediv__(self, other):
        """Element-wise division - NOT YET IMPLEMENTED."""
        try:
            if isinstance(other, Array):
                result_core = divide_arrays(self._core_array, other._core_array)
                result = Array.__new__(Array)
                result._core_array = result_core
                return result
            elif isinstance(other, (int, float)):
                result_core = divide_scalar(self._core_array, float(other))
                result = Array.__new__(Array)
                result._core_array = result_core
                return result
            else:
                return NotImplemented
        except RuntimeError as e:
            if "not implemented yet" in str(e):
                print(f"{e}")
                print(" Hint: Check src/kumpy_core.cpp to implement this function!")
                return None
            else:
                raise

    # Right-hand side operations
    def __radd__(self, other):
        return self.__add__(other)

    def __rmul__(self, other):
        return self.__mul__(other)


def array(data: Union[List, Tuple, List[List]]) -> Array:
    """
    Create a Kumpy array.

    Args:
        data: Input data as list, tuple, or nested list

    Returns:
        Array: A new Kumpy array
    """
    return Array(data)
