import sqlalchemy as sa
from sqlalchemy.orm import Session, joinedload
from datetime import datetime


# Import db_services
from db_service.items.schema import Item
from db_service.asset_stacks.schema import AssetStack
from db_service.vendor_offers.schema import VendorOffer
from db_service.price_histories.schema import HistoryListing


def get_shop_items(*, db_session: Session,
                   skip:int ,
                   limit:int,
                   q:str | None,
                   type: str | None,
                   condition: str | None,
                   extra: str | None,
                   rarity: str | None,
                   min_price: float | None,
                   max_price: float | None,
                   min_release_year: datetime | None,
                   max_release_year: datetime | None):



    stmt = (
        sa.select(Item)
            .join(Item.vendor_offers)
            .offset(skip)
            .limit(limit)
            .distinct()
    )




    if q:
        stmt = stmt.where(Item.market_hash_name.like(f"%{q}%"))
    if type:
        stmt = stmt.where(Item.type.like(f"%{type}%"))
    if condition:
        stmt = stmt.where(Item.market_hash_name.like(f"%{condition}%"))
    if extra:
        stmt = stmt.where(Item.market_hash_name.like(f"%{extra}%"))
    if rarity:
        stmt = stmt.where(Item.type.like(f"%{rarity}%"))
    if min_price:
        stmt = stmt.where(VendorOffer.lowest_price >= min_price)
        pass
    if max_price:
        stmt = stmt.where(VendorOffer.lowest_price <= max_price)
        pass
    if min_release_year:
        pass # TODO: implement
    if max_release_year:
        pass  # TODO: implement


    result = db_session.execute(stmt).scalars().all()
    print(result)
    return result
