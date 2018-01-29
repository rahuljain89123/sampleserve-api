"""changed date column to datetime from integer

Revision ID: 267d414e9a7d
Revises: 8e147ebbcee8
Create Date: 2017-04-07 09:19:47.972317

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '267d414e9a7d'
down_revision = '8e147ebbcee8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('schedule_tests',
    sa.Column('schedule_id', sa.Integer(), nullable=True),
    sa.Column('test_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['schedule_id'], ['schedule.id'], ),
    sa.ForeignKeyConstraint(['test_id'], ['test.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('schedule_tests')
    # ### end Alembic commands ###