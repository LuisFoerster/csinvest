from vendor_processing.skinport.endpoints import get_all_tradehistories_from_skinport
#import vendor_offers.service as vendor_offers_service
from db_service.migrations import get_session, Session
import db_service.items.service as item_service
import vendor_processing.skinport.service as skinport_service

session = get_session()


# def fetch_items():
#     items = get_all_items_from_skinport()
#
#     offer_data = list(
#        filter(lambda x: x is not None, map(lambda x: preprocess_offer(db_session=session, data=x), items)))
#
#
#     vendor_offers_service.create_or_update(db_session=session, offers_in=offer_data)
#

def fetch_tradehistories(db_session: Session):
    tradehistories = get_all_tradehistories_from_skinport()

    tradehistories_data = []

    for tradehistorie in tradehistories:
        classid = item_service.get_classid_by_market_hash_name(
            db_session= db_session, market_hash_name=tradehistorie["market_hash_name"])
        avg_price = tradehistorie["last_90_days"]["avg"]
        volume = tradehistorie["last_90_days"]["volume"]

        if classid is not None and avg_price is not None:
            tradehistories_data.append({
                "classid" : classid,
                "avg_price": avg_price,
                "volume": volume
            })

    skinport_service.create(db_session=db_session, data_in=tradehistories_data)

#fetch_tradehistories(get_session())
print(skinport_service.get_total_market_price_volume_over_90_days(db_session=get_session()))


