from typing import List

import requests

from settings import settings


def get_player_summaries(steamids: List[str]):
    url = 'https://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/'
    params = {'steamids': steamids, 'key': settings.STEAM_WEBAPI_KEY}
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()  # Raise an exception for 4xx and 5xx status codes

        return response.json()

    except requests.exceptions.RequestException as e:
        # Handle network errors, timeouts, etc.
        print(f"Error occurred while making the API request: {e}")
        return []
    except ValueError as e:
        # Handle JSON decoding errors
        print(f"Error occurred while parsing JSON response: {e}")
        return []
