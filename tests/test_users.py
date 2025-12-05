import pytest
from app.models.user import User

@pytest.mark.parametrize(
    "email,passwordHash",
    [
        ("test1@example.com", "hash_prueba1"),
        ("test2@example.com", "hash_prueba2"),
    ],
)
def test_create_user(db_session, email, passwordHash):
    """
    Test user creation using a parameterized approach.
    Verifies that the user is correctly stored and retrievable.
    """
    # Create a new user instance
    user = User(email=email, passwordHash=passwordHash)
    
    # Add and flush to the database
    db_session.add(user)
    db_session.flush()

    # Retrieve user from the database
    retrieved = db_session.query(User).filter_by(email=email).first()
    
    # Assertions
    assert retrieved is not None
    assert retrieved.passwordHash == passwordHash

