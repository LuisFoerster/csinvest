from sqlalchemy import Column, String, Text, text, Integer, DateTime, func, URL, ForeignKey
from sqlalchemy.orm import relationship, class_mapper
from database.base import Base
from pydantic import BaseModel, validator
from vendor_offers.models import VendorOfferBase

""" sqlalchemy models """


class Item(Base):
    __tablename__ = "items"
    classid = Column(String(64), primary_key=True)
    appid = Column(Integer)
    market_hash_name = Column(Text)
    name = Column(Text)
    icon_url = Column(Text)
    background_color = Column(String(64))
    name_color = Column(String(64))
    type = Column(Text)
    updated_at = Column(DateTime, server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'))
    created_at = Column(DateTime, server_default=func.CURRENT_TIMESTAMP())

    vendor_offers = relationship("VendorOffer", back_populates="item", cascade="all, delete-orphan")



""" pydantic models """


class ItemBase(BaseModel):
    market_hash_name: str
    classid: str
    name: str
    icon_url: str


class ItemWithVendorOffers(ItemBase):
    vendor_offers: list[VendorOfferBase] = []
