"""CAS-24 create staff table schema

Revision ID: 5398f90b0e12
Revises: 9bfb91323b7e
Create Date: 2026-01-06 14:25:39.338639
"""

from typing import Sequence, Union
from alembic import op


# revision identifiers, used by Alembic.
revision: str = "5398f90b0e12"
down_revision: Union[str, Sequence[str], None] = "9bfb91323b7e"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Create staff table safely
    op.execute(
        """
        CREATE TABLE IF NOT EXISTS staff (
            id SERIAL PRIMARY KEY,
            name VARCHAR NOT NULL,
            email VARCHAR NOT NULL,
            phone VARCHAR,
            role_id INTEGER NOT NULL,
            is_active BOOLEAN NOT NULL DEFAULT true,
            created_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT now()
        );
        """
    )

    # Unique email constraint
    op.execute(
        """
        DO $$
        BEGIN
            IF NOT EXISTS (
                SELECT 1 FROM pg_constraint WHERE conname = 'uq_staff_email'
            ) THEN
                ALTER TABLE staff
                ADD CONSTRAINT uq_staff_email UNIQUE (email);
            END IF;
        END
        $$;
        """
    )


def downgrade() -> None:
    op.execute(
        """
        ALTER TABLE staff
        DROP CONSTRAINT IF EXISTS uq_staff_email;
        """
    )

    op.execute(
        """
        DROP TABLE IF EXISTS staff;
        """
    )

