
from sqlalchemy import Column, String, Text, text, Integer, DateTime, func, URL, ForeignKey
from sqlalchemy.orm import relationship
from database.base import Base
from pydantic import BaseModel


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
    # updated_at = Column(DateTime, server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'))
    # created_at = Column(DateTime, server_default=func.CURRENT_TIMESTAMP())

    prices = relationship("Price", back_populates="item", cascade="all, delete-orphan")



""" pydantic models """
class ItemBase(BaseModel):
    market_hash_name: str
    classid: str
    name: str
    sell_price: int

    class Config:
        orm_mode = True

class ItemRead(ItemBase):
    pass
