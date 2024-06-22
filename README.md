# learn-python
Learn python language

### Strings
Strings in Pythin can be enclosd by `'Single quotes: Pursuit of excellence'` or `"Double quotes: Pursuit of excellence"`. Strings can be escaped using backslash `\` character, for example `\n` is newline, and `\t` is tab. Literal strings are enclosed within triple single-quotes or triple double-quotes. For example `'''String literal'''` or `"""String literal"""`. An escape in string literal means continuation of next line.

#### Formatted Stings
The strings can fill in variables values, e.g.:
```python
what = 42
# use the f-string mechanism
answer = f"The answer to the Ultimate Question of Life, the Universe, and Everything is {what}."
```

### Lists
Refers to an array. You can create a list, and append, extend or clear it.
```python
# Create and array:
primes = []
primes.extend([2,3,5,7]) # Add 4 primes
primes.append(11) # Add another prime
primes[:] = [] # clear the list
```

While iterating over a list do not update the list. If you need to update the list in a loop iterate over copy. 
```python
repeat = [1, 2, 3]
for value in repeat[:]:  # repeat[:] creates a copy
    repeat.append(value)
# repeat now is [1,2,3,1,2,3]
```

#### List APIs
The [Data Structures - More on lists](https://docs.python.org/3/tutorial/datastructures.html) documents all APIs. Some are:

```python
colors = ["violet", "indigo", "blue"]

# Stack, push (append function)
colors.append("green")
colors.append("yellow")

# Pop first element
violet = colors.pop(0) # colors now is: ["indigo", "blue", "green", "green"]

# Sort 
colors.sort(reverse = True)
```

## Control Statements

### for
A for-loop is used for iterating over a list, a tuple, a dictionary, a set, or a string sequence. 

```python
squares = [1**2, 2**2, 3**2, 4**2]
# Print each value
for val in squares:
    print(f"val = {val}") 
```

Use enumerate to get a index. 
```python
cubes = [1**3, 2**3, 3**3, 4**3]
for i, c in enumerate(cubes):
    print(f"cube[{i}]={c}")
```

for-loop can work with `range()` function.


# Utilities

```shell
# Masure time of each function execution

python -m cProfile file.py
```
