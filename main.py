from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

from database import Base, engine, SessionLocal
import crud
from schemas import ServiceCreate, ServiceUpdate

# Create database tables if they do not exist
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Lune API", version="1.0.0")

# CORS settings
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -----------------------------
# Service Endpoints
# -----------------------------

@app.post("/services", response_class=JSONResponse)
def create_service(service: ServiceCreate):
    """Create a new service entry."""
    db = SessionLocal()
    created = crud.create_service(db, service)
    db.close()
    return {"message": "Service created successfully", "service": created}


@app.get("/services", response_class=JSONResponse)
def list_services():
    """List all services."""
    db = SessionLocal()
    services = crud.get_services(db)
    db.close()
    return {"services": services}


@app.get("/services/{service_id}", response_class=JSONResponse)
def get_service(service_id: str):
    """Retrieve a single service by ID."""
    db = SessionLocal()
    service = crud.get_service(db, service_id)
    db.close()

    if not service:
        return JSONResponse(status_code=404, content={"error": "Service not found"})

    return {"service": service}


@app.put("/services/{service_id}", response_class=JSONResponse)
def update_service(service_id: str, data: ServiceUpdate):
    """Update an existing service."""
    db = SessionLocal()
    updated = crud.complete_service(db, service_id, data)
    db.close()

    if not updated:
        return JSONResponse(status_code=404, content={"error": "Service not found"})

    return {"message": "Service updated successfully", "service": updated}


@app.delete("/services/{service_id}", response_class=JSONResponse)
def delete_service(service_id: str):
    """Delete a service by ID."""
    db = SessionLocal()
    deleted = crud.delete_service(db, service_id)
    db.close()

    if not deleted:
        return JSONResponse(status_code=404, content={"error": "Service not found"})

    return {"message": "Service deleted successfully"}


# -----------------------------
# Root
# -----------------------------

@app.get("/", response_class=JSONResponse)
def root():
    """Root endpoint."""
    return {"message": "Lune API is running"}
