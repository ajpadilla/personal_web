"""empty message

Revision ID: b255cc262a9d
Revises: 519b7a588f71
Create Date: 2022-08-27 20:56:01.644715

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'b255cc262a9d'
down_revision = '519b7a588f71'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_cart')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user_cart',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('payment_date', postgresql.TIMESTAMP(), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='user_cart_pkey')
    )
    # ### end Alembic commands ###
