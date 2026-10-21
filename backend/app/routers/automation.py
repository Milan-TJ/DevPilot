from fastapi import APIRouter, HTTPException

from app.services.automation_service import run_validation

router = APIRouter(
    prefix="/automation",
    tags=["Automation"],
)


@router.post("/validate")
async def validate_project():
    try:
        return await run_validation()
    except Exception:
        # Log the full exception on the server in production.
        raise HTTPException(
            status_code=500,
            detail="Validation workflow failed.",
        )
