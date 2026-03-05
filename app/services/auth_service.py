from fastapi import HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from app.models.user import User
from app.schemas.auth import RegisterRequest, RegisterResponse, LoginRequest, LoginResponse
from app.utils.passwords import hashPassword, verifyPassword
from app.utils.jwt_utils import generate_token

class AuthService:

    @staticmethod
    def register(payload: RegisterRequest, db: Session) -> RegisterResponse:
        if len(payload.password.encode("utf-8")) > 72:
            raise HTTPException(
                status_code=400,
                detail="Password cannot exceed 72 bytes."
            )

        hashed = hashPassword(payload.password)

        new_user = User(
            email=payload.email,
            hashed_password=hashed,
            role=payload.role or "user"
        )

        try:
            db.add(new_user)
            db.commit()
            db.refresh(new_user)
        except IntegrityError:
            db.rollback()
            raise HTTPException(status_code=409, detail="Email already registered")

        token = generate_token(new_user.id, new_user.role)

        return RegisterResponse(
            id=new_user.id,
            email=new_user.email,
            role=new_user.role,
            token=token
        )

    @staticmethod
    def login(payload: LoginRequest, db: Session) -> LoginResponse:
        user = db.query(User).filter(User.email == payload.email).first()

        if not user or not verifyPassword(payload.password, user.hashed_password):
            raise HTTPException(status_code=401, detail="Invalid credentials")

        token = generate_token(user.id, user.role)

        return LoginResponse(
            id=user.id,
            email=user.email,
            role=user.role,
            token=token
        )

