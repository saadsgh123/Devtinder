from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from models.basemodel import Base, BaseModel


class Education(BaseModel, Base):
    __tablename__ = 'education'
    id = Column(Integer, primary_key=True)
    start_date = Column(String(50))
    end_date = Column(String(50))

    user_id = Column(String(36), ForeignKey('user.id'))
    school_id = Column(Integer, ForeignKey('school.id'))

    # Many-to-One relationship: An education record belongs to one user
    user = relationship("User", back_populates="education")
    school = relationship("School", back_populates="educations")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
