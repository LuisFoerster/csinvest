from sqlalchemy import Column, Float, Boolean, text, Integer, DateTime, func, ForeignKey
from sqlalchemy.orm import relationship
from database.base import Base
from pydantic import BaseModel, model_validator


""" sqlalchemy models """


class AssetStack(Base):
    __tablename__ = "assetstacks"
    id = Column(Integer, primary_key=True, autoincrement=True)
    classid = Column(ForeignKey("items.classid"))
    steamid = Column(ForeignKey("accounts.steamid"))
    buyin = Column(Float)
    virtual = Column(Boolean)
    virtual_size = Column(Integer)
    updated_at = Column(DateTime, server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'))
    created_at = Column(DateTime, server_default=func.CURRENT_TIMESTAMP())

    item = relationship("Item", back_populates="asset_stacks")
    account = relationship("Account", back_populates="asset_stacks")
    assets = relationship("Asset", back_populates="asset_stack")

""" pydantic models """

class DepotBase(BaseModel):
    user_name: str

class AssetStackBase(BaseModel):
    market_hash_name: str
    size: int
    buyin: float
    virtual: bool

class Depot(BaseModel):
    # def __init__(self, *args, **kwargs):
    #     self.calculate_total_buyin()

    asset_stacks : list[AssetStackBase]  =[]
    total_buyin: float = 0

    # @property
    # def total_buyin(self):
    #     total_buyin = sum(each.buyin for each in self.asset_stacks)



