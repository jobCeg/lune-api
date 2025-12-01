from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
from uuid import UUID

class ServiceBase(BaseModel):
    name: str = Field(..., max_length=255)
    description: Optional[str] = None
    duration_minutes: int = Field(..., ge=0)

class ServiceCreate(ServiceBase):
    pass

class ServiceUpdate(BaseModel):
    name: Optional[str] = Field(None, max_length=255)
    description: Optional[str] = None
    duration_minutes: Optional[int] = Field(None, ge=0)

class Service(ServiceBase):
    id: UUID
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
