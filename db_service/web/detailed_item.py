import sqlalchemy as sa
from sqlalchemy.orm import Session, joinedload
from datetime import datetime


# Import db_services
from db_service.items.schema import Item
from db_service.asset_stacks.schema import AssetStack
from db_service.vendor_offers.schema import VendorOffer
from db_service.price_histories.schema import HistoryListing


def get_one_shop_item(*, db_session: Session, market_hash_name):
    stmt = (
        sa.select(Item)
        .where(Item.market_hash_name == market_hash_name)
        .join(Item.vendor_offers)
    )
    result = db_session.execute(stmt).scalar()

    return result