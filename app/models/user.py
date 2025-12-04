from datetime import datetime, timezone
from sqlalchemy import Column, Integer, String, DateTime
from app.core.db import Base  # Asegúrate de que tu Base esté en app/core/db.py

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, nullable=False, index=True)
    passwordHash = Column(String, nullable=False)
    
    createdAt = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), nullable=False)
    updatedAt = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc),
                       onupdate=lambda: datetime.now(timezone.utc), nullable=False)
    lastLoginAt = Column(DateTime(timezone=True), nullable=True)

    def __repr__(self):
        return f"<User(id={self.id}, email='{self.email}')>"

