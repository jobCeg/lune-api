import os
import jwt
import pytest
from app.utils.jwt_utils import generate_token

def test_generate_token():
    os.environ["JWT_SECRET"] = "test_secret"
    os.environ["JWT_EXP_DELTA_SECONDS"] = "3600"

    token = generate_token(1)
    decoded = jwt.decode(token, "test_secret", algorithms=["HS256"])

    assert decoded["user_id"] == 1
    assert "exp" in decoded
    assert "iat" in decoded

def test_generate_token_missing_secret_raises_value_error(monkeypatch):
    # Ensure JWT_SECRET is not set
    monkeypatch.delenv("JWT_SECRET", raising=False)
    monkeypatch.setenv("JWT_EXP_DELTA_SECONDS", "3600")

    with pytest.raises(ValueError):
        generate_token(1)

def test_generate_token_invalid_signature():
    os.environ["JWT_SECRET"] = "test_secret"
    os.environ["JWT_EXP_DELTA_SECONDS"] = "3600"

    token = generate_token(1)

    with pytest.raises(jwt.exceptions.InvalidSignatureError):
        jwt.decode(token, "wrong_secret", algorithms=["HS256"])

