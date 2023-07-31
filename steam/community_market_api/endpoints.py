from typing import List

import requests

from settings import settings


def get_some_items_from_steam(start, count):
    url = 'https://steamcommunity.com/market/search/render/'
    params = {"appid": 730, "count": count, "start": start, "language": "DE", "norender": "1",
               "search_description": "0", "sort_column": "name", "sort_dir": "asc", "currency": 0}
    headers = {"Accept-Language": "de-DE", "Accept": "application/json, text/javascript, */*; q=0.01"}

    try:
        response = requests.get(url, params=params,headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error occurred while making the API request: {e}")
        return None
    except ValueError as e:
        # Handle JSON decoding errors
        print(f"Error occurred while parsing JSON response: {e}")
        return None

