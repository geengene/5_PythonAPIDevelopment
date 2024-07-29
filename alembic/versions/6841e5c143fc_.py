"""empty message

Revision ID: 6841e5c143fc
Revises: 
Create Date: 2024-07-29 08:28:58.481916

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6841e5c143fc'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
  op.create_table('posts', sa.Column('id', sa.Integer(), nullable=False, primary_key=True), sa.Column('title', sa.String(), nullable=False))
  pass


def downgrade() -> None:
  op.drop_table("posts")
  pass
