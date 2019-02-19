"""empty message

Revision ID: f891cd0a5c10
Revises: 28c6372874bf
Create Date: 2019-02-15 01:47:52.618647

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f891cd0a5c10'
down_revision = '28c6372874bf'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('user', sa.Column('name', sa.String(50), nullable=False))

def downgrade():
    op.drop_column('user')