from fastapi import APIRouter, HTTPException, status, Query
from typing import List

from app.schemas.staff import StaffCreate, StaffResponse
from app.services.staff_service import create_staff, get_staff_list

router = APIRouter(
    prefix="/staff",
    tags=["Staff"]
)


@router.post(
    "",
    response_model=StaffResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_staff_endpoint(payload: StaffCreate):
    try:
        return create_staff(payload)
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e),
        )


@router.get(
    "",
    response_model=List[StaffResponse],
    status_code=status.HTTP_200_OK,
)
def list_staff(
    include_inactive: bool = Query(False, description="Include inactive staff members")
):
    return get_staff_list(include_inactive)

