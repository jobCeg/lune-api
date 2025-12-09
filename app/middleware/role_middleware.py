from fastapi import HTTPException, Request

def require_role(*allowed_roles: str):
    """
    Dependency to protect routes by role.
    """
    async def role_checker(request: Request):
        user = getattr(request.state, "user", None)

        if user is None:
            raise HTTPException(status_code=401, detail="Authentication required")

        if user["role"] not in allowed_roles:
            raise HTTPException(status_code=403, detail="Insufficient permissions")

        return user
    return role_checker

