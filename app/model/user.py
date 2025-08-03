# model/user_service.py
from sqlalchemy import Column, Integer, String
from app.core.database import db_manager

class User(db_manager.Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    user_name = Column(String(255), nullable=False)
    lan_id = Column(String(255), unique=True, nullable=False)
    email_id = Column(String(255), unique=True, nullable=False)
    line_manager = Column(String(255))
    line_manager_mail_id = Column(String(255))
    designation = Column(String(255))
    hashed_password = Column(String(255), nullable=False)
