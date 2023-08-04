import time

import requests
from sqlalchemy.orm import Session

import assets.service as assets_service
import items.service as items_service
import vendor_offers.service as vendor_offers_service
from database.session import get_session
from vendor_processing.steam.community_market_api.endpoints import get_some_items, get_inventory
from vendor_processing.steam.community_market_api.preprocessing import preprocess_item, preprocess_offer, \
    preprocess_asset

session = get_session()


def fetch_some_items(start: int, count: int):
    items = get_some_items(start, count)
    item_data = list(map(lambda x: preprocess_item(x), items["results"]))
    offer_data = list(map(lambda x: preprocess_offer(x), items["results"]))
    print("\n\n")
    print(items)
    print("fetched " + str(len(items["results"])) + " items from steam community market")
    print("\n\n")
    items_service.create_or_skip(db_session=session, items_in=item_data)
    vendor_offers_service.create_or_update(db_session=session, offers_in=offer_data)


def fetch_and_update_all_items():
    start = 2100
    try:
        total_count = get_some_items(0, 1)["total_count"]
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


def fetch_inventory(db_session: Session, steamid):
    inventory = get_inventory(steamid)
    # inventory["describtions"]["some_classid"]["tradable"] jetzt aufrufbar
    describtions = {describtion["classid"]: describtion for describtion in inventory["descriptions"]}
    assets_in = list(
        filter(lambda asset: asset is not None,
               map(lambda asset: preprocess_asset(db_session=db_session, asset_in=asset, describtions=describtions),
                   inventory["assets"]))
    )
    assets_service.create_or_update(db_session=session, assets_in=assets_in)


# fetch_some_items(0, 100)
fetch_inventory(db_session=session, steamid="76561198202508143")