"""added gauged_wells relational table

Revision ID: 0977b4626e1d
Revises: 409247407c67
Create Date: 2017-05-04 08:41:15.617361

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0977b4626e1d'
down_revision = '409247407c67'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('gauged_wells',
    sa.Column('schedule_id', sa.Integer(), nullable=True),
    sa.Column('well_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['schedule_id'], ['schedule.id'], ),
    sa.ForeignKeyConstraint(['well_id'], ['well.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('gauged_wells')
    # ### end Alembic commands ###
