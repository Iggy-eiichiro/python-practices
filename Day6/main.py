from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from Database import get_db
from models import User
from schemas import UserLogin
from auth import create_access_token


app = FastAPI()


@app.post("/login")
def login(
    user_data: UserLogin,
    db: Session = Depends(get_db)
):

    # Find the user
    user = db.query(User).filter(
        User.name == user_data.name
    ).first()

    # User does not exist
    if user is None:
        raise HTTPException(
            status_code=401,
            detail="Incorrect name or password"
        )

    # Check the password
    if user.password != user_data.password:
        raise HTTPException(
            status_code=401,
            detail="Incorrect name or password"
        )

    # Create JWT
    access_token = create_access_token(user.id)

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }