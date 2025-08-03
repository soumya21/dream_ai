# schemas/user_schema.py
from pydantic import BaseModel, EmailStr, Field

class UserCreate(BaseModel):
    user_name: str
    lan_id: str
    email_id: EmailStr
    line_manager: str = None
    line_manager_mail_id: EmailStr = None
    designation: str = None
    hashed_password: str

class UserUpdate(BaseModel):
    user_name: str = None
    lan_id: str = None
    email_id: EmailStr = None
    line_manager: str = None
    line_manager_mail_id: EmailStr = None
    designation: str = None
    hashed_password: str = None

class UserResponse(BaseModel):
    id: int
    user_name: str
    lan_id: str
    email_id: EmailStr
    line_manager: str = None
    line_manager_mail_id: EmailStr = None
    designation: str = None
    hashed_password: str

    class Config:
        orm_mode = True
