"""empty message

Revision ID: 5c6d8879cca7
Revises: ecf2f1bced2c
Create Date: 2022-09-25 20:16:45.874653

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5c6d8879cca7'
down_revision = 'ecf2f1bced2c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('client', sa.Column('advisor_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'client', 'advisor', ['advisor_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'client', type_='foreignkey')
    op.drop_column('client', 'advisor_id')
    # ### end Alembic commands ###
