from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "postgresql://postgres.ahtvumqsnxlvspnasbpn:Pass%40bcd122333@aws-0-ap-northeast-1.pooler.supabase.com:5432/pagila"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()