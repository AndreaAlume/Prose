from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from Database.Models.module import Module
from Database.database import start_database

router = APIRouter(
    prefix="/modules",
    tags=["modules"]
)

@router.get("/")
def getAllModules(db: Session = Depends(start_database)):
    modules = db.query(Module).all()
    return [{"id": p.id, "name": p.name} for p in modules]

@router.get("/{id}")
def getModuleById(id: int, db: Session = Depends(start_database)):
    module = db.query(Module).filter(Module.id == id).first()
    if not module:
        return {"error": "Module not found"}
    return {"id": module.id, "name": module.name}
