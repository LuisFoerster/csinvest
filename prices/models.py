from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from database.base import Base
from items.models import Item

class Price(Base):
    __tablename__ = "prices"
    id = Column(Integer, primary_key=True, autoincrement=True)
    classid = Column(String(64), ForeignKey("items.classid"))
    sell_price = Column(Integer)

    item = relationship("Item",  back_populates= "prices")


