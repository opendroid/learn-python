"""Stdio-based MCP Client implementation using ClientSession."""
import sys
import asyncio
import os

try:
    from mcp import ClientSession, StdioServerParameters
    from mcp.client.stdio import stdio_client
except ImportError:
    print("Error: The 'mcp' package is not installed.", file=sys.stderr)
    print("Please install it via: pip install 'mcp>=1.0.0'", file=sys.stderr)
    sys.exit(1)


async def run_stdio_client():
    """Connects to the local MCP server via stdio and queries tools, resources, and prompts."""
    server_script = os.path.abspath(os.path.join(os.path.dirname(__file__), "../server/server.py"))

    # Define server parameters for subprocess execution
    server_params = StdioServerParameters(
        command=sys.executable,
        args=[server_script, "--transport", "stdio"],
        env=dict(os.environ)
    )

    print(f"Connecting to MCP Server via Stdio: {server_script} ...")

    async with stdio_client(server_params) as (read_stream, write_stream):
        async with ClientSession(read_stream, write_stream) as session:
            # 1. Initialize session handshake
            init_result = await session.initialize()
            print(f"\n[Handshake] Connected to: {init_result.serverInfo.name} v{init_result.serverInfo.version}")

            # 2. List Available Tools
            tools_response = await session.list_tools()
            print("\n=== Discovered Tools ===")
            for tool in tools_response.tools:
                print(f" - {tool.name}: {tool.description}")

            # 3. List Available Resources
            resources_response = await session.list_resources()
            print("\n=== Discovered Resources ===")
            for resource in resources_response.resources:
                print(f" - {resource.uri}: {resource.name}")

            # 4. List Available Prompts
            prompts_response = await session.list_prompts()
            print("\n=== Discovered Prompts ===")
            for prompt in prompts_response.prompts:
                print(f" - {prompt.name}: {prompt.description}")

            # 5. Execute a Tool Call (get_state_sales_summary)
            print("\n=== Executing Tool: get_state_sales_summary(state='VIC') ===")
            vic_result = await session.call_tool("get_state_sales_summary", arguments={"state": "VIC"})
            for content in vic_result.content:
                print("Output:", content.text)

            # 6. Execute a Tool Call (compute_summary_statistics)
            print("\n=== Executing Tool: compute_summary_statistics(...) ===")
            stats_result = await session.call_tool(
                "compute_summary_statistics",
                arguments={"numbers": [10.5, 20.0, 30.5, 40.0, 50.5, 100.0]}
            )
            for content in stats_result.content:
                print("Output:", content.text)

            # 7. Read a Resource
            print("\n=== Reading Resource: data://aal-summary ===")
            res_content = await session.read_resource("data://aal-summary")
            for content in res_content.contents:
                print(content.text)


if __name__ == "__main__":
    asyncio.run(run_stdio_client())
