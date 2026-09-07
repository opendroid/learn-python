"""Main entrypoint for Python MCP Server using FastMCP."""
import sys
import argparse

try:
    from mcp.server.fastmcp import FastMCP
except ImportError:
    print("Error: The 'mcp' package is not installed.", file=sys.stderr)
    print("Please install it via: pip install 'mcp>=1.0.0'", file=sys.stderr)
    sys.exit(1)

from tools.stats_tools import register_stats_tools
from tools.math_tools import register_math_tools
from resources.data_resources import register_resources
from prompts.analysis_prompts import register_prompts

# 1. Initialize FastMCP Server instance
mcp = FastMCP(
    name="Learn-Python-MCP-Server",
    description="MCP Server providing statistical tools, retail dataset analytics, math operations, and prompts."
)

# 2. Register modular capabilities
register_stats_tools(mcp)
register_math_tools(mcp)
register_resources(mcp)
register_prompts(mcp)


def main():
    parser = argparse.ArgumentParser(description="Run the Python Learning MCP Server.")
    parser.add_argument(
        "--transport",
        choices=["stdio", "sse"],
        default="stdio",
        help="Transport mechanism to use (default: stdio)."
    )
    args = parser.parse_args()

    # 3. Launch server with chosen transport
    if args.transport == "stdio":
        mcp.run(transport="stdio")
    elif args.transport == "sse":
        mcp.run(transport="sse")


if __name__ == "__main__":
    main()
