from fastapi import FastAPI
#FastAPI = your web/API application
#SQLAlchemy = the tool that lets Python communicate with the database
#PostgreSQL = the actual database
from Database import Base, engine, SessionLocal
from models import User, Post


# make the table
Base.metadata.create_all(engine)


app = FastAPI()


# How to Create a Session That Interacts with a Database
db = SessionLocal()


# Make "User"
user = User(
    name="Eiichiro",
    email="eiichiro@example.com"
)


# Make "Post"
post = Post(
    title="My First Post",
    content="Hello World!",
    user=user
)


# Add to "Session"
db.add(user)

# Sessionに追加
db.add(post)


# Extension of the Retention Period for the Database
db.commit()


@app.get("/")
def home():
    return {
        "User": "users table",
        "Post": "posts table"
    }
# session, a mechanism for maintaining a series of exchanges and states