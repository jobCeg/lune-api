"""add is_active to spa_services

Revision ID: 0e430b023a47
Revises: 9d2afc0f3bde
Create Date: 2026-01-22
"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "0e430b023a47"
down_revision = "9d2afc0f3bde"
branch_labels = None
depends_on = None


def upgrade():
    op.add_column(
        "spa_services",
        sa.Column(
            "is_active",
            sa.Boolean(),
            nullable=False,
            server_default=sa.true()
        )
    )


def downgrade():
    op.drop_column("spa_services", "is_active")

