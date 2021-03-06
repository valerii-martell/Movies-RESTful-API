"""empty message

Revision ID: 83486b3ad29b
Revises: df8d6424defd
Create Date: 2022-07-08 13:13:43.411163

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '83486b3ad29b'
down_revision = 'df8d6424defd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('actors',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('birthday', sa.Date(), nullable=True),
    sa.Column('is_active', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name'),
    schema='ActorSchema'
    )
    op.create_table('movies',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(), nullable=False),
    sa.Column('release_date', sa.Date(), nullable=False),
    sa.Column('uuid', sa.String(length=36), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('distributed_by', sa.String(length=128), nullable=False),
    sa.Column('length', sa.Float(), nullable=True),
    sa.Column('rating', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('uuid'),
    schema='MovieSchema'
    )
    op.create_index(op.f('ix_MovieSchema_movies_release_date'), 'movies', ['release_date'], unique=False, schema='MovieSchema')
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=50), nullable=False),
    sa.Column('email', sa.String(length=50), nullable=False),
    sa.Column('password', sa.String(length=254), nullable=False),
    sa.Column('is_admin', sa.Boolean(), nullable=True),
    sa.Column('uuid', sa.String(length=36), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username'),
    sa.UniqueConstraint('uuid'),
    schema='UserSchema'
    )
    op.drop_index('ix_movies_release_date', table_name='movies')
    op.drop_table('movies')
    op.drop_table('users')
    op.drop_table('actors')
    op.drop_constraint(None, 'movies_actors', type_='foreignkey')
    op.drop_constraint(None, 'movies_actors', type_='foreignkey')
    op.create_foreign_key(None, 'movies_actors', 'movies', ['movie_id'], ['id'], referent_schema='MovieSchema')
    op.create_foreign_key(None, 'movies_actors', 'actors', ['actor_id'], ['id'], referent_schema='ActorSchema')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'movies_actors', type_='foreignkey')
    op.drop_constraint(None, 'movies_actors', type_='foreignkey')
    op.create_foreign_key(None, 'movies_actors', 'actors', ['actor_id'], ['id'])
    op.create_foreign_key(None, 'movies_actors', 'movies', ['movie_id'], ['id'])
    op.create_table('actors',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.VARCHAR(length=50), nullable=False),
    sa.Column('birthday', sa.DATE(), nullable=True),
    sa.Column('is_active', sa.BOOLEAN(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('users',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('username', sa.VARCHAR(length=50), nullable=False),
    sa.Column('email', sa.VARCHAR(length=50), nullable=False),
    sa.Column('password', sa.VARCHAR(length=254), nullable=False),
    sa.Column('is_admin', sa.BOOLEAN(), nullable=True),
    sa.Column('uuid', sa.VARCHAR(length=36), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username'),
    sa.UniqueConstraint('uuid')
    )
    op.create_table('movies',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('title', sa.VARCHAR(), nullable=False),
    sa.Column('release_date', sa.DATE(), nullable=False),
    sa.Column('uuid', sa.VARCHAR(length=36), nullable=True),
    sa.Column('description', sa.TEXT(), nullable=True),
    sa.Column('distributed_by', sa.VARCHAR(length=128), nullable=False),
    sa.Column('length', sa.FLOAT(), nullable=True),
    sa.Column('rating', sa.FLOAT(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('uuid')
    )
    op.create_index('ix_movies_release_date', 'movies', ['release_date'], unique=False)
    op.drop_table('users', schema='UserSchema')
    op.drop_index(op.f('ix_MovieSchema_movies_release_date'), table_name='movies', schema='MovieSchema')
    op.drop_table('movies', schema='MovieSchema')
    op.drop_table('actors', schema='ActorSchema')
    # ### end Alembic commands ###
