from fastapi import APIRouter, Request

router = APIRouter(prefix="/user", tags=["User"])

@router.get("/profile")
def profile(request: Request):
    return {"message": "User profile", "user": request.state.user}

