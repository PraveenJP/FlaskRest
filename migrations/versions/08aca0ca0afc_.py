"""empty message

Revision ID: 08aca0ca0afc
Revises: c2c37055b264
Create Date: 2017-12-18 18:46:50.986781

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '08aca0ca0afc'
down_revision = 'c2c37055b264'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=80), nullable=True),
    sa.Column('email', sa.String(length=120), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    # ### end Alembic commands ###
