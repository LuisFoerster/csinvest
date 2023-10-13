from sqlalchemy import Column, Text, text, Float, Integer, DateTime, func
from sqlalchemy.dialects.postgresql import TIMESTAMP
from sqlalchemy.orm import relationship

from db_service.base import Base


class Vendor(Base):
    __tablename__ = "vendors"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(Text)
    provision = Column(Float)
    icon_url = Column(Text)
    updated_at = Column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'), onupdate=text('CURRENT_TIMESTAMP'))
    created_at = Column(DateTime, server_default=func.CURRENT_TIMESTAMP())

    vendor_offers = relationship("VendorOffer", back_populates="vendor", cascade="all, delete-orphan")
    history_listings = relationship("HistoryListing", back_populates="vendor", cascade="all, delete-orphan")
