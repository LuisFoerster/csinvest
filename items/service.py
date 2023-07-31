import sqlalchemy as sa
from sqlalchemy.orm import Session, joinedload

from items.models import Item
from prices.models import Price


def create(*, db_session: Session, item_in) -> Item:
    db_session.bulk_insert_mappings(Item, item_in)
    db_session.commit()

def get(*, db_session: Session, market_hash_name) -> Item:
    stmt = sa.select(Item).where(Item.market_hash_name == market_hash_name).options(joinedload(Item.prices))
    response = db_session.execute(stmt).scalar()
    print(str(stmt))
    return response