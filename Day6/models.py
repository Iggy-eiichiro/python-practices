from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from Database import Base


class User(Base):

    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)

    # One User can have many Posts
    posts = relationship("Post", back_populates="user")


class Post(Base):

    __tablename__ = "posts"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    content = Column(String)

    # Connect Post to User
    user_id = Column(Integer, ForeignKey("users.id"))

    # One Post belongs to one User
    user = relationship("User", back_populates="posts")