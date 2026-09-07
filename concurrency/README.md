# Python Concurrency & Multiprocessing

This directory explores Python concurrency with a focus on CPU-bound parallelism using the [`multiprocessing`](https://docs.python.org/3/library/multiprocessing.html) package, worker pool dispatching patterns, and performance benchmarking.

---

## Why Multiprocessing in Python?

Standard Python (CPython) uses a **Global Interpreter Lock (GIL)**, which ensures that only one native thread executes Python bytecode at any given moment.

| Model | Module | Best Suited For | GIL Impact |
| :--- | :--- | :--- | :--- |
| **Multiprocessing** | `multiprocessing` | **CPU-bound tasks** (e.g. numerical computing, simulations, image processing) | **Bypasses GIL** by spawning independent OS processes with separate memory spaces |
| **Multithreading** | `threading` | **I/O-bound tasks** (e.g. network requests, disk reads/writes) | Constrained by GIL for CPU execution |
| **Asynchronous I/O** | `asyncio` | **High-concurrency network I/O** (e.g. web scrapers, API servers, websockets) | Single-threaded event loop |

---

## `multiprocessing.Pool` Dispatching Methods

A `Pool` manages a pool of worker processes to which jobs are offloaded.

```text
                     ┌──────────────────┐
                     │   Main Process   │
                     └────────┬─────────┘
                              │ Dispatches Tasks
        ┌─────────────────────┼─────────────────────┐
        ▼                     ▼                     ▼
┌───────────────┐     ┌───────────────┐     ┌───────────────┐
│ Worker Proc 1 │     │ Worker Proc 2 │     │ Worker Proc N │
└───────────────┘     └───────────────┘     └───────────────┘
```

### Method Comparison Matrix

| Method | Parallel? | Blocking? | Input Ordering Preserved? | Input Signature | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **`apply(func, args, kwds)`** | ❌ No | ✅ Yes | N/A | `*args`, `**kwds` | Runs one task at a time; blocks the main thread. |
| **`apply_async(func, args, kwds)`** | ✅ Yes | ❌ No | ✅ (when iterating futures) | `*args`, `**kwds` | Returns an `AsyncResult` immediately. Runs concurrently across workers. |
| **`map(func, iterable, chunksize)`** | ✅ Yes | ✅ Yes | ✅ Yes | Single argument per item | Divides iterable into chunks and executes in parallel. Blocks until all are done. |
| **`map_async(func, iterable)`** | ✅ Yes | ❌ No | ✅ Yes | Single argument per item | Non-blocking variant of `map()`. Returns `AsyncResult`. |
| **`imap(func, iterable)`** | ✅ Yes | ❌ Lazy | ✅ Yes | Single argument per item | Lazy generator version of `map()`. Yields results as they become ready. |
| **`imap_unordered(func, iterable)`** | ✅ Yes | ❌ Lazy | ❌ No | Single argument per item | Yields results as soon as any worker completes (faster consumption). |
| **`starmap(func, iterable)`** | ✅ Yes | ✅ Yes | ✅ Yes | Sequence of tuples `[(arg1, arg2), ...]` | Like `map()`, but unpacks tuples as positional arguments `func(*item)`. |
| **`starmap_async(func, iterable)`** | ✅ Yes | ❌ No | ✅ Yes | Sequence of tuples | Non-blocking version of `starmap()`. |

### The `AsyncResult` Object

Asynchronous pool methods return an `AsyncResult` instance:

* `result.get(timeout=None)`: Wait for and retrieve the return value. Raises exception if task failed.
* `result.wait(timeout=None)`: Wait for the result to complete without fetching value.
* `result.ready()`: Returns `True` if the call has completed.
* `result.successful()`: Returns `True` if the call completed without raising an exception.

---

## Code Structure & Modules

### 1. [`pool.py`](pool.py)

Implements and wraps five execution patterns for benchmarking:

* `_invoke(kwargs)`: Adapter pattern resolving `Pool.map()`'s single-argument limitation by unpacking `(task, params_dict)` into `task(**params_dict)`.
* `sequential(task, n_times, n_cpus, **task_params)`: Pure single-threaded Python baseline.
* `pool_apply(task, n_times, n_cpus, **task_params)`: Iterative blocking `apply()`.
* `pool_apply_async(task, n_times, n_cpus, **task_params)`: True parallel async dispatching using futures collected with `.get()`.
* `pool_map(task, n_times, n_cpus, **task_params)`: Parallel synchronous chunked mapping.
* `pool_map_async(task, n_times, n_cpus, **task_params)`: Parallel async mapping.

### 2. [`task_rng.py`](task_rng.py)

Contains the CPU-bound worker task:

* `create_random(n)`: Generates an array of $n$ pseudo-random integers (`randint(0, 100)`).

### 3. [`benchmark_rng.py`](benchmark_rng.py)

Automated multi-dimensional benchmark suite measuring execution latency and throughput:

* **Sweep Dimensions**:
  * Task sizes: `100,000`, `1,000,000`, `5,000,000` elements
  * Run counts: `1`, `2`, `4`, `8`, `16`, `32` tasks
  * CPU sweep: `1`, `2`, `4`, `8`, and max available hardware cores
* **Metrics**: Average latency ($ms$), median latency ($P50$), and throughput ($M\text{ elements/sec}$).
* **Visualization**: Generates Matplotlib scaling curves (`plot_scaling`) showing throughput vs CPU count.

---

## Core Multiprocessing Primitives

Beyond worker pools, the Python `multiprocessing` package provides lower-level primitives:

```python
import multiprocessing as mp

# 1. Process: Direct lifecycle control
p = mp.Process(target=worker_func, args=(arg1,))
p.start()
p.join()

# 2. Queue & Pipe: Inter-Process Communication (IPC)
queue = mp.Queue()
parent_conn, child_conn = mp.Pipe()

# 3. Lock & Semaphore: Synchronization
lock = mp.Lock()
with lock:
    # Critical section
    pass

# 4. Shared Memory: Value and Array
shared_num = mp.Value('d', 0.0)      # double precision float
shared_arr = mp.Array('i', range(10)) # array of integers
```

---

## Running the Benchmark

Activate the environment and execute the benchmark:

```bash
# Using conda mlx environment
conda activate mlx

# Run the benchmark suite
python concurrency/benchmark_rng.py
```
