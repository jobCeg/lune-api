from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hashPassword(password: str) -> str:
    """
    Hash a password using bcrypt. Truncate to 72 characters to comply with bcrypt limits.
    """
    truncated_password = password[:72]  # bcrypt max length
    return pwd_context.hash(truncated_password)

