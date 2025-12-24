from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.staff import Staff, Role
from app.schemas.staff import StaffBase, AssignRole

router = APIRouter(
    prefix="/staff",
    tags=["Staff"]
)

@router.put("/{staff_id}/role", response_model=StaffBase)
def assign_role_to_staff(
    staff_id: int,
    payload: AssignRole,
    db: Session = Depends(get_db)
):
    """
    Assign a role to a staff member.
    1. Validate that staff exists.
    2. Validate that role exists.
    3. Update the staff's role.
    4. Return the updated staff.
    """

    # 1. Get staff
    staff = db.query(Staff).filter(Staff.id == staff_id).first()
    if not staff:
        raise HTTPException(status_code=404, detail="Staff not found")

    # 2. Validate that role exists
    role = db.query(Role).filter(Role.id == payload.role_id).first()
    if not role:
        raise HTTPException(status_code=404, detail="Role not found")

    # 3. Assign role to staff
    staff.role_id = role.id
    db.commit()
    db.refresh(staff)

    # 4. Return updated staff
    return staff

