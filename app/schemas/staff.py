from pydantic import BaseModel

# Schema to read role info
class RoleBase(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True

# Schema to read staff info
class StaffBase(BaseModel):
    id: int
    name: str
    email: str
    role: RoleBase | None = None  # role can be null

    class Config:
        orm_mode = True

# Schema to assign role
class AssignRole(BaseModel):
    role_id: int


