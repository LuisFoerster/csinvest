from sqlalchemy import Column, String, Text, text, Integer, DateTime, func, URL, ForeignKey
from sqlalchemy.orm import relationship, class_mapper
from database.base import Base
from pydantic import BaseModel, validator
from vendor_offers.models import VendorOfferBase

""" sqlalchemy models """


class Asset(Base):
    __tablename__ = "assets"
    assetid = Column(String(64), primary_key=True)
    classid = Column(ForeignKey("items.classid"))
    stackid = Column(ForeignKey("assetstacks.id"))
    instanceid = Column(String(64))
    appid = Column(Integer)
    contextid = Column(String(64))
    amount = Column(Integer)
    updated_at = Column(DateTime, server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'))
    created_at = Column(DateTime, server_default=func.CURRENT_TIMESTAMP())




""" pydantic models """


