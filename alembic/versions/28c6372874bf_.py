"""empty message

Revision ID: 28c6372874bf
Revises: 
Create Date: 2019-02-11 21:11:03.968855

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '28c6372874bf'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'user',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('email_address', sa.String(50), nullable=False),
        sa.Column('password', sa.String(50), nullable=False),
        sa.Column('profile', sa.String(1), nullable=False),
    )

def downgrade():
    op.drop_table('user')