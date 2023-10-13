from settings import settings
from uplink import Consumer, get, headers, Query, returns, retry
from uplink.retry.when import status

from settings import settings


class SteamCommunityEndpoints(Consumer):

    @headers({
        "Accept-Language": "en-US",
        "Accept": "application/json, text/javascript, */*; q=0.01",
    })
    @returns.json()
    @retry(when=status(429), max_attempts=5, backoff=retry.backoff.fixed(100), )
    @get("/market/search/render/")
    def fetch_some_items(self,
                         count: Query(type=int) = 1,
                         start: Query(type=int) = 0,
                         appid: Query(type=int) = 730,
                         language: Query(type=str) = "US",
                         norender: Query(type=int) = 1,
                         search_description: Query(type=bool) = False,
                         sort_column: Query(type=str) = "name",
                         sort_dir: Query(type=str) = "asc",
                         currency: Query(type=int) = 0
                         ):
        """Get some items from the Steam community market"""

    @headers({
        "Accept-Language": "en-US",
        "Accept": "application/json, text/javascript, */*; q=0.01",
    })
    @returns.json()
    @get("/inventory/{steamid}/730/2/")
    def fetch_inventory(self,
                        steamid: str,
                        language: Query(type=str) = "US",
                        count: Query(type=int) = 1000
                        ):
        """Get some items from a steam users inventory"""

    @headers({
        "Accept-Language": "en-US",
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Cookie": settings.STEAM_COOKIE
    })
    @returns.json()
    @get("/market/pricehistory/")
    def fetch_pricehistory(self,
                           market_hash_name: Query(type=str),
                           country: Query(type=str) = "US",
                           currency: Query(type=int) = 1,
                           appid: Query(type=int) = 730
                           ):
        """Get the price history of an item"""


steam_community_endpoints_service = SteamCommunityEndpoints(base_url="https://steamcommunity.com")

# def fetch_some_items(start, count):
#     url = "https://steamcommunity.com/market/search/render/"
#     params = {
#         #"Cookie": settings.STEAM_COOKIE,
#         "appid": 730,
#         "count": count,
#         "start": start,
#         "language": "DE",
#         "norender": "1",
#         "search_description": "0",
#         "sort_column": "name",
#         "sort_dir": "asc",
#         "currency": 0,
#     }
#     headers = {
#         "Accept-Language": "de-DE",
#         "Accept": "application/json, text/javascript, */*; q=0.01",
#     }
#
#     try:
#         response = requests.get(url, params=params, headers=headers)
#         response.raise_for_status()
#         return response.json()
#     except requests.exceptions.RequestException as e:
#         print(f"Error occurred while making the API request: {e}")
#         return None
#     except ValueError as e:
#         # Handle JSON decoding errors
#         print(f"Error occurred while parsing JSON response: {e}")
#         return None


# def fetch_inventory(steamid):
#     url = f"https://steamcommunity.com/inventory/{steamid}/730/2/?l=english&count=5000"
#     headers = {
#         "Cookie": settings.STEAM_COOKIE,
#         "Accept-Language": "de-DE",
#         "Accept": "application/json, text/javascript, */*; q=0.01",
#     }
#     try:
#         response = requests.get(url, headers=headers)
#         response.raise_for_status()
#         return response.json()
#     except requests.exceptions.RequestException as e:
#         print(f"Error occurred while making the API request: {e}")
#         return None
#     except ValueError as e:
#         # Handle JSON decoding errors
#         print(f"Error occurred while parsing JSON response: {e}")
#         return None
#
#
# def fetch_pricehistory(market_hash_name: str):
#     params = {
#         "country": "DE",
#         "currency": 0,
#         "appid": 730,
#         "market_hash_name": market_hash_name,
#     }
#     headers = {"Cookie": settings.STEAM_COOKIE}
#     try:
#         response = requests.get(
#             "https://steamcommunity.com/market/pricehistory/",
#             params=params,
#             headers=headers,
#         )
#         response.raise_for_status()
#         return response.json()
#     except Exception as e:
#         print(e)
#         return None
#
#
# def fetch_item_orders_histogram(item_nameid: str):
#     params = {
#         "country": "DE",
#         "language": "german",
#         "currency": 3,
#         "item_nameid": item_nameid,
#         "two_factor": 0,
#         "norender": 1,
#     }
#     try:
#         response = requests.get(
#             "https://steamcommunity.com/market/itemordershistogram", params=params
#         )
#         response.raise_for_status()
#         return response.json()
#     except Exception as e:
#         print(e)
#         return None
#
#
# def fetch_item_nameid(market_hash_name: str):
#     headers = {
#         "Cookie": settings.STEAM_COOKIE,
#         "Accept-Language": "de-DE",
#         "Accept": "application/json, text/javascript, */*; q=0.01",
#     }
#     try:
#         response = requests.get(
#             f"https://steamcommunity.com/market/listings/730/{market_hash_name}",
#             headers=headers,
#         )
#         response.raise_for_status()
#         # load content of response in html parser
#         soup = BeautifulSoup(response.content, "html.parser")
#         # Find the script tag containing the item_id
#         script = soup.select_one("script:-soup-contains('Market_LoadOrderSpread')")
#         if not script:
#             return None
#         match = re.search(r"Market_LoadOrderSpread\(\s*(\d+)\s*\)", script.get_text())
#         if not match:
#             return None
#         item_id = match.group(1)
#         return item_id
#     except Exception as e:
#         print(e)
#         return None
#
#
# def fetch_item_price(market_hash_name):
#     url = "https://steamcommunity.com/market/priceoverview/"
#     params = {"appid": 730, "currency": 0, "market_hash_name": market_hash_name}
#     headers = {
#         "Accept-Language": "de-DE",
#         "Accept": "application/json, text/javascript, */*; q=0.01",
#     }
#     try:
#         response = requests.get(url, params=params, headers=headers)
#         response.raise_for_status()
#         return response.json()
#     except requests.exceptions.RequestException as e:
#         print(f"Error occurred while making the API request: {e}")
#         return None
#     except ValueError as e:
#         # Handle JSON decoding errors
#         print(f"Error occurred while parsing JSON response: {e}")
#         return None
