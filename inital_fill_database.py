from database.session import get_session

import accounts.service as accounts_service
import vendors.service as vendors_service
#from vendor_processing.steam.community_market_api.fetcher import get_some_items
import asset_stacks.service as asset_stacks_service


session = get_session()


# accounts_service.create(db_session=session,
#                         account={
#                             "steamid": "76561198086314296",
#                             "personame": "Luis"
#                         })
#
# vendors_service.create(db_session=session,
#                        vendor_in=[{
#                            "name": "Steam",
#                            "provision": "10",
#                            "icon_url": "www.steam.com"
#                             },
#                            {
#                             "name": "Skinport",
#                            "provision": "6",
#                            "icon_url": "www.skinport.com"
#                        }])
#
# get_some_items(start=0,count=100)

asset_stacks_service.create(db_session=session,
                            asset_stack_in=[{
                                "classid": "310777105",
                                "steamid": "76561198086314296",
                                "buyin": 1.2,
                                "size": 3,
                                },
                                {
                                "classid": "310777105",
                                "steamid": "76561198086314296",
                                "buyin": 1.2,
                                "size": 3,
                            }])


