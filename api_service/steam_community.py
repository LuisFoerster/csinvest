from api_service.base import APIBase, HTTPMethods


class SteamCommunityAPI(APIBase):
    class Config:
        domain = "https://steamcommunity.com"
        cookie = "test:test"
        method = HTTPMethods.GET  # default method

    @staticmethod
    def get_inventory(
            steamid: int,
            l: str = "english",
            count: int = 5000,
            route: str = '/inventory/{steamid}/730/2/'): ...

    @staticmethod
    def get_inventory_2(
            steamid: int,
            myvar: int,
            l: str = "english",
            count: int = 5000,
            method: str = HTTPMethods.GET,
            route: str = '/inventory/{steamid}/730/2/'): ...


steam_community = SteamCommunityAPI()

# Calling the method to see the output
steam_community.get_inventory(1001010)
steam_community.get_inventory_2(1001010, 11102)