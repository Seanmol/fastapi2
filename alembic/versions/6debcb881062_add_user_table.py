"""add user table

Revision ID: 6debcb881062
Revises: bd5203647d25
Create Date: 2021-12-19 14:36:21.389128

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql.schema import UniqueConstraint


# revision identifiers, used by Alembic.
revision = '6debcb881062'
down_revision = 'bd5203647d25'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table( "users",
                sa.Column("id", sa.Integer(), nullable=False),
                sa.Column("email", sa.String(64), nullable=False),
                sa.Column("password", sa.String(255), nullable=False),
                sa.Column("created_at", sa.TIMESTAMP(timezone=True),server_default=sa.text('now()'), nullable=False),
                sa.PrimaryKeyConstraint('id'),
                sa.UniqueConstraint('email')
    )

    pass


def downgrade():
    op.drop_table("users")
    pass
