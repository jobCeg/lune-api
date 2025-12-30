from starlette.middleware.base import BaseHTTPMiddleware
from fastapi import Request, HTTPException, status
import jwt

SECRET_KEY = "your_secret_key_here"

async def get_current_user(request: Request):
    """
    Extract user information from JWT token in the Authorization header.
    """
    auth_header = request.headers.get("Authorization")
    if not auth_header or not auth_header.startswith("Bearer "):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid or missing token")
    
    token = auth_header.split(" ")[1]
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return {"id": payload["user_id"], "role": payload["role"]}
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")

class JWTMiddleware(BaseHTTPMiddleware):
    """
    Middleware to handle JWT token verification globally.
    """
    async def dispatch(self, request: Request, call_next):
        # Optionally, can add global token checks here
        response = await call_next(request)
        return response


