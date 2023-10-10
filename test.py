from datetime import datetime, timedelta
from db_service.session import get_session
import db_service.items.service as items_db_service
import data_service.data_acquisition as data_service
from api_service.steam.steam_powered_api.endpoints import steam_powered_api

#data_service.create_relations_between_container_and_content(db_session=get_session())
#print(steam_powered_api.fetch_asset_class_info(classid0="1293508920"))


#data_service.get_all_item_data_from_steam(db_session=get_session())