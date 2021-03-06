"""test

Revision ID: d24a1d4b1fcd
Revises: 7cae2195cf91
Create Date: 2021-12-18 18:21:00.282733

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd24a1d4b1fcd'
down_revision = '7cae2195cf91'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('login',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('admin_username', sa.String(length=50), nullable=True),
    sa.Column('admin_password', sa.String(length=50), nullable=True),
    sa.Column('log_bool', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('login')
    # ### end Alembic commands ###
