"""test remove profiles

Revision ID: eecba9507ece
Revises: bd731cfce587
Create Date: 2020-12-16 18:11:03.506442

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'eecba9507ece'
down_revision = 'bd731cfce587'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('profiles')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('profiles',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('username', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('firstname', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('lastname', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name='profiles_user_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='profiles_pkey'),
    sa.UniqueConstraint('username', name='profiles_username_key')
    )
    # ### end Alembic commands ###
