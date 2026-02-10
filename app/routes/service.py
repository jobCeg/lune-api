from fastapi import APIRouter, Depends, status, Query, HTTPException
from sqlalchemy.orm import Session
from typing import List, Optional

from app.database import get_db
from app.schemas.spa_service import (
    SpaServiceCreate,
    SpaServiceUpdate,
    SpaServiceResponse
)
from app.services.spa_service_service import (
    create_spa_service,
    get_spa_services,
    get_spa_service_by_id,
    update_spa_service
)

router = APIRouter(
    prefix="/services",
    tags=["Services"]
)


@router.post(
    "",
    response_model=SpaServiceResponse,
    status_code=status.HTTP_201_CREATED
)
def create_service(
    payload: SpaServiceCreate,
    db: Session = Depends(get_db)
):
    return create_spa_service(db, payload)


@router.get(
    "",
    response_model=List[SpaServiceResponse],
    status_code=status.HTTP_200_OK
)
def list_services(
    is_active: Optional[bool] = Query(
        None,
        description="Filter services by active/inactive status"
    ),
    db: Session = Depends(get_db)
):
    return get_spa_services(db, is_active)


@router.patch(
    "/{service_id}",
    response_model=SpaServiceResponse,
    status_code=status.HTTP_200_OK
)
def update_service(
    service_id: int,
    payload: SpaServiceUpdate,
    db: Session = Depends(get_db)
):
    service = get_spa_service_by_id(db, service_id)

    if not service:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Service not found"
        )

    return update_spa_service(db, service, payload)

