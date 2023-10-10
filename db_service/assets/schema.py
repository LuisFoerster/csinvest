from sqlalchemy import Column, String, text, DateTime, func, ForeignKey
from sqlalchemy.orm import relationship

from db_service.base import Base


class Asset(Base):
    __tablename__ = "assets"
    assetid = Column(String(64), primary_key=True)
    classid = Column(ForeignKey("items.classid"))
    steamid = Column(ForeignKey("accounts.steamid"))
    asset_stackid = Column(ForeignKey("assetstacks.id"))
    instanceid = Column(String(64))
    contextid = Column(String(64))
    updated_at = Column(DateTime, server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'))
    created_at = Column(DateTime, server_default=func.CURRENT_TIMESTAMP())

    item = relationship("Item", back_populates="assets")
    account = relationship("Account", back_populates="assets")
    asset_stack = relationship("AssetStack", back_populates="assets")
