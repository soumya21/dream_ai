# service/basic_leave_details_service.py
from sqlalchemy.orm import Session
from app.repository.basic_leave_details_repository import BasicLeaveDetailsRepository

class BasicLeaveDetailsService:
    def __init__(self, db: Session):
        self.repository = BasicLeaveDetailsRepository(db)

    def get_all(self):
        return self.repository.get_all()
