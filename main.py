"""
Main entry for FastAPI application.
Keep route registration here; route handlers belong to app/routes.
"""

from fastapi import FastAPI
from app.routes import services as services_router
from app.database import engine, Base
import os

app = FastAPI(title="Services API", version="1.0.0")

# Create DB tables if not existing (optional; prefer alembic in production)
# This is safe for local/dev. In production rely on Alembic migrations.
if os.getenv("CREATE_TABLES_AT_STARTUP", "false").lower() in ("1", "true", "yes"):
    Base.metadata.create_all(bind=engine)

# Mount services router under /services
app.include_router(services_router.router, prefix="/services", tags=["Services"])
