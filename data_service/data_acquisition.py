import time

# import api services
import api_service.steam.communityapi.data_preperation as steam_api_service
import db_service.asset_stacks.service as asset_stacks_db_service
import db_service.assets.service as assets_db_service
import db_service.items.service as items_db_service
import db_service.price_histories.service as price_histories_db_service
# import db services
import db_service.session as db_session_maker
import db_service.vendor_offers.service as vendor_offers_db_service


def get_all_item_data_from_steam():
    """
    Gets all items and their Data from Steam (Name, Classid, Prices, Pricehistory,...) and safes the Data in DB

    """
    session = db_session_maker.get_session()

    start = 0

    # to get 0 -2100
    try:
        total_count = steam_api_service.get_total_count()
    except Exception as e:
        print(e)
        return

    while start < total_count:
        print(start)
        trys = 0
        failed = True
        while trys < 5 and failed:
            # Errorhandling: Retry if TO MANY REQUESTS schould be handled in api_service
            try:
                items, offers = steam_api_service.get_some_items_and_their_offers(start=start, count=100)
                print("fetched")
                failed = False
            except Exception as e:
                print(e)
                time.sleep(100)
                trys += 1
        start += 100

        items_db_service.create_or_skip(db_session=session, items_in=items)
        vendor_offers_db_service.create_or_update(db_session=session, offers_in=offers)

        print("sucess")
        for item in items:
            history_listings = steam_api_service.fetch_price_history(
                market_hash_name=item["market_hash_name"],
                classid=item["classid"],
            )

            price_histories_db_service.create_or_update(
                db_session=session, history_listing_in=history_listings
            )


def create_or_update_user_depot(*, steamid: str):
    db_session = db_session_maker.get_session()
    asset_stackid_table = {}

    assets, descriptions = steam_api_service.get_inventory(steamid=steamid)

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

# get_all_item_data_from_steam()
create_or_update_user_depot(steamid="76561198209388244")
