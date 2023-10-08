""" pydantic models """

# class DepotBase(BaseModel):
#     user_name: str
from pydantic import BaseModel, ConfigDict, model_validator


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

    @model_validator(mode="after")
    def compute_total(self) -> dict:
        depot_buyin = sum(each.total_buyin for each in self.asset_stacks)
        depot_value = sum(each.current_value for each in self.asset_stacks)
        total_items = sum(each.size for each in self.asset_stacks)
        self.depot_buyin = depot_buyin
        self.depot_value = depot_value
        self.total_items = total_items
