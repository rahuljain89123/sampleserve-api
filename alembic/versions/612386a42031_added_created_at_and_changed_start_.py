"""added created_at and changed start_sampling_on to datetime on Site

Revision ID: 612386a42031
Revises: b5bcde025b6e
Create Date: 2017-06-26 23:30:23.920186

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '612386a42031'
down_revision = 'b5bcde025b6e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('site', sa.Column('created_at', sa.DateTime(), nullable=True))
    op.drop_column('site', 'start_sampling_on')
    op.add_column('site', sa.Column('start_sampling_on', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('site', 'created_at')
    op.drop_column('site', 'start_sampling_on')
    op.add_column('site', sa.Column('start_sampling_on', sa.Integer(), nullable=True))
    # ### end Alembic commands ###
