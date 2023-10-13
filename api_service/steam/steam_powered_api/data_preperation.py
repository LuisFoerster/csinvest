import api_service.steam.steam_powered_api.endpoints as steam_powered_api_endpoints


def get_item_information(*, classid: str):
    """
        Get's the information about a item.
    """

    item_information = {
        "name": None,
        "exterior": None,
        "quality": None,
        "categorie": None,
        "type": None,
        "weapon_type": None,
        "sticker_type": None,
        "graffiti_type": None,
        "patch_type": None,
        "collection": None,
        "team": None,
        "tournament": None,
        "professional_player": None
    }

    asset_class_info = steam_powered_api_endpoints.steam_powered_api.fetch_asset_class_info(classid0=classid)

    item_information["name"] = asset_class_info["result"][classid]["name"]

    tags = asset_class_info["result"][classid]["tags"]

    for tag in tags.values():
        match tag["category_name"]:
            case "Type":
                item_information["type"] = tag["name"]
            case "Sticker Type":
                item_information["sticker_type"] = tag["name"]
            case "Graffit Type":
                item_information["graffiti_type"] = tag["name"]
            case "Patch Type":
                item_information["patch_type"] = tag["name"]
            case "Weapon":
                item_information["weapon_type"] = tag["name"]
            case "Collection":
                item_information["collection"] = tag["name"]
            case "Sticker Collection":
                item_information["collection"] = tag["name"]
            case "Graffiti Collection":
                item_information["collection"] = tag["name"]
            case "Patch Collection":
                item_information["collection"] = tag["name"]
            case "Category":
                item_information["categorie"] = tag["name"]
            case "Quality":
                item_information["quality"] = tag["name"]
            case "Exterior":
                item_information["exterior"] = tag["name"]
            case "Team":
                item_information["team"] = tag["name"]
            case "Tournament":
                item_information["tournament"] = tag["name"]
            case "Professional Player":
                item_information["professional_player"] = tag["name"]

    return item_information


def get_container_content(*, classid: str):
    """
        Get's content of a container.
    """

    element_is_content = False
    content: list[str] = []

    asset_class_info = steam_powered_api_endpoints.steam_powered_api.fetch_asset_class_info(classid0=classid)
    descriptions = asset_class_info["result"][classid]["descriptions"]

    for element in descriptions.values():

        if element_is_content:
            if "color" in element and not "Exceedingly Rare" in element["value"]:
                content.append(element["value"])
            else:
                return content
        else:
            if element["value"] == "Contains one of the following:":
                element_is_content = True

    return content
