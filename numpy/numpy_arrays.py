"""NUmPy arrays are a type of data structure that can be used to store data in a grid of N dimensions.
Key is "ndaarray" object that is a multi-dimensional array.
"""


import numpy as np

# Create a 1D array 6
b1 = np.random.randint(10, 20, 6)
print("B1:", b1)
# Create a 2D array 5x6 (rows x columns)
a = np.random.randint(0, 10, (5, 6))
print("A:", a, sep="\n")
# Create a 2D array 1x6
b = np.random.randint(10, 20, (1, 6))
print("B:", b)
# Create a 1D array 7 elements
c = np.random.randint(20, 30, (7, ))
print("C:", c)

# Understanding the slicing and indexing of numpy arrays
# Basic slicing:  Uses slicing, integers, and the : operator
#   (similar to Python lists).
# b[0, 1] select row 0 and column 1, scalar
# b[0, :] select row 0 and all columns
# b[:, 0] select all rows and column index 0, 1D (flattened)
# b[:, :] select all rows and all columns, (3, 1) 2D
print("B[0, 1]:", b[0, 1])
print("A[1, 1:3]:", a[1, 1:3])  # Row 1 columns 1 to 3
print("A[1:3, 2:4]:", a[1:3, 2:4], sep="\n")  # Row 1 columns 1 to 3
print("B[:, :]:", b[:, :])

# Advanced indexing: Uses integer arrays and slices.
# NumPy extends Python’s standard indexing mechanism by
#  using overloaded operators and specialized C-level optimizations.
# Key Python Features Used in NumPy Advanced Indexing
# 1.	Overloaded __getitem__() & __setitem__() Methods
# 2.	NumPy Arrays as Iterable Objects
# 3.	Vectorized Operations(Avoiding Python Loops)
# 4.	Memory Views and Indirect Indexing(Using NumPy’s nditer)
# 5.	Low-Level C Implementations for Performance

# Only in NumPy: Advanced Indexing
# Example 1. Fancy indexing: Uses integer arrays and slices.
print("Fancy indexing: A[[0, 1, 2], [5, 4, 3]]:", end="")
print(a[[0, 1, 2], [5, 4, 3]])
try:
    # Does not work in native python lists
    l1 = a.tolist()
    print("Fancy indexing: li[[0, 1, 2], [5, 4, 3]]:", end="")
    print(l1[[0, 1, 2], [5, 4, 3]])
except TypeError as e:
    print("Fancy indexing Error:", e)
print("Fancy indexing: B1[[0, 1, 2]: ", b1[[0, 1, 2]])

# Example 2. Boolean indexing: Uses boolean arrays.
mask = b1 > 15
print("Boolean indexing: B1[b1 > 15]:")
print(b1, mask, b1[mask])

# Example 3: Multidimensional fancy indexing


# Broadcasting: Is expanding the shape of the smaller array to match
# the shape of the larger array. For element-wise operations.
# The rules are:
# 1.	Compare shapes from right to left.
# 2.	Dimensions must be either:
# •	The same.
# •	One of them is 1 (it expands to match the other).
# •	Missing dimensions are assumed to be 1.

# Example 1: 1D array and 2D array
r = a + b
print(f"A ({a.shape}) + B ({b.shape}) = ({r.shape}):\n{r}")

# Example 2: Non-compatible shapes
try:
    r = a + c
    print(f"A ({a.shape}) + C ({c.shape}) = ({r.shape}):\n{r}")
except ValueError as e:
    print("Error:", e)

# Copies and Views: When you slice an array, you get a view of the original
#  array. Views are created when elements are accessed using offset and
#  strides.
# You can also create a copy of the array. Copies are created when you
# explicitly call the copy method. Advanced indexing always returns a copy.
a_view = a[:]
a_copy = a.copy()

# Change diagonal elements to 0
a_view[range(5), range(5)] = 0
print(f"A: base: {a.base} \n{a}")
print(f"A View: base:\n{a_view.base}\nView:\n{a_view}")
print(f"A Copy: base: {a_copy.base}\n{a_copy}")
