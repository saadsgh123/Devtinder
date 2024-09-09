from sqlalchemy import Column, Integer, String, ForeignKey
from models.basemodel import Base, BaseModel


class Technology(BaseModel, Base):
    __tablename__ = 'technology'
    id = Column(String(50), primary_key=True)
    name = Column(String(50))
    picture = Column(String(150))
    # parent_id = Column(Integer, ForeignKey('technology.id'))

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
