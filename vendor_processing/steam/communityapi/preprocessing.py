from sqlalchemy.orm import Session

import items.service as items_service
import asset_stacks.service as asset_stacks_service
import assets.service as assets_service
from database.session import get_session
from vendor_processing.steam.communityapi.endpoints import get_item_nameid

# def preprocess_item(item_in: dict):
#     item_nameid = get_item_nameid(item_in["asset_description"]["market_hash_name"])
#     return {
#         "classid": item_in["asset_description"]["classid"],
#         "appid": item_in["asset_description"]["appid"],
#         "market_hash_name": item_in["asset_description"]["market_hash_name"],
#         "name": item_in["asset_description"]["name"],
#         "item_nameid": item_nameid,
#         "background_color": item_in["asset_description"]["background_color"],
#         "name_color": item_in["asset_description"]["name_color"],
#         "icon_url": item_in["asset_description"]["icon_url"],
#         "type": item_in["asset_description"]["type"],
#     }
#
#
# def preprocess_offer(item_in: dict):
#     return {
#         "classid": item_in["asset_description"]["classid"],
#         "lowest_price": cent_to_euro(item_in["sell_price"]),
#         "median_price": cent_to_euro(item_in["sell_price"]),
#         "sell_listings": item_in["sell_listings"],
#         "affiliate_link": "https://steamcommunity.com/market/listings/730/" + item_in["asset_description"][
#             "market_hash_name"],
#         "vendorid": 1
#     }





def cent_to_euro(amount_cent):
    try:
        amount_cent = int(amount_cent)
        amount_euro = amount_cent / 100.0
        return round(amount_euro, 2)
    except ValueError:
        print("Invalid input. Please provide a valid integer value.")
        return None


# def preprocess_assets(db_session: Session, steamid: str, inventory: dict):
#     describtions = {describtion["classid"]: describtion for describtion in inventory["descriptions"]}
#     buyin_prices = {classid: 2.0 for classid in describtions.keys()}  # changed # TODO: fetch buyin
#
#     assets = []
#     for asset in inventory["assets"]:
#         marktable = describtions[asset["classid"]]["marketable"]
#         classid = asset["classid"]
#         item = item_from_describtions(classid=classid, describtions=describtions)
#
#         if marktable:
#             items_service.create_if_not_exist(
#                 db_session=db_session,
#                 item_in=item,
#             )
#             assets += [{
#                 "steamid": steamid,
#                 "appid": asset["appid"],
#                 "contextid": asset["contextid"],
#                 "assetid": asset["assetid"],
#                 "classid": asset["classid"],
#                 "instanceid": asset["instanceid"],
#                 "amount": asset["amount"],
#                 "buyin": buyin_prices[asset["classid"]]
#             }]
#
#     return assets


# def item_from_describtions(classid: str, describtions: dict):
#     """describtions dict must be in format {%classid%: {...},...}"""
#     return {
#         "classid": describtions[classid]["classid"],
#         "appid": describtions[classid]["appid"],
#         "market_hash_name": describtions[classid]["market_hash_name"],
#         "name": describtions[classid]["name"],
#         "background_color": describtions[classid]["background_color"],
#         "name_color": describtions[classid]["name_color"],
#         "icon_url": describtions[classid]["icon_url"],
#         "type": describtions[classid]["type"],
#     }


# def assign_to_stack(db_session: Session, preprocessed_assets: list[dict]):
#     for asset in preprocessed_assets:
#         asset["asset_stackid"] = asset_stacks_service.create_if_not_exist(
#             db_session=db_session,
#             asset_stack_in={
#                 "classid": asset["classid"],
#                 "steamid": asset["steamid"],
#                 "buyin": asset.pop("buyin"),  # changed
#                 "virtual": 0,
#                 "virtual_size": None
#             })
#     return preprocessed_assets

# stacks = preprocess_asset_stacks(get_session(),76561198086314296, {})
# print(stacks[0].classid)
