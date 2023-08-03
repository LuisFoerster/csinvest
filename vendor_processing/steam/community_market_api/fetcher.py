from vendor_processing.steam.community_market_api.endpoints import get_some_items, get_inventory
from database.session import get_session
from sqlalchemy import exists, select
from items.models import Item
import items.service as items_service
import assets.service as assets_service
import vendor_offers.service as vendor_offers_service
from database.session import get_session
from vendor_processing.steam.community_market_api.preprocessing import preprocess_item, preprocess_offer, preprocess_asset
import time
session = get_session()


def fetch_some_items(start, count):
    items = get_some_items(start, count)
    item_data = list(map(lambda x: preprocess_item(x), items["results"]))
    offer_data = list(map(lambda x: preprocess_offer(x), items["results"]))
    print("\n\n")
    print(items)
    print("fetched "+str(len(items["results"]))+" items from steam community market")
    print("\n\n")
    items_service.create_or_skip(db_session=session, data=item_data)
    vendor_offers_service.create_or_update(db_session=session, offer_in=offer_data)

def fetch_and_update_all_items():
    start = 2100
    try:
        total_count = get_some_items(0,1)["total_count"]
    except Exception as e:
        print(e)
        return

    while start < total_count:
        print(start)
        trys = 0
        failed = True
        while trys < 5 and failed:
            try:
                fetch_some_items(start, 100)
                print("fetched")
                failed = False
            except Exception as e:
                print(e)
                time.sleep(100)
                trys += 1
        start += 100

def fetch_inventory(steamid):
    inventory = get_inventory(steamid)
    assets_in = list(filter(lambda x: x is not None , map(lambda x: preprocess_asset(db_session=session,asset_in= x), inventory["assets"])))
    assets_service.create_or_update(db_session=session, assets_in=assets_in)


fetch_inventory("76561198086314296")



