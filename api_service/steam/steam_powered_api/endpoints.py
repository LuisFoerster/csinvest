from uplink import Consumer, get, Query, returns
from uplink.types import List

from settings import settings


class SteamPoweredApi(Consumer):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @returns.json()
    @get("/ISteamUser/GetPlayerSummaries/v0002/")
    def fetch_player_summaries(self, steamids: Query(type =List[int]), key : Query(type=str) = settings.STEAM_WEBAPI_KEY):
        """Get summary of a player"""

    @returns.json()
    @get("/ISteamEconomy/GetAssetClassInfo/v0001/")
    def fetch_asset_class_info(self,
                               classid0: Query(type=str),
                               appid : Query(type=int) = 730,
                               class_count : Query(type=int) = 1,
                            key: Query(type=str) = settings.STEAM_WEBAPI_KEY
                             ):
        """Get information of a item"""




steam_powered_api = SteamPoweredApi(base_url="https://api.steampowered.com")

print(steam_powered_api.fetch_asset_class_info("1011953270"))