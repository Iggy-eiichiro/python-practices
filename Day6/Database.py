from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# PostgreSQL database URL
DATABASE_URL = "postgresql://postgres.ahtvumqsnxlvspnasbpn:Pass%40bcd122333@aws-0-ap-northeast-1.pooler.supabase.com:5432/pagila"

# Create a connection to the database
engine = create_engine(DATABASE_URL)

# Create a database session
SessionLocal = sessionmaker(#make session
    autocommit=False,#not to commit automatically
    autoflush=False,#not to fluah automatically
    bind=engine# use and connect db with engine
)

# Base class for database models
Base = declarative_base()

# Create a database session for each request
def get_db():
    db = SessionLocal()

    try:
        yield db #give db session to FstAPI
    finally:
        db.close()#close db session
