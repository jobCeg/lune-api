from pydantic import BaseModel, Field
from datetime import datetime


class SpaServiceCreate(BaseModel):
    name: str = Field(..., min_length=1)
    duration: int = Field(..., gt=0)


class SpaServiceResponse(BaseModel):
    id: int
    name: str
    duration: int
    is_active: bool
    created_at: datetime

    class Config:
        from_attributes = True

