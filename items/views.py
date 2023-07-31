from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database.session import get_session
from items.models import ItemRead
import items.service as items_service

router = APIRouter()


@router.get("/get/{market_hash_name}" )#,response_model=ItemRead)
async def get_Item(market_hash_name: str, db_session: Session = Depends(get_session)):
    return items_service.get(db_session=db_session, market_hash_name=market_hash_name)