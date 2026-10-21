import os
import httpx
from fastapi import HTTPException

from dotenv import load_dotenv

load_dotenv()

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

HEADERS = {
    "Authorization": f"Bearer {GITHUB_TOKEN}",
    "Accept": "application/vnd.github+json",
    # "X-GitHub-Api-Version": "2026-03-10"
}


async def get_repository(owner: str, repo: str):

    url = f"https://api.github.com/repos/{owner}/{repo}"

    async with httpx.AsyncClient() as client:

        response = await client.get(
            url,
            headers=HEADERS
        )

        if response.status_code == 404:
            raise HTTPException(
                status_code=404,
                detail="GitHub repository not found"
            )

        if response.status_code != 200:
            raise HTTPException(
                status_code=502,
                detail="GitHub API request failed"
            )

        return response.json()

async def get_items(owner: str, repo: str, item_type: str):

    url = f"https://api.github.com/repos/{owner}/{repo}/{item_type}"

    async with httpx.AsyncClient() as client:

        response = await client.get(
            url,
            headers=HEADERS
        )

        if response.status_code == 404:
            raise HTTPException(
                status_code=404,
                detail="GitHub repository not found"
            )

        if response.status_code != 200:
            raise HTTPException(
                status_code=502,
                detail="GitHub API request failed"
            )

        return response.json()