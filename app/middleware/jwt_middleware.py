from fastapi import Request, HTTPException
from starlette.middleware.base import BaseHTTPMiddleware
from app.utils.jwt_utils import verify_token

class JWTMiddleware(BaseHTTPMiddleware):
    """
    Middleware to validate JWT token on incoming requests.
    """

    async def dispatch(self, request: Request, call_next):
        if request.url.path.startswith("/auth"):
            return await call_next(request)

        auth_header = request.headers.get("Authorization")
        if not auth_header:
            raise HTTPException(status_code=401, detail="Authorization header missing")

        try:
            token_type, token = auth_header.split()
            if token_type.lower() != "bearer":
                raise HTTPException(status_code=401, detail="Invalid token type")
        except ValueError:
            raise HTTPException(status_code=401, detail="Malformed authorization header")

        payload = verify_token(token)
        request.state.user = payload

        return await call_next(request)





