"""
This modules experiements with basic data types.
"""

# Data types in python are implicit

a = int(5)  # explicit
b = 5  # Implicitley assuming that b is a int
print("a=", a, "b=", b)  # Print is a variadic function
print(f"Formatted string print: a={a}, b={b}")
print(f"Single quote a={a} b={b}")

c = float(3.14)
d = 3.14  # Implicit

name = str("DD Thakur")
name1 = "DD Thakur"
print(name, name1)


# Pre-formatted string
poem = """
    Woods are lovely dark and deep

Miles to go before I sleep,
Miles to go before I sleep,
"""
print(poem)

# Lists are arrays.

numbers = [1, 2]  # size is two index: 0, 1
print(f"Numbers initialized: {numbers}")
numbers[0] = 0
print(f"Changed Number: {numbers}")

# Option 1: Use multiply, one value in all place
n10_1 = [1] * 10  # creates an list of 10 numbers all are 1
print(f"n10_1: {n10_1}")

# Option 2: Brute force,
n10 = []  # Create a empty lisy
for i in range(10):  # 0...9
    n10.append(i)  # Add one element at a time
    print(f"{i}: {n10}")

print(f"Done: {n10}")
"""
0: [0]
1: [0, 1]
2: [0, 1, 2]

9: [0, 1, 2, ... 9]
Done: [0, 1, 2, .. 9]
"""

# Option 3: Initialize it, you have to type all
squares = list([0, 1, 9, 16, 25, 36, 49, 64])
sqs = [0, 1, 9, 16, 25, 36, 49, 64]

cubes = [0, 8, 27, 64]  # Implicit


# Option 4: Use comprehension, will apply pattern
print(f"i = {i}")
n10_4 = ["DD number: " + str(i) for i in range(10)]
print(f"n10_4: {n10_4}")
