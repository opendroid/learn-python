"""This module provides ways of calling various Python Multiprocessing pool types.


Author: opendroid
Email: openweb@outlook.com
License: MIT
"""
from multiprocessing import Pool


def _invoke(kwargs):
    """
    Adapter to invoke a callable with keyword arguments.

    multiprocessing.Pool.map() only supports functions that take a single
    positional argument. This helper unpacks a (task, params) tuple and
    calls the task using keyword argument expansion.

    Args:
        args (tuple): (task, params)
            - task (callable): function to execute
            - params (dict): keyword arguments for the task

    Returns:
        Any: result of task(**params)

    Example:
        _invoke((funcA, {'n': 1}))  -> funcA(n=1)
        _invoke((funcB, {'n': 1, 'm': 2})) -> funcB(n=1, m=2)
    """
    task, params = kwargs
    return task(**params)


def sequential(task, n_times, n_cpus, **task_params):
    """
    Execute the task sequentially n_times in the current process.

    This serves as a baseline for comparing multiprocessing overhead
    versus pure Python execution.

    Args:
        task (callable): function to execute
        n_times (int): number of times to invoke the task
        n_cpus (int): ignored (kept for API consistency)
        **task_params: keyword arguments passed to task

    Returns:
        list: results of each task invocation

    Notes:
        - No parallelism is used.
        - Invocation pattern: task(**task_params)
    """
    return [task(**task_params) for _ in range(n_times)]



def pool_apply(task, n_times, n_cpus, **task_params):
    """
    Execute the task using Pool.apply().

    Each call to apply() is blocking, so tasks are executed one at a time,
    even though a pool of worker processes exists.

    Args:
        task (callable): function to execute
        n_times (int): number of times to invoke the task
        n_cpus (int): number of worker processes (mostly irrelevant here)
        **task_params: keyword arguments passed to task

    Returns:
        list: results of each task invocation

    Notes:
        - No parallelism across iterations due to blocking behavior.
        - Useful only for API comparison, not performance benchmarking.
    """
    with Pool(n_cpus) as pool:
        return [pool.apply(_invoke, [(task, task_params)]) for _ in range(n_times)]


def pool_apply_async(task, n_times, n_cpus, **task_params):
    """
    Execute the task in parallel using Pool.apply_async().

    Tasks are submitted asynchronously and executed in parallel across
    worker processes. Results are collected via AsyncResult.get().

    Args:
        task (callable): function to execute
        n_times (int): number of times to invoke the task
        n_cpus (int): number of worker processes
        **task_params: keyword arguments passed to task

    Returns:
        list: results in submission order

    Notes:
        - Enables true parallel execution.
        - Order is preserved because results are retrieved in submission order.
    """
    with Pool(n_cpus) as pool:
        futures = [pool.apply_async(_invoke, [(task, task_params)]) for _ in range(n_times)]
        return [f.get() for f in futures]

        
def pool_map(task, n_times, n_cpus, **task_params):
    """
    Execute the task in parallel using Pool.map().

    Tasks are distributed across worker processes and executed in parallel.
    Results are returned in the same order as the input sequence.

    Args:
        task (callable): function to execute
        n_times (int): number of times to invoke the task
        n_cpus (int): number of worker processes
        **task_params: keyword arguments passed to task

    Returns:
        list: results in input order

    Notes:
        - Uses a wrapper (_invoke) because map() only supports single-argument functions.
        - Blocks until all tasks complete.
    """
    with Pool(n_cpus) as pool:
        return pool.map(_invoke, [(task, task_params)] * n_times)


def pool_map_async(task, n_times, n_cpus, **task_params):
    """
    Execute the task in parallel using Pool.map_async().

    Similar to pool_map, but submits work asynchronously. However,
    calling .get() immediately makes this effectively blocking.

    Args:
        task (callable): function to execute
        n_times (int): number of times to invoke the task
        n_cpus (int): number of worker processes
        **task_params: keyword arguments passed to task

    Returns:
        list: results in input order

    Notes:
        - True asynchrony requires doing other work before calling .get().
        - Without that, behavior is equivalent to pool_map().
    """
    with Pool(n_cpus) as pool:
        async_result = pool.map_async(_invoke, [(task, task_params)] * n_times)
        return async_result.get()
