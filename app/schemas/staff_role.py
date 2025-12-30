from uuid import UUID
from pydantic import BaseModel


class AssignRoleRequest(BaseModel):
    role_id: UUID

