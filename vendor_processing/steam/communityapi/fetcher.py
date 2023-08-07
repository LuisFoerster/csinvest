import time
import json

import requests
from sqlalchemy.orm import Session
from datetime import datetime, timedelta
import assets.service as assets_service
import asset_stacks.service as asset_stacks_service

import items.service as items_service
import price_histories.service as price_histories_service
import vendor_offers.service as vendor_offers_service
from database.session import get_session
from vendor_processing.steam.communityapi.preprocessing import cent_to_euro
from vendor_processing.steam.communityapi.endpoints import get_some_items, get_inventory, get_item_price, get_pricehistory, get_item_nameid



session = get_session()


def get_inventory_dummy():
    with open('../api_responses/inventory_response.json', 'r', encoding="utf-8") as file:
        # Lese den Inhalt der Datei
        data = file.read()
    return json.loads(data)


def fetch_some_items(db_session: Session,start: int, count: int):
    items = get_some_items(start, count)
    item_data = list(map(lambda item: {
        "classid": item["asset_description"]["classid"],
        "appid": item["asset_description"]["appid"],
        "market_hash_name": item["asset_description"]["market_hash_name"],
        "name": item["asset_description"]["name"],
        "item_nameid":  0, #get_item_nameid(item_in["asset_description"]["market_hash_name"]), Problems, because too many requests
        "background_color": item["asset_description"]["background_color"],
        "name_color": item["asset_description"]["name_color"],
        "icon_url": item["asset_description"]["icon_url"],
        "type": item["asset_description"]["type"],
    },
                        items["results"]))

    offer_data = list(map(lambda item: {
            "classid": item["asset_description"]["classid"],
            "lowest_price": cent_to_euro(item["sell_price"]),
            "median_price": cent_to_euro(item["sell_price"]),
            "sell_listings": item["sell_listings"],
            "affiliate_link": "https://steamcommunity.com/market/listings/730/" + item["asset_description"][
                "market_hash_name"],
            "vendorid": 1
        },
                          items["results"]))

    print("\n")
    print("fetched " + str(len(items["results"])) + " items from steam community market")
    print("\n")
    items_service.create_or_skip(db_session=db_session, items_in=item_data)
    vendor_offers_service.create_or_update(db_session=db_session, offers_in=offer_data)
    for item in item_data:
        fetch_price_history(db_session=db_session,
                            market_hash_name=item["market_hash_name"],
                            classid=item["classid"])



def fetch_and_update_all_items(db_session):
    start = 11500 #to get 0 -2100
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
                fetch_some_items(db_session, start, 100)
                print("fetched")
                failed = False
            except Exception as e:
                print(e)
                time.sleep(100)
                trys += 1
        start += 100



def fetch_inventory(db_session: Session, steamid):
    assets = []
    asset_stackid_tabel = {}
    # fetching # TODO: use get_inventory(steamid)
    inventory = get_inventory_dummy()
    # filter assets and descriptions
    descriptions = {description["classid"]: description for description in inventory["descriptions"] if
                    description["marketable"]}

    for classid in descriptions.keys():
        # TODO: fetch buyin
        descriptions[classid]["buyin"] = 2.0
        # item creation if it doesnt exist for any unique classid
        if not items_service.exists(db_session=db_session, classid=classid):
            item_nameid = get_item_nameid(descriptions[classid]["market_hash_name"])
            items_service.create(db_session=db_session, item_in={
                "classid": classid,
                "appid": descriptions[classid]["appid"],
                "market_hash_name": descriptions[classid]["market_hash_name"],
                "name": descriptions[classid]["name"],
                "item_nameid": item_nameid,
                "background_color": descriptions[classid]["background_color"],
                "name_color": descriptions[classid]["name_color"],
                "icon_url": descriptions[classid]["icon_url"],
                "type": descriptions[classid]["type"],
            })


        #OLD
        # items_service.create_if_not_exist(
        #     db_session=db_session,
        #     item_in=descriptions[classid]
        # )
        # stack creation if it doesnt exist for any unique classid


        stackid = asset_stacks_service.create_if_not_exist(
            db_session=db_session,
            asset_stack_in={
                "classid": classid,
                "steamid": steamid,
                "buyin": descriptions[classid]["buyin"],
                "virtual": 0,
                "virtual_size": None
            }
        )
        asset_stackid_tabel[classid] = stackid

    for asset in inventory["assets"]:
        if  descriptions.get(asset["classid"], False):
            asset["asset_stackid"] = asset_stackid_tabel[asset["classid"]]
            asset["steamid"] = steamid
            assets.append(asset)


    newest_update_timestamp = assets_service.get_timestamp_of_last_update(db_session=db_session, steamid=steamid)

    assets_service.create_or_update(
        db_session=db_session,
        assets_in=assets
    )
    assets_service.delete_stale(
        db_session=db_session,
        steamid=steamid,
        previous_update_timestamp=newest_update_timestamp
    )


