"""Interactive command-line test runner for querying MCP servers."""
import sys
import asyncio
import os
import json

try:
    from mcp import ClientSession, StdioServerParameters
    from mcp.client.stdio import stdio_client
except ImportError:
    print("Error: The 'mcp' package is not installed.", file=sys.stderr)
    print("Please install it via: pip install 'mcp>=1.0.0'", file=sys.stderr)
    sys.exit(1)


async def interactive_runner():
    """Interactive prompt to call tools and inspect outputs."""
    server_script = os.path.abspath(os.path.join(os.path.dirname(__file__), "../server/server.py"))

    server_params = StdioServerParameters(
        command=sys.executable,
        args=[server_script, "--transport", "stdio"],
        env=dict(os.environ)
    )

    print("========================================")
    print("  MCP Interactive REPL & Testing Suite  ")
    print("========================================")

    async with stdio_client(server_params) as (read_stream, write_stream):
        async with ClientSession(read_stream, write_stream) as session:
            await session.initialize()
            print("Connected to server successfully!\n")

            while True:
                print("\nOptions:")
                print("1. List Tools")
                print("2. Call a Tool")
                print("3. List Resources")
                print("4. Read a Resource")
                print("5. List Prompts")
                print("6. Exit")

                choice = input("\nEnter choice (1-6): ").strip()

                if choice == "1":
                    tools = await session.list_tools()
                    print("\n--- Available Tools ---")
                    for t in tools.tools:
                        print(f"[{t.name}] {t.description}")
                        print(f"  Schema: {json.dumps(t.inputSchema, indent=2)}")

                elif choice == "2":
                    tool_name = input("Tool name: ").strip()
                    args_str = input("Arguments (JSON dict, e.g. {\"state\": \"NSW\"}): ").strip()
                    try:
                        args = json.loads(args_str) if args_str else {}
                        result = await session.call_tool(tool_name, arguments=args)
                        print("\n--- Result ---")
                        for item in result.content:
                            print(item.text)
                    except Exception as e:
                        print(f"Error calling tool: {e}")

                elif choice == "3":
                    resources = await session.list_resources()
                    print("\n--- Available Resources ---")
                    for r in resources.resources:
                        print(f"[{r.uri}] {r.name}")

                elif choice == "4":
                    uri = input("Resource URI (e.g. data://catalog): ").strip()
                    try:
                        res = await session.read_resource(uri)
                        print("\n--- Content ---")
                        for item in res.contents:
                            print(item.text)
                    except Exception as e:
                        print(f"Error reading resource: {e}")

                elif choice == "5":
                    prompts = await session.list_prompts()
                    print("\n--- Available Prompts ---")
                    for p in prompts.prompts:
                        print(f"[{p.name}] {p.description}")

                elif choice == "6":
                    print("Exiting...")
                    break
                else:
                    print("Invalid option. Please enter 1-6.")


if __name__ == "__main__":
    try:
        asyncio.run(interactive_runner())
    except KeyboardInterrupt:
        print("\nSession terminated.")
