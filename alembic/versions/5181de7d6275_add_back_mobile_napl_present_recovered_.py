"""add back mobile_napl_present_recovered_date

Revision ID: 5181de7d6275
Revises: 26bab668fb30
Create Date: 2017-05-10 07:21:29.537797

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5181de7d6275'
down_revision = '26bab668fb30'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('site_data', sa.Column('mobile_napl_present_recovered_date', sa.String(length=255), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('site_data', 'mobile_napl_present_recovered_date')
    # ### end Alembic commands ###
