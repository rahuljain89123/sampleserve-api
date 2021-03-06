"""add offices

Revision ID: d925222b77dd
Revises: 41d07a7c9d66
Create Date: 2017-02-09 18:25:15.292245

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd925222b77dd'
down_revision = '41d07a7c9d66'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('office',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=255), nullable=False),
    sa.Column('contact', sa.String(length=255), nullable=True),
    sa.Column('address', sa.String(length=80), nullable=False),
    sa.Column('city', sa.String(length=255), nullable=False),
    sa.Column('state', sa.String(length=2), nullable=False),
    sa.Column('zip', sa.String(length=32), nullable=False),
    sa.Column('phone', sa.String(length=32), nullable=True),
    sa.Column('cell', sa.String(length=32), nullable=True),
    sa.Column('email', sa.String(length=255), nullable=True),
    sa.Column('lat', sa.Float(precision=10), nullable=False),
    sa.Column('lng', sa.Float(precision=10), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('office')
    # ### end Alembic commands ###
