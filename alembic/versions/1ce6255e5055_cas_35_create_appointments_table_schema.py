"""CAS-35 add start/end validation to appointments

Revision ID: 1ce6255e5055
Revises: 345ab0dbaf83
Create Date: 2026-03-03 18:15:59.273828
"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "1ce6255e5055"
down_revision: Union[str, Sequence[str], None] = "345ab0dbaf83"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_check_constraint(
        "check_start_before_end",
        "appointments",
        "start_time < end_time",
    )


def downgrade() -> None:
    op.drop_constraint(
        "check_start_before_end",
        "appointments",
        type_="check",
    )
