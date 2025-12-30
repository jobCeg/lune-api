from pydantic import BaseModel

class RoleResponse(BaseModel):
    """
    Pydantic schema for returning roles.
    """
    id: int
    name: str
    description: str | None = None

    class Config:
        from_attributes = True  # SQLAlchemy 2.x, replaces orm_mode=True


