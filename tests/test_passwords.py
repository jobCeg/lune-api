import pytest
from app.utils.passwords import hashPassword, comparePassword

def test_hash_and_compare_password():
    password = "MySecret123!"
    hashed = hashPassword(password)

    # Ensure the hash is different from the plain password
    assert hashed != password

    # Correct password should match
    assert comparePassword(password, hashed) is True

    # Incorrect password should not match
    assert comparePassword("WrongPassword", hashed) is False


