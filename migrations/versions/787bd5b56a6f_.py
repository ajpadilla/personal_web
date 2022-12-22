"""empty message

Revision ID: 787bd5b56a6f
Revises: 154c098a2d33
Create Date: 2022-08-27 21:43:19.423431

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '787bd5b56a6f'
down_revision = '154c098a2d33'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user_cart',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('shopping_cart_id', sa.Integer(), nullable=False),
    sa.Column('status', sa.String(length=30), nullable=False),
    sa.Column('payment_date', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['shopping_cart_id'], ['shopping_cart.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['blog_user.id'], ),
    sa.PrimaryKeyConstraint('user_id', 'shopping_cart_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_cart')
    # ### end Alembic commands ###
