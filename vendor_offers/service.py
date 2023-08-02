from sqlalchemy import func
from sqlalchemy.orm import Session

from vendor_offers.models import VendorOffer
import sqlalchemy.dialects.mysql as mysql_sa


def create(*, db_session: Session, item_in):
    db_session.bulk_insert_mappings(VendorOffer, item_in)
    db_session.commit()


def create_or_update(*, db_session: Session, data: dict):
    stmt = (
        mysql_sa.insert(VendorOffer)
        .values(**data)
        .on_duplicate_key_update(
            **data,
            updated_at=func.current_timestamp(),
        )
    )
    db_session.execute(stmt)
    db_session.commit()
