from fastapi import APIRouter, Depends, Request
from app.middleware.role_middleware import require_role

router = APIRouter(prefix="/admin", tags=["Admin"])

@router.get("/dashboard", dependencies=[Depends(require_role("admin"))])
def admin_dashboard(request: Request):
    return {"message": "Admin dashboard", "user": request.state.user}

