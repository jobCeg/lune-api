# app/crud.py
from sqlalchemy.orm import Session
from typing import List, Optional
from uuid import UUID
from . import models, schemas

def create_service(db: Session, service_in: schemas.ServiceCreate) -> models.Service:
    service = models.Service(
        name=service_in.name,
        description=service_in.description,
        duration_minutes=service_in.duration_minutes,
    )
    db.add(service)
    db.commit()
    db.refresh(service)
    return service

def get_service(db: Session, service_id: UUID) -> Optional[models.Service]:
    return db.get(models.Service, service_id)

def get_services(db: Session, skip: int = 0, limit: int = 100) -> List[models.Service]:
    return db.query(models.Service).offset(skip).limit(limit).all()

def update_service(db: Session, service_id: UUID, service_in: schemas.ServiceUpdate) -> Optional[models.Service]:
    service = db.get(models.Service, service_id)
    if not service:
        return None

    if service_in.name is not None:
        service.name = service_in.name
    if service_in.description is not None:
        service.description = service_in.description
    if service_in.duration_minutes is not None:
        service.duration_minutes = service_in.duration_minutes

    db.add(service)
    db.commit()
    db.refresh(service)
    return service

def delete_service(db: Session, service_id: UUID) -> bool:
    service = db.get(models.Service, service_id)
    if not service:
        return False
    db.delete(service)
    db.commit()
    return True
