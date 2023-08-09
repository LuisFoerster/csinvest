from sqlalchemy import func, desc
from sqlalchemy.orm import Session
import sqlalchemy as sa

from vendor_offers.models import VendorOffer
import sqlalchemy.dialects.mysql as mysql_sa


def create(*, db_session: Session, item_in):
    db_session.bulk_insert_mappings(VendorOffer, item_in)
    db_session.commit()


def create_or_update(*, db_session: Session, offers_in: list[dict]):
    stmt = (
        mysql_sa.insert(VendorOffer)
        .values(offers_in)

    )

    update_stmt = stmt.on_duplicate_key_update(
        vendorid=stmt.inserted.vendorid,
        lowest_price=stmt.inserted.lowest_price,
        median_price=stmt.inserted.median_price,
        sell_listings=stmt.inserted.sell_listings,
        affiliate_link=stmt.inserted.affiliate_link,
        updated_at=func.current_timestamp()
    )

    db_session.execute(update_stmt)
    db_session.commit()

def create_or_update_without_sell_listings(*, db_session: Session, offers_in: list[dict]):
    stmt = (
        mysql_sa.insert(VendorOffer)
        .values(offers_in)

    )

    update_stmt = stmt.on_duplicate_key_update(
        vendorid=stmt.inserted.vendorid,
        lowest_price=stmt.inserted.lowest_price,
        median_price=stmt.inserted.median_price,
        affiliate_link=stmt.inserted.affiliate_link,
        updated_at=func.current_timestamp()
    )

    db_session.execute(update_stmt)
    db_session.commit()


def get_update_timestamp(*, db_session: Session, classid: str, vendorid: int):
    stmt = (
        sa.select(VendorOffer)
        .where(VendorOffer.classid == classid)
        .where(VendorOffer.vendorid == vendorid)
        .order_by(desc(VendorOffer.updated_at)).limit(1)
    )
    result = db_session.execute(stmt).scalar()
    if result is None:
        return
    return result.updated_at


def exists(*, db_session: Session, classid: str, vendorid: int):
    stmt = (
        sa.select(VendorOffer)
        .where(VendorOffer.classid == classid)
        .where(VendorOffer.vendorid == vendorid)
    )
    result = db_session.execute(stmt).scalar()
    return result