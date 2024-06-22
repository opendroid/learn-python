"""
This module provides comprehension examples.


Author: opendroid
Email: openweb@outlook.com
License: MIT
"""

from math import pi

# Example-1: create a list of squares
squares = [x * x for x in range(10)]
print(f"squares: {squares}")
squares_odd_numbers = [x * x for x in range(10) if x % 2 == 1]
print(f"sq odd: {squares_odd_numbers}")

# Example-2: nested for loops
tuples = [(x, y) for x in range(3) for y in range(3)]
print(f"tuples: {tuples}")

# nested tuples
combs = [(x, y) for x in [1, 2, 3] for y in [3, 2, 1] if x != y]
print(f"combs: {combs}")

# nested functions
pi_values = [str(round(pi, i)) for i in range(4)]
print(f"pi values {pi_values}")


# Nested list comprehension explained.
# Transposed matrix: one item at a time
matrix = [[1, 2, 3, 4], [10, 20, 30, 40], [100, 200, 300, 400]]
transposed = []
for col in range(4):
    transposed_row = []
    for row in range(3):
        transposed_row.append(matrix[row][col])
    transposed.append(transposed_row)
print(f"transposed 1: {transposed}")
transposed.clear()

# Transposed: second approach
for col in range(4):
    transposed_row = []
    for row in matrix:
        transposed_row.append(row[col])
    transposed.append(transposed_row)
print(f"transposed 2: {transposed}")
transposed.clear()

# Transposed: third approach
for i in range(4):
    transposed.append([row[i] for row in matrix])
print(f"transposed 3: {transposed}")

# Transposed: forth approach (comprehension):
#  "[row[i] for row in matrix]" is evaluated in context of inner for loop: for i in range(4)
#   [row[0][0] row[1][0] row[2][0]]
#   [row[0][1] row[1][1] row[2][1]]
#   [row[0][2] row[1][2] row[2][2]]
#   [row[0][3] row[1][3] row[2][3]]
transposed = [[matrix[row][col] for row in range(3)] for col in range(4)]
print(f"transposed 4: {transposed}")

# Transposed: fifth  approach (comprehension):
transposed = [[row[i] for row in matrix] for i in range(4)]
print(f"transposed 5: {transposed}")
