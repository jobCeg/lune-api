from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import Role
from app.schemas import RoleResponse

router = APIRouter()

@router.get("/roles", response_model=list[RoleResponse])
def get_roles(db: Session = Depends(get_db)):
    """
    Return all roles including permission sets.
    """
    roles = db.query(Role).all()
    return roles

