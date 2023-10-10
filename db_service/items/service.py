import sqlalchemy as sa
import sqlalchemy.dialects.mysql as mysql_sa
from sqlalchemy.orm import Session, joinedload
from sqlalchemy import func
from db_service.items.schema import Item


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





def get_classid_by_market_hash_name(*, db_session: Session, market_hash_name: str) -> str | None:
    stmt = (
        sa.select(Item.classid)
        .where(Item.market_hash_name == market_hash_name)
    )
    result = db_session.execute(stmt).scalar()
    return result


def create_if_not_exist(*, db_session: Session, item_in: dict):
    if not exists(db_session=db_session, classid=item_in["classid"]):
        create(
            db_session=db_session,
            item_in=item_in
        )