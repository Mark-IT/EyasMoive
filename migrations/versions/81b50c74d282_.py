"""empty message

Revision ID: 81b50c74d282
Revises: 
Create Date: 2018-05-13 17:30:53.565505

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '81b50c74d282'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('auth',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=True),
    sa.Column('url', sa.String(length=255), nullable=True),
    sa.Column('addtime', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name'),
    sa.UniqueConstraint('url')
    )
    op.create_index(op.f('ix_auth_addtime'), 'auth', ['addtime'], unique=False)
    op.create_table('preview',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=255), nullable=True),
    sa.Column('logo', sa.String(length=255), nullable=True),
    sa.Column('addtime', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('logo'),
    sa.UniqueConstraint('title')
    )
    op.create_index(op.f('ix_preview_addtime'), 'preview', ['addtime'], unique=False)
    op.create_table('role',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=True),
    sa.Column('auths', sa.String(length=600), nullable=True),
    sa.Column('addtime', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_index(op.f('ix_role_addtime'), 'role', ['addtime'], unique=False)
    op.create_table('tag',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=True),
    sa.Column('addtime', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_index(op.f('ix_tag_addtime'), 'tag', ['addtime'], unique=False)
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=True),
    sa.Column('_password', sa.String(length=100), nullable=True),
    sa.Column('email', sa.String(length=100), nullable=True),
    sa.Column('phone', sa.String(length=11), nullable=True),
    sa.Column('info', sa.Text(), nullable=True),
    sa.Column('face', sa.String(length=255), nullable=True),
    sa.Column('addtime', sa.DateTime(), nullable=True),
    sa.Column('uuid', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('face'),
    sa.UniqueConstraint('name'),
    sa.UniqueConstraint('phone'),
    sa.UniqueConstraint('uuid')
    )
    op.create_index(op.f('ix_user_addtime'), 'user', ['addtime'], unique=False)
    op.create_table('admin',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=True),
    sa.Column('_password', sa.String(length=100), nullable=True),
    sa.Column('is_super', sa.SmallInteger(), nullable=True),
    sa.Column('role_id', sa.Integer(), nullable=True),
    sa.Column('addtime', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['role_id'], ['role.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_index(op.f('ix_admin_addtime'), 'admin', ['addtime'], unique=False)
    op.create_table('movie',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=255), nullable=True),
    sa.Column('url', sa.String(length=255), nullable=True),
    sa.Column('info', sa.Text(), nullable=True),
    sa.Column('logo', sa.String(length=255), nullable=True),
    sa.Column('star', sa.SmallInteger(), nullable=True),
    sa.Column('playnum', sa.BigInteger(), nullable=True),
    sa.Column('commentnum', sa.BigInteger(), nullable=True),
    sa.Column('tag_id', sa.Integer(), nullable=True),
    sa.Column('area', sa.String(length=255), nullable=True),
    sa.Column('release_time', sa.Date(), nullable=True),
    sa.Column('length', sa.String(length=100), nullable=True),
    sa.Column('addtime', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['tag_id'], ['tag.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('logo'),
    sa.UniqueConstraint('title'),
    sa.UniqueConstraint('url')
    )
    op.create_index(op.f('ix_movie_addtime'), 'movie', ['addtime'], unique=False)
    op.create_table('userlog',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('ip', sa.String(length=100), nullable=True),
    sa.Column('addtime', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_userlog_addtime'), 'userlog', ['addtime'], unique=False)
    op.create_table('adminlog',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('admin_id', sa.Integer(), nullable=True),
    sa.Column('ip', sa.String(length=100), nullable=True),
    sa.Column('addtime', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['admin_id'], ['admin.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_adminlog_addtime'), 'adminlog', ['addtime'], unique=False)
    op.create_table('comment',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('content', sa.Text(), nullable=True),
    sa.Column('movie_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('addtime', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['movie_id'], ['movie.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_comment_addtime'), 'comment', ['addtime'], unique=False)
    op.create_table('moviecol',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('movie_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('addtime', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['movie_id'], ['movie.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_moviecol_addtime'), 'moviecol', ['addtime'], unique=False)
    op.create_table('oplog',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('admin_id', sa.Integer(), nullable=True),
    sa.Column('ip', sa.String(length=100), nullable=True),
    sa.Column('reason', sa.String(length=600), nullable=True),
    sa.Column('addtime', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['admin_id'], ['admin.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_oplog_addtime'), 'oplog', ['addtime'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_oplog_addtime'), table_name='oplog')
    op.drop_table('oplog')
    op.drop_index(op.f('ix_moviecol_addtime'), table_name='moviecol')
    op.drop_table('moviecol')
    op.drop_index(op.f('ix_comment_addtime'), table_name='comment')
    op.drop_table('comment')
    op.drop_index(op.f('ix_adminlog_addtime'), table_name='adminlog')
    op.drop_table('adminlog')
    op.drop_index(op.f('ix_userlog_addtime'), table_name='userlog')
    op.drop_table('userlog')
    op.drop_index(op.f('ix_movie_addtime'), table_name='movie')
    op.drop_table('movie')
    op.drop_index(op.f('ix_admin_addtime'), table_name='admin')
    op.drop_table('admin')
    op.drop_index(op.f('ix_user_addtime'), table_name='user')
    op.drop_table('user')
    op.drop_index(op.f('ix_tag_addtime'), table_name='tag')
    op.drop_table('tag')
    op.drop_index(op.f('ix_role_addtime'), table_name='role')
    op.drop_table('role')
    op.drop_index(op.f('ix_preview_addtime'), table_name='preview')
    op.drop_table('preview')
    op.drop_index(op.f('ix_auth_addtime'), table_name='auth')
    op.drop_table('auth')
    # ### end Alembic commands ###
