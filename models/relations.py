from models.basemodel import Base
from sqlalchemy import Table, Column, String, ForeignKey

# Association table for the many-to-many relationship
user_tech_table = Table('post_tag', Base.metadata,
                        Column('post_id', String(36), ForeignKey('posts.id')),
                        Column('tag_id', String(36), ForeignKey('tags.id'))
                        )
