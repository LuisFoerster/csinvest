from sqlalchemy import Column, Float, Boolean, text, Integer, DateTime, func, ForeignKey
from sqlalchemy.orm import relationship
from database.base import Base

""" sqlalchemy models """


class BuyinStack(Base):
    __tablename__ = "buyinstacks"
    id = Column(Integer, primary_key=True, autoincrement=True)
    assetid = Column(ForeignKey("assets.assetid"))
    asset_stackid = Column(ForeignKey("assetstacks.id"))
    buyin = Column(Float)
    size = Column(Integer)
    virtual = Column(Boolean)
    updated_at = Column(DateTime, server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'))
    created_at = Column(DateTime, server_default=func.CURRENT_TIMESTAMP())

    asset = relationship("Asset", back_populates="buyin_stacks")
    asset_stack = relationship("AssetStack", back_populates="buyin_stacks")

""" pydantic models """
