import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.core.db import Base
from app.models.user import User

# Fixture for in-memory SQLite engine
@pytest.fixture
def test_engine():
    engine = create_engine("sqlite:///:memory:")  # Use in-memory DB for fast tests
    Base.metadata.create_all(engine)
    yield engine
    Base.metadata.drop_all(engine)

# Fixture for database session
@pytest.fixture
def db_session(test_engine):
    SessionLocal = sessionmaker(bind=test_engine)
    session = SessionLocal()
    yield session
    session.rollback()
    session.close()

# Test creating users with unique emails using parameterized inputs
@pytest.mark.parametrize(
    "email,passwordHash",
    [
        ("test1@example.com", "hash_prueba1"),
        ("test2@example.com", "hash_prueba2"),
    ],
)
def test_create_user(db_session, email, passwordHash):
    user = User(email=email, passwordHash=passwordHash)
    db_session.add(user)
    db_session.flush()

    retrieved = db_session.query(User).filter_by(email=email).first()
    assert retrieved is not None
    assert retrieved.passwordHash == passwordHash

