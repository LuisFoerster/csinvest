from datetime import datetime

from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from typing import List
import web_service.shop.service as shop_db_service
from db_service.session import get_session
from web_service.shop.models import PaginatedShopItems

router = APIRouter()


# @router.get("/get/{market_hash_name}", response_model=ItemWithVendorOffers)
# async def get_item(market_hash_name: str, db_session: Session = Depends(get_session)):
#     result = items_service.get_with_vendor_offers(db_session=db_session, market_hash_name=market_hash_name)
#     print(result)
#     return result
#
@router.get("/")
async def get_item(skip: int = 0, limit: int = 100, q: str = None,
                   type: list[str] = Query(None),
                   exterior: list[str] = Query(None),
                   quality: list[str] = Query(None),
                   category: list[str] = Query(None),
                   weapon_type: list[str] = Query(None),
                   collection: list[str] = Query(None),
                   min_price: float = Query(None),
                   max_price: float = Query(None),
                   min_release_year: int = Query(None),
                   max_release_year: int = Query(None),
                   just_return_match_count : bool = Query(False),
                   db_session: Session = Depends(get_session)):


    item_count, items = shop_db_service.get_shop_items(db_session=db_session,
                                            skip=skip,
                                            limit=limit,
                                            q=q,
                                            type=type,
                                            exterior = exterior,
                                            quality = quality,
                                            category = category,
                                            weapon_type = weapon_type,
                                            collection = collection,
                                            min_price=min_price,
                                            max_price=max_price,
                                            min_release_year=min_release_year,
                                            max_release_year=max_release_year,
                                            just_return_match_count = just_return_match_count
                                            )


    return PaginatedShopItems(item_count=item_count,itemsWithVendorOffers=items)






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
