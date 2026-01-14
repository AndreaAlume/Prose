from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy_utils import LtreeType
from Database.database import Base

class Module(Base):
    __tablename__ = "modules"

    id = Column(Integer, primary_key=True)
    name = Column(String(40), nullable=False)
    path = Column(LtreeType)
    
    id_project = Column(
        Integer,
        ForeignKey("projects.id"),
        nullable=False
    )

