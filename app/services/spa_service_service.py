from sqlalchemy.orm import Session
from typing import Optional

from app.models.spa_service import SpaService
from app.schemas.spa_service import SpaServiceCreate


def create_spa_service(db: Session, payload: SpaServiceCreate) -> SpaService:
    service = SpaService(
        name=payload.name,
        duration=payload.duration,
    )

    db.add(service)
    db.commit()
    db.refresh(service)

    return service


def get_spa_services(db: Session, is_active: Optional[bool] = None):
    query = db.query(SpaService)

    if is_active is not None:
        query = query.filter(SpaService.is_active == is_active)

    return query.order_by(SpaService.id.asc()).all()

