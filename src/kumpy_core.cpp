#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include <vector>
#include <stdexcept>
#include <sstream>
#include <algorithm>

namespace py = pybind11;

/**
 * Simple C++ Array class - our own implementation without numpy dependency
 */
class KumpyArray {
private:
    std::vector<double> data_;
    std::vector<size_t> shape_;
    size_t size_;

public:
    // Constructor from 1D vector
    KumpyArray(const std::vector<double>& data)
        : data_(data), shape_({data.size()}), size_(data.size()) {}

    // Constructor from 2D vector (for future expansion)
    KumpyArray(const std::vector<std::vector<double>>& data) {
        if (data.empty()) {
            shape_ = {0, 0};
            size_ = 0;
            return;
        }

        size_t rows = data.size();
        size_t cols = data[0].size();
        shape_ = {rows, cols};
        size_ = rows * cols;

        data_.reserve(size_);
        for (const auto& row : data) {
            if (row.size() != cols) {
                throw std::runtime_error("All rows must have the same length");
            }
            data_.insert(data_.end(), row.begin(), row.end());
        }
    }

    // Constructor with shape and initial value
    KumpyArray(const std::vector<size_t>& shape, double initial_value = 0.0)
        : shape_(shape) {
        size_ = 1;
        for (size_t dim : shape_) {
            size_ *= dim;
        }
        data_.resize(size_, initial_value);
    }

    // Getters
    const std::vector<double>& data() const { return data_; }
    std::vector<double>& data() { return data_; }
    const std::vector<size_t>& shape() const { return shape_; }
    size_t size() const { return size_; }

    // Element access
    double& operator[](size_t index) {
        if (index >= size_) {
            throw std::out_of_range("Index out of range");
        }
        return data_[index];
    }

    const double& operator[](size_t index) const {
        if (index >= size_) {
            throw std::out_of_range("Index out of range");
        }
        return data_[index];
    }

    // String representation
    std::string to_string() const {
        std::ostringstream oss;
        oss << "KumpyArray([";
        for (size_t i = 0; i < std::min(size_, size_t(10)); ++i) {
            if (i > 0) oss << ", ";
            oss << data_[i];
        }
        if (size_ > 10) oss << ", ...";
        oss << "])";
        return oss.str();
    }
};

/**
 * Element-wise addition of two arrays
 */
KumpyArray add_arrays(const KumpyArray& a, const KumpyArray& b) {
    if (a.size() != b.size()) {
        throw std::runtime_error("Arrays must have the same size");
    }

    std::vector<double> result_data(a.size());
    for (size_t i = 0; i < a.size(); i++) {
        result_data[i] = a[i] + b[i];
    }

    return KumpyArray(result_data);
}

/**
 * Element-wise subtraction of two arrays
 * TODO: Implement this yourself!
 * Hint: Follow the same pattern as add_arrays
 */
KumpyArray subtract_arrays(const KumpyArray& a, const KumpyArray& b) {
    if (a.size() != b.size()) {
        throw std::runtime_error("Arrays must have the same size");
    }
    std::vector<double> result_data(a.size());
    for (size_t i = 0; i < a.size(); i++) {
        result_data[i] = a[i] - b[i];
    }
    return KumpyArray(result_data);
    throw std::runtime_error("subtract_arrays not implemented yet - this is your exercise!");
}

/**
 * Element-wise multiplication of two arrays
 * TODO: Implement this yourself!
 * Hint: Follow the same pattern as add_arrays, but use * instead of +
 */
KumpyArray multiply_arrays(const KumpyArray& a, const KumpyArray& b) {
    // TODO: Your implementation here
    throw std::runtime_error("multiply_arrays not implemented yet - this is your exercise!");
}

/**
 * Element-wise division of two arrays
 * TODO: Implement this yourself!
 * Hint: Follow the same pattern as add_arrays, but use / instead of +
 * Don't forget to check for division by zero!
 */
KumpyArray divide_arrays(const KumpyArray& a, const KumpyArray& b) {
    // TODO: Your implementation here
    // Remember to check if b[i] == 0.0 and throw an error if so!
    throw std::runtime_error("divide_arrays not implemented yet - this is your exercise!");
}

/**
 * Scalar addition
 * TODO: Implement this yourself!
 * Hint: Follow the same pattern as multiply_scalar, but use + instead of *
 */
KumpyArray add_scalar(const KumpyArray& a, double scalar) {
    // TODO: Your implementation here
    throw std::runtime_error("add_scalar not implemented yet - this is your exercise!");
}

/**
 * Scalar multiplication - FULLY IMPLEMENTED as an example
 * This shows you the pattern to follow for other scalar operations
 */
KumpyArray multiply_scalar(const KumpyArray& a, double scalar) {
    std::vector<double> result_data(a.size());
    for (size_t i = 0; i < a.size(); i++) {
        result_data[i] = a[i] * scalar;
    }
    return KumpyArray(result_data);
}

/**
 * Scalar subtraction
 * TODO: Implement this yourself!
 * Hint: Follow the same pattern as multiply_scalar, but use - instead of *
 */
KumpyArray subtract_scalar(const KumpyArray& a, double scalar) {
    // TODO: Your implementation here
    throw std::runtime_error("subtract_scalar not implemented yet - this is your exercise!");
}

/**
 * Scalar division
 * TODO: Implement this yourself!
 * Hint: Follow the same pattern as multiply_scalar, but use / instead of *
 * Don't forget to check for division by zero first!
 */
KumpyArray divide_scalar(const KumpyArray& a, double scalar) {
    // TODO: Your implementation here
    // Remember to check if scalar == 0.0 and throw an error if so!
    throw std::runtime_error("divide_scalar not implemented yet - this is your exercise!");
}

// Pybind11 module definition
PYBIND11_MODULE(_core, m) {
    m.doc() = "Kumpy core C++ functions for element-wise array operations";

    // Bind the KumpyArray class
    py::class_<KumpyArray>(m, "KumpyArray")
        .def(py::init<const std::vector<double>&>())
        .def(py::init<const std::vector<std::vector<double>>&>())
        .def(py::init<const std::vector<size_t>&, double>(), py::arg("shape"), py::arg("initial_value") = 0.0)
        .def("data", [](const KumpyArray& a) { return a.data(); })
        .def("shape", &KumpyArray::shape)
        .def("size", &KumpyArray::size)
        .def("__getitem__", [](const KumpyArray& a, size_t i) { return a[i]; })
        .def("__setitem__", [](KumpyArray& a, size_t i, double value) { a[i] = value; })
        .def("__len__", &KumpyArray::size)
        .def("__repr__", &KumpyArray::to_string);

    // Bind the functions
    m.def("add_arrays", &add_arrays, "Element-wise addition of two arrays");
    m.def("subtract_arrays", &subtract_arrays, "Element-wise subtraction of two arrays");
    m.def("multiply_arrays", &multiply_arrays, "Element-wise multiplication of two arrays");
    m.def("divide_arrays", &divide_arrays, "Element-wise division of two arrays");
    m.def("add_scalar", &add_scalar, "Add scalar to array");
    m.def("subtract_scalar", &subtract_scalar, "Subtract scalar from array");
    m.def("multiply_scalar", &multiply_scalar, "Multiply array by scalar");
    m.def("divide_scalar", &divide_scalar, "Divide array by scalar");
}
