"""CAS-10: Create users table

Revision ID: 8cab17a646c7
Revises: 191cbd4b5b5a
Create Date: 2025-12-04 13:43:38.039207

"""
from alembic import op
import sqlalchemy as sa
from datetime import datetime

# revision identifiers, used by Alembic.
revision = '8cab17a646c7'
down_revision = '191cbd4b5b5a'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True, index=True),
        sa.Column('email', sa.String, nullable=False, unique=True, index=True),
        sa.Column('passwordHash', sa.String, nullable=False),
        sa.Column('createdAt', sa.DateTime, nullable=False, default=datetime.utcnow),
        sa.Column('updatedAt', sa.DateTime, nullable=False, default=datetime.utcnow),
        sa.Column('lastLoginAt', sa.DateTime, nullable=True)
    )


def downgrade() -> None:
    op.drop_table('users')

