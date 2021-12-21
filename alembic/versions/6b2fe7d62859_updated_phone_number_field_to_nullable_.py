"""Updated phone number field to Nullable =  True  in users table

Revision ID: 6b2fe7d62859
Revises: bca0008a95b1
Create Date: 2021-12-20 17:34:32.910476

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6b2fe7d62859'
down_revision = 'bca0008a95b1'
branch_labels = None
depends_on = None


def upgrade():
    pass


def downgrade():
    pass
