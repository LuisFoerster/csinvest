from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database.session import get_session
from items.models import ItemWithVendorOffers
import items.service as items_service

router = APIRouter()


@router.get("/get/{market_hash_name}", response_model=ItemWithVendorOffers)
async def get_item(market_hash_name: str, db_session: Session = Depends(get_session)):
    result = items_service.get_with_vendor_offers(db_session=db_session, market_hash_name=market_hash_name)
    print(result)
    return result
