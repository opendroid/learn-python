"""
Learn about lists (equivalent to arrays in other languages). Be careful not to change the lists while iterating over them.


Author: opendroid
Email: openweb@outlook.com
License: MIT
"""
# Int arrays
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

# Refering elements
print(f"first-four prime numbers are: {primes[:4]}")
print(f"fifth-sixth-seventh prime numbers are: {primes[4:7]}")
print(f"ninth-tenth prime numbers are: {primes[-2:]}")
print(f"Length of first 10 primes are: {len(primes)}")

# Append: add next primes 31
primes.append(31)
print(f"New primes addes are: {primes[10:]}")
print(f"Length after adding 11th prime numner: {len(primes)}")

# Extend: Add next 9 primes
primes.extend([37, 41, 43, 47, 53, 59, 61, 67, 71])
print(f"Nine primes addes are: {primes[11:]}")
print(f"Length after adding 11th prime numner: {len(primes)}")

# Clear the slide
primes[:] = []
print(f"Primr array is cleared: {len(primes)}")

# Refering sring arrays
motto = "Pursuit of Excellence"
print(f"motto: {motto}, length={len(motto)}")
print(f"motto: first char: {motto[0]}, last: {motto[-1]}")


# reverse function reverses a string
def reverse(sentence):
    idx = -1
    reversed = []
    for i in range(len(sentence)):
        reversed.append(sentence[idx])
        idx -= 1
    return "".join(reversed)


# Print reverse
print(f"Reversed: {reverse(motto)}")


# Warning, do not change lists while iterating. If needed to change make a copy using list[:]
words = motto.split(" ")
print(f"words: {len(words)}")
# create a copy words[:]. Iterating over 'words' will create infinite loop
for word in words[:]:
    words.append(word)
print(f"Duplicated words: {words}")

# Initialization of arrays
# Method-1: List Multiplication, only be used for immutable elements like numbers.
# If you use it with mutable elements (like lists), all elements will refer to the
# same underlying object, leading to unexpected behavior.
array1_10 = [99] * 10  # initialize the int array
print(f"ten ints: {[f'[{i}]:{v}'  for i, v in enumerate(array1_10)]}")

# Method-2: Comprehension
array1_5 = [100 for _ in range(5)]  # initialize the int array using list-comprehension
print(f"five ints: {[f'[{i}]:{v}'  for i, v in enumerate(array1_5)]}")

# Method-3:
array1_10 = [].extend([22] * 10)
print(f"Ten ints: {[f'[{i}]:{v}'  for i, v in enumerate(array1_10)]}")
