from fastapi import APIRouter
from app.core.db import DATABASE_URL  # o la forma de verificar tu DB
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError

router = APIRouter()

@router.get("/health")
async def health_check():
    # Check DB connection
    try:
        engine = create_engine(DATABASE_URL)
        with engine.connect() as connection:
            connection.execute("SELECT 1")
    except SQLAlchemyError:
        return {"status": "error", "db": "unreachable"}

    return {"status": "ok"}

