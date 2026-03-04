from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "345ab0dbaf83"
down_revision = "0e430b023a47"
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "appointments",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("staff_id", sa.Integer(), sa.ForeignKey("staff.id"), nullable=False),
        sa.Column("service_id", sa.Integer(), sa.ForeignKey("spa_services.id"), nullable=False),
        sa.Column("start_time", sa.DateTime(), nullable=False),
        sa.Column("end_time", sa.DateTime(), nullable=False),
    )

    op.create_index(
        "ix_appointments_start_time",
        "appointments",
        ["start_time"]
    )

    op.create_index(
        "ix_appointments_end_time",
        "appointments",
        ["end_time"]
    )


def downgrade():
    op.drop_index("ix_appointments_end_time", table_name="appointments")
    op.drop_index("ix_appointments_start_time", table_name="appointments")
    op.drop_table("appointments")
