"""empty message

Revision ID: 3eb612f56ba1
Revises: None
Create Date: 2015-04-11 16:36:25.269507

"""

# revision identifiers, used by Alembic.
revision = '3eb612f56ba1'
down_revision = None

from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql import column, table


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('session',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('username', sa.String(), nullable=True),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_table('role',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('name', sa.String(length=80), nullable=True),
                    sa.Column('description', sa.String(length=255), nullable=True),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('name')
                    )
    op.create_table('user',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('username', sa.String(length=80), nullable=True),
                    sa.Column('email', sa.String(length=80), nullable=True),
                    sa.Column('password', sa.String(), nullable=True),
                    sa.Column('active', sa.Boolean(), nullable=True),
                    sa.Column('email_activated', sa.Boolean(), nullable=True),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_index(op.f('ix_user_email'), 'user', ['email'], unique=True)
    op.create_index(op.f('ix_user_username'), 'user', ['username'], unique=True)
    op.create_table('roles_users',
                    sa.Column('user_id', sa.Integer(), nullable=True),
                    sa.Column('role_id', sa.Integer(), nullable=True),
                    sa.ForeignKeyConstraint(['role_id'], ['role.id'], ),
                    sa.ForeignKeyConstraint(['user_id'], ['user.id'], )
                    )
    op.create_table('userdata',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('username', sa.String(length=80), nullable=True),
                    sa.Column('stream', sa.String(collation='en_US.UTF-8'), nullable=True),
                    sa.Column('from_short', sa.String(), nullable=True),
                    sa.Column('from_full', sa.String(), nullable=True),
                    sa.Column('interview_location', sa.String(collation='en_US.UTF-8'), nullable=True),
                    sa.Column('interview_date', sa.DateTime(), nullable=True),
                    sa.Column('invitation_to_apply_date', sa.DateTime(), nullable=True),
                    sa.Column('mpnp_file_date', sa.DateTime(), nullable=True),
                    sa.Column('mpnp_request_additional_docs_date', sa.DateTime(), nullable=True),
                    sa.Column('mpnp_nomination_date', sa.DateTime(), nullable=True),
                    sa.Column('cio_received_date', sa.DateTime(), nullable=True),
                    sa.Column('cio_processing_fee_date', sa.DateTime(), nullable=True),
                    sa.Column('cio_file_number', sa.DateTime(), nullable=True),
                    sa.Column('embassy', sa.String(collation='en_US.UTF-8'), nullable=True),
                    sa.Column('ecas_recieved', sa.DateTime(), nullable=True),
                    sa.Column('ecas_in_process', sa.DateTime(), nullable=True),
                    sa.Column('ecas_additional_documents_request1', sa.DateTime(), nullable=True),
                    sa.Column('ecas_medical_forms', sa.DateTime(), nullable=True),
                    sa.Column('ecas_medical_exam_passed', sa.DateTime(), nullable=True),
                    sa.Column('ecas_medical_results_received', sa.DateTime(), nullable=True),
                    sa.Column('ecas_additional_documents_request2', sa.DateTime(), nullable=True),
                    sa.Column('povl_date', sa.DateTime(), nullable=True),
                    # sa.ForeignKeyConstraint(['username'], ['user.username'], ),
                    sa.PrimaryKeyConstraint('id')
                    )

    role_table = table('role',
                       column('id', sa.Integer),
                       column('name', sa.String),
                       column('description', sa.Date))

    op.bulk_insert(role_table,
                   [
                       {'id': 0, 'name': 'admin', 'description': 'admin role'},
                       {'id': 1, 'name': 'super_admin', 'description': 'super admin role'}
                   ]
                   )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('userdata')
    op.drop_table('roles_users')
    op.drop_index(op.f('ix_user_username'), table_name='user')
    op.drop_index(op.f('ix_user_email'), table_name='user')
    op.drop_table('user')
    op.drop_table('role')
    op.drop_table('session')
    ### end Alembic commands ###
