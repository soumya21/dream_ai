# schema/leave.py
from pydantic import BaseModel
from datetime import date
from typing import Optional

class LeaveRequest(BaseModel):
    user_name: str
    start_date: str
    end_date: Optional[str] = None
    leave_type: str

class GetLeaveRequest(BaseModel):
    user_name: str
    start_date: Optional[str] = None
    end_date: Optional[str] = None
    leave_type: Optional[str] = None

class UpdateLeaveRequest(BaseModel):
    user_name: str
    start_date: Optional[str] = None
    end_date: Optional[str] = None
    leave_type: Optional[str] = None

class DeleteLeaveRequest(BaseModel):
    user_name: str
    start_date: Optional[str] = None
    end_date: Optional[str] = None
    leave_type: Optional[str] = None

class CheckLeaveRequest(BaseModel):
    user_name: str
    start_date: Optional[str] = None
    end_date: Optional[str] = None
    leave_type: Optional[str] = None



