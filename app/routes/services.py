from fastapi import APIRouter, Depends
from app.middleware.role_required import role_required

router = APIRouter(prefix="/services", tags=["Services"])

@router.get("/admin")
async def admin_only(user=Depends(role_required(["admin"]))):
    """Endpoint restricted to admin users."""
    return {"message": "Welcome admin!", "user": user}

@router.get("/moderator")
async def moderator_only(user=Depends(role_required(["moderator", "admin"]))):
    """Endpoint accessible by moderator or admin."""
    return {"message": "Welcome moderator/admin!", "user": user}

