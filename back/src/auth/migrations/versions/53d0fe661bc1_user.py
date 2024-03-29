"""user

Revision ID: 53d0fe661bc1
Revises: 
Create Date: 2024-02-22 12:04:33.651611

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '53d0fe661bc1'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.UUID(), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('hash_password', sa.String(), nullable=False),
    sa.Column('create_date', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    # ### end Alembic commands ###
