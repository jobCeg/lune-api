from pydantic import BaseModel

class RoleResponse(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True


class StaffResponse(BaseModel):
    id: int
    name: str
    email: str
    role: RoleResponse | None = None

    class Config:
        from_attributes = True


class AssignRoleRequest(BaseModel):
    role_id: int

