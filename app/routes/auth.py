from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.auth import (
    RegisterRequest,
    RegisterResponse,
    LoginRequest,
    LoginResponse,
)
from app.services.auth_service import AuthService
from app.core.db import get_db

# Add prefix "/auth" so final routes become /auth/register and /auth/login
router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/register", response_model=RegisterResponse)
def register(payload: RegisterRequest, db: Session = Depends(get_db)):
    """
    Register endpoint:
    - Validates input via RegisterRequest
    - Delegates logic to AuthService
    - Catches duplicate email errors
    - Returns RegisterResponse with JWT token
    """
    try:
        return AuthService.register(payload, db)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e)) from e


@router.post("/login", response_model=LoginResponse)
def login(payload: LoginRequest, db: Session = Depends(get_db)):
    """
    Login endpoint:
    - Validates input via LoginRequest
    - Delegates logic to AuthService
    - Returns LoginResponse with JWT token if credentials are valid
    - Returns 401 Unauthorized if invalid
    """
    try:
        return AuthService.login(payload, db)
    except ValueError as e:
        raise HTTPException(status_code=401, detail=str(e)) from e

