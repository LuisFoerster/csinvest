from pydantic import BaseModel
from sqlalchemy import Column, String, Text, text, Integer, DateTime, func
from sqlalchemy.orm import relationship
from vendor_offers.models import VendorOfferBase
from db_service.migrations import Base


""" sqlalchemy models """


class Item(Base):
    __tablename__ = "items"
    classid = Column(String(64), primary_key=True)
    appid = Column(Integer)
    market_hash_name = Column(Text)
    name = Column(Text)
    item_nameid = Column(String(64))
    icon_url = Column(Text)
    background_color = Column(String(64))
    name_color = Column(String(64))
    type = Column(Text)
    updated_at = Column(DateTime, server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'))
    created_at = Column(DateTime, server_default=func.CURRENT_TIMESTAMP())

    vendor_offers = relationship("VendorOffer", back_populates="item", cascade="all, delete-orphan")
    assets = relationship("Asset", back_populates="item", cascade="all, delete-orphan")
    asset_stacks = relationship("AssetStack", back_populates="item", cascade="all, delete-orphan")
    history_listings = relationship("HistoryListing", back_populates="item", cascade="all, delete-orphan")
    skinport_pricehistory = relationship("SkinportPricehistory", back_populates="item", cascade="all, delete-orphan")

""" pydantic models """


class ItemBase(BaseModel):
    market_hash_name: str
    classid: str
    name: str
    icon_url: str


class ItemWithVendorOffers(ItemBase):
    vendor_offers: list[VendorOfferBase] = []

