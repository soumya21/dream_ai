# service/leave_service.py
from sqlalchemy.orm import Session
from datetime import datetime
from app.repository.leave_repository import LeaveRepository
from app.repository.user_repository import UserRepository
from app.repository.basic_leave_details_repository import BasicLeaveDetailsRepository

class LeaveService:
    def __init__(self, db: Session):
        self.leave_repository = LeaveRepository(db)
        self.user_repository = UserRepository(db)
        self.leave_details_repository = BasicLeaveDetailsRepository(db)

    def apply_leave(self, email_id: str, start_date: str, end_date: str, leave_type: str):
        user = self.user_repository.get_user_by_email(email_id)
        if not user:
            raise ValueError("User not found")

        user_id = user.id
        start_date = datetime.strptime(start_date, '%Y-%m-%d').date()
        end_date = datetime.strptime(end_date, '%Y-%m-%d').date()
        applied_days = (end_date - start_date).days + 1

        leave_details = self.leave_details_repository.get_all()
        leave_details_dict = {ld.leave_type: ld.allowed_days for ld in leave_details}
        if not leave_details_dict:
            raise ValueError("Leave types not defined")

        allowed_days = leave_details_dict.get(leave_type)

        if not allowed_days:
            raise ValueError("Leave type not found")

        if applied_days > allowed_days:
            raise ValueError("Applied days exceed allowed days")

        leave_data = {
            "user_id": user_id,
            "leave_type": leave_type,
            "start_date": start_date,
            "end_date": end_date,
            "days": applied_days
        }
        return self.leave_repository.create_leave(leave_data)

    def get_leaves_by_email(self, email_id: str):
        user = self.user_repository.get_user_by_email(email_id)
        if not user:
            raise ValueError("User not found")
        return self.leave_repository.get_leaves_by_user(user.id)

    def update_leave(self, leave_id: int, leave_data: dict):
        leave = self.leave_repository.update_leave(leave_id, leave_data)
        if not leave:
            raise ValueError("Leave not found")
        return leave

    def delete_leave_softly(self, leave_id: int):
        leave = self.leave_repository.delete_leave(leave_id)
        if not leave:
            raise ValueError("Leave not found")
        return {"detail": "Leave soft deleted"}

    def get_basic_leave_details(self):
        return self.leave_details_repository.get_all()

    def get_leave_balance(self, email_id: str):
        user = self.user_repository.get_user_by_email(email_id)
        if not user:
            raise ValueError("User not found")

        leaves = self.leave_repository.get_leaves_by_user_id(user.id)
        leave_details = self.leave_details_repository.get_all_leave_details()

        # Initialize leave balance dictionary
        balance = {leave.leave_type: leave.allowed_days for leave in leave_details}

        # Deduct applied leave days from the balance
        for leave in leaves:
            if not leave.deleted:  # Check if leave is not deleted
                start_date = leave.start_date
                end_date = leave.end_date
                applied_days = (end_date - start_date).days
                if leave.leave_type in balance:
                    balance[leave.leave_type] -= applied_days

        # Ensure all balances are non-negative
        for leave_type in balance:
            if balance[leave_type] < 0:
                balance[leave_type] = 0

        return balance