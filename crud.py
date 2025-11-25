from sqlalchemy.orm import Session
from models import Service
from schemas import ServiceCreate
from datetime import datetime

def create_service(db: Session, service: ServiceCreate):
    db_service = Service(
        name=service.name,
        description=service.description,
        duration_minutes=service.duration_minutes
    )
    db.add(db_service)
    db.commit()
    db.refresh(db_service)
    return db_service

def get_services(db: Session):
    return db.query(Service).all()

def get_service(db: Session, service_id: str):
    return db.query(Service).filter(Service.id == service_id).first()

def complete_service(db: Session, service_id: str):
    service = db.query(Service).filter(Service.id == service_id).first()
    if service:
        service.completed_at = datetime.utcnow()
        db.commit()
        db.refresh(service)
    return service
