from pydantic import BaseModel, EmailStr, Field, ConfigDict

class RegisterRequest(BaseModel):
    email: EmailStr
    password: str = Field(..., min_length=6)

class RegisterResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    email: EmailStr
    token: str

