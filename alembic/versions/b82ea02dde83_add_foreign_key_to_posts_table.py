"""add_foreign_key_to_posts_table

Revision ID: b82ea02dde83
Revises: d7bae5316c4b
Create Date: 2024-07-29 09:12:58.523502

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b82ea02dde83'
down_revision: Union[str, None] = 'd7bae5316c4b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
  op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=False))
  op.create_foreign_key('post_users_fk', source_table="posts", referent_table="users", local_cols=[
                        'owner_id'], remote_cols=['id'], ondelete="CASCADE")
  pass


def downgrade():
  op.drop_constraint('post_users_fk', table_name="posts")
  op.drop_column('posts', 'owner_id')
  pass