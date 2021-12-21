"""Updated phone number field to Nullable =  True  in users table 2

Revision ID: dca5c2b66cd8
Revises: 6b2fe7d62859
Create Date: 2021-12-20 17:35:19.785479

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql


# revision identifiers, used by Alembic.
revision = 'dca5c2b66cd8'
down_revision = '6b2fe7d62859'
branch_labels = None
depends_on = None


def upgrade():
   op.alter_column('users', 'phone_number',
               existing_type=mysql.VARCHAR(length=32),
               nullable=True)


def downgrade():
    op.alter_column('users', 'phone_number',
               existing_type=mysql.VARCHAR(length=32),
               nullable=False)
