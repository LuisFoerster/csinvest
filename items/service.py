import sqlalchemy as sa
from sqlalchemy.orm import Session, joinedload

from items.models import Item


def create(*, db_session: Session, item_in):
    db_session.bulk_insert_mappings(Item, item_in)
    db_session.commit()


def get_with_vendor_offers(*, db_session: Session, market_hash_name):
    stmt = (
        sa.select(Item)
        .where(Item.market_hash_name == market_hash_name)
        .options(joinedload(Item.vendor_offers))
    )
    result = db_session.execute(stmt).unique().fetchone()
    return result.Item.__dict__
