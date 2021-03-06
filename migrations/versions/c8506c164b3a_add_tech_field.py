"""add tech field

Revision ID: c8506c164b3a
Revises: 48acf5c93a4d
Create Date: 2019-04-24 23:23:24.888065

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c8506c164b3a'
down_revision = '48acf5c93a4d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('project', schema=None) as batch_op:
        batch_op.create_foreign_key(batch_op.f('fk_project_technology_id_technology'), 'technology', ['technology_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('project', schema=None) as batch_op:
        batch_op.drop_constraint(batch_op.f('fk_project_technology_id_technology'), type_='foreignkey')

    # ### end Alembic commands ###
