"""fix primary id

Revision ID: ef491f2a0812
Revises: 61dc6214242e
Create Date: 2017-03-31 16:24:05.529320

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ef491f2a0812'
down_revision = '61dc6214242e'
branch_labels = None
depends_on = None


def upgrade():
    op.execute("CREATE SEQUENCE if not exists site_id_seq")
    op.execute("ALTER TABLE site ALTER id SET DEFAULT nextval('site_id_seq')")
    op.execute("SELECT setval('site_id_seq', ((SELECT MAX(id) FROM site)+1), true)")

def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###
