"""Mathematical and statistical computing tools for MCP server."""
import numpy as np


def register_math_tools(mcp):
    """Register mathematical tools onto the FastMCP server instance."""

    @mcp.tool()
    def compute_summary_statistics(numbers: list[float]) -> dict:
        """Compute comprehensive statistical metrics (mean, median, std dev, variance, min, max, IQR) for a list of numbers.

        Args:
            numbers: List of numerical values.

        Returns:
            Dictionary of computed summary statistics.
        """
        if not numbers:
            return {"error": "Input list cannot be empty."}

        arr = np.array(numbers, dtype=float)
        q25, q75 = np.percentile(arr, [25, 75])
        iqr = q75 - q25

        return {
            "count": len(arr),
            "mean": float(np.mean(arr)),
            "median": float(np.median(arr)),
            "std_dev": float(np.std(arr)),
            "variance": float(np.var(arr)),
            "min": float(np.min(arr)),
            "max": float(np.max(arr)),
            "p25": float(q25),
            "p75": float(q75),
            "iqr": float(iqr)
        }

    @mcp.tool()
    def normalize_array(numbers: list[float], method: str = "minmax") -> list[float]:
        """Normalize a list of numbers using Min-Max scaling ([0, 1]) or Z-Score standardization.

        Args:
            numbers: List of numerical values.
            method: Normalization method, either 'minmax' or 'zscore'. Defaults to 'minmax'.

        Returns:
            List of normalized floating point numbers.
        """
        if not numbers:
            return []

        arr = np.array(numbers, dtype=float)
        if method.lower() == "minmax":
            min_val, max_val = np.min(arr), np.max(arr)
            if max_val == min_val:
                return [0.0] * len(arr)
            norm = (arr - min_val) / (max_val - min_val)
            return norm.round(4).tolist()
        elif method.lower() == "zscore":
            std_val = np.std(arr)
            if std_val == 0:
                return [0.0] * len(arr)
            zscore = (arr - np.mean(arr)) / std_val
            return zscore.round(4).tolist()
        else:
            raise ValueError(f"Unknown method '{method}'. Supported methods: 'minmax', 'zscore'.")
