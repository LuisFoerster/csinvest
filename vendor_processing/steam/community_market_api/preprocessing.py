from sqlalchemy.orm import Session
from sqlalchemy import select,exists
from items.models import Item
def preprocess_item(item_in: dict):
    return {
        "classid": item_in["asset_description"]["classid"],
        "appid": item_in["asset_description"]["appid"],
        "market_hash_name": item_in["asset_description"]["market_hash_name"],
        "name": item_in["asset_description"]["name"],
        "background_color": item_in["asset_description"]["background_color"],
        "name_color": item_in["asset_description"]["name_color"],
        "icon_url": item_in["asset_description"]["icon_url"],
        "type": item_in["asset_description"]["type"],
    }


def preprocess_offer( item_in: dict):
    return {
        "classid": item_in["asset_description"]["classid"],
        "lowest_price": cent_to_euro(item_in["sell_price"]),
        "median_price": cent_to_euro(item_in["sell_price"]),
        "sell_listings": item_in["sell_listings"],
        "affiliate_link": "https://steamcommunity.com/market/listings/730/"+item_in["asset_description"]["market_hash_name"],
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


def preprocess_asset(db_session:Session, asset_in: dict):
    stmt = select(Item).where(Item.classid == asset_in["classid"])
    result_exists = db_session.execute(stmt).scalar()
    if result_exists:
        return {
          "appid": asset_in["appid"],
          "contextid": asset_in["contextid"],
          "assetid": asset_in["assetid"],
          "classid": asset_in["classid"],
          "instanceid": asset_in["instanceid"],
          "amount": asset_in["amount"]
        }
    return