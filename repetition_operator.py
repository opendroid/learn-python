# repetition operator '*' gotchas

# The * operator, when used with sequences (like lists, strings, tuples),
# creates a repetition of the sequence.
#
# It repeats the contents of original n times.
# Behavior depends on whether the elements inside the sequence
# are mutable or immutable.

# Immutable: int, str, float, tuple:
#            makes separate value copies
# Mutatable: list, dict, set, custom objects: 
#            Be careful Repeats references, not new objects


# Immutable, int 0 is created * 2 times.
mat1 = [[0] * 2 for i in range(3)]
# [[0, 0], [0, 0], [0, 0]]
print("Mat1 created: ", mat1)
# Print same ID
for i in range(len(mat1)):
    print(f"id mat1[{i}]: {id(mat1[i])}")
# Update a immutable, only one changed
mat1[1][1] = 1
print("Mat1 (1,1) updated: ", mat1)

# Mutable:
#  Inner [0] * 2 is list of immutables
#  Outer [] * 3 repears mutable list 3 times
#  Basically same [0, 0] is repeated 3 times
mat2 = [[0] * 2] * 3
# Print same ID
for i in range(len(mat2)):
    print(f"id mat2[{i}]: {id(mat2[i])}")

# Change 1, change column
mat2[1][1] = 1
print("Mat2 col 1 updated: ", mat2)

# Mutable 2, dictionary example
dict_list = [{i: i for i in range(5)}] * 3
print(dict_list)
for i in range(len(dict_list)):
    print(f"id dict1[{i}]: {id(dict_list[i])}")
dict_list[0][4] = 40
# all elements in list [*][4] will be changed
print(dict_list)
