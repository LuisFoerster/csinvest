import sqlalchemy as sa
import sqlalchemy.dialects.mysql as mysql_sa
from sqlalchemy.orm import Session, joinedload
from sqlalchemy import func
from assets.models import Asset
from database.session import get_session


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




