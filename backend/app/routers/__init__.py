from fastapi import APIRouter

from app.routers import projects, github, ai, automation

api_router = APIRouter()
api_router.include_router(ai.router)
api_router.include_router(projects.router)
api_router.include_router(github.router)
api_router.include_router(automation.router)
