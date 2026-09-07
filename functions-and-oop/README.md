# Functions & Object-Oriented Programming (OOP)

This directory explores Python function design, parameter passing semantics (pass-by-object-reference), variadic arguments (`*args`, `**kwargs`), and Object-Oriented Programming (OOP) with classes and methods.

---

## 1. Parameter Passing: Pass-by-Object-Reference

Python uses **call-by-object-reference** (also known as *call-by-sharing*):

* Parameters are passed as references to existing objects in memory.
* The behavior inside the function depends on whether the object is **mutable** or **immutable**.

```text
┌───────────────────────────────────────────────────────────┐
│                    Caller's Variable                      │
└─────────────────────────────┬─────────────────────────────┘
                              │ Points to Object ID
                              ▼
                   ┌─────────────────────┐
                   │    Object Memory    │
                   └──────────▲──────────┘
                              │ Points to same Object ID
┌─────────────────────────────┴─────────────────────────────┐
│                    Function Parameter                     │
└───────────────────────────────────────────────────────────┘
```

### Immutable Arguments ([`args_immutable.py`](args_immutable.py))

* Primitive types (`int`, `float`, `str`, `tuple`, `frozenset`) cannot be modified in place.
* Reassigning a parameter (`a = -10` or `c = a + b`) binds the local parameter name to a **new object in memory**, leaving the caller's original object unchanged.

```python
def args_with_immutables(a, b, c):
    # a, b, c point to caller's objects initially
    c = a + b  # c is rebound to a newly created int object
    a = -10    # a is rebound locally
    # Caller's values remain unchanged
```

### Mutable Arguments ([`args_mutable.py`](args_mutable.py))

* Collection types (`list`, `dict`, `set`, custom class instances) can be modified in place.
* Calling mutating methods (e.g. `places.append(...)`, `dict.update(...)`) modifies the **underlying object**, and the changes persist in the caller's scope.

```python
def args_with_list(places, *capitals):
    for capital in capitals:
        places.append(capital)  # Mutates caller's 'places' list in place
```

---

## 2. Variadic Arguments & Unpacking ([`args_variable.py`](args_variable.py))

Python allows functions to accept variable numbers of positional and keyword arguments:

### Positional Packing (`*args`)

Packs extra positional arguments into a `tuple`:

```python
def mates(*args):
    # args is received as a tuple
    for idx, val in enumerate(args):
        print(f"[{idx}]: {val}")

mates("Alice", "Bob", "Charlie")
```

### Keyword Packing (`**kwargs`)

Packs named arguments into a `dict`:

```python
def prices(**items):
    # items is received as a dict
    for item, price in items.items():
        print(f"{item}: {price}")

prices(burger="$12.00", shake="$6.00", fries="$4.50")
```

### Argument Unpacking

Unpack sequences or dictionaries directly into function calls:

```python
state = {"state": "processing", "event": "deposit", "action": "add"}

def execute_state(state: str, event: str, action: str):
    print(f"state: {state}, event: {event}, action: {action}")

# Unpack dictionary keys/values into keyword arguments
execute_state(**state)
```

---

## 3. Object-Oriented Programming (OOP) ([`classes.py`](classes.py))

Classes define custom types with state (attributes) and behavior (methods).

```python
import math

class Circle:
    def __init__(self, radius: float, coordinates=(0.0, 0.0), name=None):
        self.radius = radius
        self.coordinates = coordinates
        self.name = name or f"Circle at {coordinates} r={radius}"

    def area(self) -> float:
        return math.pi * (self.radius ** 2)

    def circumference(self) -> float:
        return 2 * math.pi * self.radius

    def increment_radius(self, increment: float):
        self.radius += increment
```

### Key OOP Concepts Demonstrated

* **Constructor (`__init__`)**: Initializes instance attributes and default values.
* **`self` Reference**: Represents the specific instance on which a method is called.
* **Encapsulation**: Grouping related properties and behaviors together.
* **Instance Methods**: Access and modify the object's internal state.

---

## Running the Examples

Run any of the scripts using Python:

```bash
# Using conda mlx environment
conda activate mlx

python functions-and-oop/args_immutable.py
python functions-and-oop/args_mutable.py
python functions-and-oop/args_variable.py
python functions-and-oop/classes.py
```
