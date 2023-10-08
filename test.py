from datetime import datetime, timedelta
from db_service.session import get_session

# print(get_classid_by_market_hash_name(db_session=get_session(),market_hash_name="Souvenir Sawed-Off | Rust Coat (Well-Worn)"))

import db_service.price_histories.service as price_histories_service

# result = get_total_item_price_volume_over_timespan(db_session=get_session(), classid="5453609791", time_from=datetime.now() - timedelta(days=30),
#                                                    time_to= datetime.now())
# print(result)
#
result = price_histories_service.get_total_market_price_volume_over_timespan(
    db_session=get_session(),
    time_from=datetime.now() - timedelta(days=30),
    time_to=datetime.now(),
)
print(result)

# result = get_asset_count_for_each_stack(db_session=get_session(), steamid="76561198086314296")
# asset_stacks = {"asset_stacks":[r._asdict() for r in result]}
# print(asset_stacks)
# print(Depot(**asset_stacks))
# print(Depot.total_buyin)
# print(result)
# print(result)
# AssetStacks = []
# for each in result:
#     AssetStacks.append({
#         "market_hash_name" : each[0],
#         "size": each[1],
#         "buyin": each[2],
#         "virtual": each[3]
#     })
#
#
#
# Depot(asset_stacks = AssetStacks)
# print(Depot.total_buyin)
