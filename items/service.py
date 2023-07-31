import sqlalchemy as sa
from sqlalchemy.orm import Session, joinedload

from items.models import Item, ItemBase
from prices.models import Price


def create(*, db_session: Session, item_in) -> Item:
    db_session.bulk_insert_mappings(Item, item_in)
    db_session.commit()


def get(*, db_session: Session, market_hash_name):
    stmt = (
        sa.select(Item, Price)
        .join(Price)
        .where(Item.market_hash_name == market_hash_name)
    )
    result = db_session.execute(stmt).fetchone()
    return {**result.Item.__dict__, **result.Price.__dict__}
