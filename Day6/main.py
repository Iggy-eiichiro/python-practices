from fastapi import FastAPI
from fastapi import Depends
from fastapi import HTTPException

from fastapi.security import OAuth2PasswordRequestForm

from sqlalchemy.orm import Session

from Database import get_db

from models import User
from models import Post

from auth import create_access_token
from auth import get_current_user
from auth import require_admin


app = FastAPI()


# ========================================
# 09 JWT Authentication
# ========================================

@app.post("/login")
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):

    # username = users.name
    user = db.query(User).filter(
        User.name == form_data.username
    ).first()

    # Userが存在しない
    if user is None:

        raise HTTPException(
            status_code=401,
            detail="Incorrect name or password"
        )

    # password確認
    if user.password != form_data.password:

        raise HTTPException(
            status_code=401,
            detail="Incorrect name or password"
        )

    # JWTを作る
    access_token = create_access_token(
        user.id
    )

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }


# ========================================
# 10 Protected APIs
# ========================================

@app.get("/profile")
def get_profile(
    user: User = Depends(get_current_user)
):

    return {
        "message": "You are authenticated",
        "user_id": user.id,
        "name": user.name,
        "email": user.email,
        "role": user.role
    }


# ========================================
# 11 Role-based Authorization
# ========================================

@app.delete(
    "/posts/{post_id}",
    status_code=204
)
def delete_post(
    post_id: int,

    admin: User = Depends(
        require_admin
    ),

    db: Session = Depends(get_db)
):

    # Postを探す
    post = db.query(Post).filter(
        Post.id == post_id
    ).first()

    # Postがない
    if post is None:

        raise HTTPException(
            status_code=404,
            detail="Post not found"
        )

    # Postを削除
    db.delete(post)

    db.commit()

    return