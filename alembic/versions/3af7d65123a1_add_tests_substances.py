"""add tests substances

Revision ID: 3af7d65123a1
Revises: ddd5e9aeafa5
Create Date: 2017-02-10 14:27:48.488295

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3af7d65123a1'
down_revision = 'ddd5e9aeafa5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tests_substances',
    sa.Column('test_id', sa.Integer(), nullable=False),
    sa.Column('substance_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['substance_id'], ['substance.substance_id'], ),
    sa.ForeignKeyConstraint(['test_id'], ['test.test_id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('tests_substances')
    # ### end Alembic commands ###
