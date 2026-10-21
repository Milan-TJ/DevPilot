from fastapi import Depends, FastAPI, Response, HTTPException, Depends,  status
from fastapi.middleware.cors import CORSMiddleware 

# from contextlib import asynccontextmanager

from contextlib import AsyncExitStack, asynccontextmanager

from sqlmodel import text, Session
from app.db.session import create_db_and_tables, get_session

from app.routers import api_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield

app = FastAPI(
    title="DevPilot API",
    version="1.0.0",
    lifespan=lifespan
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router, prefix="/api")



@app.get("/health")
async def health_check(response: Response, session: Session = Depends(get_session)):
    try:
        test = session.execute(text("SELECT 1")).scalar()
        db_status = "connected" if test == 1 else "disconnected"
        return {
        "status": "healthy",
        "database": db_status,
        }
    except Exception as e:
        # Return 503 Service Unavailable if the database connection fails
        response.status_code = status.HTTP_503_SERVICE_UNAVAILABLE
        return {
            "status": "unhealthy",
            "database": "disconnected",
            "detail": str(e)
        }

