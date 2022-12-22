"""empty message

Revision ID: efa7f2eed648
Revises: 9fd10d97cd90
Create Date: 2022-08-27 21:29:44.225069

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'efa7f2eed648'
down_revision = '9fd10d97cd90'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_cart')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user_cart',
    sa.Column('id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('use_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('shopping_cart_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('status', sa.VARCHAR(length=30), autoincrement=False, nullable=False),
    sa.Column('payment_date', postgresql.TIMESTAMP(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['shopping_cart_id'], ['shopping_cart.id'], name='user_cart_shopping_cart_id_fkey'),
    sa.ForeignKeyConstraint(['use_id'], ['blog_user.id'], name='user_cart_use_id_fkey'),
    sa.PrimaryKeyConstraint('id', 'use_id', 'shopping_cart_id', name='user_cart_pkey')
    )
    # ### end Alembic commands ###
