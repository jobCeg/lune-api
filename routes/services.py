# app/routes/services.py
from fastapi import APIRouter, Depends, HTTPException, status, Query, Path
from sqlalchemy.orm import Session
from typing import List
from uuid import UUID

from app import schemas, crud
from app.database import get_db

router = APIRouter(prefix="", tags=["services"])

@router.post("/", response_model=schemas.Service, status_code=status.HTTP_201_CREATED)
def create_service(service: schemas.ServiceCreate, db: Session = Depends(get_db)):
    return crud.create_service(db, service)

@router.get("/", response_model=List[schemas.Service])
def list_services(db: Session = Depends(get_db), skip: int = Query(0, ge=0), limit: int = Query(100, ge=1, le=1000)):
    return crud.get_services(db, skip=skip, limit=limit)

@router.get("/{service_id}", response_model=schemas.Service)
def read_service(service_id: UUID = Path(...), db: Session = Depends(get_db)):
    service = crud.get_service(db, service_id)
    if not service:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Service not found")
    return service

@router.put("/{service_id}", response_model=schemas.Service)
def update_service(service_id: UUID, service_in: schemas.ServiceUpdate, db: Session = Depends(get_db)):
    updated = crud.update_service(db, service_id, service_in)
    if not updated:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Service not found")
    return updated

@router.delete("/{service_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_service(service_id: UUID, db: Session = Depends(get_db)):
    deleted = crud.delete_service(db, service_id)
    if not deleted:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Service not found")
    return None
