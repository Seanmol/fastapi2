"""add content column to posts table

Revision ID: bd5203647d25
Revises: 0e6436b254fe
Create Date: 2021-12-19 14:29:19.028683

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bd5203647d25'
down_revision = '0e6436b254fe'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(255), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
