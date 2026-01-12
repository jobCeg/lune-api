from sqlalchemy.orm import Session
from fastapi.encoders import jsonable_encoder

from app.database import SessionLocal
from app.models.staff import Staff


def create_staff(payload):
    db: Session = SessionLocal()

    try:
        if not payload.name or not payload.email or not payload.role_id:
            raise ValueError("Missing required fields")

        staff = Staff(
            name=payload.name,
            email=payload.email,
            phone=payload.phone,
            role_id=payload.role_id,
            is_active=True,
        )

        db.add(staff)
        db.commit()
        db.refresh(staff)

        return jsonable_encoder(staff)

    except Exception:
        db.rollback()
        raise

    finally:
        db.close()


def get_staff_list(include_inactive: bool = False):
    db: Session = SessionLocal()

    try:
        query = db.query(Staff)

        if not include_inactive:
            query = query.filter(Staff.is_active.is_(True))

        return query.order_by(Staff.id.asc()).all()

    finally:
        db.close()


def get_staff_by_id(staff_id: int):
    db: Session = SessionLocal()

    try:
        staff = db.query(Staff).filter(Staff.id == staff_id).first()
        return staff

    finally:
        db.close()

