from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.auth import RegisterRequest, RegisterResponse
from app.utils.passwords import hashPassword
from app.utils.jwt_utils import generate_token


class AuthService:

    @staticmethod
    def register(payload: RegisterRequest, db: Session) -> RegisterResponse:
        # Check duplicate email
        user = db.query(User).filter(User.email == payload.email).first()
        if user:
            raise HTTPException(status_code=409, detail="Email already registered")

        # Hash password
        hashed = hashPassword(payload.password)

        # Create new user in database
        new_user = User(
            email=payload.email,
            hashed_password=hashed  # OJO: cambiar si tu modelo usa otro nombre
        )

        db.add(new_user)
        db.commit()
        db.refresh(new_user)

        # Generate token
        token = generate_token(new_user.id)

        # Return response schema
        return RegisterResponse(
            id=new_user.id,
            email=new_user.email,
            token=token
        )

