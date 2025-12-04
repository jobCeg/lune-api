from fastapi import FastAPI
from app.routes import service, health
from app.core.exceptions import (
    http_exception_handler,
    validation_exception_handler,
    generic_exception_handler
)
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException

# Initialize FastAPI app
app = FastAPI(
    title="Lune API",
    version="1.0.0"
)

# Include routers
app.include_router(service.router)
app.include_router(health.router)

# Register global exception handlers
app.add_exception_handler(StarletteHTTPException, http_exception_handler)
app.add_exception_handler(RequestValidationError, validation_exception_handler)
app.add_exception_handler(Exception, generic_exception_handler)

