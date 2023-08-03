from sqlalchemy import Column, String, Text, text, Integer, DateTime, func, URL, ForeignKey
from sqlalchemy.orm import relationship, class_mapper
from database.base import Base
from pydantic import BaseModel, validator
from vendor_offers.models import VendorOfferBase

class Account(Base):
    __tablename__ = "accounts"
    steamid = Column(String(64), primary_key=True )
    userid = Column(Text)
    personame = Column(Text)
    avatar = Column(Text)
    avatarmedium = Column(Text)
    avatarfull = Column(Text)
    updated_at = Column(DateTime, server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'))
    created_at = Column(DateTime, server_default=func.CURRENT_TIMESTAMP())