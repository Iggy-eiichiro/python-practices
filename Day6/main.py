from fastapi import FastAPI, Depends, Query
from sqlalchemy.orm import Session

from Database import get_db
from models import User, Post

app = FastAPI()


@app.get("/posts")
def get_posts(
    page: int = 1,
    limit: int = Query(10, le=100),
    db: Session = Depends(get_db)
):

    # Calculate how many posts to skip
    skip = (page - 1) * limit

    # Get total number of posts
    total = db.query(Post).count()

    # Get posts for this page
    posts = db.query(Post).offset(skip).limit(limit).all()

    return {
        "page": page,
        "limit": limit,
        "total": total,
        "items": posts
    }