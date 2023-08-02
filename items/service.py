import sqlalchemy as sa
from sqlalchemy.orm import Session, joinedload

from items.models import Item, ItemBase
from vendor_offers.models import VendorOffer



def create(*, db_session: Session, item_in):
    db_session.bulk_insert_mappings(Item, item_in)
    db_session.commit()

def create_and_upadte_if_existing():
    pass
def get_with_vendor_offers(*, db_session: Session, market_hash_name):
    stmt = (
        sa.select(Item, VendorOffer)
        .join(VendorOffer)
        .where(Item.market_hash_name == market_hash_name)
    )
    result = db_session.execute(stmt).fetchone()
    return result#{**result.Item.__dict__, **result.VendorOffer.__dict__}
