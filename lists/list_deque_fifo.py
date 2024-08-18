"""
This module compares FIFO queue implementation by list and deque collection


Author: opendroid
Email: openweb@outlook.com
License: MIT
"""

from collections import deque


def test_fifo_list(stack):
    """pop whole list queue (FIFO)"""
    while len(stack) > 0:
        _ = stack.pop(0)


def test_fifo_deque(stack):
    """pop whole deque stack"""
    while len(stack) > 0:
        _ = stack.popleft()


def test_queues(num_items):
    """Compares the performance of 'list' and 'deque' for FIFO operations.

    Args:
        num_items (int): The number of items to push and pop."""
    # Create two stacks
    stack_list, stack_deque = [], deque([])
    for i in range(num_items):
        stack_list.append(i)
        stack_deque.append(i)

    # Test them, see output by running `python -m cProfile list_stack.py`
    test_fifo_list(stack_list)
    test_fifo_deque(stack_deque)


"""
Test the performance of 'list' and 'deque' for FIFO queue operations.
"""

# Profiling results for 1M pops:
# $ python -m cProfile list_deque_stacks.py
#   2000002    0.172    0.000    0.172    0.000 {built-in method builtins.len}
#   1000000    0.055    0.000    0.055    0.000 {method 'append' of 'collections.deque' objects}
#   1000000    0.053    0.000    0.053    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#   1000000   79.628    0.000   79.628    0.000 {method 'pop' of 'list' objects}
#   1000000    0.049    0.000    0.049    0.000 {method 'popleft' of 'collections.deque' objects}

test_queues(1_000_000)
