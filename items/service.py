import sqlalchemy as sa
import sqlalchemy.dialects.mysql as mysql_sa
from sqlalchemy.orm import Session, joinedload
from sqlalchemy import func
from items.models import Item


def create(*, db_session: Session, item_in):
    db_session.bulk_insert_mappings(Item, item_in)
    db_session.commit()


def create_or_skip(*, db_session: Session, data: dict):
    stmt = (
        mysql_sa.insert(Item)
        .values(data)
        .on_duplicate_key_update(updated_at= func.current_timestamp()
                                 )
    )
    db_session.execute(stmt)
    db_session.commit()


def get_with_vendor_offers(*, db_session: Session, market_hash_name):
    stmt = (
        sa.select(Item)
        .where(Item.market_hash_name == market_hash_name)
        .options(joinedload(Item.vendor_offers))
    )
    result = db_session.execute(stmt).unique().fetchone()


    return result.Item.__dict__

def get_classid_by_market_hash_name(*, db_session: Session, market_hash_name: str)-> str:
    stmt = (
        sa.select(Item)
        .where(Item.market_hash_name == market_hash_name)
    )
    result = db_session.execute(stmt).scalar()
    return result