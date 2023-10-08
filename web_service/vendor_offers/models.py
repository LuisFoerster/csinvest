from pydantic import BaseModel

class VendorOfferBase(BaseModel):
    vendorid: int
    lowest_price: float
    median_price: float
    affiliate_link: str
    sell_listings: int

class VendorOfferRead(VendorOfferBase):
    pass