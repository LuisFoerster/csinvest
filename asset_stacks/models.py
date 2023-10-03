from sqlalchemy import Column, Float, Boolean, text, Integer, DateTime, func, ForeignKey
from sqlalchemy.orm import relationship
from db_service.migrations import Base
from pydantic import BaseModel, model_validator, ConfigDict

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

# class DepotBase(BaseModel):
#     user_name: str

class AssetStackBase(BaseModel):
    market_hash_name: str
    asset_stackid: int
    size: int
    classid: str
    buyin: float
    virtual: bool
    lowest_price: float
    total_buyin: float
    current_value: float


class Depot(BaseModel):

    asset_stacks: list[AssetStackBase]
    depot_buyin: float = 0
    depot_value: float = 0
    total_items: int = 0

    model_config = ConfigDict(from_attributes=True)
    @model_validator(mode= "after")
    def compute_total(self) -> dict:
        depot_buyin = sum(each.total_buyin for each in self.asset_stacks)
        depot_value = sum(each.current_value for each in self.asset_stacks)
        total_items = sum(each.size for each in self.asset_stacks)
        self.depot_buyin = depot_buyin
        self.depot_value = depot_value
        self.total_items = total_items


