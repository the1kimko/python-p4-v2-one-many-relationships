"""add foreign key to Review

Revision ID: b8ba7eb3a1d0
Revises: 1d664fd71a26
Create Date: 2024-10-03 07:47:54.663226

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b8ba7eb3a1d0'
down_revision = '1d664fd71a26'
branch_labels = None
depends_on = None


def upgrade():
    with op.batch_alter_table('reviews', schema=None) as batch_op:
        batch_op.add_column(sa.Column('employee_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key('fk_employee_id', 'employees', ['employee_id'], ['id'])



def downgrade():
    with op.batch_alter_table('reviews', schema=None) as batch_op:
        batch_op.drop_constraint('fk_employee_id', type_='foreignkey')
        batch_op.drop_column('employee_id')
