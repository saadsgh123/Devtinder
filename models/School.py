from sqlalchemy import Column, Integer, String, ForeignKey
from models.basemodel import Base, BaseModel


class School(BaseModel, Base):
    __tablename__ = 'school'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))

    def __init__(self, **kwargs):
        super().__init__(**kwargs)