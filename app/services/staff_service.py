from sqlalchemy.orm import Session

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

        return staff

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
        return db.query(Staff).filter(Staff.id == staff_id).first()
    finally:
        db.close()


def update_staff(staff_id: int, payload):
    db: Session = SessionLocal()

    try:
        staff = db.query(Staff).filter(Staff.id == staff_id).first()

        if not staff:
            return None

        if payload.name is not None:
            staff.name = payload.name
        if payload.email is not None:
            staff.email = payload.email
        if payload.phone is not None:
            staff.phone = payload.phone
        if payload.role_id is not None:
            staff.role_id = payload.role_id

        db.commit()
        db.refresh(staff)

        return staff

    except Exception:
        db.rollback()
        raise

    finally:
        db.close()


def deactivate_staff(staff_id: int):
    db: Session = SessionLocal()

    try:
        staff = db.query(Staff).filter(Staff.id == staff_id).first()

        if not staff:
            return None

        staff.is_active = False
        db.commit()
        db.refresh(staff)

        return staff

    except Exception:
        db.rollback()
        raise

    finally:
        db.close()

