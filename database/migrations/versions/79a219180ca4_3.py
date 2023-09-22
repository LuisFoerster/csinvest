"""3

Revision ID: 79a219180ca4
Revises: beb0f8027f4e
Create Date: 2023-08-08 12:53:00.572694

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '79a219180ca4'
down_revision = 'beb0f8027f4e'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('accounts_ibfk_1', 'accounts', type_='foreignkey')
    op.drop_column('accounts', 'userid')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('accounts', sa.Column('userid', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True))
    op.create_foreign_key('accounts_ibfk_1', 'accounts', 'users', ['userid'], ['id'])
    # ### end Alembic commands ###