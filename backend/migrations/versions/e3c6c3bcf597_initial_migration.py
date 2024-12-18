"""Initial migration

Revision ID: e3c6c3bcf597
Revises: 
Create Date: 2024-12-18 17:38:34.384173

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e3c6c3bcf597'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('grade_distribution',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('term', sa.String(length=50), nullable=False),
    sa.Column('year', sa.String(length=4), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('grade_distribution')
    # ### end Alembic commands ###
