from pydantic import BaseModel
from uuid import UUID
from datetime import datetime
from typing import Optional

class ServiceCreate(BaseModel):
    name: str
    description: Optional[str] = None

class ServiceUpdate(BaseModel):
    completed_at: datetime
    duration_minutes: int

class ServiceResponse(BaseModel):
    id: UUID
    name: str
    description: Optional[str]
    created_at: datetime
    completed_at: Optional[datetime]
    duration_minutes: Optional[int]

    class Config:
        from_attributes = True
