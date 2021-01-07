"""empty message

Revision ID: 13d85b04c581
Revises: 
Create Date: 2021-01-07 01:31:25.721833

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '13d85b04c581'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('inventory',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('value', sa.String(length=80), nullable=False),
    sa.Column('monthyPrice', sa.Numeric(precision=10, scale=2), nullable=False),
    sa.Column('setupPrice', sa.Numeric(precision=10, scale=2), nullable=False),
    sa.Column('currency', sa.String(length=10), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('value')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('inventory')
    # ### end Alembic commands ###