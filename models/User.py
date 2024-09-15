from sqlalchemy import Column, Integer, String
from models.basemodel import Base, BaseModel


class User(BaseModel, Base):
    __tablename__ = 'user'
    id = Column(String(36), primary_key=True)
    username = Column(String(20), unique=True)
    email = Column(String(50), unique=True)
    password = Column(String(50))
    job_title = Column(String(50))
    country = Column(String(50))
    city = Column(String(50))
    description = Column(String(100))

    def __init__(self, *args, **kwargs):
        """initializes user"""
        super().__init__(*args, **kwargs)
