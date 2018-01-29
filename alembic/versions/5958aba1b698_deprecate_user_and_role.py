"""deprecate user and role

Revision ID: 5958aba1b698
Revises: abb2574a5fa6
Create Date: 2017-02-13 19:08:36.060698

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '5958aba1b698'
down_revision = 'abb2574a5fa6'
branch_labels = None
depends_on = None


def upgrade():
    op.execute('ALTER TABLE public.user RENAME TO user_deprecated')
    op.execute('ALTER TABLE public.role RENAME TO role_deprecated')


def downgrade():
    op.execute('ALTER TABLE public.user_deprecated RENAME TO user')
    op.execute('ALTER TABLE public.role_deprecated RENAME TO role')
