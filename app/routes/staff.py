from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import Staff, Role
from app.schemas.staff import StaffResponse, AssignRoleRequest

router = APIRouter(
    prefix="/staff",
    tags=["Staff"]
)

@router.put("/{staff_id}/role", response_model=StaffResponse)
def assign_role_to_staff(
    staff_id: int,
    payload: AssignRoleRequest,
    db: Session = Depends(get_db)
):
    staff = db.query(Staff).filter(Staff.id == staff_id).first()
    if not staff:
        raise HTTPException(status_code=404, detail="Staff not found")

    role = db.query(Role).filter(Role.id == payload.role_id).first()
    if not role:
        raise HTTPException(status_code=404, detail="Role not found")

    staff.role_id = role.id
    db.commit()
    db.refresh(staff)

    return staff

