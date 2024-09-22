from models.basemodel import Base
from sqlalchemy import Table, Column, String, ForeignKey

# Association table for the many-to-many relationship
user_tech_table = Table('user_tech', Base.metadata,
                        Column('user_id', String(36), ForeignKey('user.id')),
                        Column('tech_id', String(36), ForeignKey('tech.id'))
                        )
