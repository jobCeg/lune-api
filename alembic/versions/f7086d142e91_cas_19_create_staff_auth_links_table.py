"""CAS-19 create staff_auth_links table

Revision ID: f7086d142e91
Revises: 28cfcb529a87
Create Date: 2025-12-17 12:00:00.000000

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'f7086d142e91'
down_revision = '28cfcb529a87'  # <-- Aquí está la corrección
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'staff_auth_links',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('staff_id', sa.Integer, sa.ForeignKey('users.id', ondelete='CASCADE'), nullable=False),
        sa.Column('token', sa.String(length=255), nullable=False, unique=True),
        sa.Column('created_at', sa.DateTime, server_default=sa.func.now(), nullable=False),
        sa.Column('expires_at', sa.DateTime, nullable=False),
    )


def downgrade() -> None:
    op.drop_table('staff_auth_links')

