import httpx
from fastmcp import FastMCP

# from app.services.automation_service import run_validation

# from mcp.server import MCPServer

mcp = FastMCP("DevPilot Tools", showbanner=False, debug=True)


@mcp.tool()
async def list_projects() -> list[dict]:
    """List projects registered in DevPilot."""

    api_url = "http://127.0.0.1:8000/api/projects/all"

    async with httpx.AsyncClient(timeout=20) as client:
        response = await client.get(api_url)
        response.raise_for_status()
        projects = response.json()

    if not isinstance(projects, list):
        raise ValueError("Unexpected projects API response")

    return [
        {
            "id": project.get("id"),
            "name": project.get("name"),
            "repository": project.get("repository"),
            "description": project.get("description"),
        }
        for project in projects
    ]

# @mcp.tool()
# async def validate_project() -> dict:
#     """Run the allowlisted DevPilot project validation workflow."""

#     return await run_validation()


if __name__ == "__main__":
    mcp.run(transport="stdio")
