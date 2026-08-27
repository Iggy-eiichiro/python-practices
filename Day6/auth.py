import jwt

from fastapi import Depends
from fastapi import HTTPException

from fastapi.security import OAuth2PasswordBearer

from Database import SessionLocal
from models import User


SECRET_KEY = "my-secret-key"

ALGORITHM = "HS256"


oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="login"
)


# JWTを作る
def create_access_token(user_id: int):

    data = {
        "sub": str(user_id)
    }

    token = jwt.encode(
        data,
        SECRET_KEY,
        algorithm=ALGORITHM
    )

    return token


# JWTを確認してUserを取得
def get_current_user(
    token: str = Depends(oauth2_scheme)
):

    try:

        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )

        user_id = payload.get("sub")

        if user_id is None:

            raise HTTPException(
                status_code=401,
                detail="Invalid token"
            )

        db = SessionLocal()

        user = db.query(User).filter(
            User.id == int(user_id)
        ).first()

        db.close()

        if user is None:

            raise HTTPException(
                status_code=401,
                detail="User not found"
            )

        return user

    except jwt.InvalidTokenError:

        raise HTTPException(
            status_code=401,
            detail="Invalid token"
        )


# Adminか確認
def require_admin(
    user: User = Depends(get_current_user)
):

    if user.role != "Admin":

        raise HTTPException(
            status_code=403,
            detail="Admin permission required"
        )

    return user