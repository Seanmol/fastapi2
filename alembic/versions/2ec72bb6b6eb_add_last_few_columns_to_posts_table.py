"""add last few columns to posts table

Revision ID: 2ec72bb6b6eb
Revises: 653390095d44
Create Date: 2021-12-19 14:56:14.395758

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2ec72bb6b6eb'
down_revision = '653390095d44'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('published', sa.Boolean(), nullable=False, server_default='1'))
    op.add_column('posts', sa.Column("created_at", sa.TIMESTAMP(timezone=True),server_default=sa.text('now()'), nullable=False))


def downgrade():
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')