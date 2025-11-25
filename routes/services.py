from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from uuid import UUID

from app.database import SessionLocal
from app import models, schemas

router = APIRouter(prefix="/services", tags=["Services"])

# Dependency: obtener sesión de DB
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# ---------- Crear servicio ----------
@router.post("/", response_model=schemas.ServiceResponse)
def create_service(service_data: schemas.ServiceCreate, db: Session = Depends(get_db)):
    new_service = models.Service(
        name=service_data.name,
        description=service_data.description
    )
    db.add(new_service)
    db.commit()
    db.refresh(new_service)
    return new_service


# ---------- Obtener servicio ----------
@router.get("/{service_id}", response_model=schemas.ServiceResponse)
def get_service(service_id: UUID, db: Session = Depends(get_db)):
    service = db.query(models.Service).filter(models.Service.id == service_id).first()

    if not service:
        raise HTTPException(status_code=404, detail="Service not found")

    return service


# ---------- Actualizar servicio ----------
@router.patch("/{service_id}", response_model=schemas.ServiceResponse)
def update_service(service_id: UUID, update_data: schemas.ServiceUpdate, db: Session = Depends(get_db)):
    service = db.query(models.Service).filter(models.Service.id == service_id).first()

    if not service:
        raise HTTPException(status_code=404, detail="Service not found")

    service.completed_at = update_data.completed_at
    service.duration_minutes = update_data.duration_minutes

    db.commit()
    db.refresh(service)

    return service
