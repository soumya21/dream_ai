# model/my_table.py
from sqlalchemy import Column, Integer, String
from app.core.database import db_manager  # Import the db_manager instance

class MyTable(db_manager.Base):  # Use db_manager.Base for the declarative base
    __tablename__ = "my_table"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
