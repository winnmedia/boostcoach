from prisma import Prisma
from typing import List, Optional

async def get_all_workout_logs(db: Prisma):
    logs = await db.workoutlog.find_many()
    return logs

async def get_workout_log_by_id(db: Prisma, log_id: int):
    log = await db.workoutlog.find_unique(where={'id': log_id})
    return log

async def create_workout_log(db: Prisma, title: str, description: Optional[str], user_id: int):
    log = await db.workoutlog.create(
        data={
            'title': title,
            'description': description,
            'userId': user_id
        }
    )
    return log
