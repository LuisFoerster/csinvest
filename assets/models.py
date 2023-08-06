from sqlalchemy import Column, String, text, Integer, DateTime, func, ForeignKey
from sqlalchemy.orm import relationship
from database.base import Base

""" sqlalchemy models """


class Asset(Base):
    __tablename__ = "assets"
    assetid = Column(String(64), primary_key=True)
    classid = Column(ForeignKey("items.classid"))
    steamid = Column(ForeignKey("accounts.steamid"))
    asset_stackid = Column(ForeignKey("assetstacks.id"))
    instanceid = Column(String(64))
    appid = Column(Integer)
    contextid = Column(String(64))
    amount = Column(Integer)
    updated_at = Column(DateTime, server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'))
    created_at = Column(DateTime, server_default=func.CURRENT_TIMESTAMP())

    item = relationship("Item", back_populates="assets")
    account = relationship("Account", back_populates="assets")
    asset_stack = relationship("AssetStack", back_populates="assets")


""" pydantic models """
