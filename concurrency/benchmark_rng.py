import os
import time
import statistics
from collections import defaultdict
import matplotlib.pyplot as plt

from pool import (
    sequential,
    pool_map,
    pool_map_async,
    pool_apply,
    pool_apply_async,
)
from task_rng import create_random

BENCHMARKS = [
    sequential,
    pool_apply,
    pool_apply_async,
    pool_map,
    pool_map_async,
]


def run_once(fn, task, n_times, n_cpus, task_params):
    start = time.perf_counter()
    results = fn(task, n_times, n_cpus, **task_params)
    elapsed = time.perf_counter() - start
    return elapsed, results


def plot_scaling(results, size):
    """
    Plot throughput vs CPUs for different run counts.

    Args:
        results: list of dicts with keys:
            - method
            - cpus
            - runs
            - throughput
        size: task size (for title)
    """
    # Group: method -> runs -> [(cpus, throughput)]
    grouped = defaultdict(lambda: defaultdict(list))

    for r in results:
        grouped[r["method"]][r["runs"]].append((r["cpus"], r["throughput"]))

    for method, runs_map in grouped.items():
        plt.figure()

        for runs, values in sorted(runs_map.items()):
            values.sort()
            cpus = [v[0] for v in values]
            thr = [v[1] for v in values]

            plt.plot(cpus, thr, marker="o", label=f"runs={runs}")

        plt.xlabel("Number of CPUs")
        plt.ylabel("Throughput (elements/sec)")
        plt.title(f"{method} | Task size={size:,}")
        plt.legend()
        plt.grid()
        plt.tight_layout()

        plt.show()


def benchmark():
    max_cpus = getattr(os, "process_cpu_count", os.cpu_count)()

    # Sweep dimensions
    task_sizes = [100_000, 1_000_000, 5_000_000]
    task_counts = [1, 2, 4, 8, 16, 32]
    cpu_sweep = [1, 2, 4, 8, max_cpus]

    repeats = 3
    warmup = 1

    print(f"Max CPU count: {max_cpus}\n")

    for size in task_sizes:
        print(f"\n=== Task size: {size:,} ===")

        collected = []

        for n_times in task_counts:
            print(f"\n-- n_times: {n_times} --")

            task_params = {"n": size}

            for n_cpus in cpu_sweep:
                print(f"\n   CPUs: {n_cpus}")

                for fn in BENCHMARKS:
                    timings = []

                    # Warm-up
                    for _ in range(warmup):
                        run_once(fn, create_random, n_times, n_cpus, task_params)

                    # Measured runs
                    for _ in range(repeats):
                        elapsed, _ = run_once(fn, create_random, n_times, n_cpus, task_params)
                        timings.append(elapsed)

                    avg = statistics.mean(timings)
                    p50 = statistics.median(timings)

                    total_elements = n_times * size
                    throughput = total_elements / avg

                    print(
                        f"{fn.__name__:<18} "
                        f"avg={avg*1000:8.0f} ms  "
                        f"p50={p50*1000:8.0f} ms  "
                        f"thr={throughput/1e6:8.2f} M elems/s"
                    )

                    collected.append({
                        "method": fn.__name__,
                        "cpus": n_cpus,
                        "runs": n_times,
                        "throughput": throughput,
                    })

        # Plot per task size
        plot_scaling(collected, size)
        


if __name__ == "__main__":
    benchmark()
