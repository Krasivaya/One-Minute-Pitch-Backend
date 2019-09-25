"""add tables

Revision ID: 105fde4f11cc
Revises: c1a9909d186f
Create Date: 2019-09-17 21:50:33.831803

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '105fde4f11cc'
down_revision = 'c1a9909d186f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('roles')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('roles',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='roles_pkey')
    )
    # ### end Alembic commands ###
