import sqlalchemy as sa
import sqlalchemy.dialects.postgresql as postgres_sa
from sqlalchemy import func
from sqlalchemy.orm import Session

from db_service.items.schema import Item


def create(*, db_session: Session, item_in):
    stmt = sa.insert(Item).values(item_in)
    db_session.execute(stmt)
    db_session.commit()


def upsert(*, db_session: Session, items_in: list[dict]):
    stmt = (
        postgres_sa.insert(Item)
        .values(items_in)
        .on_conflict_do_update(
            index_elements=['classid'],
            set_={
                'updated_at': func.current_timestamp()
            }
        )
    )
    db_session.execute(stmt)
    db_session.commit()


def create_if_not_exist(*, db_session: Session, item_in: dict):
    stmt = (
        postgres_sa.insert(Item)
        .values(item_in)
        .on_conflict_do_nothing(index_elements=['classid'])
    )

    db_session.execute(stmt)
    db_session.commit()


# GET

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


def get_classids_by_name(*, db_session: Session, name: str) -> str | None:
    stmt = (
        sa.select(Item.classid)
        .where(Item.name.like(f"%{name}%"))
    )
    result = db_session.execute(stmt).scalars().all()
    return result


def get_by_type(*, db_session: Session, type: str):
    stmt = (
        sa.select(Item)
        .where(Item.type == type)
    )
    result = db_session.execute(stmt).scalars().all()
    return result


def get_items_by_collection(*, db_session: Session, collection: str):
    """
        returns all items not containers
    """
    stmt = (
        sa.select(Item)
        .where(Item.collection == collection)
        .where(Item.type != "Container")
    )
    result = db_session.execute(stmt).scalars().all()
    return result
