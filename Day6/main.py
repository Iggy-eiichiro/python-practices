from fastapi import FastAPI

from pydantic import BaseModel
from Database import SessionLocal

from models import User

app = FastAPI()
class UserUpdate(BaseModel):
    name: str
    email:str


# READ

@app.get("/users")

def get_users():

    db = SessionLocal()

    users = db.query(User).all()

    db.close()

    return users

# CREATE

@app.post("/users")

def create_user( name: str, email: str):

    db = SessionLocal()

    # 同じ名前・同じメールアドレスがあるか確認

    existing_user = db.query(User).filter(

        User.name == name,

        User.email == email

    ).first()

    # すでに存在する場合

    if existing_user:

        db.close()

        return {"message": "This user already exists"}

    # 存在しない場合は新しく登録

    user = User(

        name=name,

        email=email

    )

    db.add(user)

    db.commit()

    db.refresh(user)

    db.close()

    return user

# UPDATE
@app.put("/users/{user_id}")



@app.put("/users/{user_id}")

def update_user(user_id: int, user_data: UserUpdate):

    db = SessionLocal()

    # 指定されたIDのUserを探す

    user = db.query(User).filter(User.id == user_id).first()

    if user is None:

        db.close()

        return {"message": "User not found"}

    # Userのデータを変更

    user.name = user_data.name

    user.email = user_data.email

    # DBに保存

    db.commit()

    db.refresh(user)

    db.close()

    return user
# @app.put("/users/{user_id}")

# def update_user(user_id: int, name: str, email: str):

#     db = SessionLocal()

#     user = db.query(User).filter(User.id == user_id).first()

#     user.name = name

#     user.email = email

#     db.commit()

#     db.refresh(user)

#     db.close()

#     return user

# DELETE

@app.delete("/users/{user_id}")

def delete_user(user_id: int):

    db = SessionLocal()

    user = db.query(User).filter(User.id == user_id).first()

    db.delete(user)

    db.commit()

    db.close()

    return {"message": "User deleted"}
