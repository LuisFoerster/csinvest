import sqlalchemy as sa
from sqlalchemy import func
from sqlalchemy.orm import Session
from datetime import datetime
from typing import List

# Import db_services
from db_service.items.schema import Item
from db_service.vendor_offers.schema import VendorOffer


def get_shop_items(*, db_session: Session,
                   skip: int,
                   limit: int,
                   q: str | None,
                   type: list[str] | None,
                   exterior: list[str] | None,
                   quality: list[str] | None,
                   category: list[str] | None,
                   weapon_type: list[str] | None,
                   collection: list[str] | None,
                   min_price: float | None,
                   max_price: float | None,
                   min_release_year: int | None,
                   max_release_year: int | None,
                   just_return_match_count: bool ,
                   ):

    agr_func = func.count(Item.classid).label("items_found")
    def apply_filters(stmt):

        if q:
            stmt = stmt.where(Item.market_hash_name.like(f"%{q}%"))
        if type:
            stmt = stmt.where(Item.type.in_(type))
        if weapon_type:
            stmt = stmt.where(Item.weapon_type.in_(weapon_type))
        if exterior:
            stmt = stmt.where(Item.exterior.in_(exterior))
        if quality:
            stmt = stmt.where(Item.quality.in_(quality))
        if category:
            stmt = stmt.where(Item.categorie.in_(category))
        if collection:
            stmt = stmt.where(Item.collection.in_(collection))
        if min_price:
            stmt = stmt.where(VendorOffer.lowest_price >= min_price)
        if max_price:
            stmt = stmt.where(VendorOffer.lowest_price <= max_price)
        if min_release_year:
            stmt = stmt.where(Item.release_year >= datetime(min_release_year, 1, 1))
        if max_release_year:
            stmt = stmt.where(Item.release_year <= datetime(max_release_year, 1, 1))
        return stmt




    if just_return_match_count is False:
        stmt = (sa.select(Item)
                .join(Item.vendor_offers)
                .offset(skip)
                .limit(limit)
                .distinct())

        stmt = apply_filters(stmt)
        items = db_session.execute(stmt).scalars().all()
        item_count = None
    else:
        stmt = (sa.select(agr_func)
                .distinct())
        stmt = apply_filters(stmt)
        item_count = db_session.execute(stmt).scalar()
        items = None

    return item_count, items