# def fetch_inventory2(db_session: Session, steamid):
#     """setup for logging"""
#     logging_data = {
#         "steamid": steamid,
#         "items_in_inventory": 0,
#         "marktable_items": 0,
#         "items_added_to_db": 0,
#         "assets_added_to_db": 0,
#         "duration": 0,
#     }
#
#     start_time = time.time()
#
#     inventory = get_inventory_dummy()
#
#     preprocessed_assets = preprocess_assets(
#         db_session=db_session,
#         steamid=steamid,
#         inventory=inventory
#     )
#
#     assets_with_stackids = assign_to_stack(
#         db_session=db_session,
#         preprocessed_assets=preprocessed_assets
#     )
#
#     newest_update_timestamp = assets_service.get_newest_update_timestamp(
#         db_session=db_session,
#         steamid=steamid
#     )
#
#     assets_service.create_or_update(
#         db_session=db_session,
#         assets_in=assets_with_stackids
#     )
#
#     assets_service.delete_stale(
#         db_session=db_session,
#         steamid=steamid,
#         previous_update_timestamp=newest_update_timestamp
#     )
#
#     end_time = time.time()
#     logging_data["duration"] = end_time - start_time
#     print(logging_data)


def fetch_item_price(db_session: Session, market_hash_name, classid):
    price = get_item_price(market_hash_name)
    offer = {
        "classid": classid,
        "vendorid": 1,  # for steam
        "lowest_price": float(price["lowest_price"].replace('$', '').replace(',', '.')),
        "median_price": float(price["median_price"].replace('$', '').replace(',', '.')),
        "sell_listings": None,
        "affiliate_link": "https://steamcommunity.com/market/listings/730/" + market_hash_name,
    }
    vendor_offers_service.create_or_update_without_sell_listings(db_session=db_session, offers_in=offer)


def update_item_price_if_old(db_session: Session, market_hash_name, classid):
    update_time_stamp = vendor_offers_service.get_update_timestamp(db_session=db_session, classid=classid, vendorid=1)
    if update_time_stamp is None:
        print("Item doesn't exist")
        return
    if update_time_stamp <= datetime.now() - timedelta(minutes=5):
        fetch_item_price(db_session=db_session, market_hash_name=market_hash_name, classid=classid)
        print("Item " + market_hash_name + " updated")
    else:
        print("Item " + market_hash_name + " already up to date")


def fetch_price_history(db_session: Session, market_hash_name, classid):
    price_history = get_pricehistory(market_hash_name = market_hash_name)
    history_listings = list(map(lambda x: {
                            "classid": classid,
                            "vendorid": 1,
                            "time_stamp": datetime.strptime(x[0].replace(": +0", ""), "%b %d %Y %H").strftime("%Y-%m-%d %H:%M:%S"),
                            "volume": x[2],
                            "price": x[1]
                            }
                           ,price_history["prices"]))
    price_histories_service.create_or_update(db_session= db_session, history_listing_in=history_listings)
    print("\n")
    print("fetched Priehistory from: " + market_hash_name )
    print("\n")




#update_item_price_if_old(db_session=session, market_hash_name="Shadow Case", classid="1293508920")
#fetch_price_history(db_session=session, market_hash_name="Shadow Case", classid="1293508920")
# fetch_some_items(0, 100)
#fetch_inventory(db_session=session, steamid="76561198086314296")
fetch_and_update_all_items(db_session=session)