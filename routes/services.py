from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app import crud, schemas
from app.database import SessionLocal, engine, Base

router = APIRouter(prefix="/services", tags=["services"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schemas.ServiceResponse, status_code=status.HTTP_201_CREATED)
def create_service(service_in: schemas.ServiceCreate, db: Session = Depends(get_db)):
    svc = crud.create_service(db, service_in)
    return svc

@router.get("/", response_model=List[schemas.ServiceResponse])
def list_services(db: Session = Depends(get_db)):
    return crud.get_services(db)

@router.get("/{service_id}", response_model=schemas.ServiceResponse)
def retrieve_service(service_id: str, db: Session = Depends(get_db)):
    svc = crud.get_service(db, service_id)
    if not svc:
        raise HTTPException(status_code=404, detail="Service not found")
    return svc

@router.patch("/{service_id}", response_model=schemas.ServiceResponse)
def patch_service(service_id: str, payload: schemas.ServiceUpdate, db: Session = Depends(get_db)):
    svc = crud.complete_service(db, service_id, payload)
    if not svc:
        raise HTTPException(status_code=404, detail="Service not found")
    return svc

@router.delete("/{service_id}", status_code=status.HTTP_204_NO_CONTENT)
def remove_service(service_id: str, db: Session = Depends(get_db)):
    deleted = crud.delete_service(db, service_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Service not found")
    return None
