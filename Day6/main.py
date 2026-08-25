from fastapi import FastAPI, Depends, HTTPException
# Depends,  manage FastAPI dependencies
#HTTPException, Returns an HTTP error
from sqlalchemy.orm import Session

from Database import Base, engine, get_db
from models import User, Post

# Create database tables
Base.metadata.create_all(bind=engine)
# Base. base of table
# metadata. summary of data base information
# create_all. create table with information
app = FastAPI()

# Get posts belonging to a user
@app.get("/users/{user_id}/posts")
def get_user_posts(
    user_id: int,
    db: Session = Depends(get_db)
):
    # Find the user
    user = db.query(User).filter(User.id == user_id).first()

    # If the user does not exist
    if user is None:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    # Get all posts belonging to this user
    return user.posts
