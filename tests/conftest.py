import os
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.core.db import Base
from app.models.user import User

@pytest.fixture
def db_session():
    """
    Provide a SQLAlchemy session for testing.
    Cleans the 'users' table before each test to avoid unique constraint issues.
    """
    # Load environment variables
    DB_HOST = os.getenv("DB_HOST", "localhost")
    DB_PORT = os.getenv("DB_PORT", 5432)
    DB_NAME = os.getenv("DB_NAME", "choilololox")  # Use a test database if possible
    DB_USER = os.getenv("DB_USER", "Choilolox")
    DB_PASS = os.getenv("DB_PASS", "123456")

    DATABASE_URL = f"postgresql+psycopg2://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

    # Create engine and session
    engine = create_engine(DATABASE_URL)
    TestingSessionLocal = sessionmaker(bind=engine)

    # Create tables if they don't exist
    Base.metadata.create_all(bind=engine)

    session = TestingSessionLocal()

    # Clean the 'users' table before each test
    session.query(User).delete()
    session.commit()

    try:
        yield session
    finally:
        session.rollback()
        session.close()

