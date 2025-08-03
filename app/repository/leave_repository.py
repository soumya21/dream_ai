# repository/leave_repository.py
from sqlalchemy.orm import Session
from app.model.leave import Leave

class LeaveRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_leave(self, leave_data):
        leave = Leave(**leave_data)
        self.db.add(leave)
        self.db.commit()
        self.db.refresh(leave)
        return leave

    def get_leaves_by_user(self, user_id: int):
        return self.db.query(Leave).filter(Leave.user_id == user_id, Leave.deleted == False).all()

    def update_leave(self, leave_id: int, leave_data):
        leave = self.db.query(Leave).filter(Leave.id == leave_id).first()
        if leave:
            for key, value in leave_data.items():
                setattr(leave, key, value)
            self.db.commit()
            self.db.refresh(leave)
        return leave

    def delete_leave(self, leave_id: int):
        leave = self.db.query(Leave).filter(Leave.id == leave_id).first()
        if leave:
            leave.deleted = True
            self.db.commit()
        return leave

    def get_leaves_by_user_id(self, user_id: int):
        return self.db.query(Leave).filter(Leave.user_id == user_id).all()
