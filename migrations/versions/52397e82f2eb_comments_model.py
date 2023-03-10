"""Comments model

Revision ID: 52397e82f2eb
Revises: 56316719682f
Create Date: 2023-02-10 13:42:15.683488

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '52397e82f2eb'
down_revision = '56316719682f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('comment', schema=None) as batch_op:
        batch_op.add_column(sa.Column('news_id', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('user_id', sa.Integer(), nullable=True))
        batch_op.alter_column('text',
               existing_type=sa.TEXT(),
               nullable=False)
        batch_op.create_index(batch_op.f('ix_comment_news_id'), ['news_id'], unique=False)
        batch_op.create_index(batch_op.f('ix_comment_user_id'), ['user_id'], unique=False)
        batch_op.create_foreign_key(None, 'user', ['user_id'], ['id'], ondelete='CASCADE')
        batch_op.create_foreign_key(None, 'news', ['news_id'], ['id'], ondelete='CASCADE')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('comment', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_index(batch_op.f('ix_comment_user_id'))
        batch_op.drop_index(batch_op.f('ix_comment_news_id'))
        batch_op.alter_column('text',
               existing_type=sa.TEXT(),
               nullable=True)
        batch_op.drop_column('user_id')
        batch_op.drop_column('news_id')

    # ### end Alembic commands ###
