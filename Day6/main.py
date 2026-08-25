from fastapi import FastAPI, Depends
from pydantic import BaseModel #pydantic. data checker
from sqlalchemy.orm import Session

from Database import get_db
from models import User, Post


app = FastAPI()


# -------------------------
# Request data models
# -------------------------

class UserUpdate(BaseModel):
    name: str
    email: str


class PostCreate(BaseModel):
    title: str
    content: str


# -------------------------
# User CRUD
# -------------------------

# READ
@app.get("/users")
def get_users(db: Session = Depends(get_db)):

    users = db.query(User).all()

    return users


# CREATE
@app.post("/users")
def create_user(
    name: str,
    email: str,
    db: Session = Depends(get_db) # just depends on get_depens
):

    # Check if the same user already exists
    existing_user = db.query(User).filter(
        User.name == name,
        User.email == email
    ).first()

    if existing_user:
        return {"message": "This user already exists"}

    # Create a new User
    user = User(
        name=name,
        email=email
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    return user


# UPDATE
@app.put("/users/{user_id}")
def update_user(
    user_id: int,
    user_data: UserUpdate,
    db: Session = Depends(get_db)
):

    # Find the User
    user = db.query(User).filter(
        User.id == user_id
    ).first()

    if user is None:
        return {"message": "User not found"}

    # Update User data
    user.name = user_data.name
    user.email = user_data.email

    db.commit()
    db.refresh(user)

    return user


# DELETE
@app.delete("/users/{user_id}")
def delete_user(
    user_id: int,
    db: Session = Depends(get_db)
):

    # Find the User
    user = db.query(User).filter(
        User.id == user_id
    ).first()

    if user is None:
        return {"message": "User not found"}

    db.delete(user)
    db.commit()

    return {"message": "User deleted"}


# -------------------------
# Post
# -------------------------

# CREATE POST
@app.post("/users/{user_id}/posts")
def create_post(
    user_id: int,
    post_data: PostCreate,
    db: Session = Depends(get_db)
):

    # Find the User
    user = db.query(User).filter(
        User.id == user_id
    ).first()

    if user is None:
        return {"message": "User not found"}

    # Create a new Post
    post = Post(
        title=post_data.title,
        content=post_data.content,
        user_id=user_id
    )

    db.add(post)
    db.commit()
    db.refresh(post)

    return post


# GET POSTS BELONGING TO A USER
@app.get("/users/{user_id}/posts")
def get_user_posts(
    user_id: int,
    db: Session = Depends(get_db)
):

    # Find the User
    user = db.query(User).filter(
        User.id == user_id
    ).first()

    if user is None:
        return {"message": "User not found"}

    # Get Posts belonging to this User
    return user.posts
