# Learn Python 3 Concepts

A comprehensive repository and reference guide exploring Python 3 core concepts, built-in data structures, object-oriented programming, concurrency, standard libraries, algorithms, and data science fundamentals.

---

## Directory & Topic Overview

```text
learn-python/
├── lang-basics/                     # Python 3 Core Syntax, Types & Collections
│   ├── README.md                    # Core language concepts, tables & reference guide
│   ├── basic_data_types.py          # Primitive types, dynamic typing, type hints
│   ├── strings.py                   # String literals, formatting (f-strings), escaping
│   ├── repetition_operator.py       # Sequence repetition (*) gotchas (mutable vs immutable)
│   ├── loop_for.py                  # Loops, range(), enumerate(), continue/break/else
│   ├── loop_for_tuples.py           # Tuple unpacking and iteration
│   ├── lists.py                     # List manipulation APIs (append, extend, pop, sort)
│   ├── list_slicing.py              # Slicing patterns [start:end:step]
│   ├── list_of_class.py             # Storing & querying objects in lists, lambda helpers
│   ├── list_deque_fifo.py           # FIFO queues: list.pop(0) vs collections.deque.popleft() benchmark
│   ├── sets.py                      # Set operations (unions, intersections, differences)
│   ├── comprehensions.py            # List, set, and nested comprehensions
│   ├── exceptions.py                # Error handling (try / except / else / finally)
│   └── std_library_examples.py      # Standard library modules (os, sys, time, system introspection)
│
├── functions-and-oop/               # Functional Programming & Object-Oriented Design
│   ├── README.md                    # Parameter semantics (*args, **kwargs) & OOP guide
│   ├── args_immutable.py            # Passing immutable arguments
│   ├── args_mutable.py              # Passing mutable arguments & in-place mutations
│   ├── args_variable.py             # Variadic arguments (*args, **kwargs, unpacking)
│   └── classes.py                   # Object-oriented programming (classes, methods, state)
│
├── algorithms-and-ds/               # Data Structures & Algorithmic Problem Solving
│   ├── three_sum.py                 # 3-Sum algorithm (hash set / two-pointer approach)
│   ├── binary_tree.py               # Binary Tree traversals (pre-order, in-order, post-order)
│   ├── trie.py                      # Trie (Prefix Tree) implementation & recursive traversal
│   └── graphs_example_1.py          # Graph algorithms & representation
│
├── concurrency/                     # Parallelism & Multiprocessing
│   ├── README.md                    # Multiprocessing concepts & guide
│   ├── pool.py                      # multiprocessing.Pool (map, apply, async workers)
│   ├── task_rng.py                  # Random number generation worker tasks
│   └── benchmark_rng.py             # Performance benchmarking across worker pools
│
├── ip-relay-gpus/                   # Mathematical Modeling & Capacity Simulation
│   └── gpus-need.py                 # GPU capacity planning, Poisson/Normal arrival rate simulation
│
├── numpy/                           # Numerical Computing
│   └── numpy_basics.ipynb           # N-dimensional arrays, operations, indexing
│
├── pytorch/                         # Deep Learning & Tensors
│   └── matrices.ipynb               # Matrix operations and PyTorch tensor manipulation
│
├── stats/                           # Statistics, Data Analysis & Visualization
│   ├── data_frame_1.py              # Pandas DataFrame creation, indexing, CSV filtering
│   ├── stats_fundamentals.ipynb     # Descriptive statistics and probability fundamentals
│   ├── probability_distribution.ipynb # Common probability distributions
│   ├── advanced_statistics.ipynb    # Inferential statistics & hypothesis testing
│   ├── z_test_problems.ipynb        # Z-test hypothesis testing exercises
│   ├── linear_algebra.ipynb         # Linear algebra in data science
│   ├── data_wrangling.ipynb         # Data cleaning & wrangling techniques
│   ├── feature_engineering.ipynb    # Feature transformations & preparation
│   ├── seaborn.ipynb                # Statistical visualizations with Seaborn
│   ├── seaborn_caltech.ipynb        # Applied visualization case study
│   ├── aal_stats_project.ipynb      # End-to-end statistics analysis project
│   ├── inc_capstone_2.ipynb         # Capstone analytics notebook (Part 2)
│   ├── inc_capstone_3.ipynb         # Capstone analytics notebook (Part 3)
│   ├── numpy_arrays.py              # NumPy array manipulations
│   ├── plot_scatter.py              # Scatter plot generation
│   └── plot_box.py                  # Box-and-whisker plot visualization
│
└── data/                            # Datasets for Stats & Pandas Examples
    ├── ADANIPORTS.csv
    ├── AusApparalSales4thQrt2020.csv
    ├── HousePrices.csv
    ├── NSMES1988.csv
    ├── employee_satisfaction.csv
    ├── weather-data-gilroy.csv
    └── ... (additional test/data files)
```

---

## Core Concepts & Modules

### 1. Basic Data Types & Dynamic Typing

`lang-basics/basic_data_types.py`, `lang-basics/repetition_operator.py`

Python uses dynamic and implicit typing, with optional explicit casting:

```python
# Implicit typing
count = 5          # int
ratio = 3.14       # float
title = "Python 3" # str

# Repetition operator '*' gotcha
# Immutable types: creates new copies
matrix_safe = [[0] * 2 for _ in range(3)]

# Mutable types warning: `[[0] * 2] * 3` creates shared references!
```

---

### 2. Strings & Formatted Strings

`lang-basics/strings.py`, `lang-basics/basic_data_types.py`

