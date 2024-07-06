"""This module provides examples of various libraries.


Author: opendroid
Email: openweb@outlook.com
License: MIT
"""

import os
import sys
import time
import glob


def os_examples():
    """OS Examples. Uses time to display ns in string."""
    curr_directory = os.getcwd()
    stats = os.stat(curr_directory)
    files = os.listdir(curr_directory)
    print(f"Current Directory: {curr_directory}")
    print(f"Stats: size: {stats.st_size} Bytes")
    print(f"Created at: {time.ctime(stats.st_mtime)}, ", end="")
    print(f"Modifiled at: {time.ctime(stats.st_atime)}")
    print(f"Files: {[file for file in files]}")
    return


def sys_examples():
    """sys library provides access to python interpretor and its enviornment."""

    # Command line interpreter
    print("Command line arguments: ", end="")
    for i, arg in enumerate(sys.argv):
        print(f"[{i}]: {arg} ", end="")

    # Python interpreter
    print(f"\nPlatform {sys.platform}")
    print(f" Python version: {sys.version}\n Excutable path: {sys.executable}")
    print(f"\nSystem-Specific Parameters.:\n Recusion limit: {sys.getrecursionlimit()}")

    # Interpreter values
    print(f"\nImplementation attributes:")
    for attr in dir(sys.implementation):
        if not attr.startswith("_"):  # Exclude private attributes (e.g., __name__)
            value = getattr(sys.implementation, attr)
            print(f" {attr}: {value}")

    print(f" Size of object: {sys.getsizeof(int)}")
    print(f"\nModules:\n {str(sys.modules)[:80]}...")
    print(f"Paths:")
    for i, path in enumerate(sys.path):
        print(f" [{i}]: {path}")
    return


"""
https://financialmodelingprep.com/api/v3/quote-short/AAPL?apikey=KLgUUoaVSZN0FaCkTwCUhhWHWDQ85hCj
"""

if __name__ == "__main__":
    os_examples()
    sys_examples()
