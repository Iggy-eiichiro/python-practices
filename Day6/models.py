from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from Database import Base


# User table
class User(Base):

    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)

    # One User can have many Posts
    posts = relationship("Post", back_populates="user")


# Post table
class Post(Base):

    __tablename__ = "posts"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    content = Column(String)

    # Connect Post to User
    user_id = Column(Integer, ForeignKey("users.id"))

    # Connect Post and User
    user = relationship("User", back_populates="posts")
