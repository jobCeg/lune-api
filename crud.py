from sqlalchemy.orm import Session
from .models import Service
from .schemas import ServiceCreate, ServiceUpdate
from datetime import datetime

def create_service(db: Session, data: ServiceCreate):
    svc = Service(name=data.name, description=data.description)
    db.add(svc)
    db.commit()
    db.refresh(svc)
    return svc

def get_services(db: Session):
    return db.query(Service).order_by(Service.created_at.desc()).all()

def get_service(db: Session, service_id: str):
    return db.query(Service).filter(Service.id == service_id).first()

def complete_service(db: Session, service_id: str, data: ServiceUpdate):
    svc = db.query(Service).filter(Service.id == service_id).first()
    if not svc:
        return None
    svc.completed_at = data.completed_at
    svc.duration_minutes = data.duration_minutes
    db.commit()
    db.refresh(svc)
    return svc

def delete_service(db: Session, service_id: str):
    svc = db.query(Service).filter(Service.id == service_id).first()
    if not svc:
        return False
    db.delete(svc)
    db.commit()
    return True
