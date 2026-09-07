"""This module provides functions for creating and working with random arrays.

Author: opendroid
Email: openweb@outlook.com
License: MIT
"""

from random import randint


def create_random(n):
    """
    Worker function that create and returns an array of n random numbers.
    """
    return [randint(0, 100) for _ in range(n)]