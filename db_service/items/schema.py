from sqlalchemy import Column, String, Text, text, Float, Integer, DateTime, func
from sqlalchemy.dialects.postgresql import TIMESTAMP
from sqlalchemy.orm import relationship

from db_service.base import Base


class Item(Base):
    __tablename__ = "items"
    classid = Column(String(64), primary_key=True)
    market_hash_name = Column(Text)
    item_nameid = Column(String(64))
    name = Column(Text)
    name_spezifier = Column(Text)
    exterior = Column(Text)
    quality = Column(Text)
    categorie = Column(Text)
    type = Column(Text)
    weapon_type = Column(Text)
    sticker_type = Column(Text)
    graffiti_type = Column(Text)
    patch_type = Column(Text)
    collection = Column(Text)
    professional_player = Column(Text)
    tournament = Column(Text)
    team = Column(Text)
    min_float = Column(Float)
    max_float = Column(Float)
    droppool = Column(Text)
    release_year = Column(DateTime)

    appid = Column(Integer)
    icon_url = Column(Text)
    background_color = Column(String(64))
    name_color = Column(String(64))
    updated_at = Column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'), onupdate=text('CURRENT_TIMESTAMP'))
    created_at = Column(DateTime, server_default=func.CURRENT_TIMESTAMP())

    vendor_offers = relationship("VendorOffer", back_populates="item", cascade="all, delete-orphan")
    assets = relationship("Asset", back_populates="item", cascade="all, delete-orphan")
    asset_stacks = relationship("AssetStack", back_populates="item", cascade="all, delete-orphan")
    history_listings = relationship("HistoryListing", back_populates="item", cascade="all, delete-orphan")
    skinport_pricehistory = relationship("SkinportPricehistory", back_populates="item", cascade="all, delete-orphan")
    statistic = relationship("Statistic", back_populates="item", cascade="all, delete-orphan")
