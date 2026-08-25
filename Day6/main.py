from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from sqlalchemy import or_

from Database import get_db
from models import Post

app = FastAPI()


@app.get("/posts")
def search_and_sort_posts(
    search: str,
    sort: str = "created_at",
    db: Session = Depends(get_db)
):

    # Start the query
    query = db.query(Post)

    # Search title OR content
    query = query.filter(
        or_(# title or content
            Post.title.contains(search),
            Post.content.contains(search)
        )
    )

    # Sort by created_at
    if sort == "created_at":
        query = query.order_by(Post.created_at)

    # Get the results
    posts = query.all()

    return posts