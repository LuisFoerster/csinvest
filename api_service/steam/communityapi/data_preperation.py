import json
from datetime import datetime

from api_service.steam.communityapi.endpoints import steam_community_endpoints_service
from api_service.steam.communityapi.utils import cent_to_euro


def get_inventory_dummy():
    with open(
            "/api_service/steam/response_examples/inventory_response.json", "r", encoding="utf-8"
    ) as file:
        # Lese den Inhalt der Datei
        data = file.read()
    return json.loads(data)


def get_total_count() -> int:
    """
    Returns:
        The total_count, which is the number of all items that can be queried from steam community market.
    """

    raw_data = steam_community_endpoints_service.fetch_some_items(start=0, count=0)

    total_count = raw_data["total_count"]

    return total_count


def get_some_items_and_their_offers(*, start: int, count: int):
    """
    Get's some items from steam communitymarket, the amount of returned items depends on the count value.
    The startpoint can be choosen by the start value.
    The rawdata get's processed.

    Args:
        start: The starting point in the Steam database from which items be returned
        count: Number of items to be returned

    Prepared_return_data:

        item_data is a list of:
            {
                "classid" (int): 1321231,

                "appid" (int): 730,

                "market_hash_name" (String): Chroma 2 Case,

                "name" (String): Chroma 2 Case,

                "item_nameid" (int) : 12312,

                "background_color" (String): D2D2D2,

                "name_color" (String): F2D2D2,

                "icon_url" (String): -9a81dlWLwJ2UUGcVs_nsVtzdOEd,

                "type" (String): Behälter (Standardqualität),
            }


        offer_data is a list of:
            {
                "classid" (int): 1231231,

                "lowest_price" (float): 1.25,

                "median_price" (float): 1.25,

                "sell_listings" (int): 3213,

                "affiliate_link" (String): www.steam.com/chroma 2 Case,

                "vendorid" (int): 1 ,
            }
    """

    item_data = []
    offer_data = []

    raw_data = steam_community_endpoints_service.fetch_some_items(start=start, count=count)

    for item in raw_data["results"]:
        item_nameid = 1  # get_item_nameid(market_hash_name) ISSUE: TO MANY REQUESTS (Only 20 Items possible)
        lowest_price = cent_to_euro(item["sell_price"])
        median_price = cent_to_euro(item["sell_price"])
        affiliate_link = "https://steamcommunity.com/market/listings/730/" + item["asset_description"][
            "market_hash_name"]

        if "|" in item["asset_description"]["name"]:
            name_spezifier = item["asset_description"]["name"].split("|")[1].split("(")[0]
        else:
            name_spezifier = None

        item_data.append(
            {
                "classid": item["asset_description"]["classid"],
                "market_hash_name": item["asset_description"]["market_hash_name"],
                "item_nameid": item_nameid,
                "name_spezifier": name_spezifier,
                "min_float": None,
                "max_float": None,
                "droppool": None,
                "appid": item["asset_description"]["appid"],
                "background_color": item["asset_description"]["background_color"],
                "name_color": item["asset_description"]["name_color"],
                "icon_url": item["asset_description"]["icon_url"],
            }
        )

        offer_data.append({
            "classid": item["asset_description"]["classid"],
            "lowest_price": lowest_price,
            "median_price": median_price,
            "sell_listings": item["sell_listings"],
            "affiliate_link": affiliate_link,
            "vendorid": 1  # vendorid 1 for steam,
        })

    return item_data, offer_data


def get_price_history(*, market_hash_name: str, classid: str):
    """
        Get's the whole pricehistory of one item from the steam community market.
        The raw Data gets prepared

        Args:
            market_hash_name: The market_hash_name of the item
            classid: The classid of the item

        Prepared_return_data:

            history_listings is a list of:
                {
                "classid" (str): 12312312,

                "vendorid" (str): 1 (steam),

                "time_stamp" (datetime): 2015-09-18 01:00:00,

                "volume" (int): 1232 (total sells about one day or hour),

                "price" (flaot): 1.52 (in Dollar),
            }
        """

    history_listings = []
    price_history = steam_community_endpoints_service.fetch_pricehistory(market_hash_name=market_hash_name)
    for price in price_history["prices"]:
        time_stamp = datetime.strptime(price[0].replace(": +0", ""), "%b %d %Y %H").strftime("%Y-%m-%d %H:%M:%S")

        history_listings.append(
            {
                "classid": classid,
                "vendorid": 1,
                "time_stamp": time_stamp,
                "volume": price[2],
                "price": price[1],
            }
        )

    return history_listings


