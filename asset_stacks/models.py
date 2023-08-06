from sqlalchemy import Column, Float, Boolean, text, Integer, DateTime, func, ForeignKey
from sqlalchemy.orm import relationship
from database.base import Base

""" sqlalchemy models """


class AssetStack(Base):
    __tablename__ = "assetstacks"
    id = Column(Integer, primary_key=True, autoincrement=True)
    classid = Column(ForeignKey("items.classid"))
    steamid = Column(ForeignKey("accounts.steamid"))
    average_buyin = Column(Float)
    size = Column(Integer)
    updated_at = Column(DateTime, server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'))
    created_at = Column(DateTime, server_default=func.CURRENT_TIMESTAMP())

    item = relationship("Item", back_populates="asset_stacks")
    account = relationship("Account", back_populates="asset_stacks")
    buyin_stacks = relationship("BuyinStack", back_populates="asset_stack", cascade="all, delete-orphan")

""" pydantic models """
