"""init

Revision ID: 62e6fb150643
Revises: 
Create Date: 2024-11-06 16:50:57.844463

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '62e6fb150643'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('permits',
    sa.Column('PMT_permitId', sa.Integer(), nullable=False),
    sa.Column('PMT_type', sa.String(length=80), nullable=False),
    sa.PrimaryKeyConstraint('PMT_permitId')
    )
    op.create_table('status',
    sa.Column('ST_statusId', sa.Integer(), nullable=False),
    sa.Column('ST_value', sa.String(length=80), nullable=False),
    sa.Column('ST_status_type', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('ST_statusId')
    )
    op.create_table('users',
    sa.Column('USR_userId', sa.Integer(), nullable=False),
    sa.Column('USR_PER_permitId', sa.Integer(), nullable=True),
    sa.Column('USR_email', sa.String(length=120), nullable=False),
    sa.Column('USR_password', sa.String(length=250), nullable=False),
    sa.Column('USR_password_salt', sa.String(length=250), nullable=False),
    sa.Column('USR_telephone', sa.String(length=15), nullable=True),
    sa.Column('USR_name', sa.String(length=80), nullable=False),
    sa.Column('USR_last_name', sa.String(length=80), nullable=False),
    sa.Column('USR_ST_statusId', sa.Integer(), nullable=True),
    sa.Column('USR_address', sa.String(length=50), nullable=True),
    sa.Column('USR_last_modified', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['USR_PER_permitId'], ['permits.PMT_permitId'], ),
    sa.ForeignKeyConstraint(['USR_ST_statusId'], ['status.ST_statusId'], ),
    sa.PrimaryKeyConstraint('USR_userId'),
    sa.UniqueConstraint('USR_email')
    )
    op.create_table('packages',
    sa.Column('PCK_packageId', sa.Integer(), nullable=False),
    sa.Column('PCK_USR_assigned_to', sa.Integer(), nullable=True),
    sa.Column('PCK_USR_assigned_by', sa.Integer(), nullable=True),
    sa.Column('PCK_street', sa.String(length=200), nullable=False),
    sa.Column('PCK_ext_number', sa.String(length=10), nullable=False),
    sa.Column('PCK_int_number', sa.String(length=10), nullable=True),
    sa.Column('PCK_neighborhood', sa.String(length=50), nullable=False),
    sa.Column('PCK_zip_code', sa.String(length=5), nullable=False),
    sa.Column('PCK_city', sa.String(length=50), nullable=False),
    sa.Column('PCK_state', sa.String(length=50), nullable=False),
    sa.Column('PCK_special_instructions', sa.String(length=200), nullable=True),
    sa.Column('PCK_client_name', sa.String(length=100), nullable=False),
    sa.Column('PCK_client_phone_num', sa.String(length=15), nullable=False),
    sa.Column('PCK_ST_statusId', sa.Integer(), nullable=True),
    sa.Column('PCK_last_modified', sa.DateTime(), nullable=False),
    sa.Column('PCK_delivery_date', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['PCK_ST_statusId'], ['status.ST_statusId'], ),
    sa.ForeignKeyConstraint(['PCK_USR_assigned_by'], ['users.USR_userId'], ),
    sa.ForeignKeyConstraint(['PCK_USR_assigned_to'], ['users.USR_userId'], ),
    sa.PrimaryKeyConstraint('PCK_packageId')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('packages')
    op.drop_table('users')
    op.drop_table('status')
    op.drop_table('permits')
    # ### end Alembic commands ###