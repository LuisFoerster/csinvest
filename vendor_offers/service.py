import sqlalchemy as sa
from sqlalchemy.orm import Session, joinedload

from vendor_offers.models import VendorOffer



def create(*, db_session: Session, item_in) -> VendorOffer:
    db_session.bulk_insert_mappings(VendorOffer, item_in)
    db_session.commit()


# def get(*, db_session: Session, market_hash_name):
#     stmt = (
#         sa.select(Item, Price)
#         .join(Price)
#         .where(Item.market_hash_name == market_hash_name)
#     )
#     result = db_session.execute(stmt).fetchone()
#     return {**result.Item.__dict__, **result.Price.__dict__}
