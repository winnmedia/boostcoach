from fastapi import FastAPI
from routes import user, workout_log, exercise_analysis
from prisma import Prisma

app = FastAPI()

@app.on_event("startup")
async def startup():
    app.state.db = Prisma()
    await app.state.db.connect()

@app.on_event("shutdown")
async def shutdown():
    await app.state.db.disconnect()

app.include_router(user.router)
app.include_router(workout_log.router)
app.include_router(exercise_analysis.router)

@app.get("/")
async def read_root():
    return {"message": "Welcome to BoostCoach Backend!"}
