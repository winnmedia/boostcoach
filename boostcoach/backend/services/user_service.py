from prisma import Prisma

# db = Prisma() # 더 이상 여기서 직접 Prisma 인스턴스를 생성하지 않습니다.

async def get_all_users(db: Prisma):
    users = await db.user.find_many()
    return users

async def get_user_by_id(db: Prisma, user_id: int):
    user = await db.user.find_unique(where={'id': user_id})
    return user
