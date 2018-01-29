"""add schedules

Revision ID: b2c9c6a7e170
Revises: f4bc69ce830e
Create Date: 2017-02-10 00:01:20.353928

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b2c9c6a7e170'
down_revision = 'f4bc69ce830e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('schedule',
    sa.Column('schedule_id', sa.Integer(), nullable=False),
    sa.Column('active', sa.Boolean(), nullable=False),
    sa.Column('finished', sa.Boolean(), nullable=False),
    sa.Column('site_id', sa.Integer(), nullable=False),
    sa.Column('date', sa.Integer(), nullable=False),
    sa.Column('timeofday', sa.String(length=255), nullable=False),
    sa.Column('starttime', sa.String(length=16), nullable=False),
    sa.Column('endtime', sa.String(length=16), nullable=False),
    sa.Column('typeofactivity', sa.String(length=255), nullable=False),
    sa.Column('release_number', sa.String(length=255), nullable=False),
    sa.Column('frequency_association', sa.String(length=255), nullable=False),
    sa.Column('test_ids', sa.Text(), nullable=False),
    sa.ForeignKeyConstraint(['site_id'], ['site.site_id'], ),
    sa.PrimaryKeyConstraint('schedule_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('schedule')
    # ### end Alembic commands ###