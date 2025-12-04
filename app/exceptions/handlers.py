from fastapi import Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException
import logging

logger = logging.getLogger(__name__)


async def http_exception_handler(request: Request, exc: StarletteHTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.detail},
    )


async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=422,
        content={"detail": exc.errors()},
    )


async def generic_exception_handler(request: Request, exc: Exception):
    # Log unexpected exceptions so they are traceable in logs
    logger.exception("Unhandled exception during request processing")
    return JSONResponse(
        status_code=500,
        content={"detail": "Internal server error"},
    )

