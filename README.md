![MCP Football Stats Logo](images/imng.png)

# Football Stats MCP

A Model Context Protocol (MCP) implementation for fetching and analyzing football statistics.

Note: This particular MCP is not a final product and will be updated as time goes by.

## What is MCP?

Model Context Protocol (MCP) is a standardized way to interact with LLM and agents. It provides a structured interface for:
- Fetching real-time match data
- Accessing team statistics
- Retrieving player information
- Getting news and updates

## Features

This MCP implementation provides the following tools:

### Team Tools
- `get_team_profile(team_id)`: Fetches detailed information about a specific team
- `get_team_news(team_id)`: Retrieves the latest news and updates for a team

### Match Tools
- `get_match_details(match_id)`: Gets comprehensive match statistics and details

## Installation

### Using uv (Recommended)

```bash
# Install uv if you haven't already
pip install uv

# Install MCP CLI
uv add "mcp[cli]"

# Run the MCP server
uv run mcp
```

### Using pip
```bash
pip install -r requirements.txt
```

## Usage

### Running the Server

You can run the MCP server in several ways:

1. **Using MCP CLI directly:**
```bash
mcp run server.py
```

2. **Using uv:**
```bash
uv run mcp server.py
```

### Testing and Development

You can test the MCP server using the MCP Inspector:

```bash
mcp dev server.py
```

### Installing in Claude Desktop

You can install this server in Claude Desktop and interact with it right away:

```bash
mcp install server.py
```

### Example API Calls

```python
# Get team profile
team_data = await get_team_profile(team_id=123)

# Get team news
news = await get_team_news(team_id=123)

# Get match details
match_data = await get_match_details(match_id=456)
```

## Dependencies

- Python >= 3.13
- mcp[cli] >= 1.8.0
- httpx
- uv (recommended for installation)

## Configuration

The MCP uses authentication tokens for accessing the FotMob API. These are stored in `src/headers.py`.

## Contributing

Feel free to submit issues and enhancement requests!
