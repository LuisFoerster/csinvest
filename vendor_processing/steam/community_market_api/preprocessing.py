from sqlalchemy.orm import Session

import items.service as items_service
import asset_stacks.service as asset_stacks_service
import assets.service as assets_service
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


def buyin_table(marketable_assets_in: list[dict]):
    buyin_prices = {}
    for asset in marketable_assets_in:
        if not asset["classid"] in buyin_prices:
            #TODO: get buyin
            buyin_prices[asset["classid"]] = 2.0
    return buyin_prices

def assign_to_stack(db_session: Session, buyin_table: dict, marketable_assets_in: list[dict]):
    for asset in marketable_assets_in:
        asset_stack = asset_stacks_service.get_id_by_classid_and_buyin(db_session=db_session,
            steamid=asset["steamid"], classid=asset["classid"], buyin= buyin_table[asset["classid"]])
        if asset_stack is not None:
            asset["asset_stackid"] = asset_stack.id
        else:
            asset_stack_id= asset_stacks_service.create(db_session=db_session,asset_stack_in={
                "classid": asset["classid"],
                "steamid": asset["steamid"],
                "buyin": buyin_table[asset["classid"]],
                "virtual": 0,
                "virtual_size":None
            })
            asset["asset_stackid"] = asset_stack_id
    return marketable_assets_in







#stacks = preprocess_asset_stacks(get_session(),76561198086314296, {})
#print(stacks[0].classid)