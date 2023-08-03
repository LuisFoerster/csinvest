from items.service import get_with_vendor_offers, get_classid_by_market_hash_name
from database.session import get_session

print(get_classid_by_market_hash_name(db_session=get_session(),market_hash_name="Souvenir Sawed-Off | Rust Coat (Well-Worn)"))
