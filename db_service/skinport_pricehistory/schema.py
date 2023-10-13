from sqlalchemy import Column, String, Float, text, Integer, DateTime, func, ForeignKey
from sqlalchemy.dialects.postgresql import TIMESTAMP
from sqlalchemy.orm import relationship

from db_service.base import Base


class SkinportPricehistory(Base):
    __tablename__ = "skinport_pricehistories"
    id = Column(Integer, autoincrement=True, primary_key=True)
    classid = Column(String(64), ForeignKey("items.classid"))
    avg_price = Column(Float)
    volume = Column(Integer)
    updated_at = Column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'), onupdate=text('CURRENT_TIMESTAMP'))
    created_at = Column(DateTime, server_default=func.CURRENT_TIMESTAMP())

    item = relationship("Item", back_populates="skinport_pricehistory")
