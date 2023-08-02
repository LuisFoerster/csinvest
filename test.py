from items.service import get_with_vendor_offers
from database.session import get_session

session = get_session()

result = get_with_vendor_offers(db_session=session, market_hash_name="Souvenir Sawed-Off | Irradiated Alert (Minimal Wear)")

print(result.Item.__dict__)
#item = ItemBase(**result.Item.__dict__, vendor_offers =  [vendor_offers,vendor_offers] )
#print(item.model_dump_json())