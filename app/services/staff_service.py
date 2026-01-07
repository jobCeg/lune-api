from sqlalchemy.orm import Session
from fastapi.encoders import jsonable_encoder

from app.database import SessionLocal
from app.models.staff import Staff


def create_staff(payload):
    db: Session = SessionLocal()

    try:
        # Validate required fields (extra safety)
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

    except Exception as e:
        db.rollback()
        raise e

    finally:
        db.close()

