from sqlalchemy import Column, Integer, String
from app.database import Base  # Base from database.py

class Role(Base):
    """
    SQLAlchemy model for roles table.
    """
    __tablename__ = "roles"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)
    description = Column(String, nullable=True)

