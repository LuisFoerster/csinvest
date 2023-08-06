from sqlalchemy.orm import Session

import items.service as items_service
import asset_stacks.service as asset_stacks_service
import  buyin_stacks.service as buyin_stacks_service
from database.session import get_session
from vendor_processing.steam.community_market_api.endpoints import get_item_nameid
def preprocess_item(item_in: dict):
    item_nameid = get_item_nameid(item_in["asset_description"]["market_hash_name"])
    return {
        "classid": item_in["asset_description"]["classid"],
        "appid": item_in["asset_description"]["appid"],
        "market_hash_name": item_in["asset_description"]["market_hash_name"],
        "name": item_in["asset_description"]["name"],
        "item_nameid": item_nameid,
        "background_color": item_in["asset_description"]["background_color"],
        "name_color": item_in["asset_description"]["name_color"],
        "icon_url": item_in["asset_description"]["icon_url"],
        "type": item_in["asset_description"]["type"],
    }


def preprocess_offer(item_in: dict):
    return {
        "classid": item_in["asset_description"]["classid"],
        "lowest_price": cent_to_euro(item_in["sell_price"]),
        "median_price": cent_to_euro(item_in["sell_price"]),
        "sell_listings": item_in["sell_listings"],
        "affiliate_link": "https://steamcommunity.com/market/listings/730/" + item_in["asset_description"][
            "market_hash_name"],
        "vendorid": 1
    }


def cent_to_euro(amount_cent):
    try:
        amount_cent = int(amount_cent)
        amount_euro = amount_cent / 100.0
        return round(amount_euro, 2)
    except ValueError:
        print("Invalid input. Please provide a valid integer value.")
        return None


def preprocess_asset(db_session: Session, steamid:str ,asset_in: dict, describtions: dict, logging_data = dict):
    """describtions dict must be in format {%classid%: {...},...}"""
    marktable = describtions[asset_in["classid"]]["marketable"]

    if marktable:
        logging_data["marktable_items"] += 1
        if not items_service.exists(db_session=db_session, classid=asset_in["classid"]):
            logging_data["items_added_to_db"] += 1
            items_service.create(
                db_session=db_session,
                item_in=item_from_describtions(classid=asset_in["classid"], describtions=describtions)
            )
        return {
            "steamid": steamid,
            "appid": asset_in["appid"],
            "contextid": asset_in["contextid"],
            "assetid": asset_in["assetid"],
            "classid": asset_in["classid"],
            "instanceid": asset_in["instanceid"],
            "amount": asset_in["amount"]
            }
    return


def item_from_describtions(classid: str, describtions: dict):
    """describtions dict must be in format {%classid%: {...},...}"""
    return {
        "classid": describtions[classid]["classid"],
        "appid": describtions[classid]["appid"],
        "market_hash_name": describtions[classid]["market_hash_name"],
        "name": describtions[classid]["name"],
        "background_color": describtions[classid]["background_color"],
        "name_color": describtions[classid]["name_color"],
        "icon_url": describtions[classid]["icon_url"],
        "type": describtions[classid]["type"],
    }


def generate_asset_groups(steamid, assets_in: dict):
    asset_groups = []
    for asset in assets_in:
        index = next((index for index, asset_group in enumerate(
            asset_groups) if asset_group["classid"] == asset["classid"]), None)
        if index is not None:
            asset_groups[index]["size"] += 1
        else:
            asset_groups.append({
                # this is a asset_group
                    "steamid": steamid,
                    "assetid": asset,
                    "classid": asset["classid"],
                    "buyin": None,
                    "size": 1,
                    "virtual": 0
                })

    return asset_groups


def preprocess_asset_stacks(db_session: Session, steamid, assets_in: dict):
    asset_stacks = []
    buyin_stacks = []
    asset_gorups = generate_asset_groups(steamid,assets_in)
    for asset_group in asset_gorups:
        asset_stack = asset_stacks_service.get(db_session=db_session, steamid=steamid, classid=asset_group["classid"])
        if asset_stack:
            if asset_group["size"] > asset_stack.size:
                size_diff = asset_group["size"] - asset_stack.size
                asset_stack.append(
                    {
                        "classid": asset_group["classid"],
                        "steamid": steamid,
                        "average_buyin": None,
                        "size": size_diff,
                        "virtual": 0
                    })
                buyin_stacks.append(
                {
                    "assetid": steamid,
                    "asset_stackid": None,
                    "buyin": None, # TODO: Insert current price of Item
                    "size": size_diff,
                    "virtual": 0
                })
        else:
            asset_stack.append(
                {
                    "classid": asset_group["classid"],
                    "steamid": steamid,
                    "average_buyin": None,
                    "size": asset_group["size"],
                    "virtual": 0
                })
            buyin_stacks.append(
                {
                    "assetid": steamid,
                    "asset_stackid": None,
                    "buyin": None,
                    "size": asset_group["size"],
                    "virtual": 0
                })



    return asset_stacks, buyin_stacks


#stacks = preprocess_asset_stacks(get_session(),76561198086314296, {})
#print(stacks[0].classid)