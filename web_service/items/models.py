class ItemBase(BaseModel):
    market_hash_name: str
    classid: str
    name: str
    icon_url: str


class ItemWithVendorOffers(ItemBase):
    vendor_offers: list[VendorOfferBase] = []

