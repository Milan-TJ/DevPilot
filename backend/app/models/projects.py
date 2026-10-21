from sqlmodel import SQLModel, Field


class Project(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True )
    name: str
    repository: str