def get_inventory(*, steamid: str):
    """
          Get's the whole inventory of one player from the steam.
          The raw Data gets prepared.
          The functions creates a list of all assets and a list of all itemdescriptions.

          Args:
              steamid: The steamid of the user

          Prepared_return_data:

              assets is a list of:
                  {
                    "classid": asset["classid"],

                    "assetid": asset["assetid"],

                    "instanceid": asset["instanceid"]
                    }

              descriptions is a list of:
                 {
                  "appid": 730,

                  "classid": "1989279141",

                  "instanceid": "302028390",

                  "currency": 0,

                  "background_color": "",

                  "icon_url": "IzMF03bi9WpSBq-S-ekoE33L-iLqGFHVaU25ZzQNQcXdB2ozio1RrlIWFK3UfvMYB8UsvjiMXojflsZalyxSh31CIyHz2GZ-KuFpPsrTzBG0suOBCG25Pm-Te3WBHg84T7ZdPT6N-WChtOqVE2vAEuglSwECf_cM9mIdbprYPgx9itAdqGq0mFZwCxo8e9VKaVK4m3dCMuyaadCusA",

                  "icon_url_large": "IzMF03bi9WpSBq-S-ekoE33L-iLqGFHVaU25ZzQNQcXdB2ozio1RrlIWFK3UfvMYB8UsvjiMXojflsZalyxSh31CIyHz2GZ-KuFpPsrTzBG0suOBCG3IZDbWKCSXSlsxHLENZDvaqjSi4-TCEDyaQeF6QlhSeaMA-mcaOMzcORJr09YKqSuomUM7HRkkfddLZQOvw2QfKOAmmSJDJpoMGFMTmg",

                  "descriptions": [
                    {
                      "type": "html",

                      "value": "Dies ist das versiegelte Gefäß eines Graffitimusters. Wenn dieses Graffitimuster entsiegelt wird, erhalten Sie genug Aufladungen, um das Graffitimuster \u003cb\u003e50\u003c/b\u003e-mal in der Spielwelt zu sprühen."
                    },
                    {
                      "type": "html",

                      "value": " "
                    },
                    {
                      "type": "html",

                      "value": "",

                      "color": "00a000"
                    }
                  ],
                  "tradable": 1,

                  "actions": [
                    {
                      "link": "steam://rungame/730/76561202255233023/+csgo_econ_action_preview%20S%owner_steamid%A%assetid%D13874084005722762082",

                      "name": "Im Spiel untersuchen …"
                    }
                  ],
                  "name": "Versiegeltes Graffito | NaCl (Haiweiß)",

                  "name_color": "D2D2D2",

                  "type": "Graffiti (Standardqualität)",

                  "market_name": "Versiegeltes Graffito | NaCl (Haiweiß)",

                  "market_hash_name": "Sealed Graffiti | NaCl (Shark White)",

                  "market_actions": [
                    {
                      "link": "steam://rungame/730/76561202255233023/+csgo_econ_action_preview%20M%listingid%A%assetid%D13874084005722762082",

                      "name": "Im Spiel untersuchen …"
                    }
                  ],
                  "commodity": 1,

                  "market_tradable_restriction": 7,

                  "marketable": 1,

                  "tags": [
                    {
                      "category": "Type",

                      "internal_name": "CSGO_Type_Spray",

                      "localized_category_name": "Typ",

                      "localized_tag_name": "Graffiti"
                    },
                    {
                      "category": "Quality",

                      "internal_name": "normal",

                      "localized_category_name": "Kategorie",

                      "localized_tag_name": "Normal"
                    },
                    {
                      "category": "Rarity",

                      "internal_name": "Rarity_Common",

                      "localized_category_name": "Qualität",

                      "localized_tag_name": "Standardqualität",

                      "color": "b0c3d9"
                    },
                    {
                      "category": "SprayColorCategory",

                      "internal_name": "Tint19",

                      "localized_category_name": "Graffitifarbe",

                      "localized_tag_name": "Haiweiß"
                    }
                  ]
                }
          """

    assets = []
    descriptions = {}
    inventory = steam_community_endpoints_service.fetch_inventory(steamid)
    # inventory = get_inventory_dummy()

    for description in inventory["descriptions"]:
        if description["marketable"]:
            descriptions[description["classid"]] = description

    for asset in inventory["assets"]:
        assets.append(
            {
                "classid": asset["classid"],
                "assetid": asset["assetid"],
                "instanceid": asset["instanceid"]
            }
        )

    return assets, descriptions
