from fastapi import APIRouter, HTTPException, status, Header
from pydantic import BaseModel
import jwt
from datetime import datetime, timedelta

SECRET_KEY = "your_secret_key_here"

router = APIRouter(prefix="/auth", tags=["Authentication"])

# Dummy in-memory users
USERS_DB = [
    {"id": 1, "email": "admin@example.com", "password": "123456", "role": "admin"},
    {"id": 2, "email": "user@example.com", "password": "123456", "role": "user"}
]

class LoginRequest(BaseModel):
    email: str
    password: str


@router.post("/login")
async def login(data: LoginRequest):
    """Login endpoint returning JWT token"""
    user = next(
        (u for u in USERS_DB if u["email"] == data.email and u["password"] == data.password),
        None
    )

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials"
        )

    payload = {
        "user_id": user["id"],
        "role": user["role"],
        "exp": datetime.utcnow() + timedelta(hours=1),
        "iat": datetime.utcnow()
    }

    token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")

    return {
        "id": user["id"],
        "email": user["email"],
        "role": user["role"],
        "token": token
    }


@router.get("/me")
async def get_current_user(authorization: str = Header(...)):
    """
    Get current authenticated user from JWT token
    """
    if not authorization.startswith("Bearer "):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authorization header"
        )

    token = authorization.replace("Bearer ", "")

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
    except jwt.ExpiredSignatureError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token expired"
        )
    except jwt.InvalidTokenError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token"
        )

    user_id = payload.get("user_id")

    user = next((u for u in USERS_DB if u["id"] == user_id), None)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )

    return {
        "id": user["id"],
        "email": user["email"],
        "role": user["role"]
    }

