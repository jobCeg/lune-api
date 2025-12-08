from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.auth import RegisterRequest, RegisterResponse, LoginRequest, LoginResponse
from app.utils.passwords import hashPassword, verifyPassword
from app.utils.jwt_utils import generate_token

class AuthService:

    @staticmethod
    def register(payload: RegisterRequest, db: Session) -> RegisterResponse:
        # Check duplicate email
        user = db.query(User).filter(User.email == payload.email).first()
        if user:
            raise ValueError("Email already registered")

        # Hash password
        hashed = hashPassword(payload.password)

        # Create new user in database
        new_user = User(
            email=payload.email,
            hashed_password=hashed
        )

        db.add(new_user)
        db.commit()
        db.refresh(new_user)

        # Generate token
        token = generate_token(new_user.id)

        return RegisterResponse(
            id=new_user.id,
            email=new_user.email,
            token=token
        )

    @staticmethod
    def login(payload: LoginRequest, db: Session) -> LoginResponse:
        # Find user by email
        user = db.query(User).filter(User.email == payload.email).first()
        if not user:
            raise ValueError("Invalid credentials")

        # Verify password
        if not verifyPassword(payload.password, user.hashed_password):
            raise ValueError("Invalid credentials")

        # Generate token
        token = generate_token(user.id)

        return LoginResponse(
            id=user.id,
            email=user.email,
            token=token
        )

