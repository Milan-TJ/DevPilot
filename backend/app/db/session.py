import os

from sqlmodel import SQLModel, Session, create_engine
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL: str = os.getenv(
    "DATABASE_URL",
    "postgresql://app_user:appuser123@localhost:5432/devpilot_db"
)

if not DATABASE_URL:
    raise ValueError("DATABASE_URL is not configured")

engine = create_engine( DATABASE_URL, echo=True )


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session