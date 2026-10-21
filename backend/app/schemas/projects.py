from sqlmodel import SQLModel


class ProjectCreate(SQLModel):
    name: str
    repository: str

class ProjectUpdate(SQLModel):
    name: str
    repository: str