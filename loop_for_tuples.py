# For loop over tuples

complex_numbers = [(1, -(1**2)), (2, -(2**2)), (3, -(3**3))]

# Iterare of numbers and each value
for complex in complex_numbers:
    for i, val in enumerate(complex):
        print(f"Complex:{i} is {val} ")
else:
    print("Finished")

# Iterate over tuple values
for real, img in complex_numbers:
    print(f"Complex: {real} + {img}i")
