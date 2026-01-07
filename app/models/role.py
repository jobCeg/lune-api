from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.core.db import Base


class Role(Base):
    __tablename__ = "roles"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)

    staff_members = relationship(
        "Staff",
        back_populates="role",
        cascade="all, delete-orphan",
    )


