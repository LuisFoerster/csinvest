from steam.community_market_api.endpoints import get_some_items_from_steam
from database.session import get_session
from items.models import Item
import items.service as items_service
import prices.service as price_service
from utils import flatten_dict
from steam.community_market_api.preprocessing import preprocess_item

items = get_some_items_from_steam(0, 100)
session = get_session()

# print(items)
item_data = list(map(lambda x: preprocess_item(x), items["results"]))
# print(item_data)
items_service.create(db_session=session, item_in=item_data)
price_service.create(db_session=session, price_in=item_data)
