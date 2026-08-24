from sqlalchemy import create_engine# Building an Engine to Connect to a Database
from sqlalchemy.orm import declarative_base, sessionmaker # This is used to define Python classes as database tables. 

DATABASE_URL = "postgresql://postgres.ahtvumqsnxlvspnasbpn:Pass%40bcd122333@aws-0-ap-northeast-1.pooler.supabase.com:5432/pagila"

engine = create_engine(DATABASE_URL)#Please use the database connection information stored in DATABASE_URL to connect.

Base = declarative_base()# Now I'm going to create a database table using a Python class.

SessionLocal = sessionmaker(bind=engine)#session,An interface for exchanging data between Python and a database