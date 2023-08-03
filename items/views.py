from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

import items.service as items_service
from database.session import get_session
from items.models import ItemWithVendorOffers

router = APIRouter()


@router.get("/get/{market_hash_name}", response_model=ItemWithVendorOffers)
async def get_item(market_hash_name: str, db_session: Session = Depends(get_session)):
    result = items_service.get_with_vendor_offers(db_session=db_session, market_hash_name=market_hash_name)
    print(result)
    return result
