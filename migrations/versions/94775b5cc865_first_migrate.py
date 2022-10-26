"""First migrate

Revision ID: 94775b5cc865
Revises: 
Create Date: 2022-10-22 17:18:53.237603

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '94775b5cc865'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('area',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    schema='public'
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('area', schema='public')
    # ### end Alembic commands ###