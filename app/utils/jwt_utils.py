import os
from datetime import datetime, timedelta, timezone
import jwt

def generate_token(user_id: int) -> str:
    """
    Generate a JWT token for a given user ID.
    Returns the encoded JWT as a string.
    """
    # Load secret and expiration from environment inside the function
    JWT_SECRET = os.getenv("JWT_SECRET")
    JWT_EXP_DELTA_SECONDS = int(os.getenv("JWT_EXP_DELTA_SECONDS", 3600))

    if not JWT_SECRET:
        raise ValueError("JWT_SECRET is not set in the environment")

    payload = {
        "user_id": user_id,
        "exp": datetime.now(timezone.utc) + timedelta(seconds=JWT_EXP_DELTA_SECONDS),
        "iat": datetime.now(timezone.utc)
    }

    return jwt.encode(payload, JWT_SECRET, algorithm="HS256")

