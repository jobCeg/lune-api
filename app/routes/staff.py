from fastapi import APIRouter, HTTPException, status, Query
from typing import List

from app.schemas.staff import StaffCreate, StaffResponse, StaffUpdate
from app.services.staff_service import (
    create_staff,
    get_staff_list,
    get_staff_by_id,
    update_staff,
)

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


@router.get(
    "/{staff_id}",
    response_model=StaffResponse,
    status_code=status.HTTP_200_OK,
)
def get_staff(staff_id: int):
    staff = get_staff_by_id(staff_id)

    if not staff:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Staff member not found",
        )

    return staff


@router.put(
    "/{staff_id}",
    response_model=StaffResponse,
    status_code=status.HTTP_200_OK,
)
def update_staff_endpoint(staff_id: int, payload: StaffUpdate):
    staff = update_staff(staff_id, payload)

    if not staff:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Staff member not found",
        )

    return staff

