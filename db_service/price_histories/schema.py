from sqlalchemy import Column, Float, text, Integer, DateTime, func, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship

from db_service.base import Base


class HistoryListing(Base):
    __tablename__ = "pricehistories"
    id = Column(Integer, primary_key=True, autoincrement=True)
    classid = Column(ForeignKey("items.classid"))
    vendorid = Column(ForeignKey("vendors.id"))
    time_stamp = Column(DateTime)
    volume = Column(Integer)
    price = Column(Float)
    updated_at = Column(DateTime, server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'))
    created_at = Column(DateTime, server_default=func.CURRENT_TIMESTAMP())

    item = relationship("Item", back_populates="history_listings")
    vendor = relationship("Vendor", back_populates="history_listings")

    __table_args__ = (
        UniqueConstraint('classid', 'vendorid', 'time_stamp', name='unique_class_and_vendor_id_and_time_stamp'),
    )
