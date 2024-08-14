"""Create users and user_sessions tables

Revision ID: 1966108e6ed5
Revises:
Create Date: 2024-08-09 04:03:22.489490

"""
from typing import Sequence, Union

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision: str = '1966108e6ed5'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.create_table('users',
                    sa.Column('id', sa.BigInteger(), autoincrement=True, nullable=False),
                    sa.Column('email', sa.String(length=255), nullable=False),
                    sa.Column('password', sa.String(length=255), nullable=True),
                    sa.Column('full_name', sa.String(length=255), nullable=False),
                    sa.Column('is_active', sa.Boolean(), nullable=True),
                    sa.Column('created_at', sa.DateTime(), nullable=False),
                    sa.Column('updated_at', sa.DateTime(), nullable=False),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_index(op.f('ix_users_email'), 'users', ['email'], unique=False)

    op.create_table('user_sessions',
                    sa.Column('id', sa.BigInteger(), autoincrement=True, nullable=False),
                    sa.Column('key', sa.String(length=255), nullable=False),
                    sa.Column('user_id', sa.BigInteger(), nullable=True),
                    sa.Column('expired_at', sa.DateTime(), nullable=False),
                    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_index(op.f('ix_user_sessions_key'), 'user_sessions', ['key'], unique=True)
    op.create_index(op.f('ix_user_sessions_user_id'), 'user_sessions', ['user_id'], unique=False)


def downgrade():
    op.drop_index(op.f('ix_user_sessions_user_id'), table_name='user_sessions')
    op.drop_index(op.f('ix_user_sessions_key'), table_name='user_sessions')
    op.drop_table('user_sessions')
    op.drop_index(op.f('ix_users_email'), table_name='users')
    op.drop_table('users')
