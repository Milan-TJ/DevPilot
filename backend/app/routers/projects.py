from fastapi import APIRouter, HTTPException, Depends, status
from sqlmodel import Session, select

from app.db.session import get_session
from app.models.projects import Project
from app.schemas.projects import ProjectCreate, ProjectUpdate


router = APIRouter(prefix="/projects", tags=["projects"])

@router.get("/all",summary="List all projects",
    description="Retrieve all projects available to the authenticated user.")
async def get_all_projects(
    session: Session = Depends(get_session)):

    projects = session.exec(
        select(Project)
    ).all()

    return projects

@router.get("/{project_id}")
async def get_project(
    project_id: int,   
    session: Session = Depends(get_session)
):

    project = session.get(Project, project_id)

    if not project:
        raise HTTPException(
            status_code=404,
            detail="Project not found"
        )

    return project


@router.post(
    "",
    status_code=status.HTTP_201_CREATED
)
async def create_project(
    project: ProjectCreate,
    session: Session = Depends(get_session)
):

    db_project = Project(
        name=project.name,
        repository=project.repository
    )

    session.add(db_project)
    session.commit()
    session.refresh(db_project)

    return db_project

@router.put("/projects/{project_id}")
async def update_project(
    project_id: int,
    project_data: ProjectUpdate,
    session: Session = Depends(get_session)
):

    project = session.get(Project, project_id)

    if not project:
        raise HTTPException(
            status_code=404,
            detail="Project not found"
        )

    project.name = project_data.name
    project.repository = project_data.repository

    session.add(project)
    session.commit()
    session.refresh(project)

    return project



@router.delete("/{project_id}")
async def delete_project(
    project_id: int,
    session: Session = Depends(get_session)
):

    project = session.get(Project, project_id)

    if not project:
        raise HTTPException(
            status_code=404,
            detail="Project not found"
        )

    session.delete(project)
    session.commit()

    return {
        "message": "Project deleted successfully"
    }