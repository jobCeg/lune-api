from fastapi import HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from app.models.user import User
from app.schemas.auth import RegisterRequest, RegisterResponse
from app.utils.passwords import hashPassword
from app.utils.jwt_utils import generate_token

class AuthService:

    @staticmethod
    def register(payload: RegisterRequest, db: Session) -> RegisterResponse:
        """
        Register a new user:
        - Validates email uniqueness
        - Validates password length (max 72 bytes for bcrypt)
        - Hashes password
        - Inserts user into DB safely handling concurrency
        - Returns RegisterResponse with JWT token
        """
        # Validate password length
        if len(payload.password.encode("utf-8")) > 72:
            raise HTTPException(
                status_code=400,
                detail="Password cannot exceed 72 bytes, please choose a shorter one."
            )

        # Hash password
        hashed = hashPassword(payload.password)

        # Create user object
        new_user = User(
            email=payload.email,
            hashed_password=hashed
        )

        # Insert user safely
        try:
            db.add(new_user)
            db.commit()
            db.refresh(new_user)
        except IntegrityError:
            db.rollback()
            raise HTTPException(status_code=409, detail="Email already registered")

        # Generate JWT token
        token = generate_token(new_user.id)

        return RegisterResponse(
            id=new_user.id,
            email=new_user.email,
            token=token
        )

