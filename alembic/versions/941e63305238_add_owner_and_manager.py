"""add owner and manager

Revision ID: 941e63305238
Revises: 7bae67c5f1a3
Create Date: 2017-02-08 23:48:23.912453

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '941e63305238'
down_revision = '7bae67c5f1a3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('manager',
    sa.Column('manager_id', sa.Integer(), nullable=False),
    sa.Column('active', sa.Boolean(), nullable=False),
    sa.Column('title', sa.String(length=255), nullable=False),
    sa.Column('address', sa.String(length=255), nullable=False),
    sa.Column('city', sa.String(length=128), nullable=False),
    sa.Column('state', sa.String(length=64), nullable=False),
    sa.Column('zip', sa.String(length=32), nullable=False),
    sa.Column('contact', sa.String(length=255), nullable=False),
    sa.Column('phone', sa.String(length=32), nullable=False),
    sa.Column('cell', sa.String(length=32), nullable=False),
    sa.Column('fax', sa.String(length=32), nullable=False),
    sa.Column('email', sa.String(length=255), nullable=False),
    sa.Column('notes', sa.Text(), nullable=False),
    sa.PrimaryKeyConstraint('manager_id')
    )
    op.create_table('owner',
    sa.Column('owner_id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=255), nullable=False),
    sa.Column('active', sa.Boolean(), nullable=False),
    sa.Column('address', sa.String(length=255), nullable=False),
    sa.Column('city', sa.String(length=128), nullable=False),
    sa.Column('state', sa.String(length=64), nullable=False),
    sa.Column('zip', sa.String(length=32), nullable=False),
    sa.Column('contact', sa.String(length=255), nullable=False),
    sa.Column('phone', sa.String(length=32), nullable=False),
    sa.Column('cell', sa.String(length=32), nullable=False),
    sa.Column('fax', sa.String(length=32), nullable=False),
    sa.Column('email', sa.String(length=255), nullable=False),
    sa.Column('notes', sa.Text(), nullable=False),
    sa.PrimaryKeyConstraint('owner_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('owner')
    op.drop_table('manager')
    # ### end Alembic commands ###
