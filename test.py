from items.service import get
from database.session import get_session
from items.models import ItemBase
from vendor_offers.models import VendorOfferBase

session = get_session()

result = get(db_session=session, market_hash_name="Souvenir Sawed-Off | Irradiated Alert (Minimal Wear)")


vendor_offers = []
vendor_offers_dict = result.VendorOffer.__dict__
vendor_offers_dict = {**vendor_offers_dict, **vendor_offers_dict}
vendor_offers = VendorOfferBase(**result.VendorOffer.__dict__)
print(vendor_offers)
item = ItemBase(**result.Item.__dict__, vendor_offers =  [vendor_offers,vendor_offers] )
print(item.model_dump_json())