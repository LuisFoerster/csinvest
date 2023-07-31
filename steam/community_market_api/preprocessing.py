def preprocess_item(item_in: dict):
    return{
        "classid": item_in["asset_description"]["classid"],
        "appid": item_in["asset_description"]["appid"],
        "market_hash_name":item_in["asset_description"]["market_hash_name"],
        "name":item_in["asset_description"]["name"],
        "background_color": item_in["asset_description"]["background_color"],
        "name_color": item_in["asset_description"]["name_color"],
        "icon_url":item_in["asset_description"]["icon_url"],
        "sell_price": item_in["sell_price"],
    }