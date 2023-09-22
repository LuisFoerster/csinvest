import re

import requests
from bs4 import BeautifulSoup

COOKIE = "timezoneOffset=7200,0; cookieSettings=%7B%22version%22%3A1%2C%22preference_state%22%3A2%2C%22content_customization%22%3Anull%2C%22valve_analytics%22%3Anull%2C%22third_party_analytics%22%3Anull%2C%22third_party_content%22%3Anull%2C%22utm_enabled%22%3Atrue%7D; strInventoryLastContext=730_2; sessionid=37e3103c9ea8c81a30b681f6; steamCountry=DE%7Cb28c5a27d6be987037b8bd58eae504de; webTradeEligibility=%7B%22allowed%22%3A1%2C%22allowed_at_time%22%3A0%2C%22steamguard_required_days%22%3A15%2C%22new_device_cooldown_days%22%3A0%2C%22time_checked%22%3A1691158525%7D; Steam_Language=english; steamLoginSecure=76561198086314296%7C%7CeyAidHlwIjogIkpXVCIsICJhbGciOiAiRWREU0EiIH0.eyAiaXNzIjogInI6MEQxQV8yMkU5RUZFN19DNDE1QSIsICJzdWIiOiAiNzY1NjExOTgwODYzMTQyOTYiLCAiYXVkIjogWyAid2ViIiBdLCAiZXhwIjogMTY5MTUxOTgyMywgIm5iZiI6IDE2ODI3OTI1OTAsICJpYXQiOiAxNjkxNDMyNTkwLCAianRpIjogIjBEMTRfMjJGMzI4RDZfQjEyNDAiLCAib2F0IjogMTY5MDU1Njk3NCwgInJ0X2V4cCI6IDE3MDg5OTI2NjYsICJwZXIiOiAwLCAiaXBfc3ViamVjdCI6ICI4MC4xNDcuNy4xNzIiLCAiaXBfY29uZmlybWVyIjogIjgwLjE0Ny43LjE3MiIgfQ.aN7vRyqaL_tGDqR7b7958SzpjQjmWQqAvNmr_q6LeOCv0rJF82IFTjDPU9Az7dBpCxJIg81-2dzq__FvneUUCQ"

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
    url = f"https://steamcommunity.com/inventory/{steamid}/730/2/?l=english&count=5000"
    headers = {"Cookie": COOKIE, "Accept-Language": "de-DE", "Accept": "application/json, text/javascript, */*; q=0.01"}
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
    headers = {"Cookie": COOKIE}
    try:
        response = requests.get("https://steamcommunity.com/market/pricehistory/", params=params, headers=headers)
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


def get_item_price(market_hash_name):
    url = 'https://steamcommunity.com/market/priceoverview/'
    params = {"appid": 730, "currency": 0, "market_hash_name": market_hash_name}
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

#print(get_item_orders_histogram(get_item_nameid("Revolution Case")))
