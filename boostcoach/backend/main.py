from fastapi import FastAPI
from routes import user, workout_log, exercise_analysis
from .database import get_db # Import get_db from database.py

app = FastAPI()

@app.on_event("startup")
async def startup():
    pass

@app.on_event("shutdown")
async def shutdown():
    pass

app.include_router(user.router)
app.include_router(workout_log.router)
app.include_router(exercise_analysis.router)

@app.get("/")
async def read_root():
    return {"message": "Welcome to BoostCoach Backend!"}
