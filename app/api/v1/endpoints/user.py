# api/user_api.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.service.user_service import UserService
from app.core.database import get_db
from app.schema.user_schema import UserCreate, UserUpdate, UserResponse

router = APIRouter()

def get_user_service(db: Session = Depends(get_db)):
    return UserService(db)

@router.post("/users/", response_model=UserResponse)
def create_user(user: UserCreate, service: UserService = Depends(get_user_service)):
    user_data = user.dict()
    return service.create_user(user_data)

@router.get("/users/{user_id}", response_model=UserResponse)
def read_user(user_id: int, service: UserService = Depends(get_user_service)):
    user = service.get_user(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.get("/users/", response_model=List[UserResponse])
def read_users(skip: int = 0, limit: int = 10, service: UserService = Depends(get_user_service)):
    return service.get_users(skip, limit)

@router.put("/users/{user_id}", response_model=UserResponse)
def update_user(user_id: int, user: UserUpdate, service: UserService = Depends(get_user_service)):
    user_data = user.dict(exclude_unset=True)
    updated_user = service.update_user(user_id, user_data)
    if not updated_user:
        raise HTTPException(status_code=404, detail="User not found")
    return updated_user

@router.delete("/users/{user_id}")
def delete_user(user_id: int, service: UserService = Depends(get_user_service)):
    user = service.delete_user(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return {"detail": "User deleted"}
