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


def preprocess_offer(item_in: dict):
    return {
        "classid": item_in["asset_description"]["classid"],
        "lowest_price": item_in["sell_price"],
        "median_price": item_in["sell_price"],
        "sell_listings": item_in["sell_listings"],
        "vendorid": 1
    }
