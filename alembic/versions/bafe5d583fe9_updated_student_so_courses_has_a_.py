"""updated  student , so courses has a relationship with student

Revision ID: bafe5d583fe9
Revises: 6356a702310e
Create Date: 2024-06-18 10:54:03.560960

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'bafe5d583fe9'
down_revision: Union[str, None] = '6356a702310e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###