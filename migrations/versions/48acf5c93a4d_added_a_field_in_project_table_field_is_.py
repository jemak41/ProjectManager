"""added a field in project table. field is called remarks

Revision ID: 48acf5c93a4d
Revises: 74650372be19
Create Date: 2019-04-20 18:20:09.369602

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '48acf5c93a4d'
down_revision = '74650372be19'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('project', sa.Column('remarks', sa.String(length=5000), nullable=True))
    op.create_index(op.f('ix_project_remarks'), 'project', ['remarks'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_project_remarks'), table_name='project')
    op.drop_column('project', 'remarks')
    # ### end Alembic commands ###
