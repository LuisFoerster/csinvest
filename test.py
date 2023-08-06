from items.service import get_with_vendor_offers, get_classid_by_market_hash_name
from database.session import get_session

#print(get_classid_by_market_hash_name(db_session=get_session(),market_hash_name="Souvenir Sawed-Off | Rust Coat (Well-Worn)"))

from collections import defaultdict


def group_assets(steamid: int, marketable_assets: list[dict]):
    groups = defaultdict(list)

    for asset in marketable_assets:
        classid = asset["classid"]
        groups[classid].append(asset)

    return groups


# Example usage
marketable_assets = [{"assetid": 123241, "classid": 3330}, {"assetid": 122332, "classid": 3330},
                     {"assetid": 111111, "classid": 4444}]
steamid = 12345

asset_groups = group_assets(steamid, marketable_assets)
print(dict(asset_groups))