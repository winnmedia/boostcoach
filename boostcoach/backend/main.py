from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from backend.routes import user, workout_log, exercise_analysis
from .models import Base # Import Base from models.py

# Database connection URL (replace with your actual database URL or environment variable)
DATABASE_URL = "postgresql://user:pass@db:5432/boostcoach"

# Create SQLAlchemy engine
engine = create_engine(DATABASE_URL)

# Create a SessionLocal class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

app = FastAPI()

@app.on_event("startup")
async def startup():
    # Create database tables if they don't exist
    Base.metadata.create_all(bind=engine)
    pass

@app.on_event("shutdown")
async def shutdown():
    pass

# Dependency to get a database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

app.include_router(user.router)
app.include_router(workout_log.router)
app.include_router(exercise_analysis.router)

@app.get("/")
async def read_root():
    return {"message": "Welcome to BoostCoach Backend!"}
