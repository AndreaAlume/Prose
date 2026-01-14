from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from Database.Models.project import Project
from Database.database import start_database

router = APIRouter(
    prefix="/projects",
    tags=["projects"]
)

@router.get("/")
def getAllProjects(db: Session = Depends(start_database)):
    projects = db.query(Project).all()
    return [{"id": p.id, "name": p.name} for p in projects]

@router.get("/{id}")
def getProjectById(id: int, db: Session = Depends(start_database)):
    project = db.query(Project).filter(Project.id == id).first()
    if not project:
        return {"error": "Project not found"}
    return {"id": project.id, "name": project.name}