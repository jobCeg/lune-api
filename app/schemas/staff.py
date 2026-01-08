from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from datetime import datetime


class StaffCreate(BaseModel):
    name: str = Field(..., min_length=1)
    email: EmailStr
    phone: Optional[str] = None
    role_id: int


class StaffResponse(BaseModel):
    id: int
    name: str
    email: str
    phone: Optional[str]
    role_id: int
    is_active: bool
    created_at: datetime

    class Config:
        from_attributes = True

