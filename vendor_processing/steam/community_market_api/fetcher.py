import time
import json

import requests
from sqlalchemy.orm import Session
from datetime import datetime
import assets.service as assets_service
import asset_stacks.service as asset_stack_service
import items.service as items_service
import vendor_offers.service as vendor_offers_service
from database.session import get_session
from vendor_processing.steam.community_market_api.endpoints import get_some_items, get_inventory
from vendor_processing.steam.community_market_api.preprocessing import preprocess_item, preprocess_offer, \
    preprocess_asset, buyin_table, group_buyin, assign_to_stack

session = get_session()

def get_inventory_dummy():
    with open('../api_responses/inventory_response.json', 'r', encoding="utf-8") as file:
        # Lese den Inhalt der Datei
        data = file.read()
    return  json.loads(data)

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

    """setup for logging"""
    logging_data = {
        "steamid": steamid,
        "items_in_inventory": 0,
        "marktable_items": 0,
        "items_added_to_db": 0,
        "assets_added_to_db": 0,
        "duration": 0,
    }

    start_time = time.time()

    """For testing for real usage use: inventory = get_inventory(steamid) """
    inventory = get_inventory_dummy()

    logging_data["items_in_inventory"] = inventory["total_inventory_count"]

    describtions = {describtion["classid"]: describtion for describtion in inventory["descriptions"]}
    assets_to_insert = list(
        filter(lambda asset: asset is not None,
               map(lambda asset: preprocess_asset(
                   db_session=db_session,steamid=steamid, asset_in=asset,
                   describtions=describtions, logging_data=logging_data),
                   inventory["assets"]))
    )

    logging_data["assets_added_to_db"] = len(assets_to_insert) if assets_to_insert is not None else 0
    buyin_prices = buyin_table( marketable_assets_in=assets_to_insert)
    assets_with_stackids = assign_to_stack(db_session=db_session,buyin_table=buyin_prices,marketable_assets_in=assets_to_insert)
    newest_update_timestamp = assets_service.get_newest_update_timestamp(db_session= db_session, steamid=steamid)
    assets_service.create_or_update(db_session=db_session, assets_in=assets_with_stackids)
    assets_service.delete_stale(db_session=db_session, steamid=steamid, previous_update_timestamp=newest_update_timestamp)

    end_time = time.time()
    logging_data["duration"] = end_time - start_time
    print(logging_data)

#fetch_some_items(0, 100)
fetch_inventory(db_session=session, steamid="76561198086314296")


