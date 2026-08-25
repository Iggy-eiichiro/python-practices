from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from Database import get_db
from models import User
from auth import create_access_token, get_current_user


app = FastAPI()


# 09 JWT Authentication
@app.post("/login")
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):

    user = db.query(User).filter(
        User.name == form_data.username
    ).first()

    if user is None:
        raise HTTPException(
            status_code=401,
            detail="Incorrect name or password"
        )

    if user.password != form_data.password:
        raise HTTPException(
            status_code=401,
            detail="Incorrect name or password"
        )

    access_token = create_access_token(user.id)

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }


# 10 Protected APIs
@app.get("/profile")
def get_profile(
    user_id: int = Depends(get_current_user)
):

    return {
        "message": "You are authenticated",
        "user_id": user_id
    }