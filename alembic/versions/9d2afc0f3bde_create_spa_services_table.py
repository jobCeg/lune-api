"""create spa_services table

Revision ID: 9d2afc0f3bde
Revises: 5398f90b0e12
"""

from alembic import op
import sqlalchemy as sa


revision = "9d2afc0f3bde"
down_revision = "5398f90b0e12"
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "spa_services",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("name", sa.String(255), nullable=False),
        sa.Column("duration", sa.Integer, nullable=False),
        sa.Column(
            "created_at",
            sa.DateTime(),
            server_default=sa.func.now(),
            nullable=False,
        ),
    )


def downgrade():
    op.drop_table("spa_services")

