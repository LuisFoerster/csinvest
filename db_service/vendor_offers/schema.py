from pydantic import BaseModel
from sqlalchemy import Column, Text, text, Integer, DateTime, func, Float, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship

from db_service.migrations import Base

""" sqlalchemy models """


class VendorOffer(Base):
    __tablename__ = "vendor_offers"
    id = Column(Integer, primary_key=True, autoincrement=True)
    classid = Column(ForeignKey("items.classid"))
    vendorid = Column(ForeignKey("vendors.id"))
    affiliate_link = Column(Text)
    lowest_price = Column(Float)
    median_price = Column(Float)
    sell_listings = Column(Integer)
    updated_at = Column(DateTime, server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'))
    created_at = Column(DateTime, server_default=func.CURRENT_TIMESTAMP())

    item = relationship("Item", back_populates="vendor_offers")
    vendor = relationship("Vendor", back_populates="vendor_offers")

    __table_args__ = (
        UniqueConstraint('classid', 'vendorid', name='unique_class_and_vendor_id'),
    )


""" pydantic models """



