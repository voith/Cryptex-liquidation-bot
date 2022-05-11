"""Create TcapVaults table

Revision ID: 44da2641b1ac
Revises: 
Create Date: 2022-05-10 02:39:27.743342

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '44da2641b1ac'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('TcapVaults',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('vault_type', sa.Enum('WETH', 'WBTC', 'DAI', 'USDC', name='vault_types'), nullable=False),
    sa.Column('vault_ratio', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id', 'vault_type')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('TcapVaults')
    # ### end Alembic commands ###
