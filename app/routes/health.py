from fastapi import APIRouter
from app.core.db import DATABASE_URL
from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError

router = APIRouter()

@router.get("/health")
async def health_check():
    """
    Endpoint to check API and DB connectivity.
    Returns:
        {"status": "ok"} if DB is reachable
        {"status": "error", "db": "unreachable"} if DB connection fails
    """
    try:
        engine = create_engine(DATABASE_URL)
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))
    except SQLAlchemyError:
        return {"status": "error", "db": "unreachable"}

    return {"status": "ok"}

