"""create message  table

Revision ID: a72825d53ec1
Revises: 
Create Date: 2023-09-19 22:14:51.713612

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a72825d53ec1'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:

    op.create_table('t_task',
                    sa.Column('id', sa.Integer, primary_key=True),
                    sa.Column('message', sa.String(), nullable=False, unique=False))


def downgrade() -> None:
    op.drop_table('t_task')
