"""add company relation to uploads

Revision ID: 6310f79ab571
Revises: 5eaf24d35f87
Create Date: 2017-03-22 15:22:48.575230

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6310f79ab571'
down_revision = '5eaf24d35f87'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('upload', sa.Column('company_id', sa.Integer(), nullable=True))
    op.add_column('upload', sa.Column('sent', sa.Boolean(), nullable=True))
    op.create_foreign_key(None, 'upload', 'company', ['company_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'upload', type_='foreignkey')
    op.drop_column('upload', 'sent')
    op.drop_column('upload', 'company_id')
    # ### end Alembic commands ###
