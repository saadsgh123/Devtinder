from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from models.basemodel import Base, BaseModel
from engine import relations


class Technology(BaseModel, Base):
    __tablename__ = 'technology'
    id = Column(String(50), primary_key=True)
    name = Column(String(50))
    picture = Column(String(150))
    # parent_id = Column(Integer, ForeignKey('technology.id'))
    user = relationship("User", secondary= relations.user_tech_table, back_populates="technology")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
