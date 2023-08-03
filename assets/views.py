from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database.session import get_session
from items.models import ItemWithVendorOffers
import items.service as items_service

router = APIRouter()


