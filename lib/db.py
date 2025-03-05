from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from lib.models import Base

# Define the database URL (use SQLite for now)
DATABASE_URL = "sqlite:///freebies.db"

# Create the engine (connects SQLAlchemy to the database)
engine = create_engine(DATABASE_URL, echo=True)

# Create a configured "Session" class
SessionLocal = sessionmaker(bind=engine)

# Create a session instance
session = SessionLocal()

# Create tables if they don't exist
Base.metadata.create_all(engine)
