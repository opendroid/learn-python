"""This module provides examples of system processes.


Author: opendroid
Email: openweb@outlook.com
License: MIT
"""
from multiprocessing import Pool
from random import randint
import os
import time


def create_random(n):
    """Worker function that create and returns an array of n random numbers.
    """
    return [randint(0, 100) for _ in range(n)]


def pool_main():
    """
    Compare sync and async versions of Pool.apply and Pool.map.

    The results on Mac with 12 CPUs are:
        apply-sync: 20282.022953033447ms 10 x 10000000
        apply-async: 4340.411186218262ms 10 x 10000000
        map-sync: 4198.2128620147705ms 10 x 10000000
        map-async: 4394.35076713562ms 10 x 10000000
    """
    count = 10_000_000
    rows = 10
    with Pool(processes=os.process_cpu_count()//2) as pool:
        # Sync Apply: Crate rows large random arrays sequentially
        start = time.time()
        # Each apply blocks next apply.
        results = [pool.apply(func=create_random, args=(count,))
                   for _ in range(rows)]
        interval = time.time() - start
        time_taken = interval * 1000
        print(
            f"apply-sync: {time_taken}ms {len(results)} x {len(results[0])}"
        )

    with Pool(processes=os.process_cpu_count()//2) as pool:
        # Async Apply: Crate rows large random arrays async
        start = time.time()
        results_obj = [pool.apply_async(func=create_random, args=(count,))
                       for _ in range(rows)]
        results = [row.get() for row in results_obj]
        interval = time.time() - start
        time_taken = interval * 1000
        print(
            f"apply-async: {time_taken}ms {len(results)} x {len(results[0])}"
        )

    with Pool(processes=os.process_cpu_count()//2) as pool:
        # Sync Map: Crate rows large random arrays sequentially
        start = time.time()
        # blocked until results are fetched
        results = pool.map(create_random, [count for _ in range(rows)])
        interval = time.time() - start
        time_taken = interval * 1000
        print(
            f"map-sync: {time_taken}ms {len(results)} x {len(results[0])}"
        )

    with Pool(processes=os.process_cpu_count()//2) as pool:
        # Async Map: Crate 4 large random arrays sequentially
        start = time.time()
        # Immediately return
        results_obj = pool.map_async(
            create_random, [count for _ in range(rows)])
        # Do other things before you need results.
        results = results_obj.get()
        interval = time.time() - start
        time_taken = interval * 1000
        print(
            f"map-async: {time_taken}ms {len(results)} x {len(results[0])}"
        )
    return


if __name__ == "__main__":
    pool_main()
