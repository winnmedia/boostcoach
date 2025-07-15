from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from services import user_service
from main import get_db # Import get_db from main.py
from ..database import get_db # Import get_db from database.py

router = APIRouter()

@router.get("/users/")
async def read_users(db: Session = Depends(get_db)):
    users = user_service.get_all_users(db)
    return users

@router.get("/users/{user_id}")
async def read_user(user_id: int, db: Session = Depends(get_db)):
    user = user_service.get_user_by_id(db, user_id)
    return user
