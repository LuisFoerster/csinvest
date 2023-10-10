from data_service.data_acquisition import get_all_item_data_from_steam
from inital_fill_database import init_db
from db_service.session import get_session

init_db(session=get_session())

get_all_item_data_from_steam(db_session=get_session())