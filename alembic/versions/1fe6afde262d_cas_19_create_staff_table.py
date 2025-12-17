"""cas 19 create staff table

Revision ID: 1fe6afde262d
Revises: None
Create Date: 2025-12-16
"""

from alembic import op
import sqlalchemy as sa

revision = "1fe6afde262d"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "staff",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("name", sa.String(length=100), nullable=False),
        sa.Column("email", sa.String(length=255), nullable=True),
        sa.Column("is_active", sa.Boolean, nullable=False, server_default=sa.true()),
        sa.Column(
            "user_id",
            sa.Integer,
            sa.ForeignKey("users.id", ondelete="SET NULL"),
            nullable=True,
        ),
        sa.Column(
            "created_at",
            sa.DateTime,
            server_default=sa.func.now(),
            nullable=False,
        ),
        sa.Column("updated_at", sa.DateTime, nullable=True),
    )


def downgrade():
    op.drop_table("staff")

