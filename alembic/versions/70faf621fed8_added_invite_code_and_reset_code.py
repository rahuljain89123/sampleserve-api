"""added invite_code and reset_code

Revision ID: 70faf621fed8
Revises: 9a9a05a32305
Create Date: 2017-03-30 01:59:44.434588

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '70faf621fed8'
down_revision = '9a9a05a32305'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('invite_code', sa.String(length=255), nullable=True))
    op.add_column('user', sa.Column('reset_code', sa.String(length=255), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'reset_code')
    op.drop_column('user', 'invite_code')
    # ### end Alembic commands ###
