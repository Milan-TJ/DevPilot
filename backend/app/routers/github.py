from fastapi import APIRouter
from app.services.github import get_repository, get_items

router = APIRouter(prefix="/github", tags=["github"])


@router.get("/repos/{owner}/{repo}")
async def get_repository(
    owner: str,
    repo: str
):
    return await get_repository(owner, repo)

@router.get("/repos/{owner}/{repo}/branches")
async def get_branches(
    owner: str,
    repo: str
):
    return await get_items(owner, repo, "branches")

@router.get("/repos/{owner}/{repo}/commits")
async def get_commits(
    owner: str,
    repo: str
):
    return await get_items(owner, repo, "commits")

@router.get("/repos/{owner}/{repo}/pulls")
async def get_pulls(
    owner: str,
    repo: str
):
    return await get_items(owner, repo, "pulls")