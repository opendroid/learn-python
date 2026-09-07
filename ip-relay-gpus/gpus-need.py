import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

def gpus_cost():
    # --- Parameters ---
    annual_minutes = 25000000
    daily_minutes = annual_minutes / 365
    avg_call_duration = 17.5 
    daily_calls_target = int(daily_minutes / avg_call_duration) # ~3914 calls
    calls_per_tz = daily_calls_target / 3

    std_dev = 120 # 2 hours in minutes
    means_pst = [540, 600, 720] # EST, CST, PST peaks relative to PST midnight

    concurrency = 2 # 2 calls per GPU
    lag = 10 # 10 minute provisioning warm-up
    cost_per_gpu_min = 0.0363

    # --- Step 1: Generate Arrival Rate (Calls/Min) ---
    x_mins = np.arange(0, 1440)
    arrival_rate = np.zeros(1440)
    for mu in means_pst:
        arrival_rate += norm.pdf(x_mins, mu, std_dev) * calls_per_tz

    # --- Step 2: Calculate Concurrent Calls & GPU Demand ---
    # We use a rolling sum to represent calls lasting avg_call_duration
    concurrent_calls = np.convolve(arrival_rate, np.ones(int(avg_call_duration)), mode='same')

    # GPU Demand: Calls divided by concurrency (2:1)
    gpu_demand = np.ceil(concurrent_calls / concurrency)

    # GPU Capacity: Must provision 10 mins ahead of demand
    gpu_capacity = np.zeros(1440)
    for t in range(1440):
        lookahead_idx = min(t + lag, 1439)
        gpu_capacity[t] = gpu_demand[lookahead_idx]

    # --- Step 3: Plotting ---
    fig, ax1 = plt.subplots(figsize=(14, 7))

    # Axis 1: Concurrent Calls
    color_calls = 'tab:blue'
    ax1.set_xlabel('Time of Day (PST)', fontsize=12)
    ax1.set_ylabel('Concurrent IP Relay Calls', color=color_calls, fontsize=12)
    ax1.plot(x_mins, concurrent_calls, color=color_calls, linewidth=2, label="Concurrent Calls")
    ax1.tick_params(axis='y', labelcolor=color_calls)

    # Axis 2: GPU-Minutes (Instantaneous GPU Count)
    ax2 = ax1.twinx()
    color_gpu = 'tab:red'
    ax2.set_ylabel('GPU Count (Billed Minutes/Min)', color=color_gpu, fontsize=12)
    ax2.plot(x_mins, gpu_capacity, color=color_gpu, linestyle='--', linewidth=2, label="Billed GPU Capacity")
    ax2.fill_between(x_mins, gpu_demand, gpu_capacity, color=color_gpu, alpha=0.15, label="Provisioning Lag (Waste)")
    ax2.tick_params(axis='y', labelcolor=color_gpu)

    # Formatting
    plt.title("Daily Load Profile: IP Relay Calls vs. GPU Capacity (10-Min Lag)", fontsize=14, pad=20)
    ax1.set_xticks(np.arange(0, 1441, 120))
    ax1.set_xticklabels(['12AM', '2AM', '4AM', '6AM', '8AM', '10AM', '12PM', '2PM', '4PM', '6PM', '8PM', '10PM', '12AM'])
    ax1.grid(True, alpha=0.3)

    # Legend
    lines, labels = ax1.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    ax2.legend(lines + lines2, labels + labels2, loc='upper left')

    plt.tight_layout()
    plt.show()

    # --- Step 4: Cost Analysis Output ---
    total_billed_gpu_mins = np.sum(gpu_capacity)
    annual_total_cost = total_billed_gpu_mins * 365 * cost_per_gpu_min
    theoretical_min_cost = (annual_minutes / concurrency) * cost_per_gpu_min

    print(f"--- Financial Summary ---")
    print(f"Annual Billed GPU-Minutes: {total_billed_gpu_mins * 365:,.0f}")
    print(f"Annual Estimated Cost: ${annual_total_cost:,.2f}")
    print(f"Theoretical Min Cost: ${theoretical_min_cost:,.2f}")
    print(f"Efficiency Loss (Lag Penalty): ${annual_total_cost - theoretical_min_cost:,.2f}")
    return


gpus_cost()
