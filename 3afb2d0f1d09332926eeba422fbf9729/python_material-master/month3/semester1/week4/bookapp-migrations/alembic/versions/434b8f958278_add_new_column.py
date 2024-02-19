"""add new column

Revision ID: 434b8f958278
Revises: 777d0e150730
Create Date: 2023-05-15 22:45:13.204346

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '434b8f958278'
down_revision = '777d0e150730'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('books', sa.Column('author', sa.String(), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('books', 'author')
    # ### end Alembic commands ###
