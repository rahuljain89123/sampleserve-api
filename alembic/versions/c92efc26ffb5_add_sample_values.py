"""add sample values

Revision ID: c92efc26ffb5
Revises: 3088f8bb52be
Create Date: 2017-02-09 20:46:28.801620

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c92efc26ffb5'
down_revision = '3088f8bb52be'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('sample_value',
    sa.Column('substance_id', sa.Integer(), nullable=False),
    sa.Column('sample_id', sa.Integer(), nullable=False),
    sa.Column('well_id', sa.Integer(), nullable=False),
    sa.Column('import_id', sa.Integer(), nullable=True),
    sa.Column('value', sa.Float(precision=12), nullable=False),
    sa.Column('details', sa.String(length=20), nullable=True),
    sa.Column('new', sa.Boolean(), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['sample_id'], ['sample.sample_id'], ),
    sa.ForeignKeyConstraint(['substance_id'], ['substance.substance_id'], ),
    sa.ForeignKeyConstraint(['well_id'], ['well.well_id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('sample_value')
    # ### end Alembic commands ###