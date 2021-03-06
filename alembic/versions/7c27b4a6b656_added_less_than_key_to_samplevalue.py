"""added less_than key to samplevalue

Revision ID: 7c27b4a6b656
Revises: 989a22a92ea0
Create Date: 2017-04-24 11:47:43.355078

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7c27b4a6b656'
down_revision = '989a22a92ea0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('sample_value', sa.Column('less_than', sa.Float(precision=12), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('sample_value', 'less_than')
    # ### end Alembic commands ###
