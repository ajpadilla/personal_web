"""empty message

Revision ID: eb19a9ceba4e
Revises: 3d2781bb20bc
Create Date: 2022-08-27 20:52:21.424129

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'eb19a9ceba4e'
down_revision = '3d2781bb20bc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user_cart',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('payment_date', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_cart')
    # ### end Alembic commands ###
