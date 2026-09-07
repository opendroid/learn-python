"""Reusable prompt templates for MCP server."""


def register_prompts(mcp):
    """Register prompt templates onto the FastMCP server instance."""

    @mcp.prompt()
    def state_performance_review(state: str) -> str:
        """Prompt template to generate an executive review for a specific Australian state."""
        return (
            f"You are a Senior Retail Data Strategist at Australian Apparel Limited (AAL).\n"
            f"Please review the Q4 2020 retail performance of state '{state.upper()}':\n"
            f"1. Call `get_state_sales_summary(state='{state.upper()}')` to fetch the actual numbers.\n"
            f"2. Assess market standing compared to other national territories.\n"
            f"3. Propose 3 high-impact promotional and merchandising strategies for the upcoming quarter.\n"
        )

    @mcp.prompt()
    def statistical_data_cleaning_guide() -> str:
        """Prompt template guiding statistical data wrangling and transformation."""
        return (
            "You are a Data Science Specialist.\n"
            "Explain the practical differences and mathematical formulations of:\n"
            "1. Min-Max Normalization: [0, 1] interval scaling.\n"
            "2. Z-Score Standardization: (x - mean) / std.\n"
            "3. When to prefer normalization over standardization in downstream ML algorithms.\n"
        )
