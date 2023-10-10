from sqlalchemy.orm import Session

# import api services
import api_service.steam.communityapi.data_preperation as steam_community_api_service
import api_service.steam.steam_powered_api.data_preperation as steam_powered_api_service


import db_service.asset_stacks.service as asset_stacks_db_service
import db_service.assets.service as assets_db_service
import db_service.items.service as items_db_service
import db_service.container_contents.service as container_contents_db_serivce
import db_service.price_histories.service as price_histories_db_service
# import db services
import db_service.vendor_offers.service as vendor_offers_db_service


def get_all_item_data_from_steam(*, db_session: Session):
    """
    Gets all items and their Data from Steam (Name, Classid, Prices, Pricehistory,...) and safes the Data in DB

    """

    #TODO: get Release_date from pricehistory and insert into items.
    #TODO: get items Info (rarity, Collection) from ClassInfoApi and insert into items.
    #TODO: split information (quality)
    #TODO: create relationships and insert in container_content table
    #TODO: Errorhandling, if classid doesn't exists, retry...

    start = 3500



    total_count = steam_community_api_service.get_total_count()


    while start < total_count:
        print(start)
        history_listings = []
        items, offers = steam_community_api_service.get_some_items_and_their_offers(start=start, count=100)

        # Get Pricehistory for each item

        for item in items:
            # history_listings_of_one_item = steam_community_api_service.get_price_history(
            #     market_hash_name=item["market_hash_name"],
            #     classid=item["classid"],
            # )
            # item["release_year"] = history_listings_of_one_item[0]["time_stamp"]
            # history_listings += history_listings_of_one_item
            item_information = steam_powered_api_service.get_item_information(classid=item["classid"])
            item.update(item_information)


        # Insert into DB

        items_db_service.create_or_skip(db_session=db_session, items_in=items)
        vendor_offers_db_service.create_or_update(db_session=db_session, offers_in=offers)
        # price_histories_db_service.create_or_update(
        #     db_session=session, history_listing_in=history_listings
        # )


        start += 100




def create_or_update_user_depot(*,db_session: Session, steamid: str):
    asset_stackid_table = {}

    assets, descriptions = steam_community_api_service.get_inventory(steamid=steamid)

    for classid in descriptions.keys():

        # item creation if it doesnt exist for any unique classid
        if not items_db_service.exists(db_session=db_session, classid=classid):
            item_nameid = 0  # get_item_nameid(descriptions[classid]["market_hash_name"])
            items_db_service.create(
                db_session=db_session,
                item_in={
                    "classid": classid,
                    "appid": descriptions[classid]["appid"],
                    "market_hash_name": descriptions[classid]["market_hash_name"],
                    "name": descriptions[classid]["name"],
                    "item_nameid": item_nameid,
                    "background_color": descriptions[classid]["background_color"],
                    "name_color": descriptions[classid]["name_color"],
                    "icon_url": descriptions[classid]["icon_url"],
                    "type": descriptions[classid]["type"],
                },
            )

        # if not vendor_offers_db_service.exists(
        #     db_session=db_session, classid=classid, vendorid=1
        # ):
        #     #Nicht nötig, wenn das item nicht vorhanden ist, dann existiert es nicht auf dem Marktplatz!
        #     fetch_item_price(
        #         db_session=db_session,
        #         market_hash_name=descriptions[classid]["market_hash_name"],
        #         classid=classid,
        #     )

        # OLD
        # items_service.create_if_not_exist(
        #     db_session=db_session,
        #     item_in=descriptions[classid]
        # )
        # stack creation if it doesnt exist for any unique classid

        # TODO: fetch buyin
        buyin = 1  # vendor_offers_db_service.get_current_price(db_session=db_session, classid=classid, vendorid=1)

        stackid = asset_stacks_db_service.create_if_not_exist(
            db_session=db_session,
            asset_stack_in={
                "classid": classid,
                "steamid": steamid,
                "buyin": buyin,
                "virtual": 0,
                "virtual_size": None,
            },
        )
        asset_stackid_table[classid] = stackid

    assets_to_insert = []
    for asset in assets:
        if descriptions.get(asset["classid"], False):
            asset["asset_stackid"] = asset_stackid_table[asset["classid"]]
            asset["steamid"] = steamid
            assets_to_insert.append(asset)

    newest_update_timestamp = assets_db_service.get_timestamp_of_last_update(
        db_session=db_session, steamid=steamid
    )

    assets_db_service.create_or_update(db_session=db_session, assets_in=assets_to_insert)

    if newest_update_timestamp is not None:
        assets_db_service.delete_stale(
            db_session=db_session,
            steamid=steamid,
            previous_update_timestamp=newest_update_timestamp,
        )


# def update_item_price_if_old(db_session: Session, market_hash_name, classid):
#     update_time_stamp = vendor_offers_service.get_update_timestamp(
#         db_session=db_session, classid=classid, vendorid=1
#     )
#     if update_time_stamp is None:
#         print("Item doesn't exist")
#         return
#     if update_time_stamp <= datetime.now() - timedelta(minutes=5):
#         fetch_item_price(
#             db_session=db_session, market_hash_name=market_hash_name, classid=classid
#         )
#         print("Item " + market_hash_name + " updated")
#     else:
#         print("Item " + market_hash_name + " already up to date")

def create_relations_between_container_and_content(*,db_session:Session):

    relations = []

    container = items_db_service.get_by_type(db_session= db_session, type = "Container")
    for container_element in container:
        content = steam_powered_api_service.get_container_content(classid=container_element.classid)
        for content_element in content:
            content_classids = items_db_service.get_classids_by_name(db_session=db_session, name=content_element)
            for each_classid in content_classids:
                relations.append({
                    "container_classid": container_element.classid,
                    "content_classid": each_classid
                })
    container_contents_db_serivce.create_or_skip(db_session=db_session,relation_in=relations)


