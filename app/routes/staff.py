from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel, EmailStr
from typing import Optional

from app.services.staff_service import create_staff

router = APIRouter(
    prefix="/staff",
    tags=["Staff"]
)


class StaffCreateRequest(BaseModel):
    name: str
    email: EmailStr
    phone: Optional[str] = None
    role_id: int


class StaffResponse(BaseModel):
    id: int
    name: str
    email: str
    phone: Optional[str]
    role_id: int
    is_active: bool


@router.post(
    "",
    response_model=StaffResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_staff_endpoint(payload: StaffCreateRequest):
    try:
        staff = create_staff(payload)
        return staff
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e),
        )

