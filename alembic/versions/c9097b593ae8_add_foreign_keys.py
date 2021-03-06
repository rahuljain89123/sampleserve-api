"""add foreign keys

Revision ID: c9097b593ae8
Revises: 37b8c276b8d0
Create Date: 2017-02-10 17:46:44.993176

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c9097b593ae8'
down_revision = '37b8c276b8d0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key(None, 'site', 'owner', ['owner_id'], ['owner_id'])
    op.create_foreign_key(None, 'site', 'state', ['state_id'], ['state_id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'site', type_='foreignkey')
    op.drop_constraint(None, 'site', type_='foreignkey')
    # ### end Alembic commands ###
