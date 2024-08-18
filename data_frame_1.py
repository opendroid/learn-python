"""
This module experiments with Pandas DataFrame. Crate, update index and add elements to a DataFrame,


Author: opendroid
Email: openweb@outlook.com
License: MIT
"""

import pandas as pd


def dp_examples_1():
    """use dictionary to create the DataFrame.

    Create a frame with theree column names: "column-1-heading", "column-2-heading" and "column-3-heading".
    The default row index labels are 0, 1, 2, 3.
    """
    data = {
        "column-1-heading": [-2, -1, 0, 1, 2],
        "column-2-heading": ["Minus Two", "Minus One", "Zero", "One", "Two"],
        "column-3-heading": [x**2 for x in range(5)],
    }
    # Create a default
    df1 = pd.DataFrame(data)
    print(f"dp_examples_1: df1:\n{df1}")

    # Create data-frame idex with labels
    df2 = pd.DataFrame(
        data,
        index=["row-0", "row-1", "row-2", "row-3", "row-4"],
    )
    print(f"dp_examples_1: df2:\n{df2}")

    # Rename the row-labels.
    df2.rename(
        index={"row-0": 0, "row-1": 100, "row-2": 200, "row-3": 300, "row-4": 400},
        inplace=True,
    )

    # Add a row to the dataframe
    row = {"column-1-heading": 3, "column-2-heading": "Three", "column-3-heading": 25}
    df2.loc[len(df2)] = row  # Add row at default index = 5
    df2.rename(index={5: 500}, inplace=True)
    print(f"dp_examples_1: df2-updated index and adding a row:\n{df2}")
    values = df2.loc[[500]]  # DF with data at index label: 500
    print(f"dp_examples_1: Values at loc[[500]]:\n{values}")
    values = df2.iloc[[5]]  # DF with data at index location 5
    print(f"dp_examples_1: Values at iloc[[5]]:\n{values}")
    print(f"dp_examples_1: df2 Axes:\n{df2.axes}")
    return


def read_df_from_csv(filename):
    """Reads a DF from a CSV and filter it"""
    df = pd.read_csv(filename)
    print(f"read_df_from_csv: Describe: {df.describe()}")
    # Filter all rows where "state" is "MA"
    ma = df[df["state"] == "MA"]
    print(f"read_df_from_csv: MA\n{ma}")
    print(df)
    print(f"read_df_from_csv: original\n{df}")
    return


if __name__ == "__main__":
    read_df_from_csv("./data/sample_1.txt")
    dp_examples_1()
