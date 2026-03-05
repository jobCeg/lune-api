from sqlalchemy import Column, Integer, String, DateTime, Boolean
from sqlalchemy.sql import func

from app.core.db import Base


class SpaService(Base):
    __tablename__ = "spa_services"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    duration = Column(Integer, nullable=False)
    is_active = Column(Boolean, default=True, nullable=False)
    created_at = Column(DateTime, server_default=func.now(), nullable=False)

