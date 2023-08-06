from sqlalchemy import Column, String, Text, text, DateTime, func
from sqlalchemy.orm import relationship
from database.base import Base


class Account(Base):
    __tablename__ = "accounts"
    steamid = Column(String(64), primary_key=True)
    userid = Column(Text)
    personame = Column(Text)
    avatar = Column(Text)
    avatarmedium = Column(Text)
    avatarfull = Column(Text)
    updated_at = Column(DateTime, server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'))
    created_at = Column(DateTime, server_default=func.CURRENT_TIMESTAMP())

    assets = relationship("Asset", back_populates="account", cascade="all, delete-orphan")
    asset_stacks = relationship("AssetStack", back_populates="account", cascade="all, delete-orphan")
