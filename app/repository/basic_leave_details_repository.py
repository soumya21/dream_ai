# repository/basic_leave_details_repository.py
from sqlalchemy.orm import Session
from app.model.basic_leave_details import BasicLeaveDetails

class BasicLeaveDetailsRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_all(self):
        return self.db.query(BasicLeaveDetails).all()

    def get_all_leave_details(self):
        return self.db.query(BasicLeaveDetails).all()