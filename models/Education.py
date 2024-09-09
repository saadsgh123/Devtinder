from sqlalchemy import Column, Integer, String, ForeignKey
from models.basemodel import Base, BaseModel


class Education(BaseModel, Base):
    __tablename__ = 'education'
    id = Column(Integer, primary_key=True)
    school_id = Column(Integer, ForeignKey('school.id'))
    start_date = Column(String(50))
    end_date = Column(String(50))
    user_id = Column(Integer, ForeignKey('user.id'))

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
