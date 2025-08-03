# core/db.py
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

class DatabaseManager:
    def __init__(self):
        self.DB_USER = os.getenv("DB_USER", "your_username")
        self.DB_PASSWORD = os.getenv("DB_PASSWORD", "your_password")
        self.DB_HOST = os.getenv("DB_HOST", "your_rds_host")
        self.DB_PORT = os.getenv("DB_PORT", "3306")
        self.DB_NAME = os.getenv("DB_NAME", "your_db_name")

        self.SQLALCHEMY_DATABASE_URL = f"mysql+pymysql://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

        self.engine = create_engine(self.SQLALCHEMY_DATABASE_URL, pool_size=10, max_overflow=20)
        self.SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)
        self.Base = declarative_base()

    def get_session(self):
        db = self.SessionLocal()
        try:
            yield db
        finally:
            db.close()

# Initialize DatabaseManager
db_manager = DatabaseManager()

# Dependency for getting a DB session
def get_db():
    db = db_manager.SessionLocal()
    try:
        yield db
    finally:
        db.close()
