# model/leave.py
from sqlalchemy import Column, Integer, String, Date, Boolean
from app.core.database import db_manager

class Leave(db_manager.Base):
    __tablename__ = "leave_details"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, nullable=False)
    leave_type = Column(String(255), nullable=False)
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=False)
    days = Column(Integer, nullable=False)
    deleted = Column(Boolean, default=False)
