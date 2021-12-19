"""Create Post Table

Revision ID: 0e6436b254fe
Revises: ce179eacd324
Create Date: 2021-12-19 14:17:02.426553

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0e6436b254fe'
down_revision = 'ce179eacd324'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table("posts", sa.Column("id", sa.Integer(), nullable=False, primary_key=True),
                            sa.Column("title", sa.String(255), nullable=False))
    pass


def downgrade():
    op.drop_table('posts')
    pass
