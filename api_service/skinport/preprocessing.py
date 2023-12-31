from sqlalchemy.orm import Session

import db_service as item_service


def preprocess_offer(db_session: Session, data: dict):
    result = item_service.get_classid_by_market_hash_name(db_session=db_session,
                                                          market_hash_name=data["market_hash_name"])
    if result is None:
        return
    return {
        "classid": result.classid,
        "lowest_price": data["min_price"],
        "median_price": data["median_price"],
        "sell_listings": data["quantity"],
        "affiliate_link": data["item_page"],
        "vendorid": 2
    }
