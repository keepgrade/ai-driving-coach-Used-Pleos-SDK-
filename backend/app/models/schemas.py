from pydantic import BaseModel

class DrivingData(BaseModel):
    speed: float
    brake_count: int