# model/basic_leave_details.py
from sqlalchemy import Column, Integer, String
from app.core.database import db_manager

class BasicLeaveDetails(db_manager.Base):
    __tablename__ = "basic_leave_details"

    id = Column(Integer, primary_key=True, index=True)
    leave_type = Column(String(255), nullable=False)
    allowed_days = Column(Integer, nullable=False)
