"""add foreign key to onboarding

Revision ID: e449e2a359b1
Revises: b8ba7eb3a1d0
Create Date: 2024-10-03 08:26:53.770757

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e449e2a359b1'
down_revision = 'b8ba7eb3a1d0'
branch_labels = None
depends_on = None


def upgrade():
    with op.batch_alter_table('onboardings', schema=None) as batch_op:
        batch_op.add_column(sa.Column('employee_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key('fk_employee_id', 'employees', ['employee_id'], ['id'])


def downgrade():
    with op.batch_alter_table('onboardings', schema=None) as batch_op:
        batch_op.drop_constraint('fk_employee_id', type_='foreignkey')
        batch_op.drop_column('employee_id')
