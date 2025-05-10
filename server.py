import httpx
from mcp.server.fastmcp import FastMCP
from src.headers import HEADERS

# Create an MCP server
mcp = FastMCP("Football Stats MCP")

""" Prompts """

@mcp.prompt()
def summary_team_stats() -> str:
    return """
    You are a football stats analyst.
    You need to return a summary of the team stats.
    """

""" Team Tools """

@mcp.tool()
async def get_team_profile(team_id: int) -> str:
    """Fetch Current Team Profile"""
    url = f"https://www.fotmob.com/api/teams?id={team_id}&ccode3=PRT"
    async with httpx.AsyncClient() as client:
        response = await client.get(url, headers=HEADERS)
        return response.json()

@mcp.tool()
async def get_team_news(team_id: int) -> str:
    """Fetch Team News"""
    url = f"https://www.fotmob.com/api/tlnews?id={team_id}&type=team&language=en&startIndex=0"
    async with httpx.AsyncClient() as client:
        response = await client.get(url, headers=HEADERS)
        res = response.json()

        news_title = res['data'][0].get('title', "")
        news_article = res['data'][0].get('page', []).get('url', "")
        news_source = res['data'][0].get('sourceStr', "")
        news_date = res['data'][0].get('gmtTime', "")

        return f"Title: {news_title}\nArticle: {news_article}\nSource: {news_source}\nDate: {news_date}"

""" Match Tools """

@mcp.tool()
async def get_match_details(match_id: int) -> str:
    """Fetch Match Details"""
    url = f"https://www.fotmob.com/api/matchDetails?matchId={match_id}"
    async with httpx.AsyncClient() as client:
        response = await client.get(url, headers=HEADERS)
        return response.json()


if __name__ == "__main__":
    mcp.run()