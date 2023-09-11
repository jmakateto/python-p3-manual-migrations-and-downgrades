"""Create student table

Revision ID: 4a9c2902bc47
Revises: 
Create Date: 2023-09-11 23:23:01.513223

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4a9c2902bc47'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Define the 'students' table and its columns
    op.create_table(
        'students',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String),
        
    )


def downgrade() -> None:
    
    op.drop_table('students')
