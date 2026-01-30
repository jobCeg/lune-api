from sqlalchemy.orm import Session
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

