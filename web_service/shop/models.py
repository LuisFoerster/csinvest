from pydantic import BaseModel, ConfigDict


class ItemBase(BaseModel):
    model_config = ConfigDict(from_attributes=True, extra="ignore")
    market_hash_name: str
    classid: str
    name: str
    icon_url: str


class VendorOfferBase(BaseModel):
    model_config = ConfigDict(from_attributes=True, extra="ignore")
    vendorid: int
    lowest_price: float | None
    median_price: float | None
    affiliate_link: str
    sell_listings: int | None


class ItemWithVendorOffers(ItemBase):
    model_config = ConfigDict(from_attributes=True, extra="ignore")
    vendor_offers: list[VendorOfferBase] = []


class PaginatedShopItems(BaseModel):
    model_config = ConfigDict(from_attributes=True, extra="ignore")
    item_count: int | None
    itemsWithVendorOffers: list[ItemWithVendorOffers] | None

# result = shop_db_service.get_one_shop_item(db_session=get_session(), market_hash_name = "UMP-45 | Riot (Factory New)")
# for each in result:
#     print(each.sell_listings)
# print(result.to_dict())
# print(ItemWithVendorOffers.model_validate(result))

# result = shop_db_service.get_paginated_shop_items(db_session = get_session(), skip= 0, limit= 10 )

# print(result)

# print(PaginatedShopItems(limit = 0, skip = 10, itemsWithVendorOffers= result))
