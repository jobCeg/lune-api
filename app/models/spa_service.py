from sqlalchemy import Column, Integer, String, Numeric, Text
from app.db.base import Base


class SpaService(Base):
    __tablename__ = "spa_services"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    description = Column(Text, nullable=True)
    duration_minutes = Column(Integer, nullable=False)
    price = Column(Numeric(10, 2), nullable=False)

