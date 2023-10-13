from sqlalchemy import Column, String, Text, text, DateTime, func
from sqlalchemy.dialects.postgresql import TIMESTAMP
from sqlalchemy.orm import relationship

from db_service.base import Base


class Account(Base):
    __tablename__ = "accounts"
    steamid = Column(String(64), primary_key=True)
    # userid = Column(Integer, ForeignKey("users.id")) impl. later, when multiple steam accounts
    personame = Column(Text)
    avatar = Column(Text)
    avatarmedium = Column(Text)
    avatarfull = Column(Text)
    updated_at = Column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'), onupdate=text('CURRENT_TIMESTAMP'))
    created_at = Column(DateTime, server_default=func.CURRENT_TIMESTAMP())

    # user = relationship("User", back_populates="account")
    assets = relationship("Asset", back_populates="account", cascade="all, delete-orphan")
    asset_stacks = relationship("AssetStack", back_populates="account", cascade="all, delete-orphan")
