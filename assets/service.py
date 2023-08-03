import sqlalchemy.dialects.mysql as mysql_sa
from sqlalchemy import func
from sqlalchemy.orm import Session

from assets.models import Asset


def create(*, db_session: Session, assets_in):
    db_session.bulk_insert_mappings(Asset, assets_in)
    db_session.commit()


def create_or_update(*, db_session: Session, assets_in):
    stmt = (
        mysql_sa.insert(Asset)
        .values(assets_in)
    )

    update_stmt = stmt.on_duplicate_key_update(
        updated_at=func.current_timestamp()
    )

    db_session.execute(update_stmt)
    db_session.commit()
