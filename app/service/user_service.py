# service/user_service.py
from sqlalchemy.orm import Session
from app.repository.user_repository import UserRepository

class UserService:
    def __init__(self, db: Session):
        self.repository = UserRepository(db)

    def create_user(self, user_data):
        return self.repository.create_user(user_data)

    def get_user(self, user_id: int):
        return self.repository.get_user(user_id)

    def get_users(self, skip: int = 0, limit: int = 10):
        return self.repository.get_users(skip, limit)

    def update_user(self, user_id: int, user_data):
        return self.repository.update_user(user_id, user_data)

    def delete_user(self, user_id: int):
        return self.repository.delete_user(user_id)
