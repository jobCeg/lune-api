import os
from datetime import datetime, timedelta, timezone
import jwt
from fastapi import HTTPException

def generate_token(user_id: int, role: str) -> str:
    """
    Generate a JWT token for a given user ID and role.
    """
    JWT_SECRET = os.getenv("JWT_SECRET")
    JWT_EXP_DELTA_SECONDS = int(os.getenv("JWT_EXP_DELTA_SECONDS", 3600))

    if not JWT_SECRET:
        raise ValueError("JWT_SECRET is not set in the environment")

    payload = {
        "user_id": user_id,
        "role": role,
        "exp": datetime.now(timezone.utc) + timedelta(seconds=JWT_EXP_DELTA_SECONDS),
        "iat": datetime.now(timezone.utc)
    }

    return jwt.encode(payload, JWT_SECRET, algorithm="HS256")


def verify_token(token: str) -> dict:
    """
    Verify a JWT token and return the payload.
    """
    JWT_SECRET = os.getenv("JWT_SECRET")

    if not JWT_SECRET:
        raise ValueError("JWT_SECRET is not set in the environment")

    try:
        payload = jwt.decode(token, JWT_SECRET, algorithms=["HS256"])

        if payload.get("user_id") is None or payload.get("role") is None:
            raise HTTPException(status_code=401, detail="Invalid token payload")

        return payload

    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")


