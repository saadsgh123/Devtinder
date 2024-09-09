from sqlalchemy import Column, Integer, String
from models.basemodel import Base, BaseModel


class User(BaseModel, Base):
    __tablename__ = 'user'
    id = Column(String(36), primary_key=True)
    username = Column(String(20), unique=True, nullable=False)
    email = Column(String(50), unique=True, nullable=False)
    password = Column(String(50), nullable=False)
    job_title = Column(String(50), nullable=False)
    country = Column(String(50), nullable=False)
    city = Column(String(50), nullable=False)
    bio = Column(String(100))
    small_bio = Column(String(100))
    location = Column(String(50))
    Exp = Column(Integer, nullable=False)
    profile_pic = Column(String(100))
    github_url = Column(String(100))
    facebook_url = Column(String(100))
    linkedln = Column(String(100))
    stackoverflow = Column(String(100))
    medium_url = Column(String(100))
    pro_mail = Column(String(100))

    def __init__(self, *args, **kwargs):
        """initializes user"""
        super().__init__(*args, **kwargs)



