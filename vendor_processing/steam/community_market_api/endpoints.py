import re

import requests
from bs4 import BeautifulSoup


def get_some_items(start, count):
    url = 'https://steamcommunity.com/market/search/render/'
    params = {"appid": 730, "count": count, "start": start, "language": "DE", "norender": "1",
              "search_description": "0", "sort_column": "name", "sort_dir": "asc", "currency": 0}
    headers = {"Accept-Language": "de-DE", "Accept": "application/json, text/javascript, */*; q=0.01"}

    try:
        response = requests.get(url, params=params, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error occurred while making the API request: {e}")
        return None
    except ValueError as e:
        # Handle JSON decoding errors
        print(f"Error occurred while parsing JSON response: {e}")
        return None


def get_inventory(steamid):
    url = f"https://steamcommunity.com/inventory/{steamid}/730/2"
    headers = {"Accept-Language": "de-DE", "Accept": "application/json, text/javascript, */*; q=0.01"}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error occurred while making the API request: {e}")
        return None
    except ValueError as e:
        # Handle JSON decoding errors
        print(f"Error occurred while parsing JSON response: {e}")
        return None


def get_pricehistory(market_hash_name: str):
    params = {"country": "DE", "currency": 0, "appid": 730, "market_hash_name": market_hash_name}
    try:
        response = requests.get("https://steamcommunity.com/market/pricehistory/", params=params)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(e)
        return None


def get_item_orders_histogram(item_nameid: str):
    params = {
        "country": "DE",
        "language": "german",
        "currency": 3,
        "item_nameid": item_nameid,
        "two_factor": 0,
        "norender": 1
    }
    try:
        response = requests.get("https://steamcommunity.com/market/itemordershistogram", params=params)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(e)
        return None


def get_item_nameid(market_hash_name: str):
    try:
        response = requests.get(f"https://steamcommunity.com/market/listings/730/{market_hash_name}")
        response.raise_for_status()
        # load content of response in html parser
        soup = BeautifulSoup(response.content, "html.parser")
        # Find the script tag containing the item_id
        script = soup.select_one("script:-soup-contains('Market_LoadOrderSpread')")
        if not script: return None
        match = re.search(r"Market_LoadOrderSpread\(\s*(\d+)\s*\)", script.get_text())
        if not match: return None
        item_id = match.group(1)
        return item_id
    except Exception as e:
        print(e)
        return None


#print(get_item_orders_histogram(get_item_nameid("Revolution Case")))
