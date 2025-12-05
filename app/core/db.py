import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import declarative_base

# Load environment variables from .env
load_dotenv()

DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", 5432)
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")

# Build database URL
DATABASE_URL = f"postgresql+psycopg2://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# Base for models


Base = declarative_base()

def get_engine():
    """Creates and returns a SQLAlchemy engine."""
    return create_engine(DATABASE_URL)

def test_connection():
    """Tests the database connection."""
    try:
        engine = get_engine()
        with engine.connect() as connection:
            connection.execute("SELECT 1")
        return True
    except SQLAlchemyError:
        return False

