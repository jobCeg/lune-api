from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = "a951349b69a5"
down_revision = "75a5f4d5d7cb"
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "roles",
        sa.Column(
            "id",
            postgresql.UUID(as_uuid=True),
            primary_key=True,
            server_default=sa.text("gen_random_uuid()"),
        ),
        sa.Column("name", sa.String(length=50), nullable=False, unique=True),
    )


def downgrade():
    op.drop_table("roles")

