import pytest
from app.utils.passwords import hashPassword, comparePassword

@pytest.mark.parametrize("password,wrong_password", [
    ("MySecret123!", "WrongPassword"),
    ("AnotherPass!456", "Wrong123"),
])
def test_hash_and_compare_password(password, wrong_password):
    hashed = hashPassword(password)

    # Ensure the hash is different from the plain password
    assert hashed != password

    # Correct password should match
    assert comparePassword(password, hashed)

    # Incorrect password should not match
    assert not comparePassword(wrong_password, hashed)


