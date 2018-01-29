"""remove username

Revision ID: e7392ade6a19
Revises: 72443181714d
Create Date: 2017-02-26 06:41:21.348469

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e7392ade6a19'
down_revision = '72443181714d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'username')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('username', sa.VARCHAR(length=255), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
