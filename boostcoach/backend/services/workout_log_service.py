from sqlalchemy.orm import Session
from typing import List, Optional
from ..models import WorkoutLog

def get_all_workout_logs(db: Session):
    return db.query(WorkoutLog).all()

def get_workout_log_by_id(db: Session, log_id: int):
    return db.query(WorkoutLog).filter(WorkoutLog.id == log_id).first()

def create_workout_log(db: Session, title: str, description: Optional[str], user_id: int):
    new_log = WorkoutLog(title=title, description=description, user_id=user_id)
    db.add(new_log)
    db.commit()
    db.refresh(new_log)
    return new_log
