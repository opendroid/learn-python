"""Statistical and dataset querying tools for MCP server."""
import os
import pandas as pd


def register_stats_tools(mcp):
    """Register statistics tools onto the FastMCP server instance."""

    @mcp.tool()
    def get_state_sales_summary(state: str) -> dict:
        """Fetch Q4 2020 retail sales and unit metrics for a specific Australian state.

        Args:
            state: Two/three-letter state abbreviation (e.g. 'VIC', 'NSW', 'QLD', 'WA', 'SA', 'TAS', 'NT').

        Returns:
            Dictionary containing total revenue, units sold, and average daily revenue.
        """
        data_path = os.path.join(os.path.dirname(__file__), "../../data/AusApparalSales4thQrt2020.csv")
        if not os.path.exists(data_path):
            data_path = os.path.join(os.path.dirname(__file__), "../../../data/AusApparalSales4thQrt2020.csv")

        df = pd.read_csv(data_path, converters={"State": str.strip, "Group": str.strip, "Time": str.strip})
        state_df = df[df["State"].str.upper() == state.strip().upper()]

        if state_df.empty:
            return {"error": f"State '{state}' not found. Available states: {sorted(df['State'].unique().tolist())}"}

        total_sales = int(state_df["Sales"].sum())
        total_units = int(state_df["Unit"].sum())
        avg_daily_sales = float(state_df.groupby("Date")["Sales"].sum().mean())

        return {
            "state": state.upper(),
            "total_sales_aud": total_sales,
            "total_units_sold": total_units,
            "avg_daily_sales_aud": round(avg_daily_sales, 2),
            "record_count": len(state_df)
        }

    @mcp.tool()
    def compare_demographic_groups() -> list:
        """Compare Q4 2020 overall performance across all demographic groups (Kids, Men, Women, Seniors).

        Returns:
            List of dictionaries with ranking, group name, revenue, and unit share.
        """
        data_path = os.path.join(os.path.dirname(__file__), "../../data/AusApparalSales4thQrt2020.csv")
        if not os.path.exists(data_path):
            data_path = os.path.join(os.path.dirname(__file__), "../../../data/AusApparalSales4thQrt2020.csv")

        df = pd.read_csv(data_path, converters={"State": str.strip, "Group": str.strip, "Time": str.strip})
        group_summary = df.groupby("Group").agg({"Sales": "sum", "Unit": "sum"}).reset_index()
        group_summary = group_summary.sort_values(by="Sales", ascending=False)

        total_rev = group_summary["Sales"].sum()
        results = []
        for rank, row in enumerate(group_summary.itertuples(), start=1):
            results.append({
                "rank": rank,
                "group": row.Group,
                "sales_aud": int(row.Sales),
                "units_sold": int(row.Unit),
                "revenue_share_pct": round((row.Sales / total_rev) * 100, 2)
            })

        return results
