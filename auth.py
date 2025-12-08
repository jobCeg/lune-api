from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.auth.schemas import RegisterRequest, RegisterResponse
from app.auth.service import AuthService

router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post("/register", response_model=RegisterResponse, status_code=201)
def register_user(payload: RegisterRequest, db: Session = Depends(get_db)):
    """
    Register a new user in the system.
    """
    service = AuthService(db)

    # Check if email already exists
    if service.get_user_by_email(payload.email):
        raise HTTPException(status_code=400, detail="Email already registered")

    return service.register_user(payload)

