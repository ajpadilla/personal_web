"""empty message

Revision ID: 9fd10d97cd90
Revises: b255cc262a9d
Create Date: 2022-08-27 20:56:27.701005

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9fd10d97cd90'
down_revision = 'b255cc262a9d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user_cart',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('use_id', sa.Integer(), nullable=False),
    sa.Column('shopping_cart_id', sa.Integer(), nullable=False),
    sa.Column('status', sa.String(length=30), nullable=False),
    sa.Column('payment_date', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['shopping_cart_id'], ['shopping_cart.id'], ),
    sa.ForeignKeyConstraint(['use_id'], ['blog_user.id'], ),
    sa.PrimaryKeyConstraint('id', 'use_id', 'shopping_cart_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_cart')
    # ### end Alembic commands ###
