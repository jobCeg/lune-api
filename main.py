from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException

from app.routes import staff, service, health, roles
from app.exceptions.handlers import (
    http_exception_handler,
    validation_exception_handler,
    generic_exception_handler
)

app = FastAPI(
    title="Lune API",
    description="Backend service for Lune",
    version="1.0.0",
)

# Routers
app.include_router(health.router, tags=["Health"])
app.include_router(service.router, tags=["Services"])
app.include_router(roles.router, tags=["Roles"])
app.include_router(staff.router, tags=["Staff"])

# Exception handlers
app.add_exception_handler(StarletteHTTPException, http_exception_handler)
app.add_exception_handler(RequestValidationError, validation_exception_handler)
app.add_exception_handler(Exception, generic_exception_handler)

@app.get("/", tags=["Health"])
def root():
    return {"message": "Lune API is running"}

