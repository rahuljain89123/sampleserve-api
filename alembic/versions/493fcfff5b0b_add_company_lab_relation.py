"""add company lab relation

Revision ID: 493fcfff5b0b
Revises: a71cbdbb9753
Create Date: 2017-03-09 03:33:22.866043

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '493fcfff5b0b'
down_revision = 'a71cbdbb9753'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('company', sa.Column('lab_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'company', 'lab', ['lab_id'], ['laboratory_id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'company', type_='foreignkey')
    op.drop_column('company', 'lab_id')
    # ### end Alembic commands ###