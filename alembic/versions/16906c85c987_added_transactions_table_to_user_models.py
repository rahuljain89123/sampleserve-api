"""added transactions table to user models

Revision ID: 16906c85c987
Revises: be073f62a788
Create Date: 2017-03-19 23:03:24.496989

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '16906c85c987'
down_revision = 'be073f62a788'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('transaction',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('lab_id', sa.Integer(), nullable=True),
    sa.Column('site_id', sa.Integer(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('total_amount', sa.Float(precision=12), nullable=True),
    sa.Column('lab_earnings_amount', sa.Float(precision=12), nullable=True),
    sa.Column('samples', postgresql.JSON(astext_type=sa.Text()), nullable=True),
    sa.Column('stripe_transaction_id', sa.String(length=255), nullable=True),
    sa.Column('stripe_card_id', sa.String(length=255), nullable=True),
    sa.Column('cc_last4', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['lab_id'], ['lab.laboratory_id'], ),
    sa.ForeignKeyConstraint(['site_id'], ['site.site_id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column(u'user', sa.Column('created_at', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column(u'user', 'created_at')
    op.drop_table('transaction')
    # ### end Alembic commands ###
