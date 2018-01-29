"""add consultant

Revision ID: 7bae67c5f1a3
Revises: 55cae16d0d7d
Create Date: 2017-02-08 22:55:04.436330

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7bae67c5f1a3'
down_revision = '55cae16d0d7d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('consultant',
    sa.Column('consultant_id', sa.Integer(), nullable=False),
    sa.Column('active', sa.Boolean(), nullable=False),
    sa.Column('qcid', sa.String(length=32), nullable=False),
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
    sa.PrimaryKeyConstraint('consultant_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('consultant')
    # ### end Alembic commands ###
