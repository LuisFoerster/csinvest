from sqlalchemy.orm import Session

from vendor_offers.models import VendorOffer


def create(*, db_session: Session, item_in):
    db_session.bulk_insert_mappings(VendorOffer, item_in)
    db_session.commit()