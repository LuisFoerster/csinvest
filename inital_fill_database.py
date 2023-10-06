import db_service as accounts_service
import db_service as user_service
import db_service as vendors_service
from api_service.steam.communityapi import fetch_some_items
from db_service import get_session

session = get_session()

user_service.create(db_session=session, user_in={"username": "Luis", "role": "admin"})

accounts_service.create(
    db_session=session,
    account_in={"steamid": "76561198086314296", "personame": "Luis"},
)

vendors_service.create(
    db_session=session,
    vendor_in=[
        {"name": "Steam", "provision": "10", "icon_url": "www.steam.com"},
        {"name": "Skinport", "provision": "6", "icon_url": "www.skinport.com"},
    ],
)

fetch_some_items(start=0, count=100, db_session=session)
