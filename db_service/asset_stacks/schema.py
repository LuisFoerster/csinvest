from sqlalchemy import Column, Float, Boolean, text, Integer, DateTime, func, ForeignKey
from sqlalchemy.orm import relationship

from db_service.base import Base


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
