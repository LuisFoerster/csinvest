"""init

Revision ID: 85c9ba82c475
Revises: 
Create Date: 2023-10-13 12:07:04.584668

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '85c9ba82c475'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('accounts',
    sa.Column('steamid', sa.String(length=64), nullable=False),
    sa.Column('personame', sa.Text(), nullable=True),
    sa.Column('avatar', sa.Text(), nullable=True),
    sa.Column('avatarmedium', sa.Text(), nullable=True),
    sa.Column('avatarfull', sa.Text(), nullable=True),
    sa.Column('updated_at', postgresql.TIMESTAMP(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=True),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=True),
    sa.PrimaryKeyConstraint('steamid')
    )
    op.create_table('items',
    sa.Column('classid', sa.String(length=64), nullable=False),
    sa.Column('market_hash_name', sa.Text(), nullable=True),
    sa.Column('item_nameid', sa.String(length=64), nullable=True),
    sa.Column('name', sa.Text(), nullable=True),
    sa.Column('name_spezifier', sa.Text(), nullable=True),
    sa.Column('exterior', sa.Text(), nullable=True),
    sa.Column('quality', sa.Text(), nullable=True),
    sa.Column('categorie', sa.Text(), nullable=True),
    sa.Column('type', sa.Text(), nullable=True),
    sa.Column('weapon_type', sa.Text(), nullable=True),
    sa.Column('sticker_type', sa.Text(), nullable=True),
    sa.Column('graffiti_type', sa.Text(), nullable=True),
    sa.Column('patch_type', sa.Text(), nullable=True),
    sa.Column('collection', sa.Text(), nullable=True),
    sa.Column('professional_player', sa.Text(), nullable=True),
    sa.Column('tournament', sa.Text(), nullable=True),
    sa.Column('team', sa.Text(), nullable=True),
    sa.Column('min_float', sa.Float(), nullable=True),
    sa.Column('max_float', sa.Float(), nullable=True),
    sa.Column('droppool', sa.Text(), nullable=True),
    sa.Column('release_year', sa.DateTime(), nullable=True),
    sa.Column('appid', sa.Integer(), nullable=True),
    sa.Column('icon_url', sa.Text(), nullable=True),
    sa.Column('background_color', sa.String(length=64), nullable=True),
    sa.Column('name_color', sa.String(length=64), nullable=True),
    sa.Column('updated_at', postgresql.TIMESTAMP(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=True),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=True),
    sa.PrimaryKeyConstraint('classid')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('username', sa.Text(), nullable=True),
    sa.Column('role', sa.String(length=32), nullable=True),
    sa.Column('last_login', sa.DateTime(), nullable=True),
    sa.Column('updated_at', postgresql.TIMESTAMP(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=True),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('username')
    )
    op.create_table('vendors',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.Text(), nullable=True),
    sa.Column('provision', sa.Float(), nullable=True),
    sa.Column('icon_url', sa.Text(), nullable=True),
    sa.Column('updated_at', postgresql.TIMESTAMP(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=True),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('assetstacks',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('classid', sa.String(length=64), nullable=True),
    sa.Column('steamid', sa.String(length=64), nullable=True),
    sa.Column('buyin', sa.Float(), nullable=True),
    sa.Column('virtual', sa.Boolean(), nullable=True),
    sa.Column('virtual_size', sa.Integer(), nullable=True),
    sa.Column('updated_at', postgresql.TIMESTAMP(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=True),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=True),
    sa.ForeignKeyConstraint(['classid'], ['items.classid'], ),
    sa.ForeignKeyConstraint(['steamid'], ['accounts.steamid'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('container_contents',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('container_classid', sa.String(length=64), nullable=True),
    sa.Column('content_classid', sa.String(length=64), nullable=True),
    sa.Column('updated_at', postgresql.TIMESTAMP(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=True),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=True),
    sa.ForeignKeyConstraint(['container_classid'], ['items.classid'], ),
    sa.ForeignKeyConstraint(['content_classid'], ['items.classid'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('container_classid', 'content_classid', name='unique_relation')
    )
    op.create_table('pricehistories',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('classid', sa.String(length=64), nullable=True),
    sa.Column('vendorid', sa.Integer(), nullable=True),
    sa.Column('time_stamp', sa.DateTime(), nullable=True),
    sa.Column('volume', sa.Integer(), nullable=True),
    sa.Column('price', sa.Float(), nullable=True),
    sa.Column('updated_at', postgresql.TIMESTAMP(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=True),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=True),
    sa.ForeignKeyConstraint(['classid'], ['items.classid'], ),
    sa.ForeignKeyConstraint(['vendorid'], ['vendors.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('classid', 'vendorid', 'time_stamp', name='unique_class_and_vendor_id_and_time_stamp')
    )
    op.create_table('skinport_pricehistories',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('classid', sa.String(length=64), nullable=True),
    sa.Column('avg_price', sa.Float(), nullable=True),
    sa.Column('volume', sa.Integer(), nullable=True),
    sa.Column('updated_at', postgresql.TIMESTAMP(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=True),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=True),
    sa.ForeignKeyConstraint(['classid'], ['items.classid'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('statistics',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('classid', sa.String(length=64), nullable=True),
    sa.Column('return_of_investment', sa.Float(), nullable=True),
    sa.Column('updated_at', postgresql.TIMESTAMP(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=True),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=True),
    sa.ForeignKeyConstraint(['classid'], ['items.classid'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('vendor_offers',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('classid', sa.String(length=64), nullable=True),
    sa.Column('vendorid', sa.Integer(), nullable=True),
    sa.Column('affiliate_link', sa.Text(), nullable=True),
    sa.Column('lowest_price', sa.Float(), nullable=True),
    sa.Column('median_price', sa.Float(), nullable=True),
    sa.Column('sell_listings', sa.Integer(), nullable=True),
    sa.Column('updated_at', postgresql.TIMESTAMP(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=True),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=True),
    sa.ForeignKeyConstraint(['classid'], ['items.classid'], ),
    sa.ForeignKeyConstraint(['vendorid'], ['vendors.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('classid', 'vendorid', name='unique_class_and_vendor_id')
    )
    op.create_table('assets',
    sa.Column('assetid', sa.String(length=64), nullable=False),
    sa.Column('classid', sa.String(length=64), nullable=True),
    sa.Column('steamid', sa.String(length=64), nullable=True),
    sa.Column('asset_stackid', sa.Integer(), nullable=True),
    sa.Column('instanceid', sa.String(length=64), nullable=True),
    sa.Column('contextid', sa.String(length=64), nullable=True),
    sa.Column('updated_at', postgresql.TIMESTAMP(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=True),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=True),
    sa.ForeignKeyConstraint(['asset_stackid'], ['assetstacks.id'], ),
    sa.ForeignKeyConstraint(['classid'], ['items.classid'], ),
    sa.ForeignKeyConstraint(['steamid'], ['accounts.steamid'], ),
    sa.PrimaryKeyConstraint('assetid')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('assets')
    op.drop_table('vendor_offers')
    op.drop_table('statistics')
    op.drop_table('skinport_pricehistories')
    op.drop_table('pricehistories')
    op.drop_table('container_contents')
    op.drop_table('assetstacks')
    op.drop_table('vendors')
    op.drop_table('users')
    op.drop_table('items')
    op.drop_table('accounts')
    # ### end Alembic commands ###
