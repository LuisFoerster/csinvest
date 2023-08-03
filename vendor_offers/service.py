from sqlalchemy import func
from sqlalchemy.orm import Session

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

# def create_or_update(*, db_session: Session, offer_in: dict):
#
#     stmt = (
#         mysql_sa.insert(VendorOffer)
#         .values(offer_in)
#
#     )
#
#     update_stmt = stmt.on_duplicate_key_update(
#         classid = stmt.inserted.classid,
#         lowest_price = stmt.inserted.lowest_price,
#         median_price = stmt.inserted.median_price,
#         sell_listings = stmt.inserted.sell_listings,
#         affiliate_link = stmt.inserted.affiliate_link,
#         updated_at = func.current_timestamp()
#     ).where(VendorOffer.vendorid == 2)
#
#     db_session.execute(update_stmt)
#     db_session.commit()
