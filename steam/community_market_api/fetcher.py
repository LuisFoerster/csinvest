from steam.community_market_api.endpoints import get_some_items_from_steam
from database.session import get_session
from items.models import Item
import items.service as items_service
import vendor_offers.service as vendor_offers_service
from database.session import get_session
from steam.community_market_api.preprocessing import preprocess_item, preprocess_offer

session = get_session()


def fetch_item():
    items = get_some_items_from_steam(0, 100)

    item_data = list(map(lambda x: preprocess_item(x), items["results"]))
    offer_data = list(map(lambda x: preprocess_offer(x), items["results"]))
    print(item_data)

    items_service.create_or_skip(db_session=session, data=item_data)
    vendor_offers_service.create_or_update(db_session=session, data=offer_data)


fetch_item()
