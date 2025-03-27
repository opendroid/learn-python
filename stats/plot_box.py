import pandas as pd
import matplotlib.pyplot as plt


def box_plot(filename="../data/uber-stock.csv"):
    # Create a 2D array 5x2 (rows x columns)
    # Default data source: https://wrcc.dri.edu/cgi-bin/cliMAIN.pl?ca3417
    try:
        data = pd.read_csv(filename)
        print(data.head(5))
        # Date,Open,High,Low,Close,Volume
        y1 = data["Open"]
        y2 = data["Close"]
        plt.figure(figsize=(16, 9))
        plt.boxplot([y1, y2], patch_artist=True)
        plt.xlabel("Open or Close")
        plt.ylabel("$UBER")
        plt.title("Uber stick ")
        plt.xticks([1, 2], ["TMAX", "TMIN"])
        plt.grid(True, which="both", linestyle="--")
        plt.show()
    except FileNotFoundError:
        print(f"File {filename} not found.")
        return
