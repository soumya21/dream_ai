from fastapi import APIRouter, Depends

router = APIRouter()

@router.get("/health")
async def save_item_endpoint():
    return "welcome to the aila app, a new way to interact with the HR application"