- Single `'...'` and double `"..."` quotes for string literals.
- Multiline / docstring formatting using triple quotes `'''...'''` or `"""..."""`.
- Interpolated format strings (`f"..."`):

```python
what = 42
answer = f"The answer to the Ultimate Question of Life, the Universe, and Everything is {what}."
```

---

### 3. Lists & Queues

`lang-basics/lists.py`, `lang-basics/list_slicing.py`, `lang-basics/list_of_class.py`, `lang-basics/list_deque_fifo.py`

- **Slicing**: `list[start:end:step]` creates a shallow copy. Negative steps iterate backwards (e.g., `[::-1]`).
- **Mutation in Loops**: Always iterate over a copy `for item in original[:]` when appending or removing elements inside the loop.
- **FIFO Queues**: Use `collections.deque.popleft()` ($O(1)$) instead of `list.pop(0)` ($O(n)$) for high-performance queues:

```python
from collections import deque

queue = deque(["task1", "task2", "task3"])
queue.append("task4")
first = queue.popleft() # O(1)
```

---

### 4. Sets & Comprehensions

`lang-basics/sets.py`, `lang-basics/comprehensions.py`

- **Sets**: Unordered collections of unique elements with set operations (union `|`, intersection `&`, difference `-`).
- **Comprehensions**: Concise syntax for generating lists, sets, and dictionaries:

```python
# Filtered list comprehension
squares_odd = [x * x for x in range(10) if x % 2 != 0]

# Nested comprehension (cartesian product)
combos = [(x, y) for x in [1, 2, 3] for y in [4, 5, 6] if x != y]
```

---

### 5. Control Flow & Loops

`lang-basics/loop_for.py`, `lang-basics/loop_for_tuples.py`

- Iteration using `for ... in sequence`
- Loop sequences via `range(start, stop, step)`
- Index-value tracking with `enumerate(sequence)`
- Tuple unpacking during iteration:

```python
complex_numbers = [(1, -1), (2, -4), (3, -9)]
for real, imag in complex_numbers:
    print(f"Complex: {real} + {imag}i")
```

---

### 6. Functions & Object-Oriented Programming (OOP)

`functions-and-oop/args_variable.py`, `functions-and-oop/args_mutable.py`, `functions-and-oop/args_immutable.py`, `functions-and-oop/classes.py`

- **Variadic Arguments**: `*args` captures positional arguments as a `tuple`, and `**kwargs` captures keyword arguments as a `dict`.
- **Pass-by-Object-Reference**: Modifying mutable parameters (lists/dicts) in functions persists outside the function scope, whereas reassigning immutable parameters (ints/strings) does not.
- **Classes**: Encapsulation of state and behaviors:

```python
class Circle:
    def __init__(self, radius: float, coordinates=(0.0, 0.0)):
        self.radius = radius
        self.coordinates = coordinates

    def area(self) -> float:
        import math
        return math.pi * (self.radius ** 2)
```

---

### 7. Algorithms & Data Structures

`algorithms-and-ds/three_sum.py`, `algorithms-and-ds/binary_tree.py`, `algorithms-and-ds/trie.py`, `algorithms-and-ds/graphs_example_1.py`

- **3-Sum Problem**: $O(n^2)$ two-pointer / hash set algorithmic solution.
- **Binary Tree**: Node connections with pre-order, in-order, and post-order recursive and iterative traversals.
- **Trie (Prefix Tree)**: Efficient string and prefix storage, lookups, and frequency counting.
- **Graphs**: Node adjacency and traversal algorithms.

---

### 8. Concurrency & Multiprocessing

`concurrency/pool.py`, `concurrency/task_rng.py`, `concurrency/benchmark_rng.py`, `concurrency/README.md`

Python's `multiprocessing` library bypasses the Global Interpreter Lock (GIL) for CPU-bound tasks:

- `Pool.map()` / `Pool.starmap()`: Synchronous parallel mapping
- `Pool.apply_async()` / `Pool.map_async()`: Non-blocking asynchronous job dispatching
- Benchmarking worker pool sizes against single-threaded workloads.

---

### 9. Standard Library & Introspection

`lang-basics/std_library_examples.py`, `lang-basics/exceptions.py`

- `os`: File system operations, file metadata (`stat`), directory listing (`listdir`), CPU counts (`process_cpu_count`).
- `sys`: Python interpreter configuration, command-line arguments (`argv`), platform, recursion limits, and memory footprint (`getsizeof`).
- `exceptions`: Robust error handling with `try`, `except`, `else`, and `finally` blocks.

---

### 10. Data Science, Statistics & Machine Learning

`stats/`, `numpy/`, `pytorch/`

- **Pandas** (`stats/data_frame_1.py`): DataFrame creation, column indexing, series operations, CSV parsing.
- **NumPy** (`numpy/numpy_basics.ipynb`, `stats/numpy_arrays.py`): Matrix algebra, multi-dimensional array slicing, broadcasting.
- **PyTorch** (`pytorch/matrices.ipynb`): Tensor initialization, linear algebra operations, GPU/CPU tensor computations.
- **Statistics** (`stats/*.ipynb`): Probability distributions, Z-tests, descriptive analysis, correlation, and data visualization using Matplotlib & Seaborn.

---

## Environment Setup & Tools

### Conda (`conda mlx`)

```bash
# Activate environment
conda activate mlx

# Run any script with Python 3.12/3.13 in mlx env
python lang-basics/basic_data_types.py
```

### Performance Profiling

Profile any script execution time and function call hierarchy:

```bash
python -m cProfile -s cumulative path/to/script.py
```
