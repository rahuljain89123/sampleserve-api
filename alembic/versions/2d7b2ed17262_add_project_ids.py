"""add project ids

Revision ID: 2d7b2ed17262
Revises: 6310f79ab571
Create Date: 2017-03-25 18:34:31.653374

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2d7b2ed17262'
down_revision = '6310f79ab571'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('projects_sites')
    op.add_column('site', sa.Column('project_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'site', 'project', ['project_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'site', type_='foreignkey')
    op.drop_column('site', 'project_id')
    op.create_table('projects_sites',
    sa.Column('project_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('site_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['project_id'], [u'project.id'], name=u'projects_sites_project_id_fkey'),
    sa.ForeignKeyConstraint(['site_id'], [u'site.id'], name=u'projects_sites_site_id_fkey')
    )
    # ### end Alembic commands ###
