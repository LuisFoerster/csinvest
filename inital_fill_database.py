from database.session import get_session

import users.service as user_service
import accounts.service as accounts_service
import vendors.service as vendors_service
import asset_stacks.service as asset_stacks_service
from vendor_processing.steam.communityapi.endpoints import get_some_items

session = get_session()

user_service.create(db_session=session, user_in={"username": "Luis", "role": "admin"})
accounts_service.create(db_session=session,
                        userid=1,
                        account_in={
                            "steamid": "76561198086314296",
                            "personame": "Luis"
                        })

vendors_service.create(db_session=session,
                       vendor_in=[{
                           "name": "Steam",
                           "provision": "10",
                           "icon_url": "www.steam.com"
                       },
                           {
                               "name": "Skinport",
                               "provision": "6",
                               "icon_url": "www.skinport.com"
                           }])

get_some_items(start=0, count=100)
