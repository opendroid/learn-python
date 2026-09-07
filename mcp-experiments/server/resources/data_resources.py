"""Dynamic and static MCP resources."""
import os
import glob


def register_resources(mcp):
    """Register data resources onto the FastMCP server instance."""

    @mcp.resource("data://catalog")
    def get_dataset_catalog() -> str:
        """Returns catalog of all available CSV and data files in the repository data directory."""
        data_dir = os.path.join(os.path.dirname(__file__), "../../data")
        if not os.path.exists(data_dir):
            data_dir = os.path.join(os.path.dirname(__file__), "../../../data")

        files = glob.glob(os.path.join(data_dir, "*.*"))
        entries = []
        for file_path in sorted(files):
            name = os.path.basename(file_path)
            size = os.path.getsize(file_path)
            entries.append(f"- {name} ({size:,} bytes)")

        return "### Available Datasets Catalog\n" + "\n".join(entries)

    @mcp.resource("data://aal-summary")
    def get_aal_dataset_summary() -> str:
        """Returns metadata and column structure for the Australian Apparel Sales Q4 2020 dataset."""
        return (
            "### Australian Apparel Limited (AAL) Q4 2020 Dataset Summary\n"
            "- File: AusApparalSales4thQrt2020.csv\n"
            "- Time Span: October 1, 2020 - December 30, 2020 (90 days)\n"
            "- Observations: 7,560 rows (84 daily records)\n"
            "- Columns: Date (datetime), Time (Morning/Afternoon/Evening), State (7 states), Group (4 segments), Unit (int), Sales (AUD)\n"
            "- Pricing: Fixed $2,500 AUD / unit\n"
        )
