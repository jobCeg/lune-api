from fastapi import Request, HTTPException
from app.utils.jwt_utils import verify_token

class JWTMiddleware:
    """
    Middleware to validate JWT token in Authorization header.
    Sets request.state.user_id if token is valid.
    """
    def __init__(self, app):
        self.app = app

    async def __call__(self, scope, receive, send):
        if scope["type"] == "http":
            request = Request(scope, receive=receive)
            if request.url.path.startswith("/auth"):
                await self.app(scope, receive, send)
                return

            auth_header = request.headers.get("Authorization")
            if not auth_header or not auth_header.startswith("Bearer "):
                raise HTTPException(status_code=401, detail="Missing or invalid token")

            token = auth_header.split(" ")[1]
            try:
                payload = verify_token(token)
                scope["user_id"] = payload["user_id"]
            except Exception:
                raise HTTPException(status_code=401, detail="Invalid token")

        await self.app(scope, receive, send)

