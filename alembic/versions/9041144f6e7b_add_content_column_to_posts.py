"""add_content_column_to_posts

Revision ID: 9041144f6e7b
Revises: 6841e5c143fc
Create Date: 2024-07-29 08:53:39.310391

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9041144f6e7b'
down_revision: Union[str, None] = '6841e5c143fc'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
  op.add_column("posts", sa.Column('content', sa.String(), nullable=False))
  pass


def downgrade() -> None:
  op.drop_column("posts", 'content')
  pass
