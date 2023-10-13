import sqlalchemy as sa
import sqlalchemy.dialects.postgresql as postgres_sa
from sqlalchemy import func
from sqlalchemy.orm import Session

from db_service.price_histories.schema import HistoryListing


def create(*, db_session: Session, history_listing_in):
    stmt = sa.insert(HistoryListing).values(history_listing_in)
    db_session.execute(stmt)
    db_session.commit()


def upsert(*, db_session: Session, history_listing_in):
    stmt = (
        postgres_sa.insert(HistoryListing)
        .values(history_listing_in)
    )

    update_stmt = stmt.on_conflict_do_update(
        constraint='unique_class_and_vendor_id_and_time_stamp',
        #index_elements=['id'],
        set_={
            'volume': stmt.excluded.volume,
            'price': stmt.excluded.volume,
            'updated_at': func.current_timestamp(),
        }
    )

    db_session.execute(update_stmt)
    db_session.commit()


def get_total_item_price_volume_over_timespan(*, db_session: Session, classid: str, time_from, time_to):
    aggregated_func = func.sum(HistoryListing.volume * HistoryListing.price).label("total_item_price_volume")

    stmt = sa.select(aggregated_func). \
        where(HistoryListing.time_stamp <= time_to). \
        where(HistoryListing.time_stamp >= time_from). \
        where(HistoryListing.classid == classid)

    result = db_session.execute(stmt).scalar()
    return result


def get_total_market_price_volume_over_timespan(*, db_session: Session, time_from, time_to):
    aggregated_func = func.sum(HistoryListing.volume * HistoryListing.price).label("total_item_price_volume")

    stmt = sa.select(aggregated_func). \
        where(HistoryListing.time_stamp <= time_to). \
        where(HistoryListing.time_stamp >= time_from)

    result = db_session.execute(stmt).scalar()
    return result
