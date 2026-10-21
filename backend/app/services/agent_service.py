import logging
import os
import sys
from pathlib import Path

from google import genai
from google.genai import types
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

import logging
logger = logging.getLogger(__name__)


client = genai.Client(
    api_key=os.environ["GEMINI_API_KEY"]
)

MODEL = os.getenv("GEMINI_MODEL", "gemini-flash-latest")

MCP_SERVER_PATH = (
    Path(__file__).resolve().parents[1] / "mcp_server.py"
)

SYSTEM_PROMPT = (
    "You are the DevPilot developer platform assistant. "
    "Use list_projects for requests about registered "
    "projects and their repositories. Base factual "
    "answers on the tool results."
)


async def ask_devpilot(message: str) -> str:
    
    server_params = StdioServerParameters(
        command=sys.executable,
        args=[str(MCP_SERVER_PATH)],
        cwd=str(MCP_SERVER_PATH.parent.parent),
    )

    async with stdio_client(server_params) as (read, write):

        async with ClientSession(read, write) as session:

            await session.initialize()

            response = await client.aio.models.generate_content(
                model=MODEL,
                contents=message,
                config=types.GenerateContentConfig(
                    temperature=0.7,
                    system_instruction= SYSTEM_PROMPT,
                    tools=[session],
                ),
            )

            return response.text or "No text response was returned."
