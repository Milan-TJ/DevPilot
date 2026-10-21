from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

import logging
logger = logging.getLogger(__name__)

from app.services.agent_service import ask_devpilot

router = APIRouter(prefix="/ai", tags=["AI Assistant"])


class ChatRequest(BaseModel):
    message: str = Field(min_length=1, max_length=2000)


class ChatResponse(BaseModel):
    answer: str


@router.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    try:
        answer = await ask_devpilot(request.message)
        return ChatResponse(answer=answer)
    except Exception:
        logger.exception("ask_devpilot failed")
        raise HTTPException(
            status_code=502,
            detail="The AI assistant could not complete the request.",
        )
