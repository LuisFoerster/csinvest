import sqlalchemy as sa
import sqlalchemy.dialects.mysql as mysql_sa
from sqlalchemy.orm import Session, joinedload
from sqlalchemy import func
from items.models import Item


def create(*, db_session: Session, item_in):
    stmt = sa.insert(Item).values(item_in)
    db_session.execute(stmt)
    db_session.commit()


def create_or_skip(*, db_session: Session, items_in: list[dict]):
    stmt = (
        mysql_sa.insert(Item)
        .values(items_in)
        .on_duplicate_key_update(updated_at=func.current_timestamp())
    )
    db_session.execute(stmt)
    db_session.commit()


def exists(*, db_session: Session, classid) -> bool:
    if classid is None:
        return False

    stmt = (
        sa.select(Item)
        .where(Item.classid == classid)
    )

    return db_session.execute(stmt).scalar() is not None


def get_with_vendor_offers(*, db_session: Session, market_hash_name):
    stmt = (
        sa.select(Item)
        .where(Item.market_hash_name == market_hash_name)
        .options(joinedload(Item.vendor_offers))
    )
    result = db_session.execute(stmt).unique().fetchone()

    return result.Item.__dict__


def get_classid_by_market_hash_name(*, db_session: Session, market_hash_name: str) -> str:
    stmt = (
        sa.select(Item)
        .where(Item.market_hash_name == market_hash_name)
    )
    result = db_session.execute(stmt).scalar()
    return result

