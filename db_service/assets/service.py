from datetime import datetime

import sqlalchemy as sa
import sqlalchemy.dialects.postgresql as postgres_sa
from sqlalchemy import func, desc
from sqlalchemy.orm import Session

from db_service.assets.schema import Asset


def create(*, db_session: Session, assets_in):
    db_session.bulk_insert_mappings(Asset, assets_in)
    db_session.commit()


def upsert(*, db_session: Session, assets_in):
    stmt = (
        postgres_sa.insert(Asset)
        .values(assets_in)
        .on_conflict_do_update(
            index_elements=['assetid'],
            set_={
                'updated_at': func.current_timestamp()
            }
        )
    )

    db_session.execute(stmt)
    db_session.commit()


def get_timestamp_of_last_update(*, db_session: Session, steamid: str):
    stmt = (
        sa.select(Asset)
        .where(Asset.steamid == steamid)
        .order_by(desc(Asset.updated_at)).limit(1)
    )
    result = db_session.execute(stmt).scalar()
    if result is None:
        return
    return result.updated_at


def get_by_classid(*, db_session: Session, steamid: str, classid: str, ):
    stmt = (
        sa.select(Asset)
        .where(Asset.asset_stackid)
    )
    result = db_session.execute(stmt).scalar()
    return result


def delete_stale(*, db_session: Session, steamid: str, previous_update_timestamp: datetime):
    if previous_update_timestamp is None:
        return

    stmt = (
        sa.delete(Asset)
        .where(Asset.steamid == steamid)
        .where(Asset.updated_at <= previous_update_timestamp)
    )
    db_session.execute(stmt)
    db_session.commit()
