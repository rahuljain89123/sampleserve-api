"""remove unique email

Revision ID: 72443181714d
Revises: 7f4fb1b8cd9c
Create Date: 2017-02-26 05:51:33.122823

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '72443181714d'
down_revision = '7f4fb1b8cd9c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(u'user_email_key', 'user', type_='unique')
    op.drop_constraint(u'user_username_key', 'user', type_='unique')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(u'user_username_key', 'user', ['username'])
    op.create_unique_constraint(u'user_email_key', 'user', ['email'])
    # ### end Alembic commands ###
