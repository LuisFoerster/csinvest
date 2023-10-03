from db_service.migrations import get_session

import db_service.users.service as user_service
import db_service.accounts.service as accounts_service
import db_service.vendors.service as vendors_service
from vendor_processing.steam.communityapi.fetcher import fetch_some_items

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
