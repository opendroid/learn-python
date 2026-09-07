# Model Context Protocol (MCP) Experiments

This directory provides a modular starter architecture for building, testing, and integrating **Model Context Protocol (MCP)** servers and clients in Python using the official [`mcp`](https://github.com/modelcontextprotocol/python-sdk) SDK.

---

## What is MCP?

**Model Context Protocol (MCP)** is an open standard that allows LLMs and AI agents (such as Claude Desktop, Cursor, Antigravity IDE, custom agents) to securely connect to external tools, data resources, and prompt templates over JSON-RPC 2.0.

```text
┌────────────────────────────────────────┐
│               MCP Client               │
│  (Claude Desktop, Cursor, Custom Agent)│
└───────────────────┬────────────────────┘
                    │ JSON-RPC (stdio / SSE)
                    ▼
┌────────────────────────────────────────┐
│               MCP Server               │
│ ┌──────────────┬─────────────┬───────┐ │
│ │    Tools     │  Resources  │Prompts│ │
│ └──────────────┴─────────────┴───────┘ │
└────────────────────────────────────────┘
```

---

## Directory Structure

```text
mcp-experiments/
├── README.md                        # Master MCP guide and instructions
├── mcp_config.json                  # Standard host client configuration file
├── requirements.txt                 # Dependencies (mcp, pydantic, pandas, etc.)
│
├── server/                          # MCP Server Architecture
│   ├── __init__.py
│   ├── server.py                    # FastMCP server entrypoint & router
│   ├── tools/                       # Tool definitions (callable functions)
│   │   ├── __init__.py
│   │   ├── stats_tools.py           # Australian retail sales & demographic query tools
│   │   └── math_tools.py            # Summary statistics & normalization tools
│   ├── resources/                   # Resource definitions (custom URIs)
│   │   ├── __init__.py
│   │   └── data_resources.py        # data://catalog and data://aal-summary
│   └── prompts/                     # Prompt templates (reusable instructions)
│       ├── __init__.py
│       └── analysis_prompts.py      # State performance review & data cleaning prompts
│
└── client/                          # MCP Client Architecture
    ├── __init__.py
    ├── client_stdio.py              # Automated programmatic client using ClientSession
    └── runner.py                    # Interactive command-line REPL for tool inspection
```

---

## Core Server Components

### 1. Tools (`server/tools/`)

Tools are executable functions exposed to AI models:

* `get_state_sales_summary(state)`: Queries retail sales, units sold, and average daily revenue for an Australian state from [`AusApparalSales4thQrt2020.csv`](../data/AusApparalSales4thQrt2020.csv).
* `compare_demographic_groups()`: Returns demographic performance rankings and market share percentages.
* `compute_summary_statistics(numbers)`: Calculates mean, median, standard deviation, IQR, min/max for a list of values.
* `normalize_array(numbers, method)`: Applies Min-Max scaling or $Z$-score standardization.

```python
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Learn-Python-MCP-Server")

@mcp.tool()
def get_state_sales_summary(state: str) -> dict:
    """Fetch Q4 2020 retail sales metrics for an Australian state."""
    ...
```

---

### 2. Resources (`server/resources/`)

Resources provide contextual data streams addressable by custom URI schemes:

* `data://catalog`: Returns a dynamically generated list of all datasets in `../data/`.
* `data://aal-summary`: Returns metadata, row counts, and column definitions for the AAL retail dataset.

```python
@mcp.resource("data://catalog")
def get_dataset_catalog() -> str:
    """Returns overview of available datasets."""
    ...
```

---

### 3. Prompts (`server/prompts/`)

Pre-packaged prompt templates for common analytical workflows:

* `state_performance_review(state)`: Formats an executive briefing prompt targeting a specific state.
* `statistical_data_cleaning_guide()`: Formats a conceptual data wrangling instructional prompt.

---

## Core Client Components

### 1. Programmatic Stdio Client (`client/client_stdio.py`)

Spawns the server subprocess, establishes the JSON-RPC handshake, and demonstrates:

1. `session.list_tools()`: Tool discovery and schema inspection.
2. `session.list_resources()` & `session.read_resource(uri)`: Resource fetching.
3. `session.list_prompts()`: Prompt template discovery.
4. `session.call_tool(name, arguments)`: Tool execution and output retrieval.

```python
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

server_params = StdioServerParameters(
    command="python",
    args=["server/server.py", "--transport", "stdio"]
)

async with stdio_client(server_params) as (read, write):
    async with ClientSession(read, write) as session:
        await session.initialize()
        result = await session.call_tool("get_state_sales_summary", arguments={"state": "VIC"})
        print(result.content)
```

---

### 2. Interactive REPL (`client/runner.py`)

An interactive CLI allowing you to test, call, and debug tools and resources without needing to connect a full LLM frontend.

---

## Setup & Execution Guide

### 1. Install Dependencies

Ensure you are in the `conda mlx` environment:

```bash
# Activate conda environment
conda activate mlx

# Install MCP SDK and dependencies
pip install -r mcp-experiments/requirements.txt
```

---

### 2. Run the Automated Client Demo

Run the automated end-to-end client to query the server via standard I/O:

```bash
python mcp-experiments/client/client_stdio.py
```

---

### 3. Run the Interactive Tool Tester

Launch the interactive test console:

```bash
python mcp-experiments/client/runner.py
```

---

### 4. Connect to Host Applications (Claude Desktop / Cursor / IDE)

Add the server definition to your client configuration file (`mcp_config.json` or `claude_desktop_config.json`):

```json
{
  "mcpServers": {
    "python-learn-tools": {
      "command": "/opt/homebrew/anaconda3/envs/mlx/bin/python",
      "args": [
        "/Users/AThakur/Developer/build/py3-code/learn-python/mcp-experiments/server/server.py",
        "--transport",
        "stdio"
      ],
      "env": {}
    }
  }
}
```
