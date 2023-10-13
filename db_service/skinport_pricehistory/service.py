import sqlalchemy as sa
from sqlalchemy import func
from sqlalchemy.orm import Session

from db_service import SkinportPricehistory


def create(*, db_session: Session, data_in):
    stmt = sa.insert(SkinportPricehistory).values(data_in)
    db_session.execute(stmt)
    db_session.commit()


def get_total_market_price_volume_over_90_days(*, db_session: Session):
    aggregated_func = func.sum(SkinportPricehistory.volume * SkinportPricehistory.avg_price).label(
        "total_item_price_volume")

    stmt = sa.select(aggregated_func)

    result = db_session.execute(stmt).scalar()
    return result
