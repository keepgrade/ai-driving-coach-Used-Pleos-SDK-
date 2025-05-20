from fastapi import APIRouter
from app.models.schemas import DrivingData
from app.services.score import calculate_score

router = APIRouter()

@router.post("/score")
def get_score(data: DrivingData):
    score = calculate_score(data.speed, data.brake_count)
    return {"score": score}
