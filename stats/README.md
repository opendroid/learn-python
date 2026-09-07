# Statistics, Data Analysis & Visualization

This directory contains Jupyter notebooks and Python scripts covering applied statistics, linear algebra, numerical array computing with NumPy, data manipulation with Pandas, feature engineering, and statistical data visualization using Matplotlib and Seaborn.

---

## Topic Index

### 1. Python Scripts & Modules

| Script | Key Concepts | Data Source |
| :--- | :--- | :--- |
| [`data_frame_1.py`](data_frame_1.py) | Pandas DataFrame creation, `.loc[]` vs `.iloc[]` indexing, column filtering | [`sample_1.txt`](../data/sample_1.txt) |
| [`numpy_arrays.py`](numpy_arrays.py) | Multi-dimensional indexing, fancy indexing, boolean masks, broadcasting, views vs copies | Synthetic RNG |
| [`plot_box.py`](plot_box.py) | Box-and-whisker distribution plots, quartile analysis | [`uber-stock.csv`](../data/uber-stock.csv) |
| [`plot_scatter.py`](plot_scatter.py) | Multi-variable scatter plots, marker styling, trend visualization | [`weather-data-gilroy.csv`](../data/weather-data-gilroy.csv) |

### 2. Jupyter Notebooks

| Notebook | Topic & Core Concepts |
| :--- | :--- |
| [`stats_fundamentals.ipynb`](stats_fundamentals.ipynb) | Measures of central tendency (mean, median, mode), dispersion (variance, std dev, IQR), covariance, and correlation |
| [`probability_distribution.ipynb`](probability_distribution.ipynb) | Discrete & continuous distributions (Normal, Binomial, Poisson, Uniform), PDF/CDF, Central Limit Theorem (CLT) |
| [`advanced_statistics.ipynb`](advanced_statistics.ipynb) | Inferential statistics, confidence intervals, hypothesis testing formulation, null/alternative hypotheses, p-values |
| [`z_test_problems.ipynb`](z_test_problems.ipynb) | Applied 1-sample and 2-sample Z-test problem solving, critical values, and rejection regions |
| [`linear_algebra.ipynb`](linear_algebra.ipynb) | Vector/matrix operations, dot products, matrix multiplication, determinants, eigenvalues, eigenvectors |
| [`data_wrangling.ipynb`](data_wrangling.ipynb) | Data cleaning, missing value imputation, type casting, filtering, merging, joins, and reshaping |
| [`feature_engineering.ipynb`](feature_engineering.ipynb) | Categorical encoding (One-Hot, Ordinal), feature scaling (StandardScaler, MinMax), outlier detection & handling |
| [`seaborn.ipynb`](seaborn.ipynb) | Comprehensive statistical plotting with Seaborn (heatmaps, pairplots, violin plots, boxplots, distribution plots) |
| [`seaborn_caltech.ipynb`](seaborn_caltech.ipynb) | Applied EDA case study with Seaborn visualizations and statistical charts |
| [`aal_stats_project.ipynb`](aal_stats_project.ipynb) | End-to-end retail statistics case study (Australian Apparel Sales 2020) |
| [`inc_capstone_2.ipynb`](inc_capstone_2.ipynb) | Healthcare demographic analytics capstone (Part 2: EDA & inference on NSMES dataset) |
| [`inc_capstone_3.ipynb`](inc_capstone_3.ipynb) | Healthcare demographic analytics capstone (Part 3: Statistical modeling & evaluation) |

---

## Core Concepts & Implementation Highlights

### 1. NumPy Multi-Dimensional Array Computing (`numpy_arrays.py`)

* **Basic vs Advanced Indexing**:
  * Basic slicing (`a[1:3, 2:4]`) returns a **view** of the original memory buffer.
  * Fancy indexing (`a[[0, 1, 2], [5, 4, 3]]`) and boolean masks (`a[a > 15]`) return **copies**.
* **Broadcasting Rules**: Expands smaller arrays to match larger arrays element-wise from trailing dimensions backwards.
* **Views vs Copies**: Modifying a view mutates the base array, while copies remain isolated:

```python
import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6]])
view = arr[:, :2]  # Memory view
copy = arr.copy()  # Independent allocation
```

---

### 2. Pandas DataFrames (`data_frame_1.py`)

* **Label-based vs Position-based Indexing**:
  * `.loc[label]`: Selects by explicit row/column index label.
  * `.iloc[pos]`: Selects by integer 0-indexed position.
* **Conditional Filtering**:

```python
import pandas as pd

df = pd.read_csv("../data/sample_1.txt")
ma_residents = df[df["state"] == "MA"]
```

---

### 3. Hypothesis Testing & Inferential Statistics

* **Z-Test & T-Test**: Testing population parameters under known or unknown variances.
* **Decision Rule**: Reject $H_0$ if $p\text{-value} \le \alpha$ (commonly $\alpha = 0.05$) or if the test statistic falls in the critical rejection region.

---

### 4. Statistical Visualizations (`plot_box.py`, `plot_scatter.py`, `seaborn.ipynb`)

* **Box Plots**: Visualize distribution skewness, quartiles ($Q_1, Q_2, Q_3$), and outliers ($\pm 1.5 \times \text{IQR}$).
* **Scatter Plots**: Inspect bivariate correlations and clustering patterns across feature pairs.
* **Heatmaps & Pairplots**: Fast identification of multi-feature collinearity and covariance matrices.

---

## Environment & Running Instructions

All notebooks and scripts run in the `conda mlx` environment:

```bash
# Activate environment
conda activate mlx

# Run Python scripts
python stats/numpy_arrays.py
python stats/data_frame_1.py
python stats/plot_box.py
python stats/plot_scatter.py

# Launch Jupyter to open notebooks
jupyter lab
# or: jupyter notebook
```
