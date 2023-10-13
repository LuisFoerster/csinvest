import sqlalchemy as sa
from sqlalchemy.orm import Session

# Import db_services
from db_service import Item


def get_one_shop_item(*, db_session: Session, market_hash_name):
    stmt = (
        sa.select(Item)
        .where(Item.market_hash_name == market_hash_name)
        .join(Item.vendor_offers)
    )
    result = db_session.execute(stmt).scalar()

    return result
