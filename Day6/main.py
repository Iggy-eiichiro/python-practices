from fastapi import FastAPI, Depends, Query
from sqlalchemy.orm import Session

from Database import get_db
from models import User, Post

app = FastAPI()
@app.get("/posts")
def search_posts(
    search: str,
    db: Session = Depends(get_db)
):

    posts = db.query(Post).filter(
        Post.content.contains(search)
    ).all()

    return [
        {
            "id": post.id,
            "title": post.title,
            "content": post.content,
            "user_id": post.user_id,
            "user_name": post.user.name
        }
        for post in posts
    ]