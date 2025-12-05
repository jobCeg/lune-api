import bcrypt

def hashPassword(plain_password: str) -> str:
    """
    Hash a plain password using bcrypt.
    Returns the hashed password as a UTF-8 string.
    """
    # Use bcrypt to generate a secure salt and hash the password
    return bcrypt.hashpw(plain_password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')


def comparePassword(plain_password: str, hashed_password: str) -> bool:
    """
    Compare a plain password with a hashed password.
    Returns True if they match, False otherwise.
    """
    # Check password against the hashed value
    return bcrypt.checkpw(plain_password.encode('utf-8'), hashed_password.encode('utf-8'))

