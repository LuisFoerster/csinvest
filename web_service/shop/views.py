from datetime import datetime

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

import db_service.web.shop as shop_db_service
from db_service.session import get_session
from web_service.shop.models import PaginatedShopItems

router = APIRouter()


# @router.get("/get/{market_hash_name}", response_model=ItemWithVendorOffers)
# async def get_item(market_hash_name: str, db_session: Session = Depends(get_session)):
#     result = items_service.get_with_vendor_offers(db_session=db_session, market_hash_name=market_hash_name)
#     print(result)
#     return result
#
@router.get("/", response_model=PaginatedShopItems)
async def get_item(skip: int = 0, limit: int = 100, q: str = None,
                   type: str = None, condition: str = None,
                   extra: str = None,
                   rarity: str = None, min_price: float = None,
                   max_price: float = None, min_release_year: datetime = None,
                   max_release_year: datetime = None,
                   db_session: Session = Depends(get_session)):
    result = shop_db_service.get_shop_items(db_session=db_session, skip=skip, limit=limit, q=q, type=type,
                                            condition=condition, extra=extra, rarity=rarity, min_price=min_price,
                                            max_price=max_price,
                                            min_release_year=min_release_year, max_release_year=max_release_year)
    return PaginatedShopItems(skip=skip, limit=limit, itemsWithVendorOffers=result)

# @router.get("/search/")
# async def search(
#         q: Optional[str] = Query(None, description="Search query"),
#         rarity: Optional[str] = Query(None, description="Rarity filter"),
#         discontinued: Optional[bool] = Query(None, description="Discontinued filter"),
#         min_price: Optional[float] = Query(None, description="Minimum price"),
#         max_price: Optional[float] = Query(None, description="Maximum price"),
#         min_year: Optional[int] = Query(None, description="Minimum release year"),
#         max_year: Optional[int] = Query(None, description="Maximum release year"),
#         db_session: Session = Depends(get_session)):
#
