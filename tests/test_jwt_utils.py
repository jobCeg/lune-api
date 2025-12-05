import os
import jwt
from app.utils.jwt_utils import generateToken

def test_generate_token():
    os.environ["JWT_SECRET"] = "test_secret"
    os.environ["JWT_EXP_DELTA_SECONDS"] = "3600"

    token = generateToken(1)
    decoded = jwt.decode(token, "test_secret", algorithms=["HS256"])

    assert decoded["user_id"] == 1
    assert "exp" in decoded
    assert "iat" in decoded

