"""add foreign_key to post_table

Revision ID: 653390095d44
Revises: 6debcb881062
Create Date: 2021-12-19 14:48:21.144159

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql.schema import Column


# revision identifiers, used by Alembic.
revision = '653390095d44'
down_revision = '6debcb881062'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('post_user_fk', source_table="posts", referent_table="users", local_cols=["owner_id"], remote_cols=["id"], ondelete="CASCADE")
    pass


def downgrade():
    op.drop_constraint(constraint_name='post_user_fk', table_name="posts", type_='foreignkey')
    op.drop_column('posts', "owner_id")
    pass
