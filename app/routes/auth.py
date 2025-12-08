# sourcery skip-file
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.auth import RegisterRequest, RegisterResponse
from app.services.auth_service import AuthService
from app.core.db import get_db

# Add prefix "/auth" so final route becomes /auth/register
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

