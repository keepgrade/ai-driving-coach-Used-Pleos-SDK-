from fastapi import APIRouter
from app.api import driving

api_router = APIRouter()
api_router.include_router(driving.router, prefix="/driving")