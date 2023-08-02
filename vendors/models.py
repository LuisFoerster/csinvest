from sqlalchemy import Column, String, Text, text,Float, Integer, DateTime, func, URL, ForeignKey
from sqlalchemy.orm import relationship, class_mapper
from database.base import Base
from pydantic import BaseModel

""" sqlalchemy models """


class Vendor(Base):
    __tablename__ = "vendors"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(Text)
    provision = Column(Float)
    icon_url = Column(Text)
    updated_at = Column(DateTime, server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'))
    created_at = Column(DateTime, server_default=func.CURRENT_TIMESTAMP())

    vendor_offers = relationship("VendorOffer", back_populates="vendor", cascade="all, delete-orphan")


""" pydantic models """


class VendorBase(BaseModel):
    id: int
    name: str
    provision: float
    icon_url: str
