"""add published and created_at columns to posts

Revision ID: be94388b9d8a
Revises: b82ea02dde83
Create Date: 2024-07-29 09:19:25.470589

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'be94388b9d8a'
down_revision: Union[str, None] = 'b82ea02dde83'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
  op.add_column('posts', sa.Column('published', sa.Boolean(), nullable=False, server_default='TRUE'),)
  op.add_column('posts', sa.Column('created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('NOW()')),)
  pass


def downgrade():
  op.drop_column('posts', 'published')
  op.drop_column('posts', 'created_at')
  pass