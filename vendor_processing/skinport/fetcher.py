from vendor_processing.skinport.endpoints import get_all_items_from_skinport
import vendor_offers.service as vendor_offers_service
from database.session import get_session
from vendor_processing.skinport.preprocessing import preprocess_offer

session = get_session()


def fetch_items():
    items = get_all_items_from_skinport()

    offer_data = list(
        filter(lambda x: x is not None, map(lambda x: preprocess_offer(db_session=session, data=x), items)))

    print(offer_data)

    vendor_offers_service.create_or_update(db_session=session, offers_in=offer_data)


fetch_items()
