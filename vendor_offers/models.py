from sqlalchemy import Column, String, Text, text, Integer, DateTime, func, URL, ForeignKey
from sqlalchemy.orm import relationship, class_mapper
from database.base import Base
from pydantic import BaseModel


""" sqlalchemy models """


class VendorOffer(Base):
    __tablename__ = "vendor_offers"
    id = Column(Integer, primary_key=True, autoincrement=True)
    classid = Column(ForeignKey("items.classid"))
    vendorid = Column(ForeignKey("vendors.id"))
    affiliate_link = Column(Text)
    lowest_price = Column(Integer)
    median_price = Column(Integer)
    sell_listings = Column(Integer)
    updated_at = Column(DateTime, server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'))
    created_at = Column(DateTime, server_default=func.CURRENT_TIMESTAMP())

    item = relationship("Item", back_populates="vendor_offers")
    vendor = relationship("Vendor", back_populates="vendor_offers")



""" pydantic models """


class VendorOfferBase(BaseModel):
    vendorid: int
    #affiliate_link: str
    lowest_price: int
    median_price: int
    sell_listings: int

class VendorOfferRead(VendorOfferBase):
    pass

