"""Add Column email to model users

Revision ID: 6b890b68717c
Revises: 2cc9052225bc
Create Date: 2022-10-23 13:26:15.598691

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6b890b68717c'
down_revision = '2cc9052225bc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('email', sa.String(length=50), nullable=True))
    op.create_unique_constraint(None, 'users', ['email'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'users', type_='unique')
    op.drop_column('users', 'email')
    # ### end Alembic commands ###
