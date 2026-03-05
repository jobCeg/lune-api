from fastapi import Depends, HTTPException, status
from app.middleware.jwt_middleware import get_current_user  # Function to get user from JWT

def role_required(roles: list):
    """
    Dependency to check if the current user has one of the required roles.
    """
    async def dependency(user=Depends(get_current_user)):
        if user["role"] not in roles:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="You do not have permission to access this resource"
            )
        return user
    return dependency

