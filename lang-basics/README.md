# Python 3 Language Basics & Core Built-ins

This directory contains reference implementations and scripts exploring Python 3 core syntax, data types, collection operations, control flow, error handling, and standard library utilities.

---

## Topic Index

| Topic | File | Key Concepts |
| :--- | :--- | :--- |
| **Primitives & Typing** | [`basic_data_types.py`](basic_data_types.py) | Dynamic vs explicit typing, `int`, `float`, `str`, type casting |
| **Strings & Formatting** | [`strings.py`](strings.py) | Quotes, escapes, multiline literals, f-strings |
| **Repetition Gotchas** | [`repetition_operator.py`](repetition_operator.py) | Sequence repetition `*`, reference copying vs new value copies |
| **Control Flow & Loops** | [`loop_for.py`](loop_for.py) | `for`, `range(start, stop, step)`, `enumerate()`, `continue` |
| **Tuple Iteration** | [`loop_for_tuples.py`](loop_for_tuples.py) | Tuple unpacking in loops, `for ... else` clause |
| **Lists & APIs** | [`lists.py`](lists.py) | `append`, `extend`, `pop`, `sort`, iterating over copies `[:]` |
| **List Slicing** | [`list_slicing.py`](list_slicing.py) | `[start:end:step]`, negative indexing, reverse strides |
| **Object Collections** | [`list_of_class.py`](list_of_class.py) | Lists of custom objects, lambda mapping/filtering helpers |
| **Queue Performance** | [`list_deque_fifo.py`](list_deque_fifo.py) | $O(n)$ `list.pop(0)` vs $O(1)$ `collections.deque.popleft()` |
| **Sets** | [`sets.py`](sets.py) | Deduplication, union (`\|`), intersection (`&`), difference (`-`) |
| **Comprehensions** | [`comprehensions.py`](comprehensions.py) | List/set comprehensions, conditional filtering, nested loops |
| **Exception Handling** | [`exceptions.py`](exceptions.py) | `try`, `except`, `else`, `finally`, context managers (`with`) |
| **Standard Library** | [`std_library_examples.py`](std_library_examples.py) | `os`, `sys`, `time`, runtime parameters, memory introspection |

---

## Key Concepts & Code Examples

### 1. Dynamic Typing & Repetition Gotchas

Python variables are dynamically bound. When using the repetition operator `*`:

* **Immutable elements** (`int`, `str`): create independent values.

* **Mutable elements** (`list`, `dict`): create multiple references to the **same underlying object**.

```python
# Safe 2D matrix initialization (independent inner lists)
matrix = [[0] * 3 for _ in range(3)]
matrix[0][0] = 1  # Only row 0 is updated

# Bug-prone pattern: `[[0] * 3] * 3` creates 3 references to the SAME row!
```

---

### 2. List Slicing & Mutation Safety

* Slicing follows `sequence[start:end:step]`. Negative step values iterate backwards.
* **Important**: Never append or delete from a list while iterating over it. Always iterate over a shallow copy (`for item in original[:]`).

```python
numbers = [1, 2, 3, 4, 5]

# Reverse list via slicing
reversed_nums = numbers[::-1]  # [5, 4, 3, 2, 1]

# Mutate safely in loop
for n in numbers[:]:
    if n % 2 == 0:
        numbers.append(n * 10)
```

---

### 3. FIFO Queues: `list` vs `collections.deque`

When implementing a First-In-First-Out (FIFO) queue:

* `list.pop(0)` is **$O(n)$** because all remaining elements must shift left in memory.
* `collections.deque.popleft()` is **$O(1)$** because it is implemented as a doubly-linked block list.

```python
from collections import deque

# High-performance queue
queue = deque()
queue.append("job1")
queue.append("job2")
next_job = queue.popleft()  # O(1) operation
```

---

### 4. Sets & Comprehensions

Sets provide $O(1)$ average-time lookups and set algebra:

```python
fruits_ca = {"grapes", "oranges", "lemons"}
fruits_fl = {"oranges", "grapefruit", "limes"}

common = fruits_ca & fruits_fl       # Intersection: {'oranges'}
all_fruits = fruits_ca | fruits_fl   # Union
unique_ca = fruits_ca - fruits_fl    # Difference: {'grapes', 'lemons'}
```

Comprehensions provide compact expressions for transformations and filtering:

```python
# Filtered comprehension
even_squares = [x**2 for x in range(10) if x % 2 == 0]

# Cartesian product with conditions
pairs = [(x, y) for x in range(3) for y in range(3) if x != y]
```

---

### 5. Robust Exception Handling

Proper resource management and exception flow with `try` / `except` / `else` / `finally` / `with`:

```python
def read_number(filename: str):
    try:
        with open(filename, "r") as f:
            return int(f.readline().strip())
    except FileNotFoundError:
        print(f"File {filename} not found.")
    except ValueError as err:
        print(f"Failed to parse integer: {err}")
    else:
        print("Successfully read value.")
    finally:
        print("Cleanup completed.")
```

---

## Running the Scripts

Run any script using Python within the `conda mlx` environment:

```bash
# Using conda mlx environment
conda activate mlx

python lang-basics/basic_data_types.py
python lang-basics/strings.py
python lang-basics/lists.py
python lang-basics/list_deque_fifo.py
python lang-basics/sets.py
python lang-basics/comprehensions.py
python lang-basics/exceptions.py
python lang-basics/std_library_examples.py
```
