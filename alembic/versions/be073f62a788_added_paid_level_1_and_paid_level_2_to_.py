"""added paid_level_1 and paid_level 2 to Sample

Revision ID: be073f62a788
Revises: 5297dbe6a18e
Create Date: 2017-03-19 21:57:44.743642

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'be073f62a788'
down_revision = '5297dbe6a18e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('sample', sa.Column('paid_level_1', sa.Boolean(), nullable=True))
    op.add_column('sample', sa.Column('paid_level_2', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('sample', 'paid_level_2')
    op.drop_column('sample', 'paid_level_1')
    # ### end Alembic commands ###
