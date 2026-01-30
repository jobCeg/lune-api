from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.spa_service import SpaService
from app.schemas.spa_service import SpaServiceCreate, SpaServiceResponse

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
    service = SpaService(
        name=payload.name,
        duration=payload.duration
    )

    db.add(service)
    db.commit()
    db.refresh(service)

    return service

