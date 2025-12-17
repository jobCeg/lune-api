"""CAS-19 create staff_auth_links table

Revision ID: f7086d142e91
Revises: 423a780915de
Create Date: 2025-12-17 12:15:13.191675

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f7086d142e91'
down_revision: Union[str, Sequence[str], None] = '423a780915de'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
