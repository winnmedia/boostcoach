from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session
from ..services import workout_log_service
from ..main import get_db # Import get_db from main.py

router = APIRouter()

class WorkoutLogCreate(BaseModel):
    title: str
    description: str | None = None
    user_id: int # Changed from userId to user_id for SQLAlchemy model consistency

@router.get("/workout-logs/")
async def read_workout_logs(db: Session = Depends(get_db)):
    logs = workout_log_service.get_all_workout_logs(db)
    return logs

@router.get("/workout-logs/{log_id}")
async def read_workout_log(log_id: int, db: Session = Depends(get_db)):
    log = workout_log_service.get_workout_log_by_id(db, log_id)
    if not log:
        raise HTTPException(status_code=404, detail="Workout log not found")
    return log

@router.post("/workout-logs/")
async def create_workout_log(log: WorkoutLogCreate, db: Session = Depends(get_db)):
    created_log = workout_log_service.create_workout_log(db, log.title, log.description, log.user_id)
    return created_log
