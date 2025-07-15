from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from prisma import Prisma
from ..services import workout_log_service

router = APIRouter()

class WorkoutLogCreate(BaseModel):
    title: str
    description: str | None = None
    userId: int

async def get_db():
    yield Prisma()

@router.get("/workout-logs/")
async def read_workout_logs(db: Prisma = Depends(get_db)):
    logs = await workout_log_service.get_all_workout_logs(db)
    return logs

@router.get("/workout-logs/{log_id}")
async def read_workout_log(log_id: int, db: Prisma = Depends(get_db)):
    log = await workout_log_service.get_workout_log_by_id(db, log_id)
    if not log:
        raise HTTPException(status_code=404, detail="Workout log not found")
    return log

@router.post("/workout-logs/")
async def create_workout_log(log: WorkoutLogCreate, db: Prisma = Depends(get_db)):
    created_log = await workout_log_service.create_workout_log(db, log.title, log.description, log.userId)
    return created_log
