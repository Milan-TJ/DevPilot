import asyncio
import sys
from pathlib import Path

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

from fastmcp import Client

SERVER = Path("app/mcp_server.py").resolve()

MCP_SERVER_PATH = (
    Path(__file__).resolve().parents[1] / "app/mcp_server.py"
)


# async def main():
#     params = StdioServerParameters(
#         command=sys.executable,
#         args=[str(MCP_SERVER_PATH)],
#         cwd=str(SERVER.parent.parent),
#     )

#     async with stdio_client(params) as (read, write):
#         async with ClientSession(read, write) as session:
#             await session.initialize()
#             print("MCP initialization successful")

#             result = await session.list_tools()
#             print("Available tools:", [tool.name for tool in result.tools])

async def main():
    client = Client(SERVER)

    async with client:
        print("MCP connection successful")

        tools = await client.list_tools()
        print("Available tools:")

        for tool in tools:
            print(f"- {tool.name}: {tool.description}")



if __name__ == "__main__":
    asyncio.run(main())