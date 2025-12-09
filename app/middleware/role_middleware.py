from fastapi import HTTPException, Request

def require_role(*allowed_roles: str):
    """
    Dependency to protect routes by role.
    """
    async def role_checker(request: Request):
        user = request.state.user

        if user["role"] not in allowed_roles:
            raise HTTPException(status_code=403, detail="Insufficient permissions")

        return user
    return role_checker

