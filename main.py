from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from database import SessionLocal, engine
import models, schemas, crud

# Create the tables if they do not exist
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Services API", description="API for managing services", version="1.0.0")

# CORS (optional)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Root endpoint to verify that the server is working
@app.get("/")
def root():
    return {"message": "Services API is running!"}

# CRUD endpoints
@app.post("/services", response_model=schemas.Service)
def create_service(service: schemas.ServiceCreate):
    db = SessionLocal()
    db_service = crud.create_service(db, service)
    db.close()
    return db_service

@app.get("/services", response_model=list[schemas.Service])
def get_services():
    db = SessionLocal()
    services = crud.get_services(db)
    db.close()
    return services

@app.get("/services/{service_id}", response_model=schemas.Service)
def get_service(service_id: str):
    db = SessionLocal()
    service = crud.get_service(db, service_id)
    db.close()
    if not service:
        raise HTTPException(status_code=404, detail="Service not found")
    return service

@app.delete("/services/{service_id}", response_class=JSONResponse)
def delete_service(service_id: str):
    db = SessionLocal()
    deleted = crud.delete_service(db, service_id)
    db.close()
    if not deleted:
        raise HTTPException(status_code=404, detail="Service not found")
    return {"message": "Service deleted successfully"}
