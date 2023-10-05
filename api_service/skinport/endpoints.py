import requests


def get_all_items_from_skinport():
    url = 'https://api.skinport.com/v1/items'
    params = {"app_id": 730, "currency": "EUR", "tradable": 0}
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

def get_all_tradehistories_from_skinport():
    url = 'https://api.skinport.com/v1/sales/history?app_id=730'
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
