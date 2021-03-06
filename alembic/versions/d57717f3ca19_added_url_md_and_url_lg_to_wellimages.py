"""added url_md and url_lg to wellimages

Revision ID: d57717f3ca19
Revises: 85c136326052
Create Date: 2017-04-24 21:02:00.752392

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd57717f3ca19'
down_revision = '85c136326052'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('well_image', sa.Column('url_lg', sa.String(length=255), nullable=True))
    op.add_column('well_image', sa.Column('url_md', sa.String(length=255), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('well_image', 'url_md')
    op.drop_column('well_image', 'url_lg')
    # ### end Alembic commands ###
