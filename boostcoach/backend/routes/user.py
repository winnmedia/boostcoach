from fastapi import APIRouter, Depends
from prisma import Prisma
from ..services import user_service

router = APIRouter()

async def get_db():
    yield Prisma()

@router.get("/users/")
async def read_users(db: Prisma = Depends(get_db)):
    users = await user_service.get_all_users(db)
    return users

@router.get("/users/{user_id}")
async def read_user(user_id: int, db: Prisma = Depends(get_db)):
    user = await user_service.get_user_by_id(db, user_id)
    return user
