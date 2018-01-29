"""change owner to company

Revision ID: e6a4403a8fc1
Revises: 12166f794464
Create Date: 2017-03-06 05:21:28.208025

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e6a4403a8fc1'
down_revision = '12166f794464'
branch_labels = None
depends_on = None

# remove site.owner_id
# remove owner (drop company, rename owner to company)
# add site.company_id
def upgrade():
    op.drop_constraint(u'users_companies_company_id_fkey', 'users_companies', type_='foreignkey')
    op.drop_constraint(u'site_owner_id_fkey', 'site', type_='foreignkey')
    op.drop_column('site', 'owner_id')
    op.drop_table('company')
    op.execute('ALTER TABLE public.owner RENAME TO company')
    op.execute('ALTER TABLE public.company RENAME COLUMN owner_id TO id')
    op.add_column('site', sa.Column('company_id', sa.Integer()))
    op.create_foreign_key(None, 'site', 'company', ['company_id'], ['id'])
    op.create_foreign_key(None, 'users_companies', 'company', ['company_id'], ['id'])

# remove site.company_id
# add owner (rename company to owner, add company)
# add site.owner_id
def downgrade():
    op.drop_constraint(u'site_company_id_fkey', 'site', type_='foreignkey')
    op.drop_column('site', 'company_id')
    op.execute('ALTER TABLE public.company RENAME TO owner')
    op.execute('ALTER TABLE public.owner RENAME COLUMN id TO owner_id')
    op.create_table('company',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=80), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.add_column('site', sa.Column('owner_id', sa.INTEGER(), autoincrement=False, nullable=False))
    op.create_foreign_key(u'site_owner_id_fkey', 'site', 'owner', ['owner_id'], ['owner_id'])
