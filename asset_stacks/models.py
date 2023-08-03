from sqlalchemy import Column, String, Text,Float,Boolean, text, Integer, DateTime, func, URL, ForeignKey
from sqlalchemy.orm import relationship, class_mapper
from database.base import Base
from pydantic import BaseModel, validator
from vendor_offers.models import VendorOfferBase

""" sqlalchemy models """


class AssetStack(Base):
    __tablename__ = "assetstacks"
    id = Column(Integer, primary_key=True, autoincrement=True)
    classid = Column(ForeignKey("items.classid"))
    steamid = Column(ForeignKey("accounts.steamid"))
    buyin = Column(Float)
    size = Column(Integer)
    virtual = Column(Boolean)
    updated_at = Column(DateTime, server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'))
    created_at = Column(DateTime, server_default=func.CURRENT_TIMESTAMP())




""" pydantic models """


