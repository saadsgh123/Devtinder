from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from models.basemodel import Base, BaseModel


class School(BaseModel, Base):
    __tablename__ = 'school'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))

    # One-to-Many relationship: A school can have many education records
    educations = relationship("Education", back_populates="school")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

