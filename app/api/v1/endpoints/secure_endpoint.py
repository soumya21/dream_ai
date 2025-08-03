# app/api/v1/endpoints/secure_endpoint.py
from fastapi import APIRouter, Depends
from app.api.v1.endpoints.auth import get_current_user

router = APIRouter()

# Secure endpoint
@router.get("/secure-data")
async def secure_data(current_user: str = Depends(get_current_user)):
    return {"message": f"Hello, {current_user}. This is a secure endpoint."}
