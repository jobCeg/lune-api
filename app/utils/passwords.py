import bcrypt

def hashPassword(password: str) -> str:
    """Hash a plain password using bcrypt and return UTF-8 string."""
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")

def comparePassword(password: str, hashed: str) -> bool:
    """Compare a plain password with a hashed password."""
    return bcrypt.checkpw(password.encode("utf-8"), hashed.encode("utf-8"))

