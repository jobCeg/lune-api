from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class ServiceBase(BaseModel):
    name: str
    description: Optional[str] = None
    duration_minutes: int

class ServiceCreate(ServiceBase):
    pass

class Service(ServiceBase):
    id: str
    created_at: datetime
    completed_at: Optional[datetime]

    class Config:
        orm_mode = True
