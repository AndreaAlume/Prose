from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from Database.database import Base

class Project(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(40), nullable=False)
    