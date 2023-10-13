import sqlalchemy as sa
import sqlalchemy.dialects.postgresql as postgres_sa
from sqlalchemy import func, desc
from sqlalchemy.orm import Session

from db_service.vendor_offers.schema import VendorOffer


# CREATE

def create(*, db_session: Session, item_in):
    db_session.bulk_insert_mappings(VendorOffer, item_in)
    db_session.commit()


def upsert(*, db_session: Session, offers_in: list[dict]):
    stmt = (
        postgres_sa.insert(VendorOffer)
        .values(offers_in)
    )

    update_stmt = stmt.on_conflict_do_update(
            constraint="unique_class_and_vendor_id",
            #index_elements=['vendorid'],  # Replace with your unique constraint or primary key
            set_={
                'lowest_price': stmt.excluded.lowest_price,
                'median_price': stmt.excluded.median_price,
                'sell_listings': stmt.excluded.sell_listings,
                'affiliate_link': stmt.excluded.affiliate_link,
                'updated_at': func.current_timestamp()
            }
        )

    db_session.execute(update_stmt)
    db_session.commit()

    db_session.execute(update_stmt)
    db_session.commit()


def upsert_without_sell_listings(*, db_session: Session, offers_in: list[dict]):
    stmt = (
        postgres_sa.insert(VendorOffer)
        .values(offers_in)
    )

    update_stmt = stmt.on_conflict_do_update(
        constraint='unique_class_and_vendor_id',
        #index_elements=['id'],
        set_={
            'vendorid':stmt.excluded.vendorid,
            'lowest_price': stmt.excluded.lowest_price,
            'median_price': stmt.excluded.median_price,
            'affiliate_link': stmt.excluded.affiliate_link,
            'updated_at': func.current_timestamp(),

        }
    )

    db_session.execute(update_stmt)
    db_session.commit()


# READ

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


def get_current_price(*, db_session: Session, classid: str, vendorid: int):
    stmt = (
        sa.select(VendorOffer)
        .where(VendorOffer.classid == classid)
        .where(VendorOffer.vendorid == vendorid)
    )
    result = db_session.execute(stmt).scalar()
    return result.lowest_price
