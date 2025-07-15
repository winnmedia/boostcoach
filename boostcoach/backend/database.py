from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .models import Base

# Database connection URL (replace with your actual database URL or environment variable)
DATABASE_URL = "postgresql://user:pass@db:5432/boostcoach"

# Create SQLAlchemy engine
engine = create_engine(DATABASE_URL)

# Create a SessionLocal class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Dependency to get a database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Create database tables if they don't exist
Base.metadata.create_all(bind=engine)
