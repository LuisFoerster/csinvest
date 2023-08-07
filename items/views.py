from typing import Optional

from fastapi import APIRouter, Depends, Query
from sqlalchemy import select
from sqlalchemy.orm import Session

import items.service as items_service
from database.session import get_session
from items.models import ItemWithVendorOffers, Item
from vendor_offers.models import VendorOffer

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

    stmt = select(Item)
    if q:
        stmt = stmt.where(Item.market_hash_name.like(f"%{q}%"))
    if rarity:
        pass  # TODO: implement
    if discontinued:
        pass  # TODO: implement
    if min_price:
        # TODO: implement for differend vendors
        pass
    if max_price:
        # TODO: implement for differend vendors
        pass
    if min_year:
        pass # TODO: implement
    if max_year:
        pass  # TODO: implement
    result = db_session.execute(stmt).fetchall()
    return [r.Item.__dict__ for r in result]
