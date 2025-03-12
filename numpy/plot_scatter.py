import pandas as pd
import matplotlib.pyplot as plt


def scatter_plot(filename="../data/weather-data-gilroy.csv"):
    # Create a 2D array 5x2 (rows x columns)
    # Default data source: https://wrcc.dri.edu/cgi-bin/cliMAIN.pl?ca3417
    try:
        data = pd.read_csv(filename)
        print(data.describe())
        # Scatter plot of Temperature Max vs Precipitation
        y = data["PRECIP"]
        x1 = data["TMAX"]
        x2 = data["TMIN"]
        plt.figure(figsize=(16, 9))
        plt.scatter(x1, y, c="indianred",
                    marker="o", label="TMAX", s=50)  # scaling, s=1 is 1/72"
        plt.scatter(x2, y, c="deepskyblue",
                    marker="x", label="TMIN", s=50)
        plt.xlabel("Temperature (F)")
        plt.ylabel("Precipitation")
        plt.title("Temperature vs Precipitation in Gilroy CA (1981-2010)")
        plt.legend(loc="upper right")
        plt.grid(True, which="both", linestyle="--")
        plt.show()
    except FileNotFoundError:
        print(f"File {filename} not found.")
        return


if __name__ == "__main__":
    scatter_plot()
