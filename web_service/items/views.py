from typing import Optional

from fastapi import APIRouter, Depends, Query
from sqlalchemy import select
from sqlalchemy.orm import Session

import db_service.items.service as items_service
from db_service.migrations import get_session
from db_service.items.schema import ItemWithVendorOffers, Item
from db_service.vendor_offers.schema import VendorOffer

router = APIRouter()


@router.get("/get/{market_hash_name}", response_model=ItemWithVendorOffers)
async def get_item(market_hash_name: str, db_session: Session = Depends(get_session)):
    result = items_service.get_with_vendor_offers(db_session=db_session, market_hash_name=market_hash_name)
    print(result)
    return result


@router.get("/search/")
async def search(
        q: Optional[str] = Query(None, description="Search query"),
        rarity: Optional[str] = Query(None, description="Rarity filter"),
        discontinued: Optional[bool] = Query(None, description="Discontinued filter"),
        min_price: Optional[float] = Query(None, description="Minimum price"),
        max_price: Optional[float] = Query(None, description="Maximum price"),
        min_year: Optional[int] = Query(None, description="Minimum release year"),
        max_year: Optional[int] = Query(None, description="Maximum release year"),
        db_session: Session = Depends(get_session)):

    stmt = (select(Item.market_hash_name,Item.icon_url, VendorOffer.lowest_price).
            join(VendorOffer, VendorOffer.classid == Item.classid and VendorOffer.vendorid == 1))
    if q:
        stmt = stmt.where(Item.market_hash_name.like(f"%{q}%"))
    if rarity:
        pass  # TODO: implement
    if discontinued:
        pass  # TODO: implement
    if min_price:
        stmt = stmt.where(VendorOffer.lowest_price > min_price)
        pass
    if max_price:
        stmt = stmt.where(VendorOffer.lowest_price < max_price)
        pass
    if min_year:
        pass # TODO: implement
    if max_year:
        pass  # TODO: implement
    result = db_session.execute(stmt).fetchall()
    items = [r._asdict() for r in result]
    return items
