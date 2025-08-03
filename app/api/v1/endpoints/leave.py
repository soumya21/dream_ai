# api/leave_api.py
from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session
from app.service.leave_service import LeaveService
from app.core.database import get_db

router = APIRouter()

class ApplyLeaveRequest(BaseModel):
    email_id: str
    start_date: str
    end_date: str
    leave_type: str


def get_leave_service(db: Session = Depends(get_db)):
    return LeaveService(db)

@router.post("/apply-leave/")
def apply_leave(request: ApplyLeaveRequest, service: LeaveService = Depends(get_leave_service)):
    try:
        return service.apply_leave(request.email_id, request.start_date, request.end_date, request.leave_type)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/leaves/")
def get_leaves_by_email(email_id: str, service: LeaveService = Depends(get_leave_service)):
    try:
        return service.get_leaves_by_email(email_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.put("/leaves/{leave_id}")
def update_leave(leave_id: int, leave_data: dict, service: LeaveService = Depends(get_leave_service)):
    try:
        return service.update_leave(leave_id, leave_data)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.delete("/leaves/{leave_id}")
def delete_leave_softly(leave_id: int, service: LeaveService = Depends(get_leave_service)):
    try:
        return service.delete_leave_softly(leave_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.get("/basic-leave-details/")
def get_basic_leave_details(service: LeaveService = Depends(get_leave_service)):
    return service.get_basic_leave_details()

@router.get("/leave-balance/")
def get_leave_balance(email_id: str, service: LeaveService = Depends(get_leave_service)):
    try:
        balance = service.get_leave_balance(email_id)
        return {"email_id": email_id, "balance": balance}
    except HTTPException as e:
        raise HTTPException(status_code=e.status_code, detail=e.detail)
