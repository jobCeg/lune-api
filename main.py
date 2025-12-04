from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException

# Routers
from app.routes import service, health

# Exception handlers
from app.exceptions.handlers import (
    http_exception_handler,
    validation_exception_handler,
    generic_exception_handler
)

# Initialize FastAPI app with Swagger configuration
app = FastAPI(
    title="Lune API",
    description="Backend service for Lune. Includes service endpoints and health check.",
    version="1.0.0",
    openapi_tags=[
        {
            "name": "Health",
            "description": "Health check endpoints"
        },
        {
            "name": "Services",
            "description": "Service management endpoints"
        }
    ]
)

# Routers
app.include_router(health.router, tags=["Health"])
app.include_router(service.router, tags=["Services"])

# Global exception handlers
app.add_exception_handler(StarletteHTTPException, http_exception_handler)
app.add_exception_handler(RequestValidationError, validation_exception_handler)
app.add_exception_handler(Exception, generic_exception_handler)


# Root endpoint (optional)
@app.get("/", tags=["Health"])
def root():
    return {"message": "Lune API is running"}